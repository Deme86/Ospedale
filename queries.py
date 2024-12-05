from sqlalchemy import func

#Elenco di tutti i pazienti con i dati delle ultime visite

def elenco_pazienti_con_ultime_visite(session):
    risultati = (
        session.query(
            Paziente.ID.label("PazienteID"),
            Paziente.nome.label("NomePaziente"),
            func.max(Visita.data).label("DataUltimaVisita"),
            Visita.diagnosi.label("DiagnosiUltimaVisita"),
            Medico.nome.label("NomeMedico")
        )
        .outerjoin(Visita, Paziente.ID == Visita.paziente_id)
        .outerjoin(Medico, Visita.medico_id == Medico.ID)
        .group_by(Paziente.ID, Paziente.nome, Visita.diagnosi, Medico.nome)
        .all()
    )

    for r in risultati:
        print(
            f"Paziente: {r.NomePaziente}, Ultima Visita: {r.DataUltimaVisita}, "
            f"Diagnosi: {r.DiagnosiUltimaVisita}, Medico: {r.NomeMedico}"
        )
#Numero di ricoveri per reparto
def numero_ricoveri_per_reparto(session):
    risultati = (
        session.query(
            Reparto.nome_reparto.label("NomeReparto"),
            func.count(Ricovero.ID).label("NumeroRicoveri")
        )
        .outerjoin(Ricovero, Reparto.ID == Ricovero.reparto_id)
        .group_by(Reparto.nome_reparto)
        .all()
    )

    for r in risultati:
        print(f"Reparto: {r.NomeReparto}, Numero Ricoveri: {r.NumeroRicoveri}")

#Elenco di prescrizioni per ciascun paziente
def elenco_prescrizioni_per_paziente(session):
    risultati = (
        session.query(
            Paziente.nome.label("NomePaziente"),
            Medico.nome.label("NomeMedico"),
            Farmaco.nome_farmaco.label("NomeFarmaco"),
            Prescrizione.data_prescrizione.label("DataPrescrizione")
        )
        .join(Visita, Visita.paziente_id == Paziente.ID)
        .join(Prescrizione, Prescrizione.visita_id == Visita.ID)
        .join(Medico, Prescrizione.medico_id == Medico.ID)
        .join(Farmaco, Prescrizione.farmaco_id == Farmaco.ID)
        .all()
    )

    for r in risultati:
        print(
            f"Paziente: {r.NomePaziente}, Medico: {r.NomeMedico}, "
            f"Farmaco: {r.NomeFarmaco}, Data: {r.DataPrescrizione}"
        )
#Totale dei pagamenti effettuati per ogni paziente
def totale_pagamenti_per_paziente(session):
    risultati = (
        session.query(
            Paziente.ID.label("PazienteID"),
            Paziente.nome.label("NomePaziente"),
            func.sum(Pagamento.importo).label("TotalePagamenti")
        )
        .outerjoin(Pagamento, Paziente.ID == Pagamento.paziente_id)
        .group_by(Paziente.ID, Paziente.nome)
        .all()
    )

    for r in risultati:
        print(f"Paziente: {r.NomePaziente}, Totale Pagamenti: {r.TotalePagamenti}")
#Pazienti con diagnosi specifica
def pazienti_con_diagnosi_specifica(session, diagnosi):
    risultati = (
        session.query(
            Paziente.ID.label("PazienteID"),
            Paziente.nome.label("NomePaziente"),
            Visita.diagnosi.label("Diagnosi")
        )
        .join(Visita, Paziente.ID == Visita.paziente_id)
        .filter(Visita.diagnosi == diagnosi)
        .all()
    )

    for r in risultati:
        print(f"Paziente: {r.NomePaziente}, Diagnosi: {r.Diagnosi}")

