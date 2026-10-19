%global source0_hash 7747d4777e008e33d37f4017bfe08768d16091f66b64c49635382016d596b8e5
%bcond bootstrap 0
Name:           python-snakemake-interface-common
Version:        1.23.1
Release:        1%{?dist}
Summary:        Common functions and classes for Snakemake and its plugins
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-common
Source0:        https://github.com/snakemake/snakemake-interface-common/archive/v%{version}/snakemake-interface-common-%{version}.tar.gz
Patch:          %{url}/pull/89.patch
%if %{without bootstrap}
%endif
BuildArch:      noarch
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-snakemake-interface-common = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-interface-common
Summary:        Common functions and classes for Snakemake and its plugins
# oreon:reqs
Requires:       python3dist(argparse-dataclass) >= 2.0.0
Requires:       python3dist(configargparse) >= 1.7
Requires:       python3dist(packaging) >= 26.1
# /oreon:reqs
%description -n python3-snakemake-interface-common %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-interface-common usr/lib/python3*/site-packages/snakemake_interface_common* usr/lib64/python3*/site-packages/snakemake_interface_common* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_interface_common* usr/lib64/python3*/site-packages/snakemake_interface_common* usr/bin/*

%check

%if %{with bootstrap}
k="${k-}${k+ and }not test_snakemake_version"
%endif
%pytest -k "${k-}" -v tests/tests.py
%files
%files -n python3-snakemake-interface-common -f %{oreon_filedir}/python3-snakemake-interface-common.list

%changelog

%autochangelog
