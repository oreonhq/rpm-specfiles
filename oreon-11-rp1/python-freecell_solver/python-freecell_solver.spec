%global source0_hash b8b26d929a42da6745f55b1c232d0a546b26c1fabf68a73dc2736f695c89386d

%global pypi_name freecell_solver

Name:           python-%{pypi_name}
Version:        0.2.6
Release:        23%{?dist}
Summary:        Freecell Solver Python bindings

License:        MIT
URL:            https://fc-solve.shlomifish.org/
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(openstackdocstheme)
BuildRequires:  python3dist(oslotest) >= 1.10.0
BuildRequires:  python3dist(sphinx)

%description
Python bindings for Freecell Solver using cffi.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Python bindings for Freecell Solver using cffi.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for freecell_solver
%description -n python-%{pypi_name}-doc
Documentation for freecell_solver

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst doc/source/readme.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
