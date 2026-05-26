# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-curses
Version:        1.0.11
Release:        18%{?dist}
Summary:        OCaml bindings for ncurses
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            https://github.com/mbacarella/curses
VCS:            git:%{url}.git
Source0:        https://github.com/mbacarella/curses/archive/1.0.11/curses-1.0.11.tar.gz
# oreon url source checksums begin
%global source0_sha256 603c08e816b22e200f7818544ffd016620a808945cfa757dd1aeb245e0b51c0e
%global source0_file curses-1.0.11.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/curses-1.0.11.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "603c08e816b22e200f7818544ffd016620a808945cfa757dd1aeb245e0b51c0e" || { echo "oreon: Source0 SHA256 mismatch for curses-1.0.11.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
