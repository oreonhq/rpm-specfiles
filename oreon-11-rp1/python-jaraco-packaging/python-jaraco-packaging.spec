%global source0_hash 7537e3a2be1c90f8442442cec6e31a9a2fd0a022223b0986286f08492483fc88
Name:           python-jaraco-packaging
Version:        10.4.0
Release:        1%{?dist}
Summary:        tools to supplement packaging Python releases
License:        MIT
URL:            https://github.com/jaraco/jaraco.packaging
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco_packaging/jaraco_packaging-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-jaraco-packaging = %{version}-%{release}
# /oreon:deps
%package -n       python3-jaraco-packaging+test
Summary:        Metapackage for python3-jaraco-packaging test extras
Requires:       python3-jaraco-packaging = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(jaraco-packaging[test]) = %{version}-%{release}

%description -n python3-jaraco-packaging+test
Metapackage for python3-jaraco-packaging test extras.

%package -n       python3-jaraco-packaging+doc
Summary:        Metapackage for python3-jaraco-packaging doc extras
Requires:       python3-jaraco-packaging = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Provides:       python3dist(jaraco-packaging[doc]) = %{version}-%{release}

%description -n python3-jaraco-packaging+doc
Metapackage for python3-jaraco-packaging doc extras.

%package -n       python3-jaraco-packaging+check
Summary:        Metapackage for python3-jaraco-packaging check extras
Requires:       python3-jaraco-packaging = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.4
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(jaraco-packaging[check]) = %{version}-%{release}

%description -n python3-jaraco-packaging+check
Metapackage for python3-jaraco-packaging check extras.

%package -n       python3-jaraco-packaging+cover
Summary:        Metapackage for python3-jaraco-packaging cover extras
Requires:       python3-jaraco-packaging = %{version}-%{release}
Provides:       python3dist(jaraco-packaging[cover]) = %{version}-%{release}

%description -n python3-jaraco-packaging+cover
Metapackage for python3-jaraco-packaging cover extras.

%package -n       python3-jaraco-packaging+enabler
Summary:        Metapackage for python3-jaraco-packaging enabler extras
Requires:       python3-jaraco-packaging = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 3.4
Provides:       python3dist(jaraco-packaging[enabler]) = %{version}-%{release}

%description -n python3-jaraco-packaging+enabler
Metapackage for python3-jaraco-packaging enabler extras.

%package -n       python3-jaraco-packaging+type
Summary:        Metapackage for python3-jaraco-packaging type extras
Requires:       python3-jaraco-packaging = %{version}-%{release}
Requires:       python3dist(pytest-mypy) >= 1.0.1
Requires:       python3dist(mypy) < 1.19
Provides:       python3dist(jaraco-packaging[type]) = %{version}-%{release}

%description -n python3-jaraco-packaging+type
Metapackage for python3-jaraco-packaging type extras.

%description

%package -n     python3-jaraco-packaging
Summary:        tools to supplement packaging Python releases
%description -n python3-jaraco-packaging

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jaraco_packaging-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jaraco-packaging usr/lib/python3*/site-packages/jaraco_packaging* usr/lib64/python3*/site-packages/jaraco_packaging* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jaraco_packaging* usr/lib64/python3*/site-packages/jaraco_packaging* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jaraco-packaging -f %{oreon_filedir}/python3-jaraco-packaging.list

%changelog

%autochangelog
