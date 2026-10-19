%global source0_hash 3bdf235ed8eb70d68b900bdc35daa854fd5981c298f8de0fb848a42d61f78774
Name:           python-throttler
Version:        1.2.3
Release:        1%{?dist}
Summary:        Easy throttling with asyncio support
License:        MIT
URL:            https://github.com/uburuntu/throttler
Source0:        https://github.com/uburuntu/throttler/archive/v%{version}/throttler-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
Zero-dependency Python package for easy throttling with asyncio support.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-throttler = %{version}-%{release}
# /oreon:deps
%package -n       python3-throttler+dev
Summary:        Metapackage for python3-throttler dev extras
Requires:       python3-throttler = %{version}-%{release}
Provides:       python3dist(throttler[dev]) = %{version}-%{release}

%description -n python3-throttler+dev
Metapackage for python3-throttler dev extras.

%description %{common_description}

%package -n python3-throttler
Summary:        Easy throttling with asyncio support
%description -n python3-throttler %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-throttler usr/lib/python3*/site-packages/throttler* usr/lib64/python3*/site-packages/throttler* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/throttler* usr/lib64/python3*/site-packages/throttler* usr/bin/*

%check

%pytest -n auto -v
%files
%files -n python3-throttler -f %{oreon_filedir}/python3-throttler.list

%changelog

%autochangelog
