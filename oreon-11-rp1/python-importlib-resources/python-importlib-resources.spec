%global source0_hash 0722d4c6212489c530f2a145a34c0a7a3b4721bc96a15fada5930e2a0b760708
Name:           python-importlib-resources
Version:        7.1.0
Release:        1%{?dist}
Summary:        Read resources from Python packages
License:        Apache-2.0
URL:            https://github.com/python/importlib_resources
Source0:        https://files.pythonhosted.org/packages/source/i/importlib_resources/importlib_resources-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-importlib-resources = %{version}-%{release}
# /oreon:deps
%package -n       python3-importlib-resources+test
Summary:        Metapackage for python3-importlib-resources test extras
Requires:       python3-importlib-resources = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Requires:       python3dist(zipp) >= 3.17
Requires:       python3dist(jaraco.test) >= 5.4
Provides:       python3dist(importlib-resources[test]) = %{version}-%{release}

%description -n python3-importlib-resources+test
Metapackage for python3-importlib-resources test extras.

%package -n       python3-importlib-resources+doc
Summary:        Metapackage for python3-importlib-resources doc extras
Requires:       python3-importlib-resources = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(jaraco.tidelift) >= 1.4
Provides:       python3dist(importlib-resources[doc]) = %{version}-%{release}

%description -n python3-importlib-resources+doc
Metapackage for python3-importlib-resources doc extras.

%package -n       python3-importlib-resources+check
Summary:        Metapackage for python3-importlib-resources check extras
Requires:       python3-importlib-resources = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.14
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(importlib-resources[check]) = %{version}-%{release}

%description -n python3-importlib-resources+check
Metapackage for python3-importlib-resources check extras.

%package -n       python3-importlib-resources+cover
Summary:        Metapackage for python3-importlib-resources cover extras
Requires:       python3-importlib-resources = %{version}-%{release}
Provides:       python3dist(importlib-resources[cover]) = %{version}-%{release}

%description -n python3-importlib-resources+cover
Metapackage for python3-importlib-resources cover extras.

%package -n       python3-importlib-resources+enabler
Summary:        Metapackage for python3-importlib-resources enabler extras
Requires:       python3-importlib-resources = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 3.4
Provides:       python3dist(importlib-resources[enabler]) = %{version}-%{release}

%description -n python3-importlib-resources+enabler
Metapackage for python3-importlib-resources enabler extras.

%package -n       python3-importlib-resources+type
Summary:        Metapackage for python3-importlib-resources type extras
Requires:       python3-importlib-resources = %{version}-%{release}
Requires:       python3dist(pytest-mypy) >= 1.0.1
Provides:       python3dist(importlib-resources[type]) = %{version}-%{release}

%description -n python3-importlib-resources+type
Metapackage for python3-importlib-resources type extras.

%description

%package -n     python3-importlib-resources
Summary:        Read resources from Python packages
# oreon:reqs
Requires:       python3dist(zipp) >= 3.1.0
# /oreon:reqs
%description -n python3-importlib-resources

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir importlib_resources-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-importlib-resources usr/lib/python3*/site-packages/importlib_resources* usr/lib64/python3*/site-packages/importlib_resources* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/importlib_resources* usr/lib64/python3*/site-packages/importlib_resources* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-importlib-resources -f %{oreon_filedir}/python3-importlib-resources.list

%changelog

%autochangelog
