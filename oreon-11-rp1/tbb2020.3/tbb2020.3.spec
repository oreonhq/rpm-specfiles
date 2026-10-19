%global source0_hash ebc4f6aa47972daed1f7bf71d100ae5bf6931c2e3144cf299c8cc7d041dca2f3
Name:    tbb2020.3
Summary:        The Threading Building Blocks library abstracts low-level threading details
Version: 2020.3
Release:        1%{?dist}
License: Apache-2.0 AND BSD-3-Clause
URL:     http://threadingbuildingblocks.org/
Source0:        https://github.com/intel/tbb/archive/v%{version}/tbb-%{version}.tar.gz
Source6: tbb.pc
Source7: tbbmalloc.pc
Source8: tbbmalloc_proxy.pc
Patch0: tbb-2019-dont-snip-Wall.patch
Patch1: tbb-2020-attributes.patch
Patch2: tbb-2019-test-thread-monitor.patch
Patch3: tbb-2019-test-task-scheduler-init.patch
Patch4: tbb-mark-empty_task-execute-with-gnu-used.patch
Patch5: tbb-2020-task-namespace.patch
Patch6: tbb2020.3-compat.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  swig
BuildRequires:  tbb
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

%package devel
Summary: The Threading Building Blocks C++ headers and shared development libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: tbb%{?_isa}
Conflicts: tbb-devel
%description devel
Header files and shared object symlinks for the Threading Building
Blocks (TBB) C++ libraries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n oneTBB-%{version}

# For repeatable builds, don't query the hostname or architecture
sed -i 's/"`hostname -s`" ("`uname -m`"/fedorabuild (%{_arch}/' \
    build/version_info_linux.sh

# Insert --as-needed before the libraries to be linked.
sed -i "s/-fPIC/& -Wl,--as-needed/" build/linux.gcc.inc

%build

compiler=""
if [[ %{__cc} == *"gcc"* ]]; then
    compiler="gcc"
elif [[ %{__cc} == *"clang"* ]]; then
    compiler="clang"
else
    compiler="%{__cc}"
fi
%make_build tbb_build_prefix=obj stdver=c++14 \
    compiler=${compiler} \
    CXXFLAGS="%{optflags} -DUSE_PTHREAD" \
    LDFLAGS="$RPM_LD_FLAGS -lpthread" tbb
for file in %{SOURCE6} %{SOURCE7} %{SOURCE8}; do
    base=$(basename ${file})
    sed 's/_FEDORA_VERSION/%{version}/' ${file} > ${base}
    touch -r ${file} ${base}
done
%check

sed -i '/test_task_scheduler_observer/d' build/Makefile.test
make test tbb_build_prefix=obj stdver=c++14 CXXFLAGS="%{optflags}"
%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}
pushd build/obj_release
    for file in libtbb; do
        install -p -D -m 755 ${file}.so.2 $RPM_BUILD_ROOT/%{_libdir}
        ln -s $file.so.2 $RPM_BUILD_ROOT/%{_libdir}/$file.so
    done
popd
ln -s libtbbmalloc.so.2 $RPM_BUILD_ROOT/%{_libdir}/libtbbmalloc.so
ln -s libtbbmalloc_proxy.so.2 $RPM_BUILD_ROOT/%{_libdir}/libtbbmalloc_proxy.so
ln -s libirml.so.1 $RPM_BUILD_ROOT/%{_libdir}/libirml.so
pushd include
    find tbb -type f ! -name \*.htm\* -exec \
        install -p -D -m 644 {} $RPM_BUILD_ROOT/%{_includedir}/{} \
    \;
popd
for file in %{SOURCE6} %{SOURCE7} %{SOURCE8}; do
    install -p -D -m 644 $(basename ${file}) \
        $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/$(basename ${file})
done
mkdir -p $RPM_BUILD_ROOT%{_includedir}/rml
cp -p src/rml/include/*.h $RPM_BUILD_ROOT%{_includedir}/rml
cmake \
  -DINSTALL_DIR=$RPM_BUILD_ROOT%{_libdir}/cmake/TBB \
  -DSYSTEM_NAME=Linux \
  -DLIB_REL_PATH=../.. \
  -P cmake/tbb_config_installer.cmake
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tbb2020.3-devel -f %{oreon_filedir}/tbb2020.3-devel.list

%changelog

%autochangelog
