%global source0_hash 7240dafe35e17b01134591d7ae8f09f5a375cded8b01e43ba97ca3610a09ea61
Name:           nsnake
Version:        3.0.1
Release:        1%{?dist}
Summary:        The classic snake game with textual interface
URL:            https://github.com/alexdantas/nSnake
Source0:        https://github.com/alexdantas/nSnake/archive/v%{version}.tar.gz#/nSnake-%{version}.tar.gz
License:        GPL-3.0-or-later
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
