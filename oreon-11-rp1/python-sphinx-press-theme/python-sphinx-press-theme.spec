%global source0_hash 1643dee7365f7831d1d3971b389b7c255641a7aced75f0681f71574e380046cf
Name:           python-sphinx-press-theme
Version:        0.9.1
Release:        1%{?dist}
Summary:        A Sphinx-doc theme based on Vuepress
License:        MIT
URL:            https://github.com/schettino72/sphinx_press_theme
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_press_theme/sphinx_press_theme-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinx-press-theme = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinx-press-theme
Summary:        A Sphinx-doc theme based on Vuepress
%description -n python3-sphinx-press-theme

%prep
%global oreon_srcdir sphinx_press_theme-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-press-theme usr/lib/python3*/site-packages/sphinx_press_theme* usr/lib64/python3*/site-packages/sphinx_press_theme* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_press_theme* usr/lib64/python3*/site-packages/sphinx_press_theme* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-press-theme -f %{oreon_filedir}/python3-sphinx-press-theme.list

%changelog

%autochangelog
