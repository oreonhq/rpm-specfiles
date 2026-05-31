%global source0_hash a3f8040b0273dec773e0e807e86a4d0a9535516c0a0a35aa1bb6de6e15bb1f09

# cloud-sptheme is not included in RHEL
%bcond docs %[%{undefined rhel} || %{defined epel}]

%global pypi_name rjsmin
%global desc %{expand: \
The minifier is based on the semantics of jsmin.c by Douglas Crockford.

The module is a re-implementation aiming for speed, so it can be used at
runtime (rather than during a preprocessing step). Usually it produces the
same results as the original jsmin.c.}

Name:           python-%{pypi_name}
Version:        1.2.5
Release:        %autorelease
Summary:        Javascript Minifier

License:        Apache-2.0
URL:            http://opensource.perlig.de/rjsmin/
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%if %{with docs}
BuildRequires:  python3-furo
BuildRequires:	python3-sphinx
%endif

%description %{desc}

%package -n python3-%{pypi_name}
Summary:	Javascript Minifier

%description -n python3-%{pypi_name}
%{desc}

%package docs
Summary:	Javascript Minifier - docs

%description docs
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version}

# strip bang path from rjsmin.py
sed -i '1d' rjsmin.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with docs}
PYTHONPATH=. sphinx-build -b html docs/_userdoc docs/_userdoc/html
# Remove the sphinx-build leftovers.
rm -rf docs/_userdoc/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
	
%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/_%{pypi_name}.cpython*

%files docs
%license LICENSE
%doc README.md
%if %{with docs}
%doc docs/_userdoc/html
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.5-1
- Prepare for Oreon 11 (RP1)
