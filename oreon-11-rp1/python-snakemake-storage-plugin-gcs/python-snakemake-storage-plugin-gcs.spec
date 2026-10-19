%global source0_hash 43a40feedc97141f4508ab6ba7cbb31a3cb96eb626c3719cad181d2edd16e020
Name:           python-snakemake-storage-plugin-gcs
Version:        1.1.4
Release:        1%{?dist}
Summary:        A Snakemake storage plugin for Google Cloud Storage
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-gcs
Source0:        https://github.com/snakemake/snakemake-storage-plugin-gcs/archive/v%{version}/snakemake-storage-plugin-gcs-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-storage-plugin-gcs = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-storage-plugin-gcs
Summary:        A Snakemake storage plugin for Google Cloud Storage
# oreon:reqs
Requires:       python3dist(google-cloud-storage) >= 2.12.0
Requires:       python3dist(google-crc32c) >= 1.1.2
Requires:       python3dist(snakemake-interface-common) >= 1.14.2
Requires:       python3dist(snakemake-interface-storage-plugins) >= 4.0
# /oreon:reqs
%description -n python3-snakemake-storage-plugin-gcs %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-storage-plugin-gcs usr/lib/python3*/site-packages/snakemake_storage_plugin_gcs* usr/lib64/python3*/site-packages/snakemake_storage_plugin_gcs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_storage_plugin_gcs* usr/lib64/python3*/site-packages/snakemake_storage_plugin_gcs* usr/bin/*

%files
%files -n python3-snakemake-storage-plugin-gcs -f %{oreon_filedir}/python3-snakemake-storage-plugin-gcs.list

%changelog

%autochangelog
