
import uuid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from .models import Event, EventSession, Booking
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'events/home.html')

def event_list(request):
    events = Event.objects.all()

    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    sessions = event.sessions.all()
    return render(
        request, 'events/event_detail.html', 
        {'event': event, 
        'sessions': sessions})



@staff_member_required
@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()

            return redirect('event_list')

    else:
        form = EventForm()

    return render(request, 'events/event_form.html', {'form': form})

@login_required
def create_booking(request, session_id):
    session = get_object_or_404(EventSession, pk=session_id)

    existing_booking = Booking.objects.filter(
        user=request.user,
        session=session
    ).exists()

    if existing_booking:
        messages.warning(
            request,
            "You have already booked this session."
        )
        return redirect('event_detail', pk=session.event.pk)

    booking = Booking.objects.create(
        user=request.user,
        session=session,
        booking_reference=str(uuid.uuid4())[:8].upper()
    )

    return redirect(
        'booking_confirmation',
        booking_id=booking.id
    )

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    return render(
        request,
        'events/booking_confirmation.html',
        {'booking': booking}
    )


# Create your views here.
