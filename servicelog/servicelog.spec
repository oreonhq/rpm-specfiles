Name:           servicelog
Version:        1.1.16
Release:        10%{?dist}
Summary:        Servicelog Tools

License:        GPL-2.0-only
URL:            https://github.com/power-ras/servicelog
Source0:        https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  libservicelog-devel >= 1.1.9-2
BuildRequires:  autoconf libtool librtas-devel help2man

# because of librtas-devel in libservicelog
ExclusiveArch: ppc %{power64}

%description
Command-line interfaces for viewing and manipulating the contents of
the servicelog database. Contains entries that are useful
for performing system service operations, and for providing a history
of service operations that have been performed on the system.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
help2man -s 8 -N $RPM_BUILD_ROOT/%{_sbindir}/slog_common_event > $RPM_BUILD_ROOT/%{_mandir}/man8/slog_common_event.8

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/servicelog
%{_bindir}/v1_servicelog
%{_bindir}/v29_servicelog
%{_bindir}/servicelog_notify
%{_bindir}/log_repair_action
%{_sbindir}/slog_common_event
%{_bindir}/servicelog_manage
%{_mandir}/man[18]/*.[18]*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.16-10
- Prepare for Oreon 11 (RP1)
