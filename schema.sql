
create table country (
  country_name text not null,
  country_code char(2) unique not null
);

create table institution (
  institution_uuid uuid unique not null,
  institution_name text not null,
  institution_country_code char(2) not null references country(country_code)
);

create table ip_range (
  ip_range_value cidr unique not null,
  institution_uuid uuid not null references institution(institution_uuid)
);

create table contact (
  contact_name text not null,
  contact_email_address text not null,
  contact_notes text,
  institution_uuid uuid not null references institution(institution_uuid)
);

create table institution_relation (
  ir_parent_id uuid not null references institution(institution_uuid),
  ir_child_id uuid not null references institution(institution_uuid),
  unique (ir_parent_id, ir_child_id),
  constraint no_self_referencing check (ir_parent_id <> ir_child_id)
);

-- todo: do we nede a serial at all?
