%global source0_hash adeea0ae78f0856ee4945f413299801b82a0a01416303301f39a704282a37b73
Name:           python-widgetsnbextension
Version:        4.0.16
Release:        1%{?dist}
Summary:        Jupyter interactive widgets for Jupyter Notebook
License:        ...
URL:            http://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/w/widgetsnbextension/widgetsnbextension-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(jupyter-packaging) < 2
BuildRequires:  python3dist(jupyter-packaging) >= 0.10
Requires:       python3-widgetsnbextension = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-widgetsnbextension
Summary:        Jupyter interactive widgets for Jupyter Notebook
%description -n python3-widgetsnbextension

%prep
%global oreon_srcdir widgetsnbextension-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-widgetsnbextension usr/lib/python3*/site-packages/widgetsnbextension* usr/lib64/python3*/site-packages/widgetsnbextension* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/widgetsnbextension* usr/lib64/python3*/site-packages/widgetsnbextension* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-widgetsnbextension -f %{oreon_filedir}/python3-widgetsnbextension.list

%changelog

%autochangelog
