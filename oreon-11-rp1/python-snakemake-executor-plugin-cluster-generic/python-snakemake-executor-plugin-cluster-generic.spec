%global source0_hash f566845b691f755b5a7390cd2ab511b92f8a0deb35f3b98708d153a16373884e
Name:           python-snakemake-executor-plugin-cluster-generic
Version:        1.0.9
Release:        1%{?dist}
Summary:        Generic cluster executor for Snakemake
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-cluster-generic
Source0:        https://github.com/snakemake/snakemake-executor-plugin-cluster-generic/archive/v%{version}/snakemake-executor-plugin-cluster-generic-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
A generic Snakemake executor plugin for submission of jobs to cluster systems
that provide a submission command that accepts the path to a job script (like
PBS, LSF, SGE, ...).}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-executor-plugin-cluster-generic = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-executor-plugin-cluster-generic
Summary:        Generic cluster executor for Snakemake
%description -n python3-snakemake-executor-plugin-cluster-generic %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir snakemake-executor-plugin-cluster-generic-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-executor-plugin-cluster-generic usr/lib/python3*/site-packages/snakemake_executor_plugin_cluster_generic* usr/lib64/python3*/site-packages/snakemake_executor_plugin_cluster_generic* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_executor_plugin_cluster_generic* usr/lib64/python3*/site-packages/snakemake_executor_plugin_cluster_generic* usr/bin/*

%check

%if %{without bootstrap}
%pytest -v tests/tests.py
%endif
%files
%files -n python3-snakemake-executor-plugin-cluster-generic -f %{oreon_filedir}/python3-snakemake-executor-plugin-cluster-generic.list

%changelog

%autochangelog
