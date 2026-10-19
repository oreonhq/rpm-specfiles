%global source0_hash 0b912acf663949d73b820d3ed59362140a188ab742c94efe13c762dbd24cbbd3
Name:           python-dictdiffer
Version:        0.10.0
Release:        1%{?dist}
Summary:        Dictdiffer is a library that helps you to diff and patch dictionaries.
License:        MIT
URL:            https://github.com/inveniosoftware/dictdiffer
Source0:        https://files.pythonhosted.org/packages/source/d/dictdiffer/dictdiffer-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-tests-remove-pytest-runner-setup.py-test-support.patch
Patch:          0002-Downstream-only-remove-linting-coverage-options-for-.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dictdiffer = %{version}-%{release}
# /oreon:deps
%package -n       python3-dictdiffer+docs
Summary:        Metapackage for python3-dictdiffer docs extras
Requires:       python3-dictdiffer = %{version}-%{release}
Requires:       python3dist(sphinx-rtd-theme) >= 0.2
Requires:       python3dist(sphinx) >= 3
Provides:       python3dist(dictdiffer[docs]) = %{version}-%{release}

%description -n python3-dictdiffer+docs
Metapackage for python3-dictdiffer docs extras.

%package -n       python3-dictdiffer+numpy
Summary:        Metapackage for python3-dictdiffer numpy extras
Requires:       python3-dictdiffer = %{version}-%{release}
Requires:       python3dist(numpy) >= 1.20.0
Provides:       python3dist(dictdiffer[numpy]) = %{version}-%{release}

%description -n python3-dictdiffer+numpy
Metapackage for python3-dictdiffer numpy extras.

%package -n       python3-dictdiffer+tests
Summary:        Metapackage for python3-dictdiffer tests extras
Requires:       python3-dictdiffer = %{version}-%{release}
Requires:       python3dist(mock) >= 1.3.0
Requires:       python3dist(pycodestyle) >= 2.10.0
Requires:       python3dist(pytest-cov) >= 2.10.1
Requires:       python3dist(pytest-isort) >= 1.2.0
Requires:       python3dist(pytest-pydocstyle) >= 2.2.0
Requires:       python3dist(pytest) >= 6
Requires:       python3dist(pytest) < 9
Requires:       python3dist(sphinx) >= 3
Requires:       python3dist(tox) >= 3.7.0
Provides:       python3dist(dictdiffer[tests]) = %{version}-%{release}

%description -n python3-dictdiffer+tests
Metapackage for python3-dictdiffer tests extras.

%description

%package -n     python3-dictdiffer
Summary:        Dictdiffer is a library that helps you to diff and patch dictionaries.
%description -n python3-dictdiffer

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir dictdiffer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dictdiffer usr/lib/python3*/site-packages/dictdiffer* usr/lib64/python3*/site-packages/dictdiffer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dictdiffer* usr/lib64/python3*/site-packages/dictdiffer* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dictdiffer -f %{oreon_filedir}/python3-dictdiffer.list

%changelog

%autochangelog
