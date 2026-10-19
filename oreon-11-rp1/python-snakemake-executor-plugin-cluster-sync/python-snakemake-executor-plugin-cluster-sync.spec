%global source0_hash 00c3d9c9ea935c6ea821cd1d96cbcba3547732d496f2619db60a64daf9cf7e76
Name:           python-snakemake-executor-plugin-cluster-sync
Version:        0.1.5
Release:        1%{?dist}
Summary:        A Snakemake executor plugin for cluster jobs that are executed synchronously
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-cluster-sync
Source0:        https://github.com/snakemake/snakemake-executor-plugin-cluster-sync/archive/v%{version}/snakemake-executor-plugin-cluster-sync-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-executor-plugin-cluster-sync = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-executor-plugin-cluster-sync
Summary:        A Snakemake executor plugin for cluster jobs that are executed synchronously
%description -n python3-snakemake-executor-plugin-cluster-sync %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-executor-plugin-cluster-sync usr/lib/python3*/site-packages/snakemake_executor_plugin_cluster_sync* usr/lib64/python3*/site-packages/snakemake_executor_plugin_cluster_sync* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_executor_plugin_cluster_sync* usr/lib64/python3*/site-packages/snakemake_executor_plugin_cluster_sync* usr/bin/*

%check

%pytest -v tests/tests.py
%files
%files -n python3-snakemake-executor-plugin-cluster-sync -f %{oreon_filedir}/python3-snakemake-executor-plugin-cluster-sync.list

%changelog

%autochangelog
