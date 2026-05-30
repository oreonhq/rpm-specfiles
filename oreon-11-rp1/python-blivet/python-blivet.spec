%global source0_hash none

Summary:  A python module for system storage configuration
Name: python-blivet
Url: https://storageapis.wordpress.com/projects/blivet
Version: 3.13.2

#%%global prerelease .b2
# prerelease, if defined, should be something like .a1, .b1, .b2.dev1, or .c2
Release: 2%{?prerelease}%{?dist}
Epoch: 1
License: LGPL-2.1-or-later
%global realname blivet
%global realversion %{version}%{?prerelease}
Source0:        http://github.com/storaged-project/blivet/releases/download/blivet-3.13.2%{?prerelease}/blivet-3.13.2%{?prerelease}.tar.gz
Source1:        http://github.com/storaged-project/blivet/releases/download/blivet-3.13.2%{?prerelease}/blivet-3.13.2%{?prerelease}-tests.tar.gz

%if 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
Patch0: 0001-remove-btrfs-plugin.patch
%endif

Patch1: 0002-Ignore-btrfs-mount-errors-during-storage-scan.patch

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%global partedver 1.8.1
%global pypartedver 3.10.4
%global utillinuxver 2.15.1
%global libblockdevver 3.4.0
%global libbytesizever 0.3
%global pyudevver 0.18
%global s390utilscorever 2.31.0

BuildArch: noarch

%description
The python-blivet package is a python module for examining and modifying
storage configuration.

%package -n %{realname}-data
Summary: Data for the %{realname} python module.

BuildRequires: make
BuildRequires: systemd

Conflicts: python-blivet < 1:2.0.0
Conflicts: python3-blivet < 1:2.0.0

%description -n %{realname}-data
The %{realname}-data package provides data files required by the %{realname}
python module.

%package -n python3-%{realname}
Summary: A python3 package for examining and modifying storage configuration.

BuildRequires: gettext
BuildRequires: python3-devel

# For tests
BuildRequires: python3-pyudev >= %{pyudevver}
BuildRequires: parted >= %{partedver}
BuildRequires: python3-pyparted >= %{pypartedver}
BuildRequires: libselinux-python3
BuildRequires: python3-libmount
BuildRequires: python3-blockdev
BuildRequires: python3-bytesize >= %{libbytesizever}
BuildRequires: util-linux >= %{utillinuxver}
BuildRequires: lsof
BuildRequires: python3-gobject-base
BuildRequires: systemd-udev
BuildRequires: libblockdev-plugins-all
BuildRequires: python3-dbus
BuildRequires: python3-pyyaml
BuildRequires: python3-dasbus

Requires: python3-pyudev >= %{pyudevver}
Requires: parted >= %{partedver}
Requires: python3-pyparted >= %{pypartedver}
Requires: libselinux-python3
Requires: python3-libmount
Requires: python3-blockdev >= %{libblockdevver}
Requires: python3-dasbus
Recommends: libblockdev-btrfs >= %{libblockdevver}
Recommends: libblockdev-crypto >= %{libblockdevver}
Recommends: libblockdev-dm >= %{libblockdevver}
Recommends: libblockdev-fs >= %{libblockdevver}
Recommends: libblockdev-loop >= %{libblockdevver}
Recommends: libblockdev-lvm >= %{libblockdevver}
Recommends: libblockdev-mdraid >= %{libblockdevver}
Recommends: libblockdev-mpath >= %{libblockdevver}
Recommends: libblockdev-nvme >= %{libblockdevver}
Recommends: libblockdev-part >= %{libblockdevver}
Recommends: libblockdev-swap >= %{libblockdevver}
Recommends: libblockdev-s390 >= %{libblockdevver}
Recommends: s390utils-core >= %{s390utilscorever}

Requires: python3-bytesize >= %{libbytesizever}
Requires: util-linux >= %{utillinuxver}
Requires: lsof
Requires: python3-gobject-base
Requires: systemd-udev
Requires: %{realname}-data = %{epoch}:%{version}-%{release}

Obsoletes: blivet-data < 1:2.0.0

%description -n python3-%{realname}
The python3-%{realname} is a python3 package for examining and modifying storage
configuration.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{realname}-%{realversion} -N
%autosetup -n %{realname}-%{realversion} -b1 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
make

%install
make DESTDIR=%{buildroot} install

%find_lang %{realname}

%check
%{py3_test_envvars} %{python3} tests/run_tests.py unit_tests

%files -n %{realname}-data -f %{realname}.lang
%{_sysconfdir}/dbus-1/system.d/*
%{_datadir}/dbus-1/system-services/*
%{_libexecdir}/*
%{_unitdir}/*

%files -n python3-%{realname}
%license COPYING
%doc README.md ChangeLog examples
%{python3_sitelib}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:3.13.2-2
- Import
