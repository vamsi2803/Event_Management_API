from flask import Blueprint, request, jsonify, abort
from controllers import get_event, create_event, update_event, delete_event, search_event

api = Blueprint('api', __name__)

@api.route('/')
def home():
    """
    Home
    ---
    tags:
      - Home
    responses:
        200:
            description: Welcome message
            schema:
            type: string
        404:
            description: Not found
        500:
            description: Internal server error
        
    """
    return jsonify("Welcome to the Event Management api!")

@api.route('/api/getEvent')
def api_get_event():
    """
    Get all events
    ---
    tags:
      - Events
    responses:
      200:
        description: A list of events
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: The event ID
              name:
                type: string
                description: The name of the event
              description:
                type: string
                description: The description of the event
              location:
                type: string
                description: The location of the event
              date:
                type: string
                format: date
                description: The date of the event
              time:
                type: string
                format: time
                description: The time of the event
        500: 
            description: Internal server error
    """
    try:
        events = get_event()
        return jsonify(events), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api.route('/api/createEvent', methods=['POST'])
def api_create_event():
    """
    Create a new event
    ---
    tags:
      - Events
    parameters:
      - in: body
        name: body
        description: Event object
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: The name of the event
              example: "Sample Event"
            description:
              type: string
              description: The description of the event
              example: "This is a sample event."
            location:
              type: string
              description: The location of the event
              example: "New York"
            date:
              type: string
              format: date
              description: The date of the event
              example: "2023-12-31"
            time:
              type: string
              format: time
              description: The time of the event
              example: "18:00:00"
    responses:
      200:
        description: Event created successfully
        schema:
          type: object
          properties:
            message:
              type: string
              description: Success message
            event:
              type: object
              properties:
                id:
                  type: integer
                  description: The event ID
                name:
                  type: string
                  description: The name of the event
                description:
                  type: string
                  description: The description of the event
                location:
                  type: string
                  description: The location of the event
                date:
                  type: string
                  format: date
                  description: The date of the event
                time:
                  type: string
                  format: time
                  description: The time of the event
      400:
        description: Missing key in request data
      500:
        description: Internal server error
    """
    data = request.json
    required_fields = ['name', 'description', 'location', 'date', 'time']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing key in request data: {field}"}), 400
    try:
        event = create_event(data)
        return jsonify(event), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api.route('/api/updateEvent/<int:id>', methods=['PUT'])
def api_update_event(id):
    """
    Update an existing event
    ---
    tags:
      - Events
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: The ID of the event to update
      - in: body
        name: body
        description: Event object with updated data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "Updated Event"
            description:
              type: string
              example: "This is an updated event description."
            location:
              type: string
              example: "Los Angeles"
            date:
              type: string
              format: date
              example: "2024-01-01"
            time:
              type: string
              format: time
              example: "20:00:00"
    responses:
      200:
        description: Event updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
              description: Success message
            event:
              type: object
              properties:
                id:
                  type: integer
                  description: The event ID
                name:
                  type: string
                  description: The name of the event
                description:
                  type: string
                  description: The description of the event
                location:
                  type: string
                  description: The location of the event
                date:
                  type: string
                  format: date
                  description: The date of the event
                time:
                  type: string
                  format: time
                  description: The time of the event
      400:
        description: Missing key in request data
      404:
        description: Event not found
      500:
        description: Internal server error
    """
    data = request.json
    required_fields = ['name', 'description', 'location', 'date', 'time']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing key in request data: {field}"}), 400
    try:
        event = update_event(id, data)
        if event is None:
            return jsonify({"error": "Event not found"}), 404
        return jsonify(event), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api.route('/api/deleteEvent/<int:id>', methods=['DELETE'])
def api_delete_event(id):
    """
    Delete an existing event
    ---
    tags:
      - Events
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: The ID of the event to delete
    responses:
      200:
        description: Event deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              description: Success message
      404:
        description: Event not found
      500:
        description: Internal server error
    """
    try:
        event = delete_event(id)
        print(event)
        if event is None:
            return jsonify({"error": "Event not found"}), 404
        return jsonify(event), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api.route('/api/searchEvent/<int:id>')
def api_search_event(id):
    """
    Search for an event by ID
    ---
    tags:
      - Events
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: The ID of the event to search for
    responses:
      200:
        description: Event found successfully
        schema:
          type: object
          properties:
            id:
              type: integer
              description: The event ID
            name:
              type: string
              description: The name of the event
            description:
              type: string
              description: The description of the event
            location:
              type: string
              description: The location of the event
            date:
              type: string
              format: date
              description: The date of the event
            time:
              type: string
              format: time
              description: The time of the event
      404:
        description: Event not found
      500:
        description: Internal server error
    """
    try:
        event = search_event(id)
        if event is None:
            return jsonify({"error": "Event not found"}), 404
        return jsonify(event), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500