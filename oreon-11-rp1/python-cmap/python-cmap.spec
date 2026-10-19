%global source0_hash 9501cec4d5c2b7a821479aec3282b3d8b42fda983bad055e0f9dbc19cf7bc5b1
Name:           python-cmap
Version:        0.7.2
Release:        1%{?dist}
Summary:        Scientific colormaps for python, without dependencies
License:        BSD-3-Clause
URL:            https://github.com/pyapp-kit/cmap
Source0:        https://files.pythonhosted.org/packages/source/c/cmap/cmap-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cmap = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cmap
Summary:        Scientific colormaps for python, without dependencies
%description -n python3-cmap

%prep
%global oreon_srcdir cmap-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cmap usr/lib/python3*/site-packages/cmap* usr/lib64/python3*/site-packages/cmap* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cmap* usr/lib64/python3*/site-packages/cmap* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cmap -f %{oreon_filedir}/python3-cmap.list

%changelog

%autochangelog
