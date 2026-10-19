%global source0_hash f50197605b0f04ae92ee0945a106f1f31e4ab3ca87316de561e313bc3b1db1ed
Name:           python-resultsdb-api
Version:        2.1.6
Release:        1%{?dist}
Summary:        Library for simplifying the communication with ResultsDB
License:        GPL-2.0-or-later
URL:            https://pagure.io/taskotron/resultsdb_api
Source0:        https://files.pythonhosted.org/packages/source/r/resultsdb_api/resultsdb_api-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.6.0
Requires:       python3-resultsdb-api = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-resultsdb-api
Summary:        Library for simplifying the communication with ResultsDB
%description -n python3-resultsdb-api

%prep
%global oreon_srcdir resultsdb_api-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-resultsdb-api usr/lib/python3*/site-packages/resultsdb_api* usr/lib64/python3*/site-packages/resultsdb_api* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/resultsdb_api* usr/lib64/python3*/site-packages/resultsdb_api* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-resultsdb-api -f %{oreon_filedir}/python3-resultsdb-api.list

%changelog

%autochangelog
