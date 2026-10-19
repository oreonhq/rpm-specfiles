%global source0_hash 6aff7aa1d9e6e5351df8f979f4b647a3b347f635e306b26e2682fd3b59d8e6a8
Name:           python-matrix-nio
Version:        0.26.0
Release:        1%{?dist}
Summary:        A Python Matrix client library, designed according to sans I/O principles.
License:        ...
URL:            https://github.com/matrix-nio/matrix-nio
Source0:        https://files.pythonhosted.org/packages/source/m/matrix_nio/matrix_nio-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-matrix-nio = %{version}-%{release}
# /oreon:deps
%package -n       python3-matrix-nio+e2e
Summary:        Metapackage for python3-matrix-nio e2e extras
Requires:       python3-matrix-nio = %{version}-%{release}
Requires:       python3dist(atomicwrites) >= 1.4
Requires:       python3dist(cachetools) >= 5.3
Requires:       python3dist(peewee) >= 3.14
Requires:       python3dist(vodozemac) >= 0.9.0.post2
Provides:       python3dist(matrix-nio[e2e]) = %{version}-%{release}

%description -n python3-matrix-nio+e2e
Metapackage for python3-matrix-nio e2e extras.

%package -n       python3-matrix-nio+docs
Summary:        Metapackage for python3-matrix-nio docs extras
Requires:       python3-matrix-nio = %{version}-%{release}
Requires:       python3dist(setuptools) >= 61.0
Requires:       python3dist(sphinx) >= 7.4
Requires:       python3dist(sphinx-autodoc-typehints) >= 2.1
Requires:       python3dist(sphinx-mdinclude) >= 0.5
Requires:       python3dist(sphinx-rtd-theme) >= 2.0
Provides:       python3dist(matrix-nio[docs]) = %{version}-%{release}

%description -n python3-matrix-nio+docs
Metapackage for python3-matrix-nio docs extras.

%description

%package -n     python3-matrix-nio
Summary:        A Python Matrix client library, designed according to sans I/O principles.
# oreon:reqs
Requires:       python3dist(aiofiles) >= 24.1
Requires:       python3dist(aiohttp) >= 3.10
Requires:       python3dist(aiohttp-socks) >= 0.8
Requires:       python3dist(h11) >= 0.14
Requires:       python3dist(h2) >= 4.0
Requires:       python3dist(jsonschema) >= 4.14
Requires:       python3dist(pycryptodome) >= 3.10
Requires:       python3dist(unpaddedbase64) >= 2.1
# /oreon:reqs
%description -n python3-matrix-nio

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir matrix_nio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-matrix-nio usr/lib/python3*/site-packages/matrix_nio* usr/lib64/python3*/site-packages/matrix_nio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/matrix_nio* usr/lib64/python3*/site-packages/matrix_nio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-matrix-nio -f %{oreon_filedir}/python3-matrix-nio.list

%changelog

%autochangelog
