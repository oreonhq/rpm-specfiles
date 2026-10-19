%global source0_hash 880c577ec9720b3a052d5bc611fb9f2269b3d87902ef42440df443b88e443280
Name:           python-jaraco-functools
Version:        4.6.0
Release:        1%{?dist}
Summary:        Functools like those found in stdlib
License:        MIT
URL:            https://github.com/jaraco/jaraco.functools
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco_functools/jaraco_functools-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-jaraco-functools = %{version}-%{release}
# /oreon:deps
%package -n       python3-jaraco-functools+test
Summary:        Metapackage for python3-jaraco-functools test extras
Requires:       python3-jaraco-functools = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(jaraco-functools[test]) = %{version}-%{release}

%description -n python3-jaraco-functools+test
Metapackage for python3-jaraco-functools test extras.

%package -n       python3-jaraco-functools+doc
Summary:        Metapackage for python3-jaraco-functools doc extras
Requires:       python3-jaraco-functools = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(jaraco.tidelift) >= 1.4
Provides:       python3dist(jaraco-functools[doc]) = %{version}-%{release}

%description -n python3-jaraco-functools+doc
Metapackage for python3-jaraco-functools doc extras.

%package -n       python3-jaraco-functools+check
Summary:        Metapackage for python3-jaraco-functools check extras
Requires:       python3-jaraco-functools = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.14
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(jaraco-functools[check]) = %{version}-%{release}

%description -n python3-jaraco-functools+check
Metapackage for python3-jaraco-functools check extras.

%package -n       python3-jaraco-functools+cover
Summary:        Metapackage for python3-jaraco-functools cover extras
Requires:       python3-jaraco-functools = %{version}-%{release}
Provides:       python3dist(jaraco-functools[cover]) = %{version}-%{release}

%description -n python3-jaraco-functools+cover
Metapackage for python3-jaraco-functools cover extras.

%package -n       python3-jaraco-functools+enabler
Summary:        Metapackage for python3-jaraco-functools enabler extras
Requires:       python3-jaraco-functools = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 3.4
Provides:       python3dist(jaraco-functools[enabler]) = %{version}-%{release}

%description -n python3-jaraco-functools+enabler
Metapackage for python3-jaraco-functools enabler extras.

%package -n       python3-jaraco-functools+type
Summary:        Metapackage for python3-jaraco-functools type extras
Requires:       python3-jaraco-functools = %{version}-%{release}
Requires:       python3dist(pytest-mypy) >= 1.0.1
Provides:       python3dist(jaraco-functools[type]) = %{version}-%{release}

%description -n python3-jaraco-functools+type
Metapackage for python3-jaraco-functools type extras.

%description

%package -n     python3-jaraco-functools
Summary:        Functools like those found in stdlib
%description -n python3-jaraco-functools

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jaraco_functools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jaraco-functools usr/lib/python3*/site-packages/jaraco_functools* usr/lib64/python3*/site-packages/jaraco_functools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jaraco_functools* usr/lib64/python3*/site-packages/jaraco_functools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jaraco-functools -f %{oreon_filedir}/python3-jaraco-functools.list

%changelog

%autochangelog
