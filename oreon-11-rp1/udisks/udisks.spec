%global source0_hash f2ec82eb0ea7e01dc299b5b29b3c18cdf861236ec43dcff66b3552b4b31c6f71
%global dbus_version 1.2
%global dbus_glib_version 0.82
%global glib2_version 2.15.0
%global gudev_version 147
%global polkit_version 0.97
%global parted_version 1.8.8
%global udev_version 143
%global mdadm_version 2.6.7
%global device_mapper_version 1.02
%global libatasmart_version 0.14
%global sg3_utils_version 1.27
%global smp_utils_version 0.94
%global systemd_version 185
Summary:        Storage Management Service
Name: udisks
Version: 1.0.5
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://www.freedesktop.org/wiki/Software/udisks
Source0:        http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
Patch0:  udisks-1.0.5-fix-build-with-glibc-2.20.patch
Patch1:  fix_bash_completion.patch
Patch2:  udisks-1.0.5-fix-service-file.patch
Patch3:  udisks-1.0.5-fix-makedev-failure.patch
Requires: dbus >= %{dbus_version}
Requires: udev >= %{udev_version}
Requires: libatasmart >= %{libatasmart_version}
Requires: mdadm >= %{mdadm_version}
Requires: smp_utils >= %{smp_utils_version}
Requires: util-linux
Requires: e2fsprogs
Requires: xfsprogs
Requires: dosfstools
Requires: mtools
Requires: eject
%ifnarch ppc ppc64
Requires: ntfsprogs
%endif
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Conflicts: kernel < 2.6.26
Obsoletes: DeviceKit-disks <= 009
Provides: DeviceKit-disks = 010
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  parted-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libatasmart)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  sg3_utils-devel
BuildRequires:  systemd
# /oreon:deps
%description
udisks provides a daemon, D-Bus API and command line tools
for managing disks and storage devices.

%package devel
Summary: D-Bus interface definitions for udisks
Requires: %{name} = %{version}-%{release}
Obsoletes: DeviceKit-disks-devel <= 009
Provides: DeviceKit-disks-devel = 010
%description devel
D-Bus interface definitions and documentation for udisks.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# https://bugzilla.redhat.com/show_bug.cgi?id=673544#c15
rm -f src/*-glue.h tools/*-glue.h

autoreconf --force --install

%build

%configure --enable-gtk-doc
%make_build
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
ln -s udisks $RPM_BUILD_ROOT%{_bindir}/devkit-disks
ln -s udisks.1 $RPM_BUILD_ROOT%{_datadir}/man/man1/devkit-disks.1
chmod 0644 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/udisks-bash-completion.sh
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
mv $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/udisks-bash-completion.sh \
    $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post udisks.service
%preun

%systemd_preun udisks.service
%postun

%systemd_postun_with_restart udisks.service
%files -f %{oreon_filedir}/main.list
%files -n udisks-devel -f %{oreon_filedir}/udisks-devel.list

%changelog

%autochangelog
