%global source0_hash 1dcf140132b88e82d2d3c189464978af0a0c28dd5b8a82f23f4311b5b0211e15
Name:           btrfs-assistant
Version:        2.3.1
Release:        1%{?dist}
Summary:        GUI management tool to make managing a Btrfs filesystem easier
License:        GPL-3.0-or-later
URL:            https://gitlab.com/%{name}/%{name}
Source0:        https://gitlab.com/%{name}/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         btrfs-assistant-no-error-on-warn.patch
Patch1:         btrfs-assistant-fix-restore-subvolume-button.patch
Requires:       hicolor-icon-theme
Requires:       polkit
Recommends:     btrfsmaintenance
Recommends:     snapper
# oreon:deps
BuildRequires:  btrfs-progs-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libbtrfsutil
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Widgets)
# /oreon:deps
%description
Btrfs Assistant is a GUI management tool to make managing a Btrfs filesystem
easier.

The primary features it offers are:

* An easy to read overview of Btrfs metadata
* A simple view of subvolumes with or without Snapper/Timeshift snapshots
* Run and monitor scrub and balance operations
* A pushbutton method for removing subvolumes
* A management front-end for Snapper with enhanced restore functionality
    * View, create and delete snapshots
    * Restore snapshots in a variety of situations
        * When the filesystem is mounted in a different distro
        * When booted off a snapshot
        * From a live ISO
    * View, create, edit, remove Snapper configurations
    * Browse snapshots and restore individual files
    * Browse diffs of a single file across snapshot versions
    * Manage Snapper systemd units
* A front-end for Btrfs Maintenance
    * Manage systemd units
    * Easily manage configuration for defrag, balance and scrub settings

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix config path for btrfsmaintenance
sed -i 's|^bm_config =.*|bm_config = %{_sysconfdir}/sysconfig/btrfsmaintenance|' src/btrfs-assistant.conf

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
