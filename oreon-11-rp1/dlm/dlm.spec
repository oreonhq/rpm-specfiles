# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 ea27de56eaa3a24e39c4d4223e516f5c46bd6a2b056e6b4fae9a36797b6a9fec
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           dlm
Version:        4.3.0
Release:        8%{?dist}
License:	GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        dlm control daemon and tool
URL:            https://pagure.io/dlm
BuildRequires:  gcc
BuildRequires:  glibc-kernheaders
BuildRequires:  corosynclib-devel >= 3.1.0
BuildRequires:  pacemaker-libs-devel >= 1.1.7
BuildRequires:  libxml2-devel
BuildRequires:  systemd-units
BuildRequires:  systemd-devel
BuildRequires: make
Source0:	https://releases.pagure.org/dlm/%{name}-%{version}.tar.gz

%if 0%{?rhel} && 0%{?rhel} <= 7
ExclusiveArch: i686 x86_64
%endif

Requires:       %{name}-lib = %{version}-%{release}
Requires:       corosync >= 3.1.0
%{?fedora:Requires: kernel-modules-extra}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
The kernel dlm requires a user daemon to control membership.

%prep
%oreon_verify_sources
%setup -q

%build
# upstream does not require configure
# upstream does not support parallel builds
%set_build_flags
%make_build -j1
%make_build -j1 -C fence

%install
%make_install LIBDIR=%{_libdir} BINDIR=%{_sbindir}
make -C fence install LIBDIR=%{_libdir} DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_sbindir}

install -Dm 0644 init/dlm.service %{buildroot}%{_unitdir}/dlm.service
install -Dm 0644 init/dlm.sysconfig %{buildroot}/etc/sysconfig/dlm

%post
%systemd_post dlm.service

%preun
%systemd_preun dlm.service

%postun
%systemd_postun_with_restart dlm.service

%files
%doc README.license
%{_unitdir}/dlm.service
%{_sbindir}/dlm_controld
%{_sbindir}/dlm_tool
%{_sbindir}/dlm_stonith
%{_mandir}/man8/dlm*
%{_mandir}/man5/dlm*
%{_mandir}/man3/*dlm*
%config(noreplace) %{_sysconfdir}/sysconfig/dlm

%package        lib
Summary:        Library for %{name}
Conflicts:      clusterlib

%description    lib
The %{name}-lib package contains the libraries needed to use the dlm
from userland applications.

%ldconfig_scriptlets lib

%files          lib
/usr/lib/udev/rules.d/*-dlm.rules
%{_libdir}/libdlm*.so.*

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-lib = %{version}-%{release}
Conflicts:      clusterlib-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files          devel
%{_libdir}/libdlm*.so
%{_includedir}/libdlm*.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3.0-8
- Prepare for Oreon 11 (RP1)
