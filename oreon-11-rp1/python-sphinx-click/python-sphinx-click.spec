%global source0_hash fc78b4154a4e5159462e36de55b8643747da6cda86b3b52a8bb62289e603776c
Name:           python-sphinx-click
Version:        6.2.0
Release:        1%{?dist}
Summary:        Sphinx extension that automatically documents click applications
License:        MIT
URL:            https://github.com/click-contrib/sphinx-click
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_click/sphinx_click-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-sphinx-click = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-click+docs
Summary:        Metapackage for python3-sphinx-click docs extras
Requires:       python3-sphinx-click = %{version}-%{release}
Provides:       python3dist(sphinx-click[docs]) = %{version}-%{release}

%description -n python3-sphinx-click+docs
Metapackage for python3-sphinx-click docs extras.

%package -n       python3-sphinx-click+test
Summary:        Metapackage for python3-sphinx-click test extras
Requires:       python3-sphinx-click = %{version}-%{release}
Provides:       python3dist(sphinx-click[test]) = %{version}-%{release}

%description -n python3-sphinx-click+test
Metapackage for python3-sphinx-click test extras.

%description

%package -n     python3-sphinx-click
Summary:        Sphinx extension that automatically documents click applications
# oreon:reqs
Requires:       python3dist(click) >= 8.0
Requires:       python3dist(sphinx) >= 4.0
# /oreon:reqs
%description -n python3-sphinx-click

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sphinx_click-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-click usr/lib/python3*/site-packages/sphinx_click* usr/lib64/python3*/site-packages/sphinx_click* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_click* usr/lib64/python3*/site-packages/sphinx_click* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-click -f %{oreon_filedir}/python3-sphinx-click.list

%changelog

%autochangelog
