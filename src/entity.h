/*
 *  This file is part of Permafrost Engine. 
 *  Copyright (C) 2017 Eduard Permyakov 
 *
 *  Permafrost Engine is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  Permafrost Engine is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#ifndef ENTITY_H
#define ENTITY_H

#include "pf_math.h"
#include <stdbool.h>

#define ENTITY_NAME_LEN 32
#define BASEDIR_LEN     64

struct entity{
    uint32_t  uid;
    char      name[ENTITY_NAME_LEN];
    char      basedir[BASEDIR_LEN];
    vec3_t    pos;
    vec3_t    scale;
    bool      animated;
    void     *render_private;
    void     *anim_private;
};

void     Entity_ModelMatrix(const struct entity *ent, mat4x4_t *out);
uint32_t Entity_NewUID(void);

#endif
