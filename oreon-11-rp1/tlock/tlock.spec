%global source0_hash 28f76aae6f1adaf8de5d85ce0a679e74dfe63fabeae719fea4389ccdf40397ea
Name:           tlock
Version:        1.6
Release:        1%{?dist}
Summary:        Terminal lock
License:        GPL-2.0-or-later
URL:            http://pjp.dgplug.org/tools/
Source0:        http://pjp.dgplug.org/tools/%{name}-%{version}.tar.gz
Patch0:         tlock-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
# /oreon:deps
%description
tlock is a small program intended to lock the terminal until the correct
password is supplied by the user. By default 'tlock' locks the terminal with
the user's login password.

%package        devel
Summary:        Development library for tlock
Requires:       %{name} = %{version}-%{release}
%description    devel
This package contains the header(.h) and library(.so) files required to build
applications using librpass library. librpass is used by, and distributed with
tlock program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
rm -f $RPM_BUILD_ROOT/%{_libdir}/librpass.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tlock-devel -f %{oreon_filedir}/tlock-devel.list

%changelog

%autochangelog
