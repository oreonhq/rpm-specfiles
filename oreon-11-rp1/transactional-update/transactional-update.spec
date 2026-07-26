%global source0_hash c6703bc4ba6752c2d8ed2c1e8f9f3e17a9efc7ea181dc4627e2f411b9a46b5da

%global somajor 8

Name:           transactional-update
Version:        6.0.0
Release:        1%{?dist}
Summary:        Transactional Updates with btrfs and snapshots

License:        GPL-2.0-or-later and LGPL-2.1-or-later
URL:            https://github.com/openSUSE/transactional-update
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

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
BuildRequires:  %{_bindir}/xmllint
BuildRequires:  %{_bindir}/xsltproc
BuildRequires:  %{_bindir}/w3m

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

%files -n tukit
%license COPYING gpl-2.0.txt
%doc README.md NEWS
%{_sbindir}/tukit
%{_sbindir}/create_dirs_from_rpmdb
%{_unitdir}/create-dirs-from-rpmdb.service
%{_libexecdir}/prepare-nextroot-for-softreboot
%{_unitdir}/prepare-nextroot-for-softreboot.service
%{_libexecdir}/snapper/plugins/50-etc

#--------------------------------------------------------------------

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

%files -n tukitd
%license COPYING gpl-2.0.txt
%doc README.md NEWS
%{_sbindir}/tukitd
%{_unitdir}/tukitd.service
%{_mandir}/man5/tukit.conf.5*
%{_prefix}/share/dbus-1/system-services/org.opensuse.tukit.service
%{_prefix}/share/dbus-1/system.d/org.opensuse.tukit.conf
%{_prefix}/share/dbus-1/interfaces/org.opensuse.tukit.Snapshot.xml
%{_prefix}/share/dbus-1/interfaces/org.opensuse.tukit.Transaction.xml

#--------------------------------------------------------------------

%package -n dracut-%{name}
Summary:        Dracut module for supporting transactional updates
License:        GPL-2.0-or-later
Supplements:    (tukit and kernel)
Requires:       tukit = %{version}-%{release}

%description -n dracut-%{name}
This package contains the dracut modules for handling early boot aspects
for transactional updates.

%files -n dracut-%{name}
%license COPYING gpl-2.0.txt
%doc README.md NEWS
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%{_prefix}/lib/dracut/modules.d/50transactional-update/
%{_libexecdir}/transactional-update-sync-etc-state

#--------------------------------------------------------------------

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

%files -n libtukit
%license COPYING gpl-2.0.txt lgpl-2.1.txt
%{_libdir}/libtukit.so.%{somajor}{,.*}

#--------------------------------------------------------------------

%package -n tukit-devel
Summary:        Development files for tukit library
License:        GPL-2.0-or-later or LGPL-2.1-or-later
Requires:       libtukit%{?_isa} = %{version}-%{release}

%description -n tukit-devel
This package contains the files required to develop programs to do
transactional updates using btrfs snapshots.

%files -n tukit-devel
%license COPYING gpl-2.0.txt lgpl-2.1.txt
%{_includedir}/tukit/
%{_libdir}/libtukit.so
%{_libdir}/pkgconfig/tukit.pc

#--------------------------------------------------------------------

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

# Delete libtool cruft
rm -rf %{buildroot}%{_libdir}/*.la

# Delete transactional-update and associated files, as it's SUSE-specific
rm -rf %{buildroot}%{_sbindir}/transactional-update*
rm -rf %{buildroot}%{_sbindir}/tu-rebuild-kdump-initrd
rm -rf %{buildroot}%{_unitdir}/transactional-update*
rm -rf %{buildroot}%{_prefix}%{_sysconfdir}
rm -rf %{buildroot}%{_sysconfdir}
rm -rf %{buildroot}%{_mandir}/man*/transactional-update*
rm -rf %{buildroot}%{_docdir}

%changelog
%autochangelog
