%global source0_hash dab81970bad6f0ab53b20745f1b01da37926e4c0fcd425046aa45e0d8efa18ed
Name:           python-jaraco-collections
Version:        5.2.1
Release:        1%{?dist}
Summary:        Collection objects similar to those in stdlib by jaraco
License:        MIT
URL:            https://github.com/jaraco/jaraco.collections
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco_collections/jaraco_collections-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-jaraco-collections = %{version}-%{release}
# /oreon:deps
%package -n       python3-jaraco-collections+test
Summary:        Metapackage for python3-jaraco-collections test extras
Requires:       python3-jaraco-collections = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(jaraco-collections[test]) = %{version}-%{release}

%description -n python3-jaraco-collections+test
Metapackage for python3-jaraco-collections test extras.

%package -n       python3-jaraco-collections+doc
Summary:        Metapackage for python3-jaraco-collections doc extras
Requires:       python3-jaraco-collections = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(jaraco.tidelift) >= 1.4
Provides:       python3dist(jaraco-collections[doc]) = %{version}-%{release}

%description -n python3-jaraco-collections+doc
Metapackage for python3-jaraco-collections doc extras.

%package -n       python3-jaraco-collections+check
Summary:        Metapackage for python3-jaraco-collections check extras
Requires:       python3-jaraco-collections = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.4
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(jaraco-collections[check]) = %{version}-%{release}

%description -n python3-jaraco-collections+check
Metapackage for python3-jaraco-collections check extras.

%package -n       python3-jaraco-collections+cover
Summary:        Metapackage for python3-jaraco-collections cover extras
Requires:       python3-jaraco-collections = %{version}-%{release}
Provides:       python3dist(jaraco-collections[cover]) = %{version}-%{release}

%description -n python3-jaraco-collections+cover
Metapackage for python3-jaraco-collections cover extras.

%package -n       python3-jaraco-collections+enabler
Summary:        Metapackage for python3-jaraco-collections enabler extras
Requires:       python3-jaraco-collections = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 2.2
Provides:       python3dist(jaraco-collections[enabler]) = %{version}-%{release}

%description -n python3-jaraco-collections+enabler
Metapackage for python3-jaraco-collections enabler extras.

%package -n       python3-jaraco-collections+type
Summary:        Metapackage for python3-jaraco-collections type extras
Requires:       python3-jaraco-collections = %{version}-%{release}
Provides:       python3dist(jaraco-collections[type]) = %{version}-%{release}

%description -n python3-jaraco-collections+type
Metapackage for python3-jaraco-collections type extras.

%description

%package -n     python3-jaraco-collections
Summary:        Collection objects similar to those in stdlib by jaraco
%description -n python3-jaraco-collections

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jaraco_collections-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jaraco-collections usr/lib/python3*/site-packages/jaraco_collections* usr/lib64/python3*/site-packages/jaraco_collections* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jaraco_collections* usr/lib64/python3*/site-packages/jaraco_collections* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jaraco-collections -f %{oreon_filedir}/python3-jaraco-collections.list

%changelog

%autochangelog
