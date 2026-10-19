%global source0_hash 3a1d70bef371e42c1b8f779791ee0a3492070ba4ba7d48450167e075570d5f4e
Name:			rasdaemon
Version:		1.0.0
Release:        1%{?dist}
Summary:        Utility to receive RAS error tracings
Group:			Applications/System
License:		GPL-2.0-only
URL:			http://git.infradead.org/users/mchehab/rasdaemon.git
Source0:        https://github.com/mchehab/rasdaemon/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:		s390 s390x
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
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtraceevent-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  sqlite-devel
BuildRequires:  systemd
# /oreon:deps
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
%oreon_prep
%build

%ifarch %{arm} aarch64
%meson -Dsqlite3=enabled -Daer=enabled -Dmce=enabled -Dextlog=enabled -Ddevlink=enabled -Ddiskerror=enabled -Dmemory-failure=enabled -Dabrt-report=enabled -Dcpu-fault-isolation=enabled -Darm=enabled -Dhisi-ns-decode=enabled -Dmemory-ce-pfa=enabled -Damp-ns-decode=enabled
%else
%meson -Dsqlite3=enabled -Daer=enabled -Dmce=enabled -Dextlog=enabled -Ddevlink=enabled -Ddiskerror=enabled -Dmemory-failure=enabled -Dabrt-report=enabled -Dcpu-fault-isolation=enabled
%endif
%meson_build
%install
%meson_install
install -D -p -m 0644 misc/rasdaemon.service %{buildroot}%{_unitdir}/rasdaemon.service
install -D -p -m 0644 misc/ras-mc-ctl.service %{buildroot}%{_unitdir}/ras-mc-ctl.service
install -D -p -m 0655 misc/rasdaemon.env %{buildroot}%{_sysconfdir}/sysconfig/%{name}
rm -f %{buildroot}/usr/include/*.h
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
