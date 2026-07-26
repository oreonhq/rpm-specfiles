%global source0_hash 41564cec5f73d196e3b67897bfc3839880b8d081d709cc793a8439e733e75704

%global __python %{__python3}

# Minimum version of imgcreate (livecd-tools)
%global min_imgcreate_ver 28.3-3

%if 0%{?fedora}
%global min_imgcreate_evr 1:%{min_imgcreate_ver}
%else
%global min_imgcreate_evr %{min_imgcreate_ver}
%endif

Name:       appliance-tools
Summary:    Tools for building Appliances
Version:    011.3
Release:    10%{?dist}
License:    GPL-2.0-only
URL:        https://pagure.io/appliance-tools
BuildArch:  noarch

Source0:    https://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  which

# Ensure system deps are installed (rhbz#1409536)
Requires:   curl
Requires:   kpartx
Requires:   python3-imgcreate %{?min_imgcrate_evr:>= %{min_imgcreate_evr}}
Requires:   python3-progress
Requires:   python3-setuptools
Requires:   qemu-img
Requires:   rsync
Requires:   sssd-client
Requires:   xfsprogs
Requires:   xz
Requires:   zlib

%if 0%{?fedora}
Requires:   btrfs-progs
%endif

%description
Tools for generating appliance images on Fedora based systems, including
derived distributions such as RHEL, CentOS, and others.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%install
%make_install PYTHON=%{__python}

# Delete docs, we'll grab them later
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files
%doc README
%doc config/fedora-aos.ks
%license COPYING
%{_mandir}/man*/*
%{_bindir}/appliance-creator
%{_bindir}/ec2-converter
%{python_sitelib}/appcreate/
%{python_sitelib}/ec2convert/

%changelog
%autochangelog
