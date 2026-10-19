%global source0_hash 51cc11666391ab6f092070437ac747002ff46f3e4113a3622177ee6b488bfc53
Name:           python-build
Version:        1.6.1
Release:        1%{?dist}
Summary:        A simple, correct Python build frontend
License:        MIT
URL:            https://build.pypa.io
Source0:        https://files.pythonhosted.org/packages/source/b/build/build-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-build = %{version}-%{release}
# /oreon:deps
%package -n       python3-build+uv
Summary:        Metapackage for python3-build uv extras
Requires:       python3-build = %{version}-%{release}
Requires:       python3dist(uv) >= 0.1.18
Provides:       python3dist(build[uv]) = %{version}-%{release}

%description -n python3-build+uv
Metapackage for python3-build uv extras.

%package -n       python3-build+keyring
Summary:        Metapackage for python3-build keyring extras
Requires:       python3-build = %{version}-%{release}
Provides:       python3dist(build[keyring]) = %{version}-%{release}

%description -n python3-build+keyring
Metapackage for python3-build keyring extras.

%package -n       python3-build+virtualenv
Summary:        Metapackage for python3-build virtualenv extras
Requires:       python3-build = %{version}-%{release}
Requires:       python3dist(virtualenv) >= 20.36.1
Provides:       python3dist(build[virtualenv]) = %{version}-%{release}

%description -n python3-build+virtualenv
Metapackage for python3-build virtualenv extras.

%description

%package -n     python3-build
Summary:        A simple, correct Python build frontend
# oreon:reqs
Requires:       python3dist(importlib-metadata) >= 4.6
Requires:       python3dist(packaging) >= 24.0
Requires:       python3dist(tomli) >= 1.1.0
# /oreon:reqs
%description -n python3-build

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir build-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-build usr/lib/python3*/site-packages/build* usr/lib64/python3*/site-packages/build* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/build* usr/lib64/python3*/site-packages/build* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-build -f %{oreon_filedir}/python3-build.list

%changelog

%autochangelog
