%global source0_hash a41232732ac66a9fd001aae50bf9a7f359002ecddfd24fa4e0d83bff4edf1d86
%bcond tests 0
Name:           python-snakemake-storage-plugin-azure
Version:        0.4.4
Release:        1%{?dist}
Summary:        Snakemake storage plugin for Azure Blob Storage
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-azure
Source0:        https://github.com/snakemake/snakemake-storage-plugin-azure/archive/v%{version}/snakemake-storage-plugin-azure-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
A Snakemake storage plugin to read and write from Azure Blob Storage.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-storage-plugin-azure = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-storage-plugin-azure
Summary:        Snakemake storage plugin for Azure Blob Storage
%description -n python3-snakemake-storage-plugin-azure %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-storage-plugin-azure usr/lib/python3*/site-packages/snakemake_storage_plugin_azure* usr/lib64/python3*/site-packages/snakemake_storage_plugin_azure* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_storage_plugin_azure* usr/lib64/python3*/site-packages/snakemake_storage_plugin_azure* usr/bin/*

%check

%if %{with tests}
%pytest -v -k "${k-}" tests/tests.py
%endif
%files
%files -n python3-snakemake-storage-plugin-azure -f %{oreon_filedir}/python3-snakemake-storage-plugin-azure.list

%changelog

%autochangelog
