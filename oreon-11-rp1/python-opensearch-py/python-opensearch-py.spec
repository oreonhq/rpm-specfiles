%global source0_hash f40fb3a295275422df2ad6d9459f667af94472d5a9e567072e9ecf163eb22613
Name:           python-opensearch-py
Version:        3.2.0
Release:        1%{?dist}
Summary:        Python client for OpenSearch
License:        Apache-2.0
URL:            https://github.com/opensearch-project/opensearch-py
Source0:        https://files.pythonhosted.org/packages/source/o/opensearch_py/opensearch_py-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-opensearch-py = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-opensearch-py
Summary:        Python client for OpenSearch
%description -n python3-opensearch-py

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir opensearch_py-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-opensearch-py usr/lib/python3*/site-packages/opensearch_py* usr/lib64/python3*/site-packages/opensearch_py* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/opensearch_py* usr/lib64/python3*/site-packages/opensearch_py* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-opensearch-py -f %{oreon_filedir}/python3-opensearch-py.list

%changelog

%autochangelog
