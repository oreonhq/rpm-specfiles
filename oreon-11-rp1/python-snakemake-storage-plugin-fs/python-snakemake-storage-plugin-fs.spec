%global source0_hash 4cd9c17ab910ce21a9250fafa9e1463d27399b0c111811b72c07d95f8449b43a
Name:           python-snakemake-storage-plugin-fs
Version:        1.1.3
Release:        1%{?dist}
Summary:        Snakemake storage plugin that reads and writes from a local filesystem
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-fs
Source0:        https://github.com/snakemake/snakemake-storage-plugin-fs/archive/v%{version}/snakemake-storage-plugin-fs-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
A Snakemake storage plugin that reads and writes from a locally mounted
filesystem using rsync.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-storage-plugin-fs = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-storage-plugin-fs
Summary:        Snakemake storage plugin that reads and writes from a local filesystem
%description -n python3-snakemake-storage-plugin-fs %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-storage-plugin-fs usr/lib/python3*/site-packages/snakemake_storage_plugin_fs* usr/lib64/python3*/site-packages/snakemake_storage_plugin_fs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_storage_plugin_fs* usr/lib64/python3*/site-packages/snakemake_storage_plugin_fs* usr/bin/*

%check

%pytest -v tests/tests.py
%files
%files -n python3-snakemake-storage-plugin-fs -f %{oreon_filedir}/python3-snakemake-storage-plugin-fs.list

%changelog

%autochangelog
