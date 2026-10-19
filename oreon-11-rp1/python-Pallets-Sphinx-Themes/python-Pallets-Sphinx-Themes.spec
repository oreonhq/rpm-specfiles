%global source0_hash ef8609704b80e8a5d508a88adeb0559234311a1cf3362427aca9d283b22c80ef
Name:           python-pallets-sphinx-themes
Version:        2.5.0
Release:        1%{?dist}
Summary:        Sphinx themes for Pallets and related projects.
License:        BSD-3-Clause
URL:            https://github.com/pallets/pallets-sphinx-themes/
Source0:        https://files.pythonhosted.org/packages/source/p/pallets_sphinx_themes/pallets_sphinx_themes-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-pallets-sphinx-themes = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pallets-sphinx-themes
Summary:        Sphinx themes for Pallets and related projects.
# oreon:reqs
Requires:       python3dist(sphinx) >= 7.3
# /oreon:reqs
%description -n python3-pallets-sphinx-themes

%prep
%global oreon_srcdir pallets_sphinx_themes-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pallets-sphinx-themes usr/lib/python3*/site-packages/pallets_sphinx_themes* usr/lib64/python3*/site-packages/pallets_sphinx_themes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pallets_sphinx_themes* usr/lib64/python3*/site-packages/pallets_sphinx_themes* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pallets-sphinx-themes -f %{oreon_filedir}/python3-pallets-sphinx-themes.list

%changelog

%autochangelog
