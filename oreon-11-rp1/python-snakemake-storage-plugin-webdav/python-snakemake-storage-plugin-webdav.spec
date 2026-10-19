%global source0_hash 53165a8cf9b05f2e09166897ddc96fe33eb03d344879e38a2d8eba53a90a9182
Name:           python-snakemake-storage-plugin-webdav
Version:        0.1.2
Release:        1%{?dist}
Summary:        Snakemake storage plugin for webdav
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-webdav
Source0:        https://github.com/snakemake/snakemake-storage-plugin-webdav/archive/v%{version}/snakemake-storage-plugin-webdav-%{version}.tar.gz
Patch:          %{url}/pull/11.patch
BuildArch:      noarch
%global common_description %{expand:
A Snakemake storage plugin for handling input and output via webdav.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-storage-plugin-webdav = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-storage-plugin-webdav
Summary:        Snakemake storage plugin for webdav
%description -n python3-snakemake-storage-plugin-webdav %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-storage-plugin-webdav usr/lib/python3*/site-packages/snakemake_storage_plugin_webdav* usr/lib64/python3*/site-packages/snakemake_storage_plugin_webdav* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_storage_plugin_webdav* usr/lib64/python3*/site-packages/snakemake_storage_plugin_webdav* usr/bin/*

%check

k="${k-}${k+ and }not (TestStorage and test_storage)"
k="${k-}${k+ and }not (TestStorage and test_storage_not_existing)"
%pytest -v -k "${k-}" tests/tests.py
%files
%files -n python3-snakemake-storage-plugin-webdav -f %{oreon_filedir}/python3-snakemake-storage-plugin-webdav.list

%changelog

%autochangelog
