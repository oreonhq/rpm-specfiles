%global source0_hash 28f76aae6f1adaf8de5d85ce0a679e74dfe63fabeae719fea4389ccdf40397ea

Name:           tlock
Version:        1.6
Release:        26%{?dist}
Summary:        Terminal lock

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pjp.dgplug.org/tools/
Source0:        http://pjp.dgplug.org/tools/%{name}-%{version}.tar.gz
Patch0:         tlock-c99.patch

BuildRequires: make
BuildRequires: libxcrypt-devel
BuildRequires:  gcc
BuildRequires:  ncurses-devel pam-devel

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

%autosetup -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
rm -f $RPM_BUILD_ROOT/%{_libdir}/librpass.la

%files
%doc README COPYING
%_bindir/tlock
%_libdir/lib*.so.*
%_infodir/*
%_mandir/man1/*

%files devel
%doc README COPYING
%_includedir/readpass.h
%_libdir/lib*.so
%_mandir/man3/*

%changelog
%autochangelog
