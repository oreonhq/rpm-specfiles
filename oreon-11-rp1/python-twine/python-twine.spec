%global source0_hash 85cdb29c518efef867360ae4acd4b0dfd61c8654a22fca08e6f8539f05022177
Name:           python-twine
Version:        7.0.0
Release:        1%{?dist}
Summary:        Collection of utilities for publishing packages on PyPI
License:        Apache-2.0
URL:            https://twine.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/t/twine/twine-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.0
Requires:       python3-twine = %{version}-%{release}
# /oreon:deps
%package -n       python3-twine+keyring
Summary:        Metapackage for python3-twine keyring extras
Requires:       python3-twine = %{version}-%{release}
Requires:       python3dist(keyring) >= 21.2.0
Provides:       python3dist(twine[keyring]) = %{version}-%{release}

%description -n python3-twine+keyring
Metapackage for python3-twine keyring extras.

%description

%package -n     python3-twine
Summary:        Collection of utilities for publishing packages on PyPI
# oreon:reqs
Requires:       python3dist(keyring) >= 21.2.0
Requires:       python3dist(packaging) >= 26.1
Requires:       python3dist(readme-renderer) >= 35.0
Requires:       python3dist(requests) >= 2.20
Requires:       python3dist(requests-toolbelt) >= 0.8.0
Requires:       python3dist(rfc3986) >= 1.4.0
Requires:       python3dist(rich) >= 14.3.3
Requires:       python3dist(urllib3) >= 1.26.0
# /oreon:reqs
%description -n python3-twine

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir twine-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-twine usr/lib/python3*/site-packages/twine* usr/lib64/python3*/site-packages/twine* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/twine* usr/lib64/python3*/site-packages/twine* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-twine -f %{oreon_filedir}/python3-twine.list

%changelog

%autochangelog
