Il progetto implementa un sistema di pipeline modulare per l'elaborazione del testo, con particolare attenzione alla flessibilità e alla validazione dei tipi.

**Caratteristiche Principali**

### Modulo di Base (PipelineBaseModule)

* Definisce un'interfaccia comune per tutti i moduli
* Implementa la validazione di input/output attraverso `input_type` e `output_type`
* Utilizza il pattern Template Method con `_process()` come metodo astratto

### Moduli custom

* Ogni modulo custom deve ereditare da `PipelineBaseModule`
* Implementare il metodo `_process()`
* Il metodo `_process()` chiama l'effettiva funzione di elaborazione del modulo. 
    Questo permette di essere coerente con l'interfaccia `BaseModule` senza modificare le interfacce già definite dei singoli moduli.

### Pipeline

* La pipeline è un oggetto che contiene una lista di moduli e li esegue in sequenza.
* La pipeline può essere distribuita come libreria e configurata dinamicamente tramite un file YAML.

### Pipeline Configurabile

* Caricamento della configurazione da file YAML
* Creazione dinamica della pipeline basata sulla configurazione
* Concatenazione automatica dei moduli

### Validazione Robusta

* La validazione dei tipi avviene sia in ingresso che in uscita
* Supporto per strutture dati complesse grazie a Pydantic

**Note**
Ho deciso di passare i moduli disponibili come parametro alla classe `Pipeline` in quanto permette di utilizzare il modulo `Pipeline` come libreria senza che tutti i moduli custom siano definiti al suo interno.
Una possibile alternativa è quella di importare dinamicamente i moduli custom tramite `importlib`, ma questo vorrebbe dire indicare il path completo del modulo custom nel file YAML, il che non è desiderabile.