%global source0_hash c721a2406c0f41dab8aaa4216fbd5aab6d61f7477a08e4dab6c582f214a9a0ae
Name:           python-svg2tikz
Version:        3.3.6
Release:        1%{?dist}
Summary:        Tools for converting SVG graphics to TikZ/PGF code
License:        GPL-2.0-or-later
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/s/svg2tikz/svg2tikz-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-svg2tikz = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-svg2tikz
Summary:        Tools for converting SVG graphics to TikZ/PGF code
%description -n python3-svg2tikz

%prep
%global oreon_srcdir svg2tikz-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-svg2tikz usr/lib/python3*/site-packages/svg2tikz* usr/lib64/python3*/site-packages/svg2tikz* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/svg2tikz* usr/lib64/python3*/site-packages/svg2tikz* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-svg2tikz -f %{oreon_filedir}/python3-svg2tikz.list

%changelog

%autochangelog
