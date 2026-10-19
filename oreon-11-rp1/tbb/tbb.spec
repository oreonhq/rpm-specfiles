%global source0_hash 191288b52e1e6b17198000b64d77d194bb65e791be46ebc606e9b091781e2070
%global giturl https://github.com/uxlfoundation/oneTBB
Name:    tbb
Summary:        The Threading Building Blocks library abstracts low-level threading details
Version: 2023.1.0
Release:        1%{?dist}
License: Apache-2.0 AND BSD-3-Clause
URL:     https://uxlfoundation.github.io/oneTBB/
VCS:     git:%{giturl}.git
Source0:        https://github.com/uxlfoundation/oneTBB/archive/refs/tags/v2023.1.0.tar.gz#/tbb-2023.1.0.tar.gz
Source7: tbbmalloc.pc
Source8: tbbmalloc_proxy.pc
Patch:   tbb-c++-linkage.patch
Provides: oneTBB = %{version}-%{release}
Obsoletes:     tbb-doc < 2022.2.0
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-tbb = %{version}-%{release}
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir oneTBB-%{version}
%oreon_prep
%build

export TBBROOT=$PWD
export PYTHONPATH=$(sed "s,%{_prefix},$PWD/%{_vpath_builddir}/python/build," <<< %{python3_sitearch})
%cmake \
    -DCMAKE_CXX_STANDARD=17 \
    -DTBB4PY_BUILD:BOOL=ON \
    -DTBB_STRICT:BOOL=OFF
%cmake_build
unset PYTHONPATH
export LD_LIBRARY_PATH=$(ls -1d $PWD/%{_vpath_builddir}/*relwithdebinfo)
export LDFLAGS="-L $LD_LIBRARY_PATH %{build_ldflags}"
cd python
%pyproject_wheel
cd -
%install
%cmake_install
rm -fr %{buildroot}%{python3_sitearch}
cd python
%pyproject_install
cd -
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
for file in %{SOURCE7} %{SOURCE8}; do
    target=%{buildroot}/%{_libdir}/pkgconfig/$(basename ${file})
    sed 's/_FEDORA_VERSION/%{version}/' $file > $target
    touch -r $file $target
done
if [ -f %{buildroot}/%{_libdir}/pkgconfig/%{name}32.pc ]; then
    ln %{buildroot}/%{_libdir}/pkgconfig/%{name}32.pc %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc
fi
rm -fr %{buildroot}%{_datadir}/doc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/tbb* usr/lib64/python3*/site-packages/tbb* usr/bin/*

%check

ctest --output-on-failure --force-new-ctest-process
%files
%files -n tbb-bind -f %{oreon_filedir}/tbb-bind.list
%files -n tbb-devel -f %{oreon_filedir}/tbb-devel.list
%files -n python3-tbb -f %{oreon_filedir}/python3-tbb.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2022.3.0-3
- Prepare for Oreon 11 (RP1)
