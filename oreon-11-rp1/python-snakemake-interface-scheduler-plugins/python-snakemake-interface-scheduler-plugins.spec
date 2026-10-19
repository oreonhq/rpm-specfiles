%global source0_hash d582b20e8f963a70d917b4648802fcd058975b3062ab94d7c57134964fa4a747
%bcond bootstrap 0
Name:           python-snakemake-interface-scheduler-plugins
Version:        2.0.2
Release:        1%{?dist}
Summary:        Scheduler plugin interface for snakemake
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-scheduler-plugins
Source0:        https://github.com/snakemake/snakemake-interface-scheduler-plugins/archive/v%{version}/snakemake-interface-scheduler-plugins-%{version}.tar.gz
BuildArch:      noarch
%if %{without bootstrap}
%endif
%global common_description %{expand:
This package provides a stable interface for interactions between Snakemake and
its scheduler plugins.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-interface-scheduler-plugins = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-interface-scheduler-plugins
Summary:        Scheduler plugin interface for snakemake
# oreon:reqs
Requires:       python3dist(snakemake-interface-common) < 2.0
Requires:       python3dist(snakemake-interface-common) >= 1.20.1
# /oreon:reqs
%description -n python3-snakemake-interface-scheduler-plugins %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-interface-scheduler-plugins usr/lib/python3*/site-packages/snakemake_interface_scheduler_plugins* usr/lib64/python3*/site-packages/snakemake_interface_scheduler_plugins* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_interface_scheduler_plugins* usr/lib64/python3*/site-packages/snakemake_interface_scheduler_plugins* usr/bin/*

%check

%if %{without bootstrap}
%pytest -v tests/tests.py
%endif
%files
%files -n python3-snakemake-interface-scheduler-plugins -f %{oreon_filedir}/python3-snakemake-interface-scheduler-plugins.list

%changelog

%autochangelog
