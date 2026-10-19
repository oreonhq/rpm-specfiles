%global source0_hash 6e61fe21ca8a66039180a5cc52a433e07279d2fee79c8be963e00d55193f17a8
Name:           python-jupyterlab-widgets
Version:        3.0.17
Release:        1%{?dist}
Summary:        Jupyter interactive widgets for JupyterLab
License:        ...
URL:            https://github.com/jupyter-widgets/ipywidgets
Source0:        https://files.pythonhosted.org/packages/source/j/jupyterlab_widgets/jupyterlab_widgets-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.5.0
BuildRequires:  python3dist(jupyter-builder) >= 1.0
Requires:       python3-jupyterlab-widgets = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jupyterlab-widgets
Summary:        Jupyter interactive widgets for JupyterLab
%description -n python3-jupyterlab-widgets

%prep
%global oreon_srcdir jupyterlab_widgets-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jupyterlab-widgets usr/lib/python3*/site-packages/jupyterlab_widgets* usr/lib64/python3*/site-packages/jupyterlab_widgets* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jupyterlab_widgets* usr/lib64/python3*/site-packages/jupyterlab_widgets* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jupyterlab-widgets -f %{oreon_filedir}/python3-jupyterlab-widgets.list

%changelog

%autochangelog
