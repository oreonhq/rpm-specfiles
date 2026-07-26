%global source0_hash 7240dafe35e17b01134591d7ae8f09f5a375cded8b01e43ba97ca3610a09ea61

Name:           nsnake
Version:        3.0.1
Release:        24%{?dist}
Summary:        The classic snake game with textual interface
# the old homepage is down
#URL:            http://nsnake.alexdantas.net/
URL:            https://github.com/alexdantas/nSnake
Source0:        https://github.com/alexdantas/nSnake/archive/v%{version}.tar.gz#/nSnake-%{version}.tar.gz
License:        GPL-3.0-or-later
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  ncurses-devel

%description
nSnake is a implementation of the classic snake game with textual interface.
It is playable at command-line and uses the nCurses C library for graphics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn nSnake-%{version}
sed -i -r 's/^VERSION =.*/VERSION = %{version}/' Makefile

%build
make CFLAGS_PLATFORM="%{optflags}" LDFLAGS_PLATFORM="%{?__global_ldflags}" V=1 %{?_smp_mflags}
make doc

%install
%make_install

%files
%doc AUTHORS BUGS ChangeLog README.md TODO doc/html
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/nsnake.6*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/games/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm

%changelog
%autochangelog
