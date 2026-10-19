%global source0_hash b4c3887adfa50e25029c2f7ea67733233f1d4a593c2d77007a7a85c996195172
%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 4.2.23}
Name:    dnf-plugin-cow
Version: 0.2.0
Release:        1%{?dist}
Summary:        DNF plugin to enable Copy on Write in RPM
URL:     https://github.com/facebookincubator/dnf-plugin-cow
License: MIT
Source0:        https://github.com/facebookincubator/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-dnf
# /oreon:deps
%description
Source package for DNF plugin to enable Copy on Write in DNF and RPM.

%package -n python3-%{name}
Summary: DNF plugin to enable Copy on Write in RPM - Python3
Requires: python3-dnf >= %{dnf_lowest_compatible}
Recommends: /usr/bin/rpm2extents
Recommends: rpm-plugin-reflink
%description -n python3-%{name}
Installing this package enables a DNF plugin which changes the behaviour of
librepo. Instead of downloading rpm files directly into cache before
installation they will be "transcoded" into "extent based" rpms which contain
all the constituent files of the rpm already uncompressed. This package
depends on a version of rpm which includes /usr/bin/rpm2extents and the
sub-package rpm-plugin-reflink which understands these "extent based" rpms
and can install files without copying the underlying data.

This package broadly assumes the root filesystem supports copy on write /
reflink'ing. Today this means btrfs or xfs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%install
install -D -p reflink.conf %{buildroot}%{_sysconfdir}/dnf/plugins/reflink.conf
install -D -p reflink.py %{buildroot}%{python3_sitelib}/dnf-plugins/reflink.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-dnf-plugin-cow -f %{oreon_filedir}/python3-dnf-plugin-cow.list

%changelog

%autochangelog
