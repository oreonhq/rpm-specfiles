%global source0_hash e9739237f3915037dacba787c4b58f280e3ec5d9864953e185bf23d40ff7d021
Name:           python-cssutils
Version:        2.15.0
Release:        1%{?dist}
Summary:        A CSS Cascading Style Sheets library for Python
License:        LGPL-3.0-or-later
URL:            https://github.com/jaraco/cssutils
Source0:        https://files.pythonhosted.org/packages/source/c/cssutils/cssutils-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-cssutils = %{version}-%{release}
# /oreon:deps
%package -n       python3-cssutils+test
Summary:        Metapackage for python3-cssutils test extras
Requires:       python3-cssutils = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Requires:       python3dist(jaraco.test) >= 5.1
Provides:       python3dist(cssutils[test]) = %{version}-%{release}

%description -n python3-cssutils+test
Metapackage for python3-cssutils test extras.

%package -n       python3-cssutils+doc
Summary:        Metapackage for python3-cssutils doc extras
Requires:       python3-cssutils = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(jaraco.tidelift) >= 1.4
Provides:       python3dist(cssutils[doc]) = %{version}-%{release}

%description -n python3-cssutils+doc
Metapackage for python3-cssutils doc extras.

%package -n       python3-cssutils+check
Summary:        Metapackage for python3-cssutils check extras
Requires:       python3-cssutils = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.14
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(cssutils[check]) = %{version}-%{release}

%description -n python3-cssutils+check
Metapackage for python3-cssutils check extras.

%package -n       python3-cssutils+cover
Summary:        Metapackage for python3-cssutils cover extras
Requires:       python3-cssutils = %{version}-%{release}
Provides:       python3dist(cssutils[cover]) = %{version}-%{release}

%description -n python3-cssutils+cover
Metapackage for python3-cssutils cover extras.

%package -n       python3-cssutils+enabler
Summary:        Metapackage for python3-cssutils enabler extras
Requires:       python3-cssutils = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 3.4
Provides:       python3dist(cssutils[enabler]) = %{version}-%{release}

%description -n python3-cssutils+enabler
Metapackage for python3-cssutils enabler extras.

%package -n       python3-cssutils+type
Summary:        Metapackage for python3-cssutils type extras
Requires:       python3-cssutils = %{version}-%{release}
Requires:       python3dist(pytest-mypy) >= 1.0.1
Provides:       python3dist(cssutils[type]) = %{version}-%{release}

%description -n python3-cssutils+type
Metapackage for python3-cssutils type extras.

%description

%package -n     python3-cssutils
Summary:        A CSS Cascading Style Sheets library for Python
%description -n python3-cssutils

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cssutils-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cssutils usr/lib/python3*/site-packages/cssutils* usr/lib64/python3*/site-packages/cssutils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cssutils* usr/lib64/python3*/site-packages/cssutils* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cssutils -f %{oreon_filedir}/python3-cssutils.list

%changelog

%autochangelog
