%global source0_hash ab625f6c63c274a9d06ccc398753f7d7c8be8429729b654c659a042240328b09
%bcond bootstrap 0
Name:           python-snakemake-interface-report-plugins
Version:        2.0.1
Release:        1%{?dist}
Summary:        The interface for Snakemake report plugins
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-report-plugins
Source0:        https://github.com/snakemake/snakemake-interface-report-plugins/archive/v%{version}/snakemake-interface-report-plugins-%{version}.tar.gz
BuildArch:      noarch
%if %{without bootstrap}
%endif
%global common_description %{expand:
This package defines the interface between Snakemake and its report plugins.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-interface-report-plugins = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-interface-report-plugins
Summary:        The interface for Snakemake report plugins
%description -n python3-snakemake-interface-report-plugins %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-interface-report-plugins usr/lib/python3*/site-packages/snakemake_interface_report_plugins* usr/lib64/python3*/site-packages/snakemake_interface_report_plugins* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_interface_report_plugins* usr/lib64/python3*/site-packages/snakemake_interface_report_plugins* usr/bin/*

%check

%if %{without bootstrap}
%pytest -v tests/tests.py
%endif
%files
%files -n python3-snakemake-interface-report-plugins -f %{oreon_filedir}/python3-snakemake-interface-report-plugins.list

%changelog

%autochangelog
