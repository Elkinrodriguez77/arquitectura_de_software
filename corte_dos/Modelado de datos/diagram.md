// Diagrama para PostgreSQL
Table vehiculos {
  id integer [primary key]
  placa varchar [unique, not null]
  modelo varchar
  capacidad_kg integer
  nivel_bateria numeric
}

Table conductores {
  id integer [primary key]
  nombre_completo varchar [not null]
  licencia varchar [unique]
  telefono varchar
}

Table rutas {
  id integer [primary key]
  origen varchar
  destino varchar
  distancia_km numeric
  vehiculo_id integer
  conductor_id integer
}

Table entregas {
  id integer [primary key]
  ruta_id integer
  cliente varchar
  peso_paquete numeric
  estado varchar
}

Table lecturas_energia {
  id integer [primary key]
  vehiculo_id integer
  fecha_hora timestamp
  nivel_carga numeric
}

// Relaciones (Acoplamiento)
Ref: rutas.vehiculo_id > vehiculos.id
Ref: rutas.conductor_id > conductores.id
Ref: entregas.ruta_id > rutas.id
Ref: lecturas_energia.vehiculo_id > vehiculos.id