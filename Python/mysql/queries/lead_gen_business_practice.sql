select clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
from clients
join billing on clients.id = billing.clients_id;

select sites.domain_name, leads.first_name, leads.last_name
from sites
join leads on sites_id = leads.sites_id;

select clients.first_name as client_first, clients.last_name, sites.domain_name, leads.first_name as leads_first
from clients
join sites on clients_id = sites.clients_id
join leads on sites.id = leads.sites_id;

select clients.first_name, clients.last_name, sites.domain_name
from clients
left join sites on clients_id = sites.clients_id