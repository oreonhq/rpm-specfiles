%global source0_hash 39a0cf1ecc7e282d1d30f36594ebd55c9fae1fda8a2622cee5d100430628f88c

# note: PROJ_MIN_VERSION is defined in the setup.py file of pyproj
# a compatibility matrix is also provided in docs/installation.rst
%global minimal_needed_proj_version 9.4.0

%bcond xarray 1

Name:           pyproj
Version:        3.7.2
Release:        5%{?dist}
Summary:        Cython wrapper to provide python interfaces to Proj
# this software uses the "MIT:Modern Style with sublicense" license
License:        MIT
URL:            https://github.com/jswhit/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

# see: https://github.com/pyproj4/pyproj/issues/1553
# and: https://github.com/pyproj4/pyproj/pull/1557
Patch1:         pyproj-proj-9.7.1.patch

BuildRequires:  gcc
BuildRequires:  proj-devel >= %{minimal_needed_proj_version}
BuildRequires:  proj >= %{minimal_needed_proj_version}

# these next 3 lines are no longer needed and taken care of automagically
#BuildRequires:  make
#BuildRequires:  python3-cython
#BuildRequires:  python3-certifi
#BuildRequires:  python3-shapely

# needed to run the tests
BuildRequires:  python3-pytest
# needed for i686 testing
BuildRequires:  python3-numpy

# Pandas will drop i686 (xarray depends on pandas)
# https://bugzilla.redhat.com/show_bug.cgi?id=2263999 
%ifnarch %{ix86}
BuildRequires:  python3-pandas
%if %{with xarray}
BuildRequires:  python3-xarray
%endif
%endif

# needed to remove the hardcoded rpath '/usr/lib' from the _proj.so file
BuildRequires:  chrpath

# needed to build the documentation
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-argparse
BuildRequires:  python3-sphinx_rtd_theme

%global _description \
Cython wrapper to provide python interfaces to Proj. \
Performs cartographic transformations between geographic (Lat/Lon) \
and map projection (x/y) coordinates. Can also transform directly \
from one map projection coordinate system to another. \
Coordinates can be given as numpy arrays, python arrays, lists or scalars. \
Optimized for numpy arrays.

%description %_description

%package -n python3-%{name}

Summary: %summary

Requires:  proj >= %{minimal_needed_proj_version}

# Add shapely as (optional/weak) dependency.
# For details see: https://github.com/pyproj4/pyproj/issues/1470
Recommends: python3-shapely

# ensure python provides are provided when python3 becomes the default runtime
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name} %_description

%package -n python3-%{name}-doc

Summary:    Documentation and example code
BuildArch:  noarch

%description -n python3-%{name}-doc
This package contains the html documentation for the pyproj module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
export PROJ_DIR="%{_usr}/"

%pyproject_wheel

# generate documentation
cd docs

# Need to point to the build dir so sphinx can import the module
# before it is installed.
# Note that the new Python macros have %%{pyproject_build_lib} for this,
# but this package uses the old macros, so we need to replicate the behavior
# manually.
# The path has changed in setuptools 62.4.0,
# see https://bugzilla.redhat.com/2097115
%global py_build_libdir_old %{_builddir}/%{buildsubdir}/build/lib.%{python3_platform}-%{python3_version}
%global py_build_libdir_new %{_builddir}/%{buildsubdir}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}

# NOTE: need to add %%{_builddir}/%%{buildsubdir} as well to the path
# since sphinx needs to be able to find the PKG-INFO file
# before it will generate the documentation,
# and this is the only place where it is available before installation.
# (see: https://github.com/python/importlib_metadata/issues/364)
export PYTHONPATH=%{py_build_libdir_old}:%{py_build_libdir_new}:%{_builddir}/%{buildsubdir}

# default theme is now "furo" which is not available in fedora
# (see BZ #1910798 and https://github.com/pyproj4/pyproj/discussions/1134)
# so fall back to the previous theme:
export PYPROJ_HTML_THEME=sphinx_rtd_theme

make html
make man

%install
export PROJ_DIR="%{_usr}/"
%pyproject_install
%pyproject_save_files -l pyproj

# move html documentation to datadir/doc
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mv %{_builddir}/%{name}-%{version}/docs/_build/html \
   %{buildroot}%{_datadir}/doc/%{name}/html

# copy pyproj man page
mkdir -p %{buildroot}/%{_mandir}/man1
cp %{_builddir}/%{name}-%{version}/docs/_build/man/pyproj.1 \
   %{buildroot}/%{_mandir}/man1/

# remove the documentation sources and generated doctrees
# since they dont belong in the main package
%{__rm} -rf %{_builddir}/%{name}-%{version}/docs

# correct wrong write permission for group
%{__chmod} 755 %{buildroot}/%{python3_sitearch}/%{name}/*.so

# remove the rpath setting from _proj.so
chrpath -d %{buildroot}/%{python3_sitearch}/%{name}/*.so

%check

# check importing the pyproj module
%py3_check_import pyproj

# follow the hint given in pyproj github issue
# https://github.com/pyproj4/pyproj/issues/647
# i.e. take the test folder outside the build folder
# to prevent the
#    cannot import name '_datadir' from partially initialized module
#    'pyproj' (most likely due to a circular import) 
# error.
# (probably this is not needed anymore but it doesn't hurt to leave this in)
cd ..
mkdir pyproj-test-folder
cd pyproj-test-folder
cp -r ../pyproj-%{version}/test .
cp ../pyproj-%{version}/pytest.ini .

# Test without pandas on i686
%ifnarch %{ix86}
%pytest -m "not network"
%else
%pytest -m "not network and not pandas"
%endif

# some notes on the test suite:
# not network ==> deselects 24 tests

%files -n python3-%{name} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/pyproj*

%files -n python3-%{name}-doc
%doc %{_datadir}/doc/%{name}/

%changelog
%autochangelog
