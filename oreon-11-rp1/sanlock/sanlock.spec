Name:           sanlock
Version:        5.0.0
Release:        1%{?dist}
Summary:        A shared storage lock manager
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://pagure.io/sanlock/
BuildRequires:  gcc
BuildRequires:  libaio-devel
BuildRequires:  libblkid-devel
BuildRequires:  libuuid-devel
# TODO: This creates a cyclic dependency, as lvm2 depends on sanlock-devel
BuildRequires:  device-mapper-devel
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  systemd-units
BuildRequires:  python3-setuptools
Requires:       %{name}-lib = %{version}-%{release}
Requires(post): systemd-units
Requires(post): systemd-sysv
Requires(preun): systemd-units
Requires(postun): systemd-units
Source0:        https://releases.pagure.org/sanlock/%{name}-%{version}.tar.gz

# Patch0: 0001-foo.patch

%description
The sanlock daemon manages leases for applications on hosts using shared storage.

%prep
%setup -q
#%%patch0 -p1

%build
%set_build_flags
# upstream does not require configure
# upstream does not support _smp_mflags
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

%if 0%{?fedora} < 42
%pre
# As libvirt does, install a sysusers file, but also directly
# create the user and group to avoid rpm installation errors
# (sysusers rpm macros seem to be insufficient to avoid problems.)
getent group sanlock > /dev/null || /usr/sbin/groupadd \
    -g 179 sanlock
getent passwd sanlock > /dev/null || /usr/sbin/useradd \
    -u 179 -c "sanlock" -s /sbin/nologin -r \
    -g 179 -d /run/sanlock sanlock
/usr/sbin/usermod -a -G disk sanlock
%endif

%post
%systemd_post wdmd.service sanlock.service

%preun
%systemd_preun wdmd.service sanlock.service

%postun
%systemd_postun wdmd.service sanlock.service

%files
%{_prefix}/lib/systemd/systemd-wdmd
%{_unitdir}/sanlock.service
%{_unitdir}/wdmd.service
%{_sbindir}/sanlock
%{_sbindir}/wdmd
%dir %{_sysconfdir}/wdmd.d
%dir %{_sysconfdir}/sanlock
%dir %{_sharedstatedir}/sanlock
%{_mandir}/man8/wdmd*
%{_mandir}/man8/sanlock*
%config(noreplace) %{_sysconfdir}/logrotate.d/sanlock
%config(noreplace) %{_sysconfdir}/sanlock/sanlock.conf
%config(noreplace) %{_sysconfdir}/sysconfig/wdmd
%{_sysusersdir}/sanlock.conf

%package        lib
Summary:        A shared storage lock manager library

%description    lib
The %{name}-lib package contains the runtime libraries for sanlock,
a shared storage lock manager.
Hosts connected to a common SAN can use this to synchronize their
access to the shared disks.

%ldconfig_scriptlets lib

%files          lib
%{_libdir}/libsanlock.so.*
%{_libdir}/libsanlock_client.so.*
%{_libdir}/libwdmd.so.*

%package        -n python3-sanlock
%{?python_provide:%python_provide python3-sanlock}
Summary:        Python bindings for the sanlock library
Requires:       %{name}-lib = %{version}-%{release}

%description    -n python3-sanlock
The %{name}-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the sanlock library.

%files          -n python3-sanlock
%{python3_sitearch}/sanlock_python-*.egg-info
%{python3_sitearch}/sanlock*.so

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-lib = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files          devel
%{_libdir}/libwdmd.so
%{_includedir}/wdmd.h
%{_libdir}/libsanlock.so
%{_libdir}/libsanlock_client.so
%{_includedir}/sanlock.h
%{_includedir}/sanlock_rv.h
%{_includedir}/sanlock_admin.h
%{_includedir}/sanlock_resource.h
%{_includedir}/sanlock_direct.h
%{_libdir}/pkgconfig/libsanlock.pc
%{_libdir}/pkgconfig/libsanlock_client.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.0-1
- Prepare for Oreon 11 (RP1)
