%global source0_hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Name:           eventlog
Version:        0.2.13
Release:        1%{?dist}
Summary:        Syslog-ng v2/v3 support library
License:        LicenseRef-Callaway-BSD
URL:            http://www.balabit.com/network-security/syslog-ng/opensource-logging-system
Source0:        http://www.balabit.com/downloads/files/syslog-ng/open-source-edition/3.4.4/source/%{name}_%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The EventLog library aims to be a replacement of the simple syslog() API
provided on UNIX systems. The major difference between EventLog and syslog
is that EventLog tries to add structure to messages.

EventLog provides an interface to build, format and output an event record.
The exact format and output method can be customized by the administrator
via a configuration file.

This package is the runtime part of the library.

%package devel
Summary:        Syslog-ng v2/v3 support library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The EventLog library aims to be a replacement of the simple syslog() API
provided on UNIX systems. The major difference between EventLog and syslog
is that EventLog tries to add structure to messages.

EventLog provides an interface to build, format and output an event record.
The exact format and output method can be customized by the administrator
via a configuration file.

This package contains the development files.

%package static
Summary:        Syslog-ng v2/v3 support static library files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description static
The EventLog library aims to be a replacement of the simple syslog() API
provided on UNIX systems. The major difference between EventLog and syslog
is that EventLog tries to add structure to messages.

EventLog provides an interface to build, format and output an event record.
The exact format and output method can be customized by the administrator
via a configuration file.

This package contains the static library files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/libevtlog.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n eventlog-devel -f %{oreon_filedir}/eventlog-devel.list
%files -n eventlog-static -f %{oreon_filedir}/eventlog-static.list

%changelog

%autochangelog
