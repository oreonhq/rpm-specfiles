%global source0_hash 4f259e80cdfb6b3fc18a7de51fd1ef9ec79652f25019bae68975ca2468a34df8
Name:           python-pyjwt
Version:        2.15.1
Release:        1%{?dist}
Summary:        JSON Web Token implementation in Python
License:        MIT
URL:            https://github.com/jpadilla/pyjwt
Source0:        https://files.pythonhosted.org/packages/source/p/pyjwt/pyjwt-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-pyjwt = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyjwt+crypto
Summary:        Metapackage for python3-pyjwt crypto extras
Requires:       python3-pyjwt = %{version}-%{release}
Requires:       python3dist(cryptography) >= 3.4.0
Provides:       python3dist(pyjwt[crypto]) = %{version}-%{release}

%description -n python3-pyjwt+crypto
Metapackage for python3-pyjwt crypto extras.

%description

%package -n     python3-pyjwt
Summary:        JSON Web Token implementation in Python
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.0
# /oreon:reqs
%description -n python3-pyjwt

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyjwt-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyjwt usr/lib/python3*/site-packages/pyjwt* usr/lib64/python3*/site-packages/pyjwt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyjwt* usr/lib64/python3*/site-packages/pyjwt* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyjwt -f %{oreon_filedir}/python3-pyjwt.list

%changelog

%autochangelog
