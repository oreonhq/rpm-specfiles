%global source0_hash f8a096e0f54d2dbba2dbf606014ef1cbd00f191b3b47713c0e0d9b0b692a0cfb
Name:           pmbootstrap
Version:        3.9.0
Release:        1%{?dist}
Summary:        A sophisticated chroot/build/flash tool to develop and install postmarketOS
License:        GPL-3.0-only
URL:            https://www.postmarketos.org
Source0:        https://gitlab.postmarketos.org/postmarketOS/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExcludeArch:    s390x
Requires:       openssl
Requires:       git
Requires:       kpartx
Requires:       util-linux
Requires:       /usr/bin/ps
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-pmbootstrap = %{version}-%{release}
# /oreon:deps
%package -n       python3-pmbootstrap+test
Summary:        Metapackage for python3-pmbootstrap test extras
Requires:       python3-pmbootstrap = %{version}-%{release}
Provides:       python3dist(pmbootstrap[test]) = %{version}-%{release}

%description -n python3-pmbootstrap+test
Metapackage for python3-pmbootstrap test extras.

%package -n       python3-pmbootstrap+completion
Summary:        Metapackage for python3-pmbootstrap completion extras
Requires:       python3-pmbootstrap = %{version}-%{release}
Provides:       python3dist(pmbootstrap[completion]) = %{version}-%{release}

%description -n python3-pmbootstrap+completion
Metapackage for python3-pmbootstrap completion extras.

%description
Sophisticated chroot/build/flash tool to develop and install postmarketOS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest -k "not pkgrepo_pmaports and not random_valid_deviceinfos"
%files

%changelog

%autochangelog
