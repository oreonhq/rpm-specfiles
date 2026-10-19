%global source0_hash 41564cec5f73d196e3b67897bfc3839880b8d081d709cc793a8439e733e75704
%global __python %{__python3}
%global min_imgcreate_ver 28.3-3
%global min_imgcreate_evr %{min_imgcreate_ver}
Name:       appliance-tools
Summary:        Tools for building Appliances
Version:    011.3
Release:        10%{?dist}
License:    GPL-2.0-only
URL:        https://pagure.io/appliance-tools
BuildArch:  noarch
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2
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
# oreon:deps
BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  which
# /oreon:deps
%description
Tools for generating appliance images on Fedora based systems, including
derived distributions such as RHEL, CentOS, and others.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
%make_install PYTHON=%{__python}
rm -rf %{buildroot}%{_datadir}/doc/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
