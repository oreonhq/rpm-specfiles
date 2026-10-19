%global source0_hash bcccba38a6ec3253f7a39c943cea5b9ad01999ce071396171adbc51c6a6a8613
Name:           python-ipywidgets
Version:        8.1.9
Release:        1%{?dist}
Summary:        Jupyter interactive widgets
License:        ...
URL:            http://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/i/ipywidgets/ipywidgets-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.8.0
Requires:       python3-ipywidgets = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ipywidgets
Summary:        Jupyter interactive widgets
%description -n python3-ipywidgets

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ipywidgets-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ipywidgets usr/lib/python3*/site-packages/ipywidgets* usr/lib64/python3*/site-packages/ipywidgets* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ipywidgets* usr/lib64/python3*/site-packages/ipywidgets* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ipywidgets -f %{oreon_filedir}/python3-ipywidgets.list

%changelog

%autochangelog
