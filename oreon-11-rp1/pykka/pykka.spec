%global source0_hash 68d7b923def1b6464bbc214aa56453f00bab31c66b459803ece0c49ee43f22eb

%global pypi_name Pykka

Name:             pykka
Version:          4.2.0
Release:          6%{?dist}
Summary:          Python library that provides concurrency using actor model

License:          Apache-2.0
URL:              https://pykka.readthedocs.io/
Source0:          %{pypi_source pykka}
BuildArch:        noarch

%description
Pykka is a Python implementation of the actor model. The actor
model introduces some simple rules to control the sharing of state
and cooperation between execution units, which makes it easier to
build concurrent applications.

%package -n python3-%{pypi_name}
Summary:        Python library that provides concurrency using actor model

BuildRequires:    python3-devel
BuildRequires:    python3-pytest
BuildRequires:    python3-pytest-mock

%description -n python3-%{pypi_name}
Pykka is a Python implementation of the actor model. The actor
model introduces some simple rules to control the sharing of state
and cooperation between execution units, which makes it easier to
build concurrent applications.

%package docs
Summary:        Documentation for %{name}

BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-devhelp
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-tomli

Requires:       devhelp

%description docs
This package provides the documentation for %{name}, e.g. the API as
devhelp docs, and examples.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs
SPHINXBUILD='sphinx-build-3 %{_smp_mflags}' make %{_smp_mflags} devhelp
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
mkdir -p %{buildroot}%{_datarootdir}/devhelp/%{pypi_name}
cp -rp docs/_build/devhelp %{buildroot}%{_datarootdir}/devhelp/%{pypi_name}
%pyproject_save_files -L pykka

%check
%pytest tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files docs
%license LICENSE
%doc examples/
%{_datarootdir}/devhelp/%{pypi_name}/
%exclude %{_datarootdir}/devhelp/%{pypi_name}/.*

%changelog
%autochangelog
