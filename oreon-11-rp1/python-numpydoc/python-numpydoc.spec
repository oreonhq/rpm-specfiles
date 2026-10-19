%global source0_hash 26db0adaac8087e98da05c86b11198defd962aef7c21f4dffd2703c8c6eb4187
Name:           python-numpydoc
Version:        1.11.0
Release:        1%{?dist}
Summary:        Sphinx extension to support docstrings in Numpy format
License:        ...
URL:            https://numpydoc.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/n/numpydoc/numpydoc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-numpydoc = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-numpydoc
Summary:        Sphinx extension to support docstrings in Numpy format
# oreon:reqs
Requires:       python3dist(sphinx) >= 6
Requires:       python3dist(tomli) >= 1.1.0
# /oreon:reqs
%description -n python3-numpydoc

%prep
%global oreon_srcdir numpydoc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-numpydoc usr/lib/python3*/site-packages/numpydoc* usr/lib64/python3*/site-packages/numpydoc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/numpydoc* usr/lib64/python3*/site-packages/numpydoc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-numpydoc -f %{oreon_filedir}/python3-numpydoc.list

%changelog

%autochangelog
