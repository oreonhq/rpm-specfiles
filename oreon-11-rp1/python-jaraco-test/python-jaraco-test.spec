%global source0_hash dd4e17584be825986d6938518346b23bbb984b81f0bbb84e5c656fba61a63054
Name:           python-jaraco-test
Version:        5.7.0
Release:        1%{?dist}
Summary:        Testing support by jaraco
License:        MIT
URL:            https://github.com/jaraco/jaraco.test
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco_test/jaraco_test-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-jaraco-test = %{version}-%{release}
# /oreon:deps
%package -n       python3-jaraco-test+test
Summary:        Metapackage for python3-jaraco-test test extras
Requires:       python3-jaraco-test = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(jaraco-test[test]) = %{version}-%{release}

%description -n python3-jaraco-test+test
Metapackage for python3-jaraco-test test extras.

%package -n       python3-jaraco-test+doc
Summary:        Metapackage for python3-jaraco-test doc extras
Requires:       python3-jaraco-test = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Provides:       python3dist(jaraco-test[doc]) = %{version}-%{release}

%description -n python3-jaraco-test+doc
Metapackage for python3-jaraco-test doc extras.

%package -n       python3-jaraco-test+check
Summary:        Metapackage for python3-jaraco-test check extras
Requires:       python3-jaraco-test = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.14
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(jaraco-test[check]) = %{version}-%{release}

%description -n python3-jaraco-test+check
Metapackage for python3-jaraco-test check extras.

%package -n       python3-jaraco-test+cover
Summary:        Metapackage for python3-jaraco-test cover extras
Requires:       python3-jaraco-test = %{version}-%{release}
Provides:       python3dist(jaraco-test[cover]) = %{version}-%{release}

%description -n python3-jaraco-test+cover
Metapackage for python3-jaraco-test cover extras.

%package -n       python3-jaraco-test+enabler
Summary:        Metapackage for python3-jaraco-test enabler extras
Requires:       python3-jaraco-test = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 3.4
Provides:       python3dist(jaraco-test[enabler]) = %{version}-%{release}

%description -n python3-jaraco-test+enabler
Metapackage for python3-jaraco-test enabler extras.

%package -n       python3-jaraco-test+type
Summary:        Metapackage for python3-jaraco-test type extras
Requires:       python3-jaraco-test = %{version}-%{release}
Requires:       python3dist(pytest-mypy) >= 1.0.1
Provides:       python3dist(jaraco-test[type]) = %{version}-%{release}

%description -n python3-jaraco-test+type
Metapackage for python3-jaraco-test type extras.

%description

%package -n     python3-jaraco-test
Summary:        Testing support by jaraco
%description -n python3-jaraco-test

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jaraco_test-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jaraco-test usr/lib/python3*/site-packages/jaraco_test* usr/lib64/python3*/site-packages/jaraco_test* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jaraco_test* usr/lib64/python3*/site-packages/jaraco_test* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jaraco-test -f %{oreon_filedir}/python3-jaraco-test.list

%changelog

%autochangelog
