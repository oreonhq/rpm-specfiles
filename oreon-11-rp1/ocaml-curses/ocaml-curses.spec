%global source0_hash 78141edf97e2de2ce79adbc0abec5a4ae9fbbaaaf09830cecea9e06ff2a263fd

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-curses
Version:        1.0.12
Release:        1%{?dist}
Summary:        OCaml bindings for ncurses
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            https://github.com/mbacarella/curses
VCS:            git:%{url}.git
Source0:        https://github.com/mbacarella/curses/archive/refs/tags/1.0.12.tar.gz#/curses-1.0.12.tar.gz

BuildRequires:  ocaml >= 4.02.0
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(ncurses)


%description
OCaml bindings for ncurses.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ncurses-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n curses-%{version}


%build
%dune_build


%install
%dune_install


%check
%dune_check


%files -f .ofiles
%doc CHANGES.md README.md
%license COPYING


%files devel -f .ofiles-devel
%license COPYING


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.11-18
- Prepare for Oreon 11 (RP1)
