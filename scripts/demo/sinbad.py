#
#  This file is part of Permafrost Engine. 
#  Copyright (C) 2018 Eduard Permyakov 
#
#  Permafrost Engine is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Permafrost Engine is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import pf
from constants import *

class Sinbad(pf.AnimEntity):

    def __init__(self, path, pfobj, name):
        self.anim_idx = 0
        self.anim_map = ["Dance", "RunBase"]
        super(Sinbad, self).__init__(path, pfobj, name, self.anim_map[self.anim_idx])
        self.register(EVENT_SINBAD_TOGGLE_ANIM, Sinbad.on_anim_toggle, self)
    
    def __del__(self):
        self.unregister(EVENT_SINBAD_TOGGLE_ANIM, Sinbad.on_anim_toggle)
    
    def on_anim_toggle(self, event):
        self.anim_idx = (self.anim_idx + 1) % 2
        self.play_anim(self.anim_map[self.anim_idx])

