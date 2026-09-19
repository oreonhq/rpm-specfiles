%global source0_hash 0c4f454d6185617f67e6ebe60c6735f481ea46460c84e2132a1c47090cf8b857

Name: sheepdog
Summary: The Sheepdog distributed storage system for KVM/QEMU
Version: 1.0.1
Release: 26%{?dist}
# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License: GPL-2.0-only AND GPL-2.0-or-later
URL: http://sheepdog.github.io/sheepdog
Source0: https://github.com/sheepdog/sheepdog/archive/v1.0.1.tar.gz
Source1: sheepdog.service
Source2: sheepdog.timer
Source3: sheepdog

Patch0: sha1-extern.patch

%{?systemd_requires}

# Build bits
BuildRequires: make
BuildRequires: autoconf automake libtool systemd
BuildRequires: corosync corosynclib corosynclib-devel
BuildRequires: userspace-rcu-devel

# For sheepfs
BuildRequires: fuse-devel

%ifarch x86_64
BuildRequires: yasm
%endif

# corosync not available on these architectures
%if 0%{?rhel} >= 6
Excludearch: aarch64
Excludearch: ppc 
Excludearch: ppc64
Excludearch: ppc64le
%endif

%description
This package contains the Sheepdog server and the "dog" command line tool,
which offer a distributed object storage system for KVM.

%package devel
Summary: Header files for the Sheepdog distributed storage system
# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License: GPL-2.0-only AND GPL-2.0-or-later
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files for libsheepdog.

%package libs
Summary: Libraries for the Sheepdog distributed storage system
# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License: GPL-2.0-only AND GPL-2.0-or-later

%description libs
This package contains the libsheepdog shared library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

# urcu/compiler.h from userspace-rcu-devel requires __STDC_VERSION__ 201112L
sed -r -i 's/-std=gnu99/-std=gnu23/' configure.ac

%build
./autogen.sh

# TODO: add LTTng-ust support
%{configure} \
  --without-initddir \
  --without-systemdsystemunitdir \
  --disable-static

make %{_smp_mflags} V=1

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/libsheepdog.la
rm -f %{buildroot}/%{_libdir}/libsheepdog.a

mkdir -p %{buildroot}/%{_unitdir}
cp -a %{SOURCE1} %{buildroot}/%{_unitdir}/
cp -a %{SOURCE2} %{buildroot}/%{_unitdir}/

mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig
cp -a %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysconfig

%post
%systemd_post sheepdog.timer

%preun
%systemd_preun sheepdog.timer

%postun
%systemd_postun_with_restart sheepdog.timer

%files
%doc COPYING README
%{_bindir}/dog
%{_sbindir}/sheep
%{_sbindir}/sheepfs
%{_sbindir}/shepherd
%{_sysconfdir}/bash_completion.d/dog

%{_unitdir}/sheepdog.service
%{_unitdir}/sheepdog.timer
%config %{_sysconfdir}/sysconfig/sheepdog

%dir %{_localstatedir}/lib/sheepdog
%{_mandir}/man8/sheep.8*
%{_mandir}/man8/dog.8*
%{_mandir}/man8/sheepfs.8*

%files devel
%dir %{_includedir}/sheepdog
%{_includedir}/sheepdog/internal.h
%{_includedir}/sheepdog/list.h
%{_includedir}/sheepdog/sheepdog.h
%{_includedir}/sheepdog/sheepdog_proto.h
%{_includedir}/sheepdog/util.h

%files libs
%{_libdir}/libsheepdog.so

%changelog
%autochangelog
