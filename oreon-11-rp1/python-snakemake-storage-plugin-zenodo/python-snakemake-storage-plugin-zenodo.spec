%global source0_hash 07121c74a7a69fa9a31228ac86db372b90499150d9e1471ea91d9336558ae643
%bcond tests 0
Name:           python-snakemake-storage-plugin-zenodo
Version:        0.1.5
Release:        1%{?dist}
Summary:        A Snakemake storage plugin for reading from and writing to zenodo.org
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-zenodo
Source0:        https://github.com/snakemake/snakemake-storage-plugin-zenodo/archive/v%{version}/snakemake-storage-plugin-zenodo-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
A Snakemake storage plugin for reading from and writing to zenodo.org. The
plugin takes queries of the form zenodo://record/121246/path/to/file.txt for
downloading files (here from record 121246), and
zenodo://deposition/121246/path/to/file.txt for uploading files to an existing
deposition (i.e. an unpublished and therefore still writable record).}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-storage-plugin-zenodo = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-storage-plugin-zenodo
Summary:        A Snakemake storage plugin for reading from and writing to zenodo.org
%description -n python3-snakemake-storage-plugin-zenodo %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-storage-plugin-zenodo usr/lib/python3*/site-packages/snakemake_storage_plugin_zenodo* usr/lib64/python3*/site-packages/snakemake_storage_plugin_zenodo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_storage_plugin_zenodo* usr/lib64/python3*/site-packages/snakemake_storage_plugin_zenodo* usr/bin/*

%check

%if %{with tests}
%pytest -v -k "${k-}" tests/tests.py
%endif
%files
%files -n python3-snakemake-storage-plugin-zenodo -f %{oreon_filedir}/python3-snakemake-storage-plugin-zenodo.list

%changelog

%autochangelog
