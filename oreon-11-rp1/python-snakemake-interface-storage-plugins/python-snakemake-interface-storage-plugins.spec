%global source0_hash 424b1a8a9d74bb7b26a02df346b853c613eebc7d59b7475eeb2b933ac78b3150
%bcond bootstrap 0
%bcond network_tests 0
Name:           python-snakemake-interface-storage-plugins
Version:        4.4.1
Release:        1%{?dist}
Epoch:          1
Summary:        Stable interface for interactions between Snakemake and its storage plugins
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-storage-plugins
Source0:        https://github.com/snakemake/snakemake-interface-storage-plugins/archive/v%{version}/snakemake-interface-storage-plugins-%{version}.tar.gz
%if %{with bootstrap}
%endif
BuildArch:      noarch
%if %{without bootstrap}
%endif
%global common_description %{expand:
This package provides a stable interface for interactions between Snakemake and
its storage plugins.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-interface-storage-plugins = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-interface-storage-plugins
Summary:        Stable interface for interactions between Snakemake and its storage plugins
# oreon:reqs
Requires:       python3dist(humanfriendly) < 11
Requires:       python3dist(humanfriendly) >= 10.0
Requires:       python3dist(snakemake-interface-common) >= 1.12.0
Requires:       python3dist(tenacity) < 10.0
Requires:       python3dist(tenacity) >= 9.1.4
Requires:       python3dist(throttler) >= 1.2.2
Requires:       python3dist(wrapt) >= 1.15.0
# /oreon:reqs
%description -n python3-snakemake-interface-storage-plugins %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-interface-storage-plugins usr/lib/python3*/site-packages/snakemake_interface_storage_plugins* usr/lib64/python3*/site-packages/snakemake_interface_storage_plugins* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_interface_storage_plugins* usr/lib64/python3*/site-packages/snakemake_interface_storage_plugins* usr/bin/*

%check

%if %{without bootstrap}
%if %{without network_tests}
k="${k-}${k+ and }not (TestTestStorageBase and test_storage)"
k="${k-}${k+ and }not (TestTestStorageBase and test_storage_not_existing)"
k="${k-}${k+ and }not (TestTestStorageBase and test_inventory)"
%endif
%pytest -k "${k-}" -v tests/tests.py
%endif
%files
%files -n python3-snakemake-interface-storage-plugins -f %{oreon_filedir}/python3-snakemake-interface-storage-plugins.list

%changelog

%autochangelog
