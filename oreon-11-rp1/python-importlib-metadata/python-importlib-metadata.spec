%global source0_hash ab830580bc0ef3db61ce8fae716389e5462b67e033018bab6d8f80ef17172f99
Name:           python-importlib-metadata
Version:        9.0.1
Release:        1%{?dist}
Summary:        Read metadata from Python packages
License:        Apache-2.0
URL:            https://github.com/python/importlib_metadata
Source0:        https://files.pythonhosted.org/packages/source/i/importlib_metadata/importlib_metadata-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-importlib-metadata = %{version}-%{release}
# /oreon:deps
%package -n       python3-importlib-metadata+test
Summary:        Metapackage for python3-importlib-metadata test extras
Requires:       python3-importlib-metadata = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Requires:       python3dist(pytest-perf) >= 0.17
Provides:       python3dist(importlib-metadata[test]) = %{version}-%{release}

%description -n python3-importlib-metadata+test
Metapackage for python3-importlib-metadata test extras.

%package -n       python3-importlib-metadata+doc
Summary:        Metapackage for python3-importlib-metadata doc extras
Requires:       python3-importlib-metadata = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(jaraco.tidelift) >= 1.4
Provides:       python3dist(importlib-metadata[doc]) = %{version}-%{release}

%description -n python3-importlib-metadata+doc
Metapackage for python3-importlib-metadata doc extras.

%package -n       python3-importlib-metadata+perf
Summary:        Metapackage for python3-importlib-metadata perf extras
Requires:       python3-importlib-metadata = %{version}-%{release}
Provides:       python3dist(importlib-metadata[perf]) = %{version}-%{release}

%description -n python3-importlib-metadata+perf
Metapackage for python3-importlib-metadata perf extras.

%package -n       python3-importlib-metadata+check
Summary:        Metapackage for python3-importlib-metadata check extras
Requires:       python3-importlib-metadata = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.14
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(importlib-metadata[check]) = %{version}-%{release}

%description -n python3-importlib-metadata+check
Metapackage for python3-importlib-metadata check extras.

%package -n       python3-importlib-metadata+cover
Summary:        Metapackage for python3-importlib-metadata cover extras
Requires:       python3-importlib-metadata = %{version}-%{release}
Provides:       python3dist(importlib-metadata[cover]) = %{version}-%{release}

%description -n python3-importlib-metadata+cover
Metapackage for python3-importlib-metadata cover extras.

%package -n       python3-importlib-metadata+enabler
Summary:        Metapackage for python3-importlib-metadata enabler extras
Requires:       python3-importlib-metadata = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 3.4
Provides:       python3dist(importlib-metadata[enabler]) = %{version}-%{release}

%description -n python3-importlib-metadata+enabler
Metapackage for python3-importlib-metadata enabler extras.

%package -n       python3-importlib-metadata+type
Summary:        Metapackage for python3-importlib-metadata type extras
Requires:       python3-importlib-metadata = %{version}-%{release}
Requires:       python3dist(pytest-mypy) >= 1.0.1
Provides:       python3dist(importlib-metadata[type]) = %{version}-%{release}

%description -n python3-importlib-metadata+type
Metapackage for python3-importlib-metadata type extras.

%description

%package -n     python3-importlib-metadata
Summary:        Read metadata from Python packages
# oreon:reqs
Requires:       python3dist(zipp) >= 3.20
# /oreon:reqs
%description -n python3-importlib-metadata

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir importlib_metadata-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-importlib-metadata usr/lib/python3*/site-packages/importlib_metadata* usr/lib64/python3*/site-packages/importlib_metadata* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/importlib_metadata* usr/lib64/python3*/site-packages/importlib_metadata* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-importlib-metadata -f %{oreon_filedir}/python3-importlib-metadata.list

%changelog

%autochangelog
