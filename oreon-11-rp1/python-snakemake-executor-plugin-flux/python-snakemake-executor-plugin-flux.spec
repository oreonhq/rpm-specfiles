%global source0_hash 1a8797053017da280a0ae17c80dcedef1c82b8d855e195b758cb1640e43e8eee
Name:           python-snakemake-executor-plugin-flux
Version:        0.1.1
Release:        1%{?dist}
Summary:        A snakemake executor plugin for the Flux scheduler
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-flux
Source0:        https://github.com/snakemake/snakemake-executor-plugin-flux/archive/v%{version}/snakemake-executor-plugin-flux-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This serves both as an example implementation for an external snakemake plugin
and as a usable executor plugin for the Flux scheduler.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-executor-plugin-flux = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-executor-plugin-flux
Summary:        A snakemake executor plugin for the Flux scheduler
%description -n python3-snakemake-executor-plugin-flux %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-executor-plugin-flux usr/lib/python3*/site-packages/snakemake_executor_plugin_flux* usr/lib64/python3*/site-packages/snakemake_executor_plugin_flux* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_executor_plugin_flux* usr/lib64/python3*/site-packages/snakemake_executor_plugin_flux* usr/bin/*

%check

%files
%files -n python3-snakemake-executor-plugin-flux -f %{oreon_filedir}/python3-snakemake-executor-plugin-flux.list

%changelog

%autochangelog
