%global source0_hash 6eef7dce88bdb4ebb0ba11b209d65b6f8e47d84c9c9bff351ecbbe681c55f413

%global srcname traitlets

Name:           python-%{srcname}
Version:        5.14.3
Release:        %autorelease
Summary:        A lightweight derivative of Enthought Traits for configuring Python objects

License:        BSD-3-Clause
URL:            https://github.com/ipython/traitlets
Source0:        https://github.com/ipython/traitlets/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
A lightweight pure-Python derivative of Enthought Traits, used for
configuring Python objects.

This package powers the config system of IPython and Jupyter.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        A lightweight derivative of Enthought Traits for configuring Python objects
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
A lightweight pure-Python derivative of Enthought Traits, used for
configuring Python objects.

This package powers the config system of IPython and Jupyter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Remove tests of type annotations
rm tests/test_typing.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files traitlets

%check
%pytest -v

 
%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE

%changelog
%autochangelog
