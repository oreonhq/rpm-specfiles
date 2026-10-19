%global source0_hash 95c76ade0c31c9f6d297192473733bb04919bc0bf3fdbf0c625245b556a9af33
%global somajor 8
Name:           transactional-update
Version:        6.1.3
Release:        1%{?dist}
Summary:        Transactional Updates with btrfs and snapshots
License:        GPL-2.0-or-later and LGPL-2.1-or-later
URL:            https://github.com/openSUSE/transactional-update
Source0:        https://github.com/openSUSE/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  /bin/w3m
BuildRequires:  /bin/xmllint
BuildRequires:  /bin/xsltproc
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(libeconf)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  python3dist(lxml)
# /oreon:deps
%description
transactional-update is a tool to update a system in an atomic
way with btrfs and snapshots.

#--------------------------------------------------------------------

%package -n tukit
Summary:        Tool for doing transactional updates using Btrfs snapshots
License:        GPL-2.0-or-later
Requires:       libtukit%{?_isa} = %{version}-%{release}
%description -n tukit
tukit is a simple tool to make changes to a system in an atomic way
with btrfs and snapshots.

%post -n tukit

%systemd_post create-dirs-from-rpmdb.service prepare-nextroot-for-softreboot.service
%preun -n tukit

%systemd_preun create-dirs-from-rpmdb.service prepare-nextroot-for-softreboot.service
%package -n tukitd
Summary:        D-Bus based service for transactional updates
License:        GPL-2.0-or-later
Requires:       libtukit%{?_isa} = %{version}-%{release}
Requires:       dbus-common
%description -n tukitd
tukitd is a D-Bus based service interface to make changes to a system
in an atomic way with btrfs and snapshots.

%post -n tukitd

%systemd_post tukitd.service
%preun -n tukitd

%systemd_preun tukitd.service
%postun -n tukitd

%systemd_postun_with_restart tukitd.service
%package -n dracut-%{name}
Summary:        Dracut module for supporting transactional updates
License:        GPL-2.0-or-later
Supplements:    (tukit and kernel)
Requires:       tukit = %{version}-%{release}
%description -n dracut-%{name}
This package contains the dracut modules for handling early boot aspects
for transactional updates.

%package -n libtukit
Summary:        Library for doing transactional updates using Btrfs snapshots
License:        GPL-2.0-or-later or LGPL-2.1-or-later
Obsoletes:      tukit-libs < 3.2.0-2
Provides:       tukit-libs = %{version}-%{release}
Provides:       tukit-libs%{?_isa} = %{version}-%{release}
Requires:       btrfs-progs
Requires:       lsof
Requires:       rsync
Requires:       snapper
%description -n libtukit
This package contains the libraries required for programs to do
transactional updates using btrfs snapshots.

%package -n tukit-devel
Summary:        Development files for tukit library
License:        GPL-2.0-or-later or LGPL-2.1-or-later
Requires:       libtukit%{?_isa} = %{version}-%{release}
%description -n tukit-devel
This package contains the files required to develop programs to do
transactional updates using btrfs snapshots.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# use libexecdir for snapper stuff
find -type f -exec sed -i -e "s|lib/snapper|libexec/snapper|g" {} ';'

%build

autoreconf -fiv
%configure --disable-static
%make_build
%install
%make_install
rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_sbindir}/transactional-update*
rm -rf %{buildroot}%{_sbindir}/tu-rebuild-kdump-initrd
rm -rf %{buildroot}%{_unitdir}/transactional-update*
rm -rf %{buildroot}%{_prefix}%{_sysconfdir}
rm -rf %{buildroot}%{_sysconfdir}
rm -rf %{buildroot}%{_mandir}/man*/transactional-update*
rm -rf %{buildroot}%{_docdir}
%oreon_autofiles tukit usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles tukitd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libtukit usr/*/lib*.so.*
%oreon_autofiles tukit-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tukit -f %{oreon_filedir}/tukit.list
%files -n tukitd -f %{oreon_filedir}/tukitd.list
%files -n dracut-transactional-update -f %{oreon_filedir}/dracut-transactional-update.list
%files -n libtukit -f %{oreon_filedir}/libtukit.list
%files -n tukit-devel -f %{oreon_filedir}/tukit-devel.list

%changelog

%autochangelog
