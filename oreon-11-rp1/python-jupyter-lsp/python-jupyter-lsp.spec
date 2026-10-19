%global source0_hash fdf8a4aa7d85813976d6e29e95e6a2c8f752701f926f2715305249a3829805a6
Name:           python-jupyter-lsp
Version:        2.3.1
Release:        1%{?dist}
Summary:        Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server
License:        BSD-3-Clause
URL:            https://github.com/jupyter-lsp/jupyterlab-lsp
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_lsp/jupyter_lsp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jupyter-lsp = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jupyter-lsp
Summary:        Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server
%description -n python3-jupyter-lsp

%prep
%global oreon_srcdir jupyter_lsp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jupyter-lsp usr/lib/python3*/site-packages/jupyter_lsp* usr/lib64/python3*/site-packages/jupyter_lsp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jupyter_lsp* usr/lib64/python3*/site-packages/jupyter_lsp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jupyter-lsp -f %{oreon_filedir}/python3-jupyter-lsp.list

%changelog

%autochangelog
