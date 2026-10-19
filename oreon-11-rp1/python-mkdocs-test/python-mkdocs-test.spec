%global source0_hash ea28fd1aa737a55a3529bd9fd8277874d7365c6644785fb2fd4ac974ab77e698
Name:           python-mkdocs-test
Version:        0.6.0
Release:        1%{?dist}
Summary:        A test framework for MkDocs projects
License:        MIT
URL:            https://github.com/fralau/mkdocs-test
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_test/mkdocs_test-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-mkdocs-test = %{version}-%{release}
# /oreon:deps
%package -n       python3-mkdocs-test+test
Summary:        Metapackage for python3-mkdocs-test test extras
Requires:       python3-mkdocs-test = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0
Provides:       python3dist(mkdocs-test[test]) = %{version}-%{release}

%description -n python3-mkdocs-test+test
Metapackage for python3-mkdocs-test test extras.

%package -n       python3-mkdocs-test+doc
Summary:        Metapackage for python3-mkdocs-test doc extras
Requires:       python3-mkdocs-test = %{version}-%{release}
Provides:       python3dist(mkdocs-test[doc]) = %{version}-%{release}

%description -n python3-mkdocs-test+doc
Metapackage for python3-mkdocs-test doc extras.

%description

%package -n     python3-mkdocs-test
Summary:        A test framework for MkDocs projects
%description -n python3-mkdocs-test

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mkdocs_test-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-test usr/lib/python3*/site-packages/mkdocs_test* usr/lib64/python3*/site-packages/mkdocs_test* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_test* usr/lib64/python3*/site-packages/mkdocs_test* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-test -f %{oreon_filedir}/python3-mkdocs-test.list

%changelog

%autochangelog
