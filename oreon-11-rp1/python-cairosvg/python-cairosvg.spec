%global source0_hash 861bc28ad97ce4f537d50eb3d6ee97a7afcccec9c61ac25c4e7d073fe409aec7
Name:           python-cairosvg
Version:        2.9.1
Release:        1%{?dist}
Summary:        A Simple SVG Converter based on Cairo
License:        LGPL-3.0-or-later
URL:            https://cairosvg.org/documentation/
Source0:        https://files.pythonhosted.org/packages/source/c/cairosvg/cairosvg-%{version}.tar.gz
BuildArch:      noarch
Patch0:             %{name}-disable-flake8-isort.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cairosvg = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cairosvg
Summary:        A Simple SVG Converter based on Cairo
%description -n python3-cairosvg

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cairosvg-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cairosvg usr/lib/python3*/site-packages/cairosvg* usr/lib64/python3*/site-packages/cairosvg* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cairosvg* usr/lib64/python3*/site-packages/cairosvg* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cairosvg -f %{oreon_filedir}/python3-cairosvg.list

%changelog

%autochangelog
