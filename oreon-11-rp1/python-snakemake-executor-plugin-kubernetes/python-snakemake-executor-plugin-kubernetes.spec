%global source0_hash 613b0e8bb9e265a4bf695edb3db942f46043c7ef5f0f048fe522627d02c3430e
%bcond tests 0
Name:           python-snakemake-executor-plugin-kubernetes
Version:        0.5.1
Release:        1%{?dist}
Summary:        A snakemake executor plugin for submission of jobs to Kubernetes
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-kubernetes
Source0:        https://github.com/snakemake/snakemake-executor-plugin-kubernetes/archive/v%{version}/snakemake-executor-plugin-kubernetes-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-executor-plugin-kubernetes = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-executor-plugin-kubernetes
Summary:        A snakemake executor plugin for submission of jobs to Kubernetes
%description -n python3-snakemake-executor-plugin-kubernetes %{common_description}

%prep

%autosetup -p1
# Remove upstream’s upper-bound on the version of kubernetes. This package
# routinely ends up briefly failing to build from source and sometimes failing
# to install due to “incompatible” major-version updates in python-kubernetes,
# but there have so far never been any real incompatibilities in practice.
# Upstream will still (eventually) keep up with new versions without us filing
# PR’s because they have configured dependabot, e.g.
# https://github.com/snakemake/snakemake-executor-plugin-kubernetes/pull/45.
sed -r -i 's/(kubernetes = ".*),<[^"]+"/\1"/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-executor-plugin-kubernetes usr/lib/python3*/site-packages/snakemake_executor_plugin_kubernetes* usr/lib64/python3*/site-packages/snakemake_executor_plugin_kubernetes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_executor_plugin_kubernetes* usr/lib64/python3*/site-packages/snakemake_executor_plugin_kubernetes* usr/bin/*

%check

%if %{with tests}
%pytest -v tests/tests.py
%endif
%files
%files -n python3-snakemake-executor-plugin-kubernetes -f %{oreon_filedir}/python3-snakemake-executor-plugin-kubernetes.list

%changelog

%autochangelog
