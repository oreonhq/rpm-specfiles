%global source0_hash 18548d0c9912c45775d0a6e0ef7f0246c601cc71a576fbb5c7296566c7c03db5
Name:           python-conda-sphinx-theme
Version:        0.4.0
Release:        1%{?dist}
Summary:        Conda theme for Sphinx
License:        ...
URL:            https://github.com/conda-incubator/conda-sphinx-theme/
Source0:        https://files.pythonhosted.org/packages/source/c/conda_sphinx_theme/conda_sphinx_theme-%{version}.tar.gz
BuildArch:      noarch
Patch:          python-conda-sphinx-theme-fonts.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-conda-sphinx-theme = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-conda-sphinx-theme
Summary:        Conda theme for Sphinx
# oreon:reqs
Requires:       python3dist(pydata-sphinx-theme) >= 0.15
# /oreon:reqs
%description -n python3-conda-sphinx-theme

%prep
%global oreon_srcdir conda_sphinx_theme-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-conda-sphinx-theme usr/lib/python3*/site-packages/conda_sphinx_theme* usr/lib64/python3*/site-packages/conda_sphinx_theme* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/conda_sphinx_theme* usr/lib64/python3*/site-packages/conda_sphinx_theme* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-conda-sphinx-theme -f %{oreon_filedir}/python3-conda-sphinx-theme.list

%changelog

%autochangelog
