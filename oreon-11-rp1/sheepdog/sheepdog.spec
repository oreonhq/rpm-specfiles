%global source0_hash 0c4f454d6185617f67e6ebe60c6735f481ea46460c84e2132a1c47090cf8b857
Name: sheepdog
Summary:        The Sheepdog distributed storage system for KVM/QEMU
Version: 1.0.1
Release:        1%{?dist}
License: GPL-2.0-only AND GPL-2.0-or-later
URL: http://sheepdog.github.io/sheepdog
Source0:        https://github.com/sheepdog/sheepdog/archive/v1.0.1.tar.gz
Source1: sheepdog.service
Source2: sheepdog.timer
Source3: sheepdog
Patch0: sha1-extern.patch
%{?systemd_requires}
%ifarch x86_64
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  corosync
BuildRequires:  corosynclib
BuildRequires:  corosynclib-devel
BuildRequires:  fuse-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  userspace-rcu-devel
# /oreon:deps
%description
This package contains the Sheepdog server and the "dog" command line tool,
which offer a distributed object storage system for KVM.

%package devel
Summary: Header files for the Sheepdog distributed storage system
License: GPL-2.0-only AND GPL-2.0-or-later
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files for libsheepdog.

%package libs
Summary: Libraries for the Sheepdog distributed storage system
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post sheepdog.timer
%preun

%systemd_preun sheepdog.timer
%postun

%systemd_postun_with_restart sheepdog.timer
%files -f %{oreon_filedir}/main.list
%files -n sheepdog-devel -f %{oreon_filedir}/sheepdog-devel.list
%files -n sheepdog-libs -f %{oreon_filedir}/sheepdog-libs.list

%changelog

%autochangelog
