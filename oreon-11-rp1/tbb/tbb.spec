# Python docs can no longer be built as of version 2022.1.0 due to requiring
# sphinx_book_theme, which is not available in Fedora or RHEL

%global giturl https://github.com/uxlfoundation/oneTBB

Name:    tbb
Summary: The Threading Building Blocks library abstracts low-level threading details
Version: 2022.3.0
Release: 3%{?dist}
License: Apache-2.0 AND BSD-3-Clause
URL:     https://uxlfoundation.github.io/oneTBB/
VCS:     git:%{giturl}.git

Source0:        https://github.com/uxlfoundation/oneTBB/archive/v2022.3.0/tbb-2022.3.0.tar.gz
# These two are downstream sources.
Source7: tbbmalloc.pc
Source8: tbbmalloc_proxy.pc

# Fix failure to link with GCC 15
Patch:   tbb-c++-linkage.patch
# oreon url source checksums begin
%global source0_sha256 01598a46c1162c27253a0de0236f520fd8ee8166e9ebb84a4243574f88e6e50a
%global source0_file tbb-2022.3.0.tar.gz
# oreon url source checksums end

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: hwloc
BuildRequires: hwloc-devel
BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
BuildRequires: swig

Provides: oneTBB = %{version}-%{release}

# This can be removed when F47 reaches EOL
Obsoletes:     tbb-doc < 2022.2.0

%description
Threading Building Blocks (TBB) is a C++ runtime library that
abstracts the low-level threading details necessary for optimal
multi-core performance.  It uses common C++ templates and coding style
to eliminate tedious threading implementation work.

TBB requires fewer lines of code to achieve parallelism than other
threading models.  The applications you write are portable across
platforms.  Since the library is also inherently scalable, no code
maintenance is required as more processor cores become available.


%package bind
Summary: NUMA support library for TBB
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides: oneTBB-bind = %{version}-%{release}

%description bind
NUMA support library for TBB, allowing the binding of tasks to selected
CPU cores.


%package devel
Summary: The Threading Building Blocks C++ headers and shared development libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-bind%{?_isa} = %{version}-%{release}

Provides: oneTBB-devel = %{version}-%{release}

%description devel
Header files and shared object symlinks for the Threading Building
Blocks (TBB) C++ libraries.


%package -n python3-%{name}
Summary: Python 3 TBB module
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python 3 TBB module.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/tbb-2022.3.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "01598a46c1162c27253a0de0236f520fd8ee8166e9ebb84a4243574f88e6e50a" || { echo "oreon: Source0 SHA256 mismatch for tbb-2022.3.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n oneTBB-%{version}

%generate_buildrequires
cd python
%pyproject_buildrequires

%build
export TBBROOT=$PWD
export PYTHONPATH=$(sed "s,%{_prefix},$PWD/%{_vpath_builddir}/python/build," <<< %{python3_sitearch})
%cmake \
    -DCMAKE_CXX_STANDARD=17 \
    -DTBB4PY_BUILD:BOOL=ON \
    -DTBB_STRICT:BOOL=OFF
%cmake_build

# The python package is not built the Fedora way.  Do it over.
unset PYTHONPATH
export LD_LIBRARY_PATH=$(ls -1d $PWD/%{_vpath_builddir}/*relwithdebinfo)
export LDFLAGS="-L $LD_LIBRARY_PATH %{build_ldflags}"
cd python
%pyproject_wheel
cd -

%install
%cmake_install

# The python package is not installed the Fedora way.  Do it over.
rm -fr %{buildroot}%{python3_sitearch}
cd python
%pyproject_install
%pyproject_save_files -L TBB tbb
cd -

mkdir -p %{buildroot}/%{_libdir}/pkgconfig
for file in %{SOURCE7} %{SOURCE8}; do
    target=%{buildroot}/%{_libdir}/pkgconfig/$(basename ${file})
    sed 's/_FEDORA_VERSION/%{version}/' $file > $target
    touch -r $file $target
done

# Upstream installs tbb32.pc on 32-bit but it's already in a separate directory
# because %_libdir is different for 32-bit and 64-bit.
# Some projects expect tbb.pc and some expect tbb32.pc, so provide both (as hard
# links).
if [ -f %{buildroot}/%{_libdir}/pkgconfig/%{name}32.pc ]; then
    ln %{buildroot}/%{_libdir}/pkgconfig/%{name}32.pc %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc
fi

rm -fr %{buildroot}%{_datadir}/doc

%check
# Running the tests in parallel often leads to resource exhaustion.
ctest --output-on-failure --force-new-ctest-process

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/libtbb.so.12{,.*}
%{_libdir}/libtbbmalloc.so.2{,.*}
%{_libdir}/libtbbmalloc_proxy.so.2{,.*}
%{_libdir}/libirml.so.1

%files bind
%{_libdir}/libtbbbind_2_5.so.3{,.*}

%files devel
%doc cmake/README.md
%{_includedir}/oneapi/
%{_includedir}/tbb/
%{_libdir}/*.so
%{_libdir}/cmake/TBB/
%{_libdir}/pkgconfig/*.pc

%files -n python3-%{name} -f %{pyproject_files}
%doc python/README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2022.3.0-3
- Prepare for Oreon 11 (RP1)
