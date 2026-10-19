%global source0_hash 0168ebebd8ef2050d94876698204066d491d1b46c2408b588a898421d533d573
Name:           python-pytest-spec
Version:        6.1.0
Release:        1%{?dist}
Summary:        Library pytest-spec is a pytest plugin to display test execution output like a SPECIFICATION.
License:        GPL-2.0-or-later
URL:            https://github.com/pchomik/pytest-spec
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_spec/pytest_spec-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-spec = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-spec+test
Summary:        Metapackage for python3-pytest-spec test extras
Requires:       python3-pytest-spec = %{version}-%{release}
Provides:       python3dist(pytest-spec[test]) = %{version}-%{release}

%description -n python3-pytest-spec+test
Metapackage for python3-pytest-spec test extras.

%description

%package -n     python3-pytest-spec
Summary:        Library pytest-spec is a pytest plugin to display test execution output like a SPECIFICATION.
%description -n python3-pytest-spec

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_spec-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-spec usr/lib/python3*/site-packages/pytest_spec* usr/lib64/python3*/site-packages/pytest_spec* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_spec* usr/lib64/python3*/site-packages/pytest_spec* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-spec -f %{oreon_filedir}/python3-pytest-spec.list

%changelog

%autochangelog
