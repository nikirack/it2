# REA - Reverse Engineer Anything
[Oppgaver](https://github.com/hausnes/it2-2026-2027/blob/main/samfunn/oppgave-reverse-engineer-anything.md)

[Oppgave 1](#oppgave-1---begreper) \
[Oppgave 2](#oppgave-2---hva-er-rea) \
[Oppgave 3](#oppgave-3---for-og-mot)

## Oppgave 1 - Begreper

**Kildekode og maskinkode:**

*Kildekode* (source code) er koden som ett program består av, dette er skrevet i språk som Python, C, TypeScript og Rust

*Maskinkode* er det som faktisk kjører på prosesoren, det er svært vanskelig for mennesker å lese. Normale programmer du laster ned er som oftest maskinkode.

**Kompilering:**

Kompilering er å oversette kildekode til maskinkode. Dette blir gjort gjennom en *compiler*. Man mister masse info gjennom kompilering.

**Dekompilering:**

Dekompilering er å prøve å gjøre det motsatte av kompilering, altså at man prøver å gjøre maskinkode til kildekode. Dette er vanskelig å gjøre siden man mister en del info gjennom kompilering, derfor kan det aldri bli nøyaktig lik som orginalen.

**Rekompilering (særlig statisk rekompilering, slik det brukes i «recomp»-prosjektene):**

Å oversette maskinkoden fra en platform til en annen uten å måtte dekompilere programmet. Statisk rekompilering er at man oversetter all koden på forhånd.

**Reverse engineering:**

Samlet begrep som handler om hvordan man skal finne ut hvordan noe fungerer uten å ha tilgang til kildekoden, dette må ikke bare gjelde programvare, men også fysiske ting. Noen former av reverse engineering er dekompilering, disassemblering og å studere hva et program gjør mens det kjører.

**Modding:**

Modding handler om å modifisere programmer og ting til å gjøre ting de ikke orginalt var ment til å gjøre, f.eks. endre hvordan en karakter i et spill ser ut. 

**Emulering:**

Emulering er å etterligne et annet system for å få maskinkode til å kjøre på noe det ikke orginalt var laget for å kjøre på. Det finnes emulatorer som kan kjøre f.eks. Nintendo spill på pc.

**Open source (og lisens):**

*Open source* er at kildekoden til ett program ligger offentlig ute og at alle kan lese den, lære av den og dele den videre. Det er *lisensen* til programmet som sier hva man kan gjøre med kildekoden, noen lisenser som MIT lar deg gjøre nesten det man vil til programmet, andre lisenser som GPL har strengere krav, som at hvis du bruker kildekoden til noe annet må man la kildekoden til det du lagde være open source også, og at du må bruke samme lisens.

## Oppgave 2 - Hva er REA?
Les [rea.tools](rea.tools) og skum gjennom diskusjonen på [Hacker News](https://news.ycombinator.com/item?id=50028275).

**Hva er REA, og hva kan det brukes til?**

REA er et program som lar din ai agent prøve å reverse enginere det du vil. Det gir din ai agent tilgang til det den trenger for å prøve å forstå hvordan ett program fungerer, og hvorfor det gjør det det gjør.

**Hvordan installeres det? Vis kommandoen i en kodeblokk.**

Programmet har to måter å innstaleres, gjennom npx eller gjennom å la ai agenten gjøre det for deg. 

Ai agent: 
```
Install REA and connect it to this coding agent using npx rea-agents@latest setup. Show me the setup plan for approval, then verify the installation.`
```
Npx:
```bash
npx rea-agents@latest setup
```


**Hva slags programmer kan det analysere?**

Programmet analysere Native Binaries, JavaScript/Electron apper og netsider

**Finn ett positivt og ett kritisk innlegg på Hacker News, og gjengi dem som sitat (med lenke).**

[Positivt innlegg](https://news.ycombinator.com/item?id=50044366)
> This is insane. \
> AI is progressing so much so fast. It's already making such utterly huge and complex systems like game engines, that would take several years of hard work with extensive knowledge, reduced in just a mere worthless task a kid can do in a free weekend, just by prompting a model from a cheap laptop and an internet connection. \
> It's amazing, yeah, but... it's also... unsettling. Things that we valued so much, now will be forgotten... a remnant of past times. \
> And now, now it can not only create new systems, but crack them, modify them, replicate them. This is so strange. How would big software companies react to this? \
> How long then, until we see an open source release of Windows? How long until every single software and game would be available for any platform? Console-exclusive games ported for PC, being able to run all software on Linux, give new life to old programs... \
> All that it's for sure something amazing that I'm eager to see, but... I truly don't think people realize how big these implications could be in a near future. We're witnessing the very dawn of how AI is changing the pillars of this world.\
>AI is right now breaking one of the premises on which we based all systems since the beginning of computers: that we cannot access or generate the source code of a compiled program.\
> Reverse engineering was always a thing, but it's one of the most complex and time consuming tasks. It was, at least, until now. \
> A strange future lies ahead, as I see it. \
>I truly hope I'm wrong, but... this is the beginning of the death of software, and the world as we always knew it.

[Kritisk innlegg](https://news.ycombinator.com/item?id=50028470)
> I might be missing something but... How exactly is this better than telling Claude for example to "install and set up a full RE environment including Ghidra" on my local system and get to work? Like what does this do that my current RE methodology doesn't?

## Oppgave 3 - For og mot

Lag en tabell med argumenter for og mot det som skjer i spill- og programvareverdenen nå. Tenk for eksempel på
- Bevaring av gamle spill og programvare
- Opphavsrett og lisenser, hvem eier koden?
- Arbeidsplasser og selskaper som lever av abonnement
- Sikkerhet, både for og mot (kan verktøyene brukes til å finne sårbarheter, eller til å lage skadevare?)
- Kvalitet og brukerstøtte, hvem hjelper deg når en gratis klone ikke virker?
- Open source: Hva er nytt nå, når gratis alternativer som GIMP og LibreOffice har fantes i mange år?

**Under tabellen:** Skriv din personlige mening i ett eller flere avsnitt. Er dette mest positivt eller negativt? Begrunn svaret.


|For|Mot|
|---|---|
| At man kan få spill til å kjøre på platformer som ikke de orginalt var ment til å kjøre på er veldig bra for bevaring av gamle spill | Ai generert kode er et problem i seg selv, siden det er veldig masse plagiat i treningsdataene til ai-ene |
|  | Ifølge lovene så ligger reverse enginering i en gråsone |
| At ai kan skanne programmer og finne ut hva de gjør vil hjelpe og beskytte deg, siden ai kan finne ut hvordan virus fungerer og finne ut hvordan vi kan stoppe de før det blir et problem | At ai kan finne sårbarheter i programmer vil/og er et veldig stort problem |
|  | Kvaliteten på programmene som ai lager vil være lav kvalitet, og de vil egentlig ikke ha noe brukerstøtte (annet en hvis du spørr en ai agent) |
|  | Å lage kloner av programmer vil ta fokus (og støtte) vekk fra "ekte" open source alternativer, som GIMP |