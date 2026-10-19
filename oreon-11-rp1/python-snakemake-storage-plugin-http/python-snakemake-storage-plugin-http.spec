%global source0_hash 316d5a83f103489accb03f96606f370456bfe82355984329f53555a23d8dc974
%bcond network_tests 0
Name:           python-snakemake-storage-plugin-http
Version:        0.3.1
Release:        1%{?dist}
Summary:        Snakemake storage plugin for downloading input files from HTTP(s)
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-http
Source0:        https://github.com/snakemake/snakemake-storage-plugin-http/archive/v%{version}/snakemake-storage-plugin-http-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-storage-plugin-http = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-storage-plugin-http
Summary:        Snakemake storage plugin for downloading input files from HTTP(s)
%description -n python3-snakemake-storage-plugin-http %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-storage-plugin-http usr/lib/python3*/site-packages/snakemake_storage_plugin_http* usr/lib64/python3*/site-packages/snakemake_storage_plugin_http* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_storage_plugin_http* usr/lib64/python3*/site-packages/snakemake_storage_plugin_http* usr/bin/*

%check

%if %{without network_tests}
k="${k-}${k+ and }not (TestStorageNoSettings and test_storage)"
k="${k-}${k+ and }not (TestStorageNoSettings and test_storage_not_existing)"
k="${k-}${k+ and }not (TestStorageNoSettings and test_inventory)"
%endif
%pytest -v -k "${k-}" tests/tests.py
%files
%files -n python3-snakemake-storage-plugin-http -f %{oreon_filedir}/python3-snakemake-storage-plugin-http.list

%changelog

%autochangelog
