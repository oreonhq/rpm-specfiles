%global source0_hash 7ad941571c02b9afa685cb92fb85fb5ed2cd0e36c4ec40cb74d7782dc7975400
%global __provides_exclude_from ^(%{python3_sitearch})/.*\\.so.*$
Name:       pygrib
Version:    2.1.8
Release:        1%{?dist}
Summary:        Python module for reading and modifying GRIB files
License:    MIT AND BSD-2-Clause
URL:        https://github.com/jswhit/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch1: %{name}-build.patch
Patch2: %{name}-test-gaussian.patch
ExcludeArch: i686
ExcludeArch: armv7hl
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.29.2
BuildRequires:  python3dist(numpy) >= 2.0.0
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-pygrib = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{name}
Summary: %summary
Requires:  eccodes
Requires:  python3-pyproj
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mv %{_builddir}/%{name}-%{version}/docs/_build/html \
   %{buildroot}%{_datadir}/doc/%{name}/html
mkdir -p %{buildroot}/%{_mandir}/man1
cp %{_builddir}/%{name}-%{version}/man/*.1 \
   %{buildroot}/%{_mandir}/man1/
%{__rm} %{buildroot}%{_datadir}/doc/%{name}/html/.buildinfo
%oreon_autofiles main usr/lib/python3*/site-packages/pygrib* usr/lib64/python3*/site-packages/pygrib* usr/bin/*

%check

export PYTHONPATH=%{buildroot}/%{python3_sitearch}
export MPLBACKEND=agg
export TESTROOT=%{_builddir}/%{name}-%{version}-tmp-test
mkdir $TESTROOT
cp -R sampledata $TESTROOT
cp -R test $TESTROOT
cd  $TESTROOT/test
%{__python3} -c "import pygrib"
%{__python3} test.py
%{__python3} run_tests.py
%{__python3} test_spectral.py
%pytest test_gaussian.py test_latlons.py \
        test_lambert.py test_ndfd_conus.py \
        test_ndfd_pr.py \
        test_rotated_ll.py test_set_bitmap.py  test_stere.py \
        --mpl --mpl-baseline-path=`pwd`/baseline_images
%files
%files -n python3-pygrib -f %{oreon_filedir}/python3-pygrib.list

%changelog

%autochangelog
