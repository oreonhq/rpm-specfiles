%global source0_hash 21362b00653bbfc1c71f71a7578da66b5b5203559d43134d2dd7719e313ce041
%global snap 20251016
%bcond bootstrap 0
Summary:        The NetBSD Editline library
Name:		libedit
Version:	3.1
Release:        1%{?dist}
License:	BSD-3-Clause AND BSD-2-Clause AND ISC
URL:		https://www.thrysoee.dk/editline/
Source0:        https://www.thrysoee.dk/editline//libedit-20251016-3.1.tar.gz
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Libedit is an autotool- and libtoolized port of the NetBSD Editline library.
It provides generic line editing, history, and tokenization functions, similar
to those found in GNU Readline.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	ncurses-devel%{?_isa}
%description devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{snap}-%{version}

%conf
# Fix unused direct shared library dependencies.
sed -i "s/lncurses/ltinfo/" configure

%build

%configure --disable-static --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libedit-devel -f %{oreon_filedir}/libedit-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1-58.
- Prepare for Oreon 11 (RP1)
