%global source0_hash efa59725bba68bf97fa808b61302df32934acdceb6a5c92a8dd0e71dc266a876
%global minimal_needed_proj_version 9.4.0
%bcond xarray 1
Name:           pyproj
Version:        3.8.0
Release:        1%{?dist}
Summary:        Cython wrapper to provide python interfaces to Proj
License:        MIT
URL:            https://github.com/jswhit/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch1:         pyproj-proj-9.7.1.patch
%ifnarch %{ix86}
%if %{with xarray}
%endif
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(setuptools) >= 77.0.1
Requires:       python3-pyproj = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{name}
Summary: %summary
Requires:  proj >= %{minimal_needed_proj_version}
Recommends: python3-shapely
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}

%package -n python3-%{name}-doc
Summary:    Documentation and example code
BuildArch:  noarch
%description -n python3-%{name}-doc
This package contains the html documentation for the pyproj module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export PROJ_DIR="%{_usr}/"
%pyproject_wheel
cd docs
%global py_build_libdir_old %{_builddir}/%{buildsubdir}/build/lib.%{python3_platform}-%{python3_version}
%global py_build_libdir_new %{_builddir}/%{buildsubdir}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}
export PYTHONPATH=%{py_build_libdir_old}:%{py_build_libdir_new}:%{_builddir}/%{buildsubdir}
export PYPROJ_HTML_THEME=sphinx_rtd_theme
make html
make man
%install
export PROJ_DIR="%{_usr}/"
%pyproject_install
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mv %{_builddir}/%{name}-%{version}/docs/_build/html \
   %{buildroot}%{_datadir}/doc/%{name}/html
mkdir -p %{buildroot}/%{_mandir}/man1
cp %{_builddir}/%{name}-%{version}/docs/_build/man/pyproj.1 \
   %{buildroot}/%{_mandir}/man1/
%{__rm} -rf %{_builddir}/%{name}-%{version}/docs
%{__chmod} 755 %{buildroot}/%{python3_sitearch}/%{name}/*.so
chrpath -d %{buildroot}/%{python3_sitearch}/%{name}/*.so
%oreon_autofiles main usr/lib/python3*/site-packages/pyproj* usr/lib64/python3*/site-packages/pyproj* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%py3_check_import pyproj
cd ..
mkdir pyproj-test-folder
cd pyproj-test-folder
cp -r ../pyproj-%{version}/test .
cp ../pyproj-%{version}/pytest.ini .
%ifnarch %{ix86}
%pytest -m "not network"
%else
%pytest -m "not network and not pandas"
%endif
%files
%files -n python3-pyproj -f %{oreon_filedir}/python3-pyproj.list
%files -n python3-pyproj-doc -f %{oreon_filedir}/python3-pyproj-doc.list

%changelog

%autochangelog
