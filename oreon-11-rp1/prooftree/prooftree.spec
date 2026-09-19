%global source0_hash 9de915d949e389b3a4e21d236758d5ed6e6913f85759bddf5282d325bdc9cdcd

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           prooftree
Version:        0.14
Release:        10%{?dist}
Summary:        Proof tree visualization for Proof General

License:        GPL-3.0-or-later
URL:            https://askra.de/software/prooftree/
VCS:            git:%{url}.git
Source:         %{url}/releases/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  ocaml-ocamldoc

%description
Prooftree is a program for proof-tree visualization during interactive proof
development in a theorem prover.  It is currently being developed for Coq and
Proof General.  Prooftree helps against getting lost between different
subgoals in interactive proof development.  It clearly shows where the current
subgoal comes from and thus helps in developing the right plan for solving it.

Prooftree uses different colors for the already proven subgoals, the current
branch in the proof and the still open subgoals.  Sequent texts are not
displayed in the proof tree itself, but they are shown as a tool-tip when the
mouse rests over a sequent symbol.  Long proof commands are abbreviated in the
tree display, but show up in full length as tool-tip.  Both, sequents and
proof commands, can be shown in the display below the tree (on single click)
or in a separate window (on double or shift-click).

Prooftree can mark the proof command that introduced a certain existential
variable and thus help to locate the problem when Coq says:
No more subgoals but non-instantiated existential variables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Preserve timestamps when installing
sed -i 's/cp /cp -p /' Makefile.in

# Adapt to OCaml 5.x
sed -i 's/-I \$(LABLGTKDIR)/& -I +unix/' Makefile.in

%build
# Not an autoconf-generated script.  Do not use %%configure.
./configure --prefix %{_prefix}
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
