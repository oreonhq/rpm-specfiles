%global source0_hash 7cb4e6f316daede4fa54547371d5c986395177c12dbdec74a66298e684ac8b85

Name:           eventlog
Version:        0.2.13
Release:        31%{?dist}
Summary:        Syslog-ng v2/v3 support library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.balabit.com/network-security/syslog-ng/opensource-logging-system
Source:         http://www.balabit.com/downloads/files/syslog-ng/open-source-edition/3.4.4/source/%{name}_%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

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

%files
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README
%{_libdir}/libevtlog.so.*

%files devel
%doc doc/*
%{_libdir}/libevtlog.so
%{_libdir}/pkgconfig/eventlog.pc
%dir %{_includedir}/%{name}
%{_includedir}/%{name}

%files static
%{_libdir}/libevtlog.a

%changelog
%autochangelog
