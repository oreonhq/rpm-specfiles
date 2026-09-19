%global source0_hash eb2e116e75ecef9d4d228fdc66af54269afa26ab4463042e33785b887c628ba8

%global srcname ipython_genutils

Name:           python-%{srcname}
Version:        0.2.0
Release:        19%{?dist}
Summary:        IPython vestigial utilities

License:        BSD-3-Clause
URL:            https://github.com/ipython/%{srcname}
Source0:        https://pypi.python.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz

# nose is deprecated, use pytest instead
# originally from OpenSUSE
Patch:          Replace-nose-with-pytest.patch

BuildArch:      noarch

%description
This package is a stop-gap that contains some common utilities shared by
Jupyter and IPython projects during The Big Split™. As soon as possible,
those packages will remove their dependency on this, and this repo will go
away.

No functionality should be added to this repository, and no packages outside
IPython/Jupyter should depend on it.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        IPython vestigial utilities
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
This package is a stop-gap that contains some common utilities shared by
Jupyter and IPython projects during The Big Split™. As soon as possible,
those packages will remove their dependency on this, and this repo will go
away.

No functionality should be added to this repository, and no packages outside
IPython/Jupyter should depend on it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import

%pytest -v

 
%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
