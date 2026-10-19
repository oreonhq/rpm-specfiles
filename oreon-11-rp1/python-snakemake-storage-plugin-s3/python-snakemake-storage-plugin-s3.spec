%global source0_hash 09b18ea1ccfef16d0ee70b7d0672c8ecd1cee4abb1952829c4fd95180ffaf817
%bcond network_tests 0
Name:           python-snakemake-storage-plugin-s3
Version:        0.3.6
Release:        1%{?dist}
Summary:        A Snakemake storage plugin for S3 API storage (AWS S3, MinIO, etc.)
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-s3
Source0:        https://github.com/snakemake/snakemake-storage-plugin-s3/archive/v%{version}/snakemake-storage-plugin-s3-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
A Snakemake storage plugin for S3 API storage (AWS S3, MinIO, etc.). For
documentation and usage instructions, see the Snakemake plugin catalog,
https://snakemake.github.io/snakemake-plugin-catalog/plugins/storage/s3.html.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-storage-plugin-s3 = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-storage-plugin-s3
Summary:        A Snakemake storage plugin for S3 API storage (AWS S3, MinIO, etc.)
%description -n python3-snakemake-storage-plugin-s3 %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-storage-plugin-s3 usr/lib/python3*/site-packages/snakemake_storage_plugin_s3* usr/lib64/python3*/site-packages/snakemake_storage_plugin_s3* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_storage_plugin_s3* usr/lib64/python3*/site-packages/snakemake_storage_plugin_s3* usr/bin/*

%check

%if %{without network_tests}
k="${k-}${k+ and }not (TestStorageNoSettings and test_storage)"
k="${k-}${k+ and }not (TestStorageNoSettings and test_storage_not_existing)"
k="${k-}${k+ and }not TestWorkflows"
%endif
%pytest -v -k "${k-}" tests/tests.py
%files
%files -n python3-snakemake-storage-plugin-s3 -f %{oreon_filedir}/python3-snakemake-storage-plugin-s3.list

%changelog

%autochangelog
