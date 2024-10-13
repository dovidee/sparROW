# 9.1.6.1
# Dette er feil oppgave, sjekk heller 1C1.py for den riktige "utførelsen"

import lists as L
bunch_O_numbaz = [list: -1, 0, 1]
bunch_O_floatz = [list: -0.1, 0.6, 0.9]
bunch_O_stringz = [list: "john", "mary", "winch"]
bunch_O_randomz = [list: 10, 14, 16, 19, 20, 22]
bunch_O_evenz = [list: 10, 12, 14, 16, 18, 20]

fun form-to-str(digits :: List) -> List<String>:
  doc: "Tar tall i en liste og lager dem over til neg, zero eller pos i en liste"
  L.map(lam(elt): 
      if elt == 0:
        "zero"
      else if elt < 0:
        "neg"
      else:
        "pos"
      end
    end, digits)
where:
  form-to-str(bunch_O_numbaz) is [list: "neg", "zero", "pos"]
  form-to-str(bunch_O_floatz) is [list: "neg", "pos", "pos"]
end

fun fiver(just-str :: List) -> List<Boolean>:
  doc: "Tar string i en liste og sjekker om den er 5"
  L.map(lam(elt):
      string-length(elt) == 5
    end, just-str)
where:
  fiver(bunch_O_stringz) is [list: false, false, true]
end

fun is-even(digits :: List):
  doc: "Filtrer kun partal tall i en liste med tall"
  L.filter(lam(elt):
      if member(bunch_O_evenz, elt):
        true
      else:
        false
      end
    end, digits)
where:
  is-even([list: 10, 15, 20]) is [list: 10, 20]
end
