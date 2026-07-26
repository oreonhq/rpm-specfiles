%global source0_hash 5a20c3f79cddaa0abc6a4b99f5486aceed4f88152f29b19a57acc844e183fd4d

Name:           python-numpy-stl
Version:        3.2.0
Release:        %autorelease
Summary:        Library for reading, writing and modifying STL files

License:        BSD-3-Clause
URL:            https://github.com/WoLpH/numpy-stl/
Source:         %{pypi_source numpy_stl}

BuildRequires:  gcc

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-PyQt5
BuildRequires:  /usr/bin/xvfb-run

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
ExcludeArch:    %{ix86}
%endif

%description
Simple library to make working with STL files (and 3D objects in general) fast
and easy. Due to all operations heavily relying on numpy this is one of the
fastest STL editing libraries for Python available.

%package -n     python3-numpy-stl
Summary:        %{summary}

%description -n python3-numpy-stl
Simple library to make working with STL files (and 3D objects in general) fast
and easy. Due to all operations heavily relying on NumPy this is one of the
fastest STL editing libraries for Python available.

%package        doc
Summary:        %{name} documentation
Suggests:       python3-numpy-stl
BuildArch:      noarch
%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n numpy_stl-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files stl

%check
%pytest -v

%files -n python3-numpy-stl -f %{pyproject_files}
%doc README.rst
%{_bindir}/stl
%{_bindir}/stl2bin
%{_bindir}/stl2ascii

%files doc
%doc html

%changelog
%autochangelog
