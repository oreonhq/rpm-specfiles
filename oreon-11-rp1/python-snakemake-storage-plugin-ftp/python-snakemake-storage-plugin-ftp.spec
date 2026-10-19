%global source0_hash 020489badd7391a81f459656b8110a5ecbf80949a28e436dd9ee3e4078285272
%bcond network_tests 0
Name:           python-snakemake-storage-plugin-ftp
Version:        0.1.3
Release:        1%{?dist}
Summary:        A Snakemake plugin for handling input and output via FTP
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-ftp
Source0:        https://github.com/snakemake/snakemake-storage-plugin-ftp/archive/v%{version}/snakemake-storage-plugin-ftp-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
A Snakemake storage plugin that handles files and directories on an FTP
server.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-storage-plugin-ftp = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-storage-plugin-ftp
Summary:        A Snakemake plugin for handling input and output via FTP
%description -n python3-snakemake-storage-plugin-ftp %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-storage-plugin-ftp usr/lib/python3*/site-packages/snakemake_storage_plugin_ftp* usr/lib64/python3*/site-packages/snakemake_storage_plugin_ftp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_storage_plugin_ftp* usr/lib64/python3*/site-packages/snakemake_storage_plugin_ftp* usr/bin/*

%check

%if %{without network_tests}
k="${k-}${k+ and }not (TestStorage and test_storage)"
k="${k-}${k+ and }not (TestStorage and test_storage_not_existing)"
k="${k-}${k+ and }not (TestStorage and test_inventory)"
%endif
%pytest -v -k "${k-}" tests/tests.py
%files
%files -n python3-snakemake-storage-plugin-ftp -f %{oreon_filedir}/python3-snakemake-storage-plugin-ftp.list

%changelog

%autochangelog
