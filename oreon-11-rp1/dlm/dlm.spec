%global source0_hash ea27de56eaa3a24e39c4d4223e516f5c46bd6a2b056e6b4fae9a36797b6a9fec
Name:           dlm
Version:        4.3.0
Release:        1%{?dist}
License:	GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        dlm control daemon and tool
URL:            https://pagure.io/dlm
Source0:        https://deb.debian.org/debian/pool/main/d/dlm/dlm_%{version}.orig.tar.gz#/dlm-%{version}.tar.gz
Requires:       %{name}-lib = %{version}-%{release}
Requires:       corosync >= 3.1.0
%{?fedora:Requires: kernel-modules-extra}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
# oreon:deps
BuildRequires:  corosynclib-devel
BuildRequires:  gcc
BuildRequires:  glibc-kernheaders
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pacemaker-libs-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
# /oreon:deps
%description
The kernel dlm requires a user daemon to control membership.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%set_build_flags
%make_build -j1
%make_build -j1 -C fence
%install
%make_install LIBDIR=%{_libdir} BINDIR=%{_sbindir}
make -C fence install LIBDIR=%{_libdir} DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_sbindir}
install -Dm 0644 init/dlm.service %{buildroot}%{_unitdir}/dlm.service
install -Dm 0644 init/dlm.sysconfig %{buildroot}/etc/sysconfig/dlm
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post dlm.service
%preun

%systemd_preun dlm.service
%postun

%systemd_postun_with_restart dlm.service
%package        lib
Summary:        Library for %{name}
Conflicts:      clusterlib
%description    lib
The %{name}-lib package contains the libraries needed to use the dlm
from userland applications.

%ldconfig_scriptlets lib

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-lib = %{version}-%{release}
Conflicts:      clusterlib-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -f %{oreon_filedir}/main.list
%files -n dlm-lib -f %{oreon_filedir}/dlm-lib.list
%files -n dlm-devel -f %{oreon_filedir}/dlm-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3.0-8
- Prepare for Oreon 11 (RP1)
