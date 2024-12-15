create or replace function match_outfit (
  query_embedding vector(2048),
  match_threshold float,
  match_count int
)
returns table(id uuid, description text, url text)
language sql
as $$
  select id, description, url
  from outfit
  where outfit.embedding <=> query_embedding < 1 - match_threshold
  order by outfit.embedding <=> query_embedding asc
  limit least(match_count, 100);
$$;

create or replace function match_outfit_description (
  query_embedding vector(1536),
  match_threshold float,
  match_count int
)
returns table(id uuid, description text, url text)
language sql
as $$
  select id, description, url
  from outfit
  where outfit.description_embedding <=> query_embedding < 1 - match_threshold
  order by outfit.description_embedding <=> query_embedding asc
  limit least(match_count, 100);
$$;
