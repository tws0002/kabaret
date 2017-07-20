'''
    Copyright (c) Supamonks Studio and individual contributors.
    All rights reserved.

    This file is part of kabaret, a python Digital Creation Framework.

    Kabaret is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    Redistributions of source code must retain the above copyright notice, 
    this list of conditions and the following disclaimer.
        
    Redistributions in binary form must reproduce the above copyright 
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
    
    Kabaret is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.
    
    You should have received a copy of the GNU Lesser General Public License
    along with kabaret.  If not, see <http://www.gnu.org/licenses/>

--

    The kabaret.core.events.event module:
        Declares the Event class used to communicate and
        trigger between App and Client Views.
    
'''

class Event(object):
    '''
    Events are generated by apps or the GUI to notify all 
    the registered handlers.
    
    An event has an application key that specifies which
    application owns the object of the event, a path that 
    identifies the object of the event, a etype attribute 
    that categorize the event and a (pickable) data attribute 
    containing informations depending on the etype and the path.
    
    An event path is a list of strings.
    Each strings identify the hierarchy leading to the object 
    of the event and should be unique for this object. 
    
    Events are dispatched to handlers by the AppHost.
    Handler register themselves with given app key and event path 
    to receive all event with this app key and path or a sub path (see 
    core.mq.apphost.ProjectClient.add_event_handler()).
    The shortest path handler receive the event first and can
    call event.stop() to prevent further handlers to receive
    this event.
    
    '''
    class TYPE:
        CREATED = 'CREATED'
        INVALIDATED = 'INVALIDATED'
        UPDATED = 'UPDATED'
        DELETED = 'DELETED'
        MESSAGE = 'MESSAGE'
        
    def __init__(self, app_key, path, etype, data):
        '''
        /!\ data must be pickable.
        '''
        self.app_key = app_key
        self.path = path
        self.etype = etype
        self.data = data
    
        self.propagating = True
    
    def to_dict(self):
        return {
            'app_key':self.app_key,
            'path':self.path,
            'etype':self.etype,
            'data':self.data,
        }
    
    @classmethod
    def from_dict(cls, d):
        return cls(**d)
    
    def stop(self):
        self.propagating = False
            