CREATE TABLE "conductor" (
  "id" varchar,
  "nombre" text,
  "vigencia" date
);

CREATE TABLE "persona" (
  "id" varchar,
  "tipo_id" varchar,
  "nombre" text,
  "telefono" text,
  "direccion" text
);

CREATE TABLE "vehiculo" (
  "id" varchar,
  "modelo" text,
  "marca" text,
  "clase" text,
  "interno" integer,
  "top" integer
);

CREATE TABLE "extracto" (
  "id" varchar,
  "vehiculo_id" varchar NOT NULL,
  "fecha_registro" datetime DEFAULT 'now',
  "empresa_id" varchar NOT NULL,
  "contrato" integer NOT NULL,
  "contratante_id" varchar NOT NULL,
  "objeto_contrato" text NOT NULL,
  "recorrido" text NOT NULL,
  "convenio_id" varchar NOT NULL,
  "conductor_1_id" varchar NOT NULL,
  "conductor_2_id" varchar,
  "conductor_3_id" varchar,
  "fecha_inicio" date NOT NULL,
  "fecha_fin" date NOT NULL,
  "responsable_id" varchar NOT NULL
);

ALTER TABLE "extracto" ADD FOREIGN KEY ("vehiculo_id") REFERENCES "vehiculo" ("id");

ALTER TABLE "extracto" ADD FOREIGN KEY ("empresa_id") REFERENCES "persona" ("id");

ALTER TABLE "extracto" ADD FOREIGN KEY ("contratante_id") REFERENCES "persona" ("id");

ALTER TABLE "extracto" ADD FOREIGN KEY ("convenio_id") REFERENCES "persona" ("id");

ALTER TABLE "extracto" ADD FOREIGN KEY ("conductor_1_id") REFERENCES "conductor" ("id");

ALTER TABLE "extracto" ADD FOREIGN KEY ("conductor_2_id") REFERENCES "conductor" ("id");

ALTER TABLE "extracto" ADD FOREIGN KEY ("conductor_3_id") REFERENCES "conductor" ("id");

ALTER TABLE "extracto" ADD FOREIGN KEY ("responsable_id") REFERENCES "persona" ("id");
