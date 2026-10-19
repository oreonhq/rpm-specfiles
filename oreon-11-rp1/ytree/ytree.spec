%global source0_hash caeeeac334dac83921bd8b657ad2d4cf234c15da4ffc7d15dad0bda99e52f197
%global debug_package %{nil}
Summary:        A filemanager similar to XTree
Name:		ytree
Version:	2.13
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		https://www.han.de/~werner/ytree.html
Source0:        https://www.han.de/~werner/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
A console based file manager in the tradition of Xtree.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
install -m644 -D -p ytree.1 $RPM_BUILD_ROOT/%{_mandir}/man1/ytree.1
install -m755 -D -p ytree $RPM_BUILD_ROOT/%{_bindir}/ytree
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
