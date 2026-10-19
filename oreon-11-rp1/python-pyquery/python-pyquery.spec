%global source0_hash 75238388750fc6e254b7a52f771027b9beb3a6202b88048bef52a00b0abeadbb
Name:           python-pyquery
Version:        2.1.0
Release:        1%{?dist}
Summary:        A jquery-like library for python
License:        ...
URL:            https://github.com/gawel/pyquery
Source0:        https://files.pythonhosted.org/packages/source/p/pyquery/pyquery-%{version}.tar.gz
BuildArch:      noarch
Patch:          python-pyquery-skip-test-requiring-net-connection.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyquery = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyquery
Summary:        A jquery-like library for python
%description -n python3-pyquery

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyquery-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyquery usr/lib/python3*/site-packages/pyquery* usr/lib64/python3*/site-packages/pyquery* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyquery* usr/lib64/python3*/site-packages/pyquery* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyquery -f %{oreon_filedir}/python3-pyquery.list

%changelog

%autochangelog
