-- LIMPIEZA DE ENTORNO
DROP TABLE IF EXISTS lecturas_energia;
DROP TABLE IF EXISTS entregas;
DROP TABLE IF EXISTS rutas;
DROP TABLE IF EXISTS conductores;
DROP TABLE IF EXISTS vehiculos;

-- 1. MÓDULO DE VEHÍCULOS
CREATE TABLE vehiculos (
    id SERIAL,
    placa VARCHAR(20) NOT NULL,
    modelo VARCHAR(50),
    capacidad_kg INTEGER,
    nivel_bateria NUMERIC(5,2) DEFAULT 100.00,
    -- CONSTRAINTS INDEPENDIENTES
    CONSTRAINT pk_vehiculos PRIMARY KEY (id),
    CONSTRAINT uk_vehiculos_placa UNIQUE (placa),
    CONSTRAINT ck_vehiculos_capacidad CHECK (capacidad_kg > 0)
);

-- 2. MÓDULO DE CONDUCTORES
CREATE TABLE conductores (
    id SERIAL,
    nombre_completo VARCHAR(100) NOT NULL,
    licencia VARCHAR(50),
    telefono VARCHAR(20),
    -- CONSTRAINTS INDEPENDIENTES
    CONSTRAINT pk_conductores PRIMARY KEY (id),
    CONSTRAINT uk_conductores_licencia UNIQUE (licencia)
);

-- 3. MÓDULO DE RUTAS (Acoplamiento de Datos)
CREATE TABLE rutas (
    id SERIAL,
    origen VARCHAR(100) NOT NULL,
    destino VARCHAR(100) NOT NULL,
    distancia_km NUMERIC(10,2),
    vehiculo_id INTEGER,
    conductor_id INTEGER,
    -- CONSTRAINTS INDEPENDIENTES
    CONSTRAINT pk_rutas PRIMARY KEY (id),
    CONSTRAINT fk_rutas_vehiculo 
        FOREIGN KEY (vehiculo_id) 
        REFERENCES vehiculos(id) 
        ON DELETE SET NULL,
    CONSTRAINT fk_rutas_conductor 
        FOREIGN KEY (conductor_id) 
        REFERENCES conductores(id) 
        ON DELETE SET NULL
);

-- 4. MÓDULO DE ENTREGAS
CREATE TABLE entregas (
    id SERIAL,
    ruta_id INTEGER,
    cliente VARCHAR(100) NOT NULL,
    peso_paquete NUMERIC(10,2),
    estado VARCHAR(20) DEFAULT 'Pendiente',
    -- CONSTRAINTS INDEPENDIENTES
    CONSTRAINT pk_entregas PRIMARY KEY (id),
    CONSTRAINT fk_entregas_ruta 
        FOREIGN KEY (ruta_id) 
        REFERENCES rutas(id) 
        ON DELETE CASCADE
);

-- 5. MÓDULO DE TELEMETRÍA (LECTURAS DE ENERGÍA)
CREATE TABLE lecturas_energia (
    id SERIAL,
    vehiculo_id INTEGER,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nivel_carga NUMERIC(5,2),
    -- CONSTRAINTS INDEPENDIENTES
    CONSTRAINT pk_lecturas_energia PRIMARY KEY (id),
    CONSTRAINT fk_lecturas_vehiculo 
        FOREIGN KEY (vehiculo_id) 
        REFERENCES vehiculos(id)
);