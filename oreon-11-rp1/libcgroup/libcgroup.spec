# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 64378ec85eb4b46d1536a26120ad6cf9012a3a66d33ec9dec2fba88055c6001a
%global source1_sha256 20cb815c855bf97fb79b50b93464e397e267a6d077bacda338f752b28390da6e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source1_sha256:%(test -z "%{source1_sha256}" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_sha256}" || { echo "oreon: Source1 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%bcond_with tests

%global tests_commit 7c998caddcd8236fe4191841e361b401697fb777

Summary: Library to control and monitor control groups
Name: libcgroup
Version: 3.0
Release: 10%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: http://libcg.sourceforge.net/
Source0: https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1: https://github.com/%{name}/%{name}-tests/archive/%{tests_commit}.tar.gz
Source2: cgconfig.service

Patch0: fedora-config.patch
Patch1: libcgroup-0.37-chmod.patch
Patch2: libcgroup-0.40.rc1-coverity.patch
Patch3: libcgroup-0.40.rc1-fread.patch
Patch4: libcgroup-0.40.rc1-templates-fix.patch

Patch100: libcgroup-tests-unbundle-gtest.patch

BuildRequires: autoconf, automake, libtool
BuildRequires: gcc, gcc-c++
BuildRequires: byacc, coreutils, flex, pam-devel, systemd-units
BuildRequires: make
%if %{with tests}
BuildRequires: gtest-devel
%endif
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Control groups infrastructure. The library helps manipulate, control,
administrate and monitor control groups and the associated controllers.

%package tools
Summary: Command-line utility programs, services and daemons for libcgroup
Requires: %{name}%{?_isa} = %{version}-%{release}
# needed for Delegate property in cgconfig.service
Requires: systemd >= 217-0.2

%description tools
This package contains command-line programs, services and a daemon for
manipulating control groups using the libcgroup library.

%package pam
Summary: A Pluggable Authentication Module for libcgroup
Requires: %{name}%{?_isa} = %{version}-%{release}

%description pam
Linux-PAM module, which allows administrators to classify the user's login
processes to pre-configured control group.

%package devel
Summary: Development libraries to develop applications that utilize control groups
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
It provides API to create/delete and modify cgroup nodes. It will also in the
future allow creation of persistent configuration for control groups and
provide scripts to manage that configuration.

%prep
%oreon_verify_sources
%setup  -q  -n %{name}-%{version}
%patch -P0 -p1 -b .config-patch
%patch -P1 -p1 -b .chmod
%patch -P2 -p1 -b .coverity
%patch -P3 -p1 -b .fread
%patch -P4 -p1 -b .templates-fix

%setup -D -T -a 1
mv -T %{name}-tests-%{tests_commit} tests
%patch -P100 -p1 -b .tests-unbundle-gtest

%build
autoreconf -vif
%configure --enable-pam-module-dir=%{_libdir}/security \
           --enable-opaque-hierarchy="name=systemd" \
           --disable-daemon
%make_build

%install
%make_install

# install config files
install -d ${RPM_BUILD_ROOT}%{_sysconfdir}
install -m 644 samples/config/cgconfig.conf $RPM_BUILD_ROOT/%{_sysconfdir}/cgconfig.conf
install -m 644 samples/config/cgsnapshot_blacklist.conf $RPM_BUILD_ROOT/%{_sysconfdir}/cgsnapshot_blacklist.conf

# sanitize pam module, we need only pam_cgroup.so
rm -f $RPM_BUILD_ROOT%{_libdir}/security/pam_cgroup.{,l}a

rm -f $RPM_BUILD_ROOT/%{_libdir}/*.{,l}a

rm -f $RPM_BUILD_ROOT/%{_libdir}/libcgroupfortesting.*

rm -f $RPM_BUILD_ROOT/%{_mandir}/man5/cgred.conf.5*
rm -f $RPM_BUILD_ROOT/%{_mandir}/man5/cgrules.conf.5*
rm -f $RPM_BUILD_ROOT/%{_mandir}/man8/cgrulesengd.8*

# install unit and sysconfig files
install -d ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %SOURCE2 ${RPM_BUILD_ROOT}%{_unitdir}/
install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig

%check
%if %{with tests}
make -C tests/gunit check
%endif

%post tools
%systemd_post cgconfig.service

%preun tools
%systemd_preun cgconfig.service

%postun tools
%systemd_postun_with_restart cgconfig.service

%triggerun -- libcgroup < 0.38
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply cgconfig
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save cgconfig >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del cgconfig >/dev/null 2>&1 || :
/bin/systemctl try-restart cgconfig.service >/dev/null 2>&1 || :

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%{_libdir}/libcgroup.so.3*

%files tools
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README README_systemd
%config(noreplace) %{_sysconfdir}/cgconfig.conf
%config(noreplace) %{_sysconfdir}/cgsnapshot_blacklist.conf
%{_bindir}/cgcreate
%{_bindir}/cgget
%{_bindir}/cgset
%{_bindir}/cgxget
%{_bindir}/cgxset
%{_bindir}/cgdelete
%{_bindir}/lscgroup
%{_bindir}/lssubsys
%{_sbindir}/cgconfigparser
%{_bindir}/cgsnapshot
%{_bindir}/cgclassify
%attr(0755, root, root) %{_bindir}/cgexec
%attr(0644, root, root) %{_mandir}/man1/*
%attr(0644, root, root) %{_mandir}/man5/*
%attr(0644, root, root) %{_mandir}/man8/*
%{_unitdir}/cgconfig.service

%files pam
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%attr(0755,root,root) %{_libdir}/security/pam_cgroup.so

%files devel
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%{_includedir}/libcgroup.h
%{_includedir}/libcgroup/*.h
%{_libdir}/libcgroup.so
%{_libdir}/pkgconfig/libcgroup.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0-10
- Prepare for Oreon 11 (RP1)
