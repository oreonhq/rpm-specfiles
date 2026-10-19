%global source0_hash 2552a706695f4274022e5b4d9ee4338df78af0cd7ee535cb5bb38a6b33848745
Name:           sanlock
Version:        5.1.1
Release:        1%{?dist}
Summary:        A shared storage lock manager
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://pagure.io/sanlock/
Requires:       %{name}-lib = %{version}-%{release}
Requires(post): systemd-units
Requires(post): systemd-sysv
Requires(preun): systemd-units
Requires(postun): systemd-units
Source0:        https://codeberg.org/sanlock/sanlock/archive/sanlock-5.0.0.tar.gz#/sanlock-%{version}.tar.gz
# oreon:deps
BuildRequires:  device-mapper-devel
BuildRequires:  gcc
BuildRequires:  libaio-devel
BuildRequires:  libblkid-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-units
# /oreon:deps
%description
The sanlock daemon manages leases for applications on hosts using shared storage.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n sanlock
#%%patch0 -p1

%build

%set_build_flags
CFLAGS=$RPM_OPT_FLAGS make -C wdmd
CFLAGS=$RPM_OPT_FLAGS make -C src
CFLAGS=$RPM_OPT_FLAGS make -C python PY_VERSION=3
%install
rm -rf $RPM_BUILD_ROOT
make -C src \
        install LIBDIR=%{_libdir} BINDIR=%{_sbindir} \
        DESTDIR=$RPM_BUILD_ROOT
make -C wdmd \
        install LIBDIR=%{_libdir} BINDIR=%{_sbindir} \
        DESTDIR=$RPM_BUILD_ROOT
make -C python \
        install LIBDIR=%{_libdir} BINDIR=%{_sbindir} \
        DESTDIR=$RPM_BUILD_ROOT \
        PY_VERSION=3
install -D -m 0644 init.d/sanlock.service.native $RPM_BUILD_ROOT%{_unitdir}/sanlock.service
install -D -m 0755 init.d/systemd-wdmd $RPM_BUILD_ROOT%{_prefix}/lib/systemd/systemd-wdmd
install -D -m 0644 init.d/wdmd.service $RPM_BUILD_ROOT%{_unitdir}/wdmd.service
install -p -D -m 0644 src/sanlock.sysusers $RPM_BUILD_ROOT/%{_sysusersdir}/sanlock.conf
install -D -m 0644 src/logrotate.sanlock \
    $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/sanlock
install -D -m 0644 src/sanlock.conf \
    $RPM_BUILD_ROOT%{_sysconfdir}/sanlock/sanlock.conf
install -D -m 0644 init.d/wdmd.sysconfig \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/wdmd
install -Dd -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/wdmd.d
install -Dd -m 0755 $RPM_BUILD_ROOT%{_sharedstatedir}/sanlock
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post wdmd.service sanlock.service
%preun

%systemd_preun wdmd.service sanlock.service
%postun

%systemd_postun wdmd.service sanlock.service
%package        lib
Summary:        A shared storage lock manager library
%description    lib
The %{name}-lib package contains the runtime libraries for sanlock,
a shared storage lock manager.
Hosts connected to a common SAN can use this to synchronize their
access to the shared disks.

%ldconfig_scriptlets lib

%package        -n python3-sanlock
%{?python_provide:%python_provide python3-sanlock}
Summary:        Python bindings for the sanlock library
Requires:       %{name}-lib = %{version}-%{release}
%description    -n python3-sanlock
The %{name}-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the sanlock library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-lib = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -f %{oreon_filedir}/main.list
%files -n sanlock-lib -f %{oreon_filedir}/sanlock-lib.list
%files -n python3-sanlock -f %{oreon_filedir}/python3-sanlock.list
%files -n sanlock-devel -f %{oreon_filedir}/sanlock-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.0-1
- Prepare for Oreon 11 (RP1)
