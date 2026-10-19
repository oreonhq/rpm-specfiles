%global source0_hash 60e3b8da9f5e68446d4ae3922298e49d54ae534110ac18c29bc1e32d671b5c44
Name:           python-pydaraja
Version:        1.0.0
Release:        1%{?dist}
Summary:        Python wrapper for Mpesa_s Daraja API
License:        ...
URL:            https://github.com/raykipkorir/pydaraja
Source0:        https://files.pythonhosted.org/packages/source/p/pydaraja/pydaraja-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80.8.0
BuildRequires:  python3dist(setuptools-scm) == 8.3.1
Requires:       python3-pydaraja = %{version}-%{release}
# /oreon:deps
%package -n       python3-pydaraja+dev
Summary:        Metapackage for python3-pydaraja dev extras
Requires:       python3-pydaraja = %{version}-%{release}
Requires:       python3dist(pre-commit) >= 3.7.0
Requires:       python3dist(black) >= 23.3.0
Requires:       python3dist(coverage) >= 7.6.0
Requires:       python3dist(pytest) >= 8.3.1
Requires:       python3dist(ruff) >= 0.11.12
Requires:       python3dist(pyright) == 1.1.401
Provides:       python3dist(pydaraja[dev]) = %{version}-%{release}

%description -n python3-pydaraja+dev
Metapackage for python3-pydaraja dev extras.

%package -n       python3-pydaraja+ci
Summary:        Metapackage for python3-pydaraja ci extras
Requires:       python3-pydaraja = %{version}-%{release}
Requires:       python3dist(tox) == 4.34.1
Requires:       python3dist(tox-uv) == 1.29.0
Provides:       python3dist(pydaraja[ci]) = %{version}-%{release}

%description -n python3-pydaraja+ci
Metapackage for python3-pydaraja ci extras.

%description

%package -n     python3-pydaraja
Summary:        Python wrapper for Mpesa_s Daraja API
# oreon:reqs
Requires:       python3dist(requests) >= 2.31.0
# /oreon:reqs
%description -n python3-pydaraja

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pydaraja-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pydaraja usr/lib/python3*/site-packages/pydaraja* usr/lib64/python3*/site-packages/pydaraja* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pydaraja* usr/lib64/python3*/site-packages/pydaraja* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pydaraja -f %{oreon_filedir}/python3-pydaraja.list

%changelog

%autochangelog
