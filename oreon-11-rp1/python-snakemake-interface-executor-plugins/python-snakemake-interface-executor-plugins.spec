%global source0_hash e3169ea2169f68ecd8e6aa7f841d580dd4d74482c8ba799ce0aeb0744e3ac117
%bcond bootstrap 0
Name:           python-snakemake-interface-executor-plugins
Version:        9.4.0
Release:        1%{?dist}
Summary:        Stable interface for interactions between Snakemake and its executor plugins
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-executor-plugins
Source0:        https://github.com/snakemake/snakemake-interface-executor-plugins/archive/v%{version}/snakemake-interface-executor-plugins-%{version}.tar.gz
BuildArch:      noarch
%if %{without bootstrap}
%endif
%global common_description %{expand:
This package provides a stable interface for interactions between Snakemake and
its executor plugins.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-interface-executor-plugins = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-interface-executor-plugins
Summary:        Stable interface for interactions between Snakemake and its executor plugins
# oreon:reqs
Requires:       python3dist(argparse-dataclass) >= 2.0.0
Requires:       python3dist(snakemake-interface-common) >= 1.19.0
Requires:       python3dist(throttler) >= 1.2.2
# /oreon:reqs
%description -n python3-snakemake-interface-executor-plugins %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-interface-executor-plugins usr/lib/python3*/site-packages/snakemake_interface_executor_plugins* usr/lib64/python3*/site-packages/snakemake_interface_executor_plugins* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_interface_executor_plugins* usr/lib64/python3*/site-packages/snakemake_interface_executor_plugins* usr/bin/*

%check

%if %{without bootstrap}
%pytest -v tests/tests.py
%endif
%files
%files -n python3-snakemake-interface-executor-plugins -f %{oreon_filedir}/python3-snakemake-interface-executor-plugins.list

%changelog

%autochangelog
