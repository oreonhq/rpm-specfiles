%global source0_hash f40bb0117c7d5feeed9a53258e86911c34aa6f0020e591bf36f3308626d44df6
%bcond bootstrap 0
Name:           python-snakemake-interface-logger-plugins
Version:        2.1.0
Release:        1%{?dist}
Summary:        Logger plugin interface for snakemake
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-logger-plugins
Source0:        https://github.com/snakemake/snakemake-interface-logger-plugins/archive/v%{version}/snakemake-interface-logger-plugins-%{version}.tar.gz
BuildArch:      noarch
%if %{without bootstrap}
%endif
%global common_description %{expand:
This package provides a stable interface for interactions between Snakemake and
its logger plugins.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-interface-logger-plugins = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-interface-logger-plugins
Summary:        Logger plugin interface for snakemake
# oreon:reqs
Requires:       python3dist(snakemake-interface-common) >= 1.17.4
# /oreon:reqs
%description -n python3-snakemake-interface-logger-plugins %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-interface-logger-plugins usr/lib/python3*/site-packages/snakemake_interface_logger_plugins* usr/lib64/python3*/site-packages/snakemake_interface_logger_plugins* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_interface_logger_plugins* usr/lib64/python3*/site-packages/snakemake_interface_logger_plugins* usr/bin/*

%check

%if %{without bootstrap}
%pytest -v tests/tests.py
%endif
%files
%files -n python3-snakemake-interface-logger-plugins -f %{oreon_filedir}/python3-snakemake-interface-logger-plugins.list

%changelog

%autochangelog
