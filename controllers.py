from models import db, Event

def get_event():
    events = Event.query.all()
    if not events:
        return {"message": "No events found"}
    return [event.to_dict() for event in events]

def create_event(data):
    name = data.get('name')
    description = data.get('description')
    location = data.get('location')
    date = data.get('date')
    time = data.get('time')
    
    if not all([name, description, location, date, time]):
        return {"error": "Missing required fields"}
    
    event = Event(name=name, description=description, location=location, date=date, time=time)
    db.session.add(event)
    db.session.commit()
    return {"message": f"Event {event.name} created"}

def update_event(id, data):
    event = Event.query.get(id)
    if not event:
        return {"error": "Event not found"}
    
    name = data.get('name')
    description = data.get('description')
    location = data.get('location')
    date = data.get('date')
    time = data.get('time')
    
    if not all([name, description, location, date, time]):
        return {"error": "Missing required fields"}
    
    event.name = name
    event.description = description
    event.location = location
    event.date = date
    event.time = time
    db.session.commit()
    return {"message": f"Event {event.name} updated"}

def delete_event(id):
    event = Event.query.get(id)
    if not event:
        return {"error": "Event not found"}
    
    db.session.delete(event)
    db.session.commit()
    return {"message": f"Event {event.name} deleted"}

def search_event(id):
    event = Event.query.get(id)
    if not event:
        return {"error": "Event not found"}
    
    return event.to_dict()