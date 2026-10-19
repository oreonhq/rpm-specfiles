%global source0_hash d247dab8b96de9e4cfb701d6f3cd31418c686029cef4e6d07c604818b19d7e42
%bcond tests 0
Name:           python-snakemake-executor-plugin-slurm-jobstep
Version:        0.6.1
Release:        1%{?dist}
Summary:        A Snakemake executor plugin for running srun jobs inside of SLURM jobs
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-slurm-jobstep
Source0:        https://github.com/snakemake/snakemake-executor-plugin-slurm-jobstep/archive/v%{version}/snakemake-executor-plugin-slurm-jobstep-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
A Snakemake executor plugin for running srun jobs inside of SLURM jobs (meant
for internal use by snakemake-executor-plugin-slurm).}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-executor-plugin-slurm-jobstep = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-executor-plugin-slurm-jobstep
Summary:        A Snakemake executor plugin for running srun jobs inside of SLURM jobs
%description -n python3-snakemake-executor-plugin-slurm-jobstep %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-executor-plugin-slurm-jobstep usr/lib/python3*/site-packages/snakemake_executor_plugin_slurm_jobstep* usr/lib64/python3*/site-packages/snakemake_executor_plugin_slurm_jobstep* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_executor_plugin_slurm_jobstep* usr/lib64/python3*/site-packages/snakemake_executor_plugin_slurm_jobstep* usr/bin/*

%check

%if %{with tests}
%pytest -v tests/tests.py
%endif
%files
%files -n python3-snakemake-executor-plugin-slurm-jobstep -f %{oreon_filedir}/python3-snakemake-executor-plugin-slurm-jobstep.list

%changelog

%autochangelog
