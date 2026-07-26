%global source0_hash 3bbbbd32f568cdae3e03fc735b1783d8cba605a2ca6056d1b971143d7ddd517d

%global debug_package %{nil}

Summary:	A filemanager similar to XTree
Name:		ytree
Version:	2.10
Release:	%autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://www.han.de/~werner/ytree.html
Source0:	https://www.han.de/~werner/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	ncurses-devel >= 5.4
BuildRequires:	readline-devel >= 4.3 

%description
A console based file manager in the tradition of Xtree.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build

%install
install -m644 -D -p ytree.1 $RPM_BUILD_ROOT/%{_mandir}/man1/ytree.1
install -m755 -D -p ytree $RPM_BUILD_ROOT/%{_bindir}/ytree

%files 
%doc CHANGES COPYING README THANKS ytree.conf
%doc %{_mandir}/man1/ytree.1.gz
%{_bindir}/ytree

%changelog
%autochangelog
