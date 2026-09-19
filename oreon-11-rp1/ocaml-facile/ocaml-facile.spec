%global source0_hash 5712a00802c525d19fb59b7800ffd9d3f7ca08ee9cd295b3905b64676ce5194b

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global giturl https://github.com/Emmanuel-PLF/facile

Name:          ocaml-facile
Version:       1.1.4
Release:       18%{?dist}
Summary:       OCaml library for constraint programming
Summary(fr):   Librairie OCaml de programmation par contraintes
License:       LGPL-2.1-or-later

URL:           http://facile.recherche.enac.fr/
VCS:           git:%{giturl}.git
Source0:       %{giturl}/releases/download/%{version}/facile-%{version}.tbz

# Build with dune and adapt to recent OCaml changes
# https://github.com/Emmanuel-PLF/facile/pull/2
# The PR does not apply cleanly, so the patch has been modified manually
Patch0:        %{name}-use-dune.patch

# Build with debuginfo and fix an underlinked library
Patch1:        %{name}-debug.patch

BuildRequires: ocaml >= 4.03.0
BuildRequires: ocaml-dune

%description
FaCiLe is a constraint programming library on integer and integer set finite
domains written in OCaml. It offers all usual facilities to create and
manipulate finite domain variables, arithmetic expressions and constraints
(possibly non-linear), built-in global constraints (difference, cardinality,
sorting etc.) and search and optimization goals. FaCiLe allows as well to build
easily user-defined constraints and goals (including recursive ones), making
pervasive use of OCaml higher-order functionals to provide a simple and flexible
interface for the user. As FaCiLe is an OCaml library and not "yet another
language", the user benefits from type inference and strong typing discipline,
high level of abstraction, modules and objects system, as well as native code
compilation efficiency, garbage collection and replay debugger, all features of
OCaml (among many others) that allow to prototype and experiment quickly:
modeling, data processing and interface are implemented with the same powerful
and efficient language.

%description -l fr
FaCiLe est une librairie de Programmation par Contraintes sur les domaines
finis (entiers et ensembles d'entiers) entièrement écrite avec OCaml. FaCiLe
intègre toutes les fonctionnalités standards de création et manipulation de
variables (logiques) à domaine fini, d'expressions et de contraintes
arithmétiques (éventuellement non-linéaires), de contraintes globales
(différence, cardinalité, tri etc.) et de buts de recherche et d'optimisation.
FaCiLe permet aussi de construire facilement de nouvelles contraintes et de
nouveaux buts (éventuellement récursifs) définis par l'utilisateur, à l'aide
d'interfaces simples et puissantes qui utilisent intensivement des fonctions
d'ordre supérieur. Comme FaCiLe est une librairie OCaml et pas "encore un
nouveau langage", l'utilisateur bénéficie de l'inférence de type et du typage
statique strict, d'un haut niveau d'abstraction, des systèmes de modules et
d'objets, ainsi que de l'efficacité du compilateur qui produit du code natif
optimisé (pour toutes les plates-formes courantes), de la gestion automatique de
la mémoire et du débogueur avec retour arrière, autant de caractéristiques
d'OCaml qui permettent de prototyper et expérimenter très rapidement: la
modélisation, le traitement des données et les interfaces sont implémentés à
l'aide du même langage puissant et efficace.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n facile-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
