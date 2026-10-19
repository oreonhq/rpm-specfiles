%global source0_hash bbd48d6970ee8e884e9c527656fe040ea6d8f070bffb32d010ab770054f4b80c
%bcond tests 0
Name:           python-snakemake-executor-plugin-tes
Version:        0.1.3
Release:        1%{?dist}
Summary:        A Snakemake executor plugin for submitting jobs via GA4GH TES
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-tes
Source0:        https://github.com/snakemake/snakemake-executor-plugin-tes/archive/v%{version}/snakemake-executor-plugin-tes-%{version}.tar.gz
Patch:          %{url}/pull/16.patch
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-executor-plugin-tes = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-executor-plugin-tes
Summary:        A Snakemake executor plugin for submitting jobs via GA4GH TES
%description -n python3-snakemake-executor-plugin-tes %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-executor-plugin-tes usr/lib/python3*/site-packages/snakemake_executor_plugin_tes* usr/lib64/python3*/site-packages/snakemake_executor_plugin_tes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_executor_plugin_tes* usr/lib64/python3*/site-packages/snakemake_executor_plugin_tes* usr/bin/*

%check

%if %{with tests}
%pytest -v tests/tests.py
%endif
%files
%files -n python3-snakemake-executor-plugin-tes -f %{oreon_filedir}/python3-snakemake-executor-plugin-tes.list

%changelog

%autochangelog
