%global source0_hash ef0b8df430746b3907f8d0808e7fdd1f8bf2ebdfa098a4f8db1edbf89a760349

Name:			rasdaemon
Version:		0.8.0
Release:		9%{?dist}
Summary:		Utility to receive RAS error tracings
Group:			Applications/System
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:		GPL-2.0-only
URL:			http://git.infradead.org/users/mchehab/rasdaemon.git
Source0:        http://www.infradead.org/~mchehab/rasdaemon/%{name}-%{version}.tar.bz2

ExcludeArch:		s390 s390x
BuildRequires:		make
BuildRequires:		gcc
BuildRequires:		autoconf automake libtool
BuildRequires:		gettext-devel
BuildRequires:		perl-generators
BuildRequires:		sqlite-devel
BuildRequires:		systemd
BuildRequires:		libtraceevent-devel
Provides:		bundled(kernel-event-lib)
Requires:		hwdata
Requires:		perl-DBD-SQLite
Requires:		libtraceevent
%ifarch %{ix86} x86_64
Requires:		dmidecode
%endif

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
%{name} is a RAS (Reliability, Availability and Serviceability) logging tool.
It currently records memory errors, using the EDAC tracing events.
EDAC is drivers in the Linux kernel that handle detection of ECC errors
from memory controllers for most chipsets on i386 and x86_64 architectures.
EDAC drivers for other architectures like arm also exists.
This userspace component consists of an init script which makes sure
EDAC drivers and DIMM labels are loaded at system startup, as well as
an utility for reporting current error counts from the EDAC sysfs files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
autoreconf -vfi

%build
%ifarch %{arm} aarch64
%configure --enable-sqlite3 --enable-aer --enable-non-standard --enable-arm \
	   --enable-mce --enable-extlog --enable-devlink --enable-diskerror \
	   --enable-memory-failure --enable-abrt-report --enable-hisi-ns-decode \
	   --enable-memory-ce-pfa --enable-amp-ns-decode --enable-cpu-fault-isolation \
	   --with-sysconfdefdir=%{_sysconfdir}/sysconfig
%else
%configure --enable-sqlite3 --enable-aer \
	   --enable-mce --enable-extlog --enable-devlink --enable-diskerror \
	   --enable-memory-failure --enable-abrt-report --enable-cpu-fault-isolation \
	   --with-sysconfdefdir=%{_sysconfdir}/sysconfig
%endif
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -D -p -m 0644 misc/rasdaemon.service %{buildroot}%{_unitdir}/rasdaemon.service
install -D -p -m 0644 misc/ras-mc-ctl.service %{buildroot}%{_unitdir}/ras-mc-ctl.service
install -D -p -m 0655 misc/rasdaemon.env %{buildroot}%{_sysconfdir}/sysconfig/%{name}
rm INSTALL %{buildroot}/usr/include/*.h

%files
%doc AUTHORS ChangeLog COPYING README.md TODO
%{_sbindir}/rasdaemon
%{_sbindir}/ras-mc-ctl
%{_mandir}/*/*
%{_unitdir}/*.service
%{_sysconfdir}/ras/dimm_labels.d
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.0-9
- Import
