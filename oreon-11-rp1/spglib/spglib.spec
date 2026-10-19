%global source0_hash b22fc9abae9716c574fbc6d55cfc53ed654a714fccc5657a26ff5d18114bd8bd
%bcond python %[ !(0%{?epel} && 0%{?epel} <= 9) ]
Name:           spglib
Summary:        C library for finding and handling crystal symmetries
Version:        2.7.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://spglib.readthedocs.io/
Source0:        https://github.com/spglib/spglib/archive/refs/tags/v%{version}.tar.gz
%if %{with python}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy) >= 2.0
BuildRequires:  python3dist(scikit-build-core) >= 0.11
Requires:       python3-spglib = %{version}-%{release}
# /oreon:deps
%package -n       python3-spglib+test
Summary:        Metapackage for python3-spglib test extras
Requires:       python3-spglib = %{version}-%{release}
Provides:       python3dist(spglib[test]) = %{version}-%{release}

%description -n python3-spglib+test
Metapackage for python3-spglib test extras.

%package -n       python3-spglib+docs
Summary:        Metapackage for python3-spglib docs extras
Requires:       python3-spglib = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.0
Requires:       python3dist(sphinxcontrib-bibtex) >= 2.5
Requires:       python3dist(myst-parser) >= 2.0
Provides:       python3dist(spglib[docs]) = %{version}-%{release}

%description -n python3-spglib+docs
Metapackage for python3-spglib docs extras.

%package -n       python3-spglib+test-cov
Summary:        Metapackage for python3-spglib test-cov extras
Requires:       python3-spglib = %{version}-%{release}
Provides:       python3dist(spglib[test-cov]) = %{version}-%{release}

%description -n python3-spglib+test-cov
Metapackage for python3-spglib test-cov extras.

%package -n       python3-spglib+test-benchmark
Summary:        Metapackage for python3-spglib test-benchmark extras
Requires:       python3-spglib = %{version}-%{release}
Provides:       python3dist(spglib[test-benchmark]) = %{version}-%{release}

%description -n python3-spglib+test-benchmark
Metapackage for python3-spglib test-benchmark extras.

%package -n       python3-spglib+dev
Summary:        Metapackage for python3-spglib dev extras
Requires:       python3-spglib = %{version}-%{release}
Provides:       python3dist(spglib[dev]) = %{version}-%{release}

%description -n python3-spglib+dev
Metapackage for python3-spglib dev extras.

%package -n       python3-spglib+doc
Summary:        Metapackage for python3-spglib doc extras
Requires:       python3-spglib = %{version}-%{release}
Provides:       python3dist(spglib[doc]) = %{version}-%{release}

%description -n python3-spglib+doc
Metapackage for python3-spglib doc extras.

%package -n       python3-spglib+testing
Summary:        Metapackage for python3-spglib testing extras
Requires:       python3-spglib = %{version}-%{release}
Provides:       python3dist(spglib[testing]) = %{version}-%{release}

%description -n python3-spglib+testing
Metapackage for python3-spglib testing extras.

%description
C library for finding and handling crystal symmetries.

%package        devel
Summary:        Development files for spglib
Requires:       spglib%{?_isa} = %{version}-%{release}
%description    devel
This package contains libraries and header files for developing
applications that use spglib.

%package        fortran
Summary:        Runtime files for spglib Fortran bindings
Requires:       spglib = %{version}-%{release}
Requires:       gcc-gfortran%{_isa}
%description    fortran
This package contains runtime files to run applications that were built
using spglib's Fortran bindings.

%package        fortran-devel
Summary:        Development files for spglib with Fortran bindings
Requires:       spglib-fortran%{?_isa} = %{version}-%{release}
Requires:       spglib-devel = %{version}-%{release}
%description    fortran-devel
This package contains Fortran module and header files for developing
Fortran applications that use spglib.

%if %{with python}
%package -n     python3-spglib
Summary:        Python3 library of spglib
Requires:       spglib = %{version}-%{release}
# oreon:reqs
Requires:       python3dist(numpy) < 3
Requires:       python3dist(numpy) >= 1.20
Requires:       python3dist(typing-extensions) >= 4.9.0
# /oreon:reqs
%description -n python3-spglib
This package contains the libraries to
develop applications with spglib Python3 bindings.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n spglib-%{version}
%if %{with python}
# Remove the numpy version constraint
tomcli set pyproject.toml arrays replace "build-system.requires" "numpy.*" "numpy"
%endif

%build

%cmake \
    -DSPGLIB_SHARED_LIBS=ON \
    -DSPGLIB_WITH_Fortran=ON \
    -DSPGLIB_WITH_Python=OFF \
    -DSPGLIB_WITH_TESTS=ON \
    -DCMAKE_INSTALL_MODULEDIR=%{_fmoddir}
%cmake_build
%if %{with python}
%{pyproject_wheel %{shrink:
  -C cmake.define.Spglib_ROOT=%{__cmake_builddir}
}}
%endif
%install
%cmake_install
%if %{with python}
%pyproject_install
%oreon_autofiles python3-spglib usr/lib/python3*/site-packages/spglib* usr/lib64/python3*/site-packages/spglib* usr/bin/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/spglib* usr/lib64/python3*/site-packages/spglib* usr/bin/*
%endif
%check

%ctest
%if %{with python}
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %pytest -v
%endif
%files
%files -n spglib-devel -f %{oreon_filedir}/spglib-devel.list
%files -n spglib-fortran -f %{oreon_filedir}/spglib-fortran.list
%files -n spglib-fortran-devel -f %{oreon_filedir}/spglib-fortran-devel.list
%files -n python3-spglib -f %{oreon_filedir}/python3-spglib.list

%changelog

%autochangelog
