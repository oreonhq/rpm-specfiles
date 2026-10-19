%global source0_hash b87a35835f30333760cc46194bd90b6a4958d12f488f50131d4c4c0962ad9c3c
Name:           python-cartopy
Version:        0.26.0
Release:        1%{?dist}
Summary:        A Python library for cartographic visualizations with Matplotlib
License:        BSD-3-Clause
URL:            https://github.com/SciTools/cartopy
Source0:        https://files.pythonhosted.org/packages/source/c/cartopy/cartopy-%{version}.tar.gz
Patch:          0001-Reduce-numpy-build-dependency.patch
Patch:          0002-Increase-tolerance-for-new-FreeType.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.0
BuildRequires:  python3dist(numpy) >= 2.0.0
BuildRequires:  python3dist(setuptools) >= 77.0.3
BuildRequires:  python3dist(setuptools-scm) >= 8.0.0
Requires:       python3-cartopy = %{version}-%{release}
# /oreon:deps
%package -n       python3-cartopy+doc
Summary:        Metapackage for python3-cartopy doc extras
Requires:       python3-cartopy = %{version}-%{release}
Provides:       python3dist(cartopy[doc]) = %{version}-%{release}

%description -n python3-cartopy+doc
Metapackage for python3-cartopy doc extras.

%package -n       python3-cartopy+speedups
Summary:        Metapackage for python3-cartopy speedups extras
Requires:       python3-cartopy = %{version}-%{release}
Provides:       python3dist(cartopy[speedups]) = %{version}-%{release}

%description -n python3-cartopy+speedups
Metapackage for python3-cartopy speedups extras.

%package -n       python3-cartopy+ows
Summary:        Metapackage for python3-cartopy ows extras
Requires:       python3-cartopy = %{version}-%{release}
Requires:       python3dist(owslib) >= 0.29.0
Requires:       python3dist(pillow) >= 9.1
Provides:       python3dist(cartopy[ows]) = %{version}-%{release}

%description -n python3-cartopy+ows
Metapackage for python3-cartopy ows extras.

%package -n       python3-cartopy+plotting
Summary:        Metapackage for python3-cartopy plotting extras
Requires:       python3-cartopy = %{version}-%{release}
Requires:       python3dist(pillow) >= 9.1
Requires:       python3dist(scipy) >= 1.11
Provides:       python3dist(cartopy[plotting]) = %{version}-%{release}

%description -n python3-cartopy+plotting
Metapackage for python3-cartopy plotting extras.

%package -n       python3-cartopy+srtm
Summary:        Metapackage for python3-cartopy srtm extras
Requires:       python3-cartopy = %{version}-%{release}
Provides:       python3dist(cartopy[srtm]) = %{version}-%{release}

%description -n python3-cartopy+srtm
Metapackage for python3-cartopy srtm extras.

%package -n       python3-cartopy+test
Summary:        Metapackage for python3-cartopy test extras
Requires:       python3-cartopy = %{version}-%{release}
Requires:       python3dist(pytest) >= 5.1.2
Requires:       python3dist(pytest-mpl) >= 0.11
Requires:       python3dist(packaging) >= 21.0
Provides:       python3dist(cartopy[test]) = %{version}-%{release}

%description -n python3-cartopy+test
Metapackage for python3-cartopy test extras.

%description

%package -n     python3-cartopy
Summary:        A Python library for cartographic visualizations with Matplotlib
# oreon:reqs
Requires:       python3dist(matplotlib) >= 3.8
Requires:       python3dist(numpy) >= 1.26
Requires:       python3dist(packaging) >= 21
Requires:       python3dist(pyproj) >= 3.6
Requires:       python3dist(pyshp) >= 2.3.1
Requires:       python3dist(shapely) >= 2.0
# /oreon:reqs
%description -n python3-cartopy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cartopy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cartopy usr/lib/python3*/site-packages/cartopy* usr/lib64/python3*/site-packages/cartopy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cartopy* usr/lib64/python3*/site-packages/cartopy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cartopy -f %{oreon_filedir}/python3-cartopy.list

%changelog

%autochangelog
