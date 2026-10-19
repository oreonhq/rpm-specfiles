%global source0_hash da8a66ffc315e9eabfbcb3d260499dc7f9a8f9583a544af979d028e09b2026ad
Name:           python-enthought-sphinx-theme
Version:        0.7.5
Release:        1%{?dist}
Summary:        Sphinx theme for Enthought products
License:        ...
URL:            https://github.com/enthought/enthought-sphinx-theme
Source0:        https://files.pythonhosted.org/packages/source/e/enthought_sphinx_theme/enthought_sphinx_theme-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-enthought-sphinx-theme = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-enthought-sphinx-theme
Summary:        Sphinx theme for Enthought products
%description -n python3-enthought-sphinx-theme

%prep
%global oreon_srcdir enthought_sphinx_theme-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-enthought-sphinx-theme usr/lib/python3*/site-packages/enthought_sphinx_theme* usr/lib64/python3*/site-packages/enthought_sphinx_theme* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/enthought_sphinx_theme* usr/lib64/python3*/site-packages/enthought_sphinx_theme* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-enthought-sphinx-theme -f %{oreon_filedir}/python3-enthought-sphinx-theme.list

%changelog

%autochangelog
