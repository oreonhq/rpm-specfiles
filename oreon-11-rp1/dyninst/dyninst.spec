Summary: An API for Run-time Code Generation
License: LGPL-2.1-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2 AND LicenseRef-Fedora-Public-Domain AND BSD-3-Clause
Name: dyninst
Group: Development/Libraries
Release: 9%{?dist}
URL: https://www.paradyn.org
Version: 13.0.0
ExclusiveArch: x86_64 ppc64le aarch64

Source0: https://github.com/dyninst/dyninst/archive/refs/tags/v%{version}.tar.gz#/dyninst-%{version}.tar.gz
Patch1: github-pr1721.patch
Patch2: github-pr1880.patch
Patch3: github-pr1880-ish.patch
Patch4: github-pr1730.patch

%global dyninst_base dyninst-%{version}

BuildRequires: gcc-c++
BuildRequires: elfutils-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: elfutils-debuginfod-client-devel
BuildRequires: boost-devel
BuildRequires: binutils-devel
BuildRequires: cmake
BuildRequires: libtirpc-devel
BuildRequires: tbb tbb-devel
BuildRequires: tex-latex
BuildRequires: make

# https://fedoraproject.org/wiki/Changes/Linker_Error_On_Security_Issues
# may impact the RT library
%undefine _hardened_linker_errors

%description

Dyninst is an Application Program Interface (API) to permit the insertion of
code into a running program. The API also permits changing or removing
subroutine calls from the application program. Run-time code changes are
useful to support a variety of applications including debugging, performance
monitoring, and to support composing applications out of existing packages.
The goal of this API is to provide a machine independent interface to permit
the creation of tools and applications that use run-time code patching.

%package doc
Summary: Documentation for using the Dyninst API
Group: Documentation
%description doc
dyninst-doc contains API documentation for the Dyninst libraries.
License: LGPL-2.1-or-later

%package devel
Summary: Header files for compiling programs with Dyninst
Group: Development/System
Requires: dyninst = %{version}-%{release}
Requires: boost-devel
Requires: tbb-devel
License: LGPL-2.1-or-later AND BSD-3-Clause AND MIT
# FindTBB.cmake: presumed MIT, removed in next version of dyninst

%description devel
dyninst-devel includes the C header files that specify the Dyninst user-space
libraries and interfaces. This is required for rebuilding any program
that uses Dyninst.

%prep
%setup -q -n %{name}-%{version} -c
# %setup -q -T -D -a 1

pushd %{dyninst_base}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
popd

# cotire seems to cause non-deterministic gcc errors
# https://bugzilla.redhat.com/show_bug.cgi?id=1420551
# sed -i.cotire -e 's/USE_COTIRE true/USE_COTIRE false/' \
#  %{dyninst_base}/cmake/shared.cmake

%build

cd %{dyninst_base}

CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
LDFLAGS="$LDFLAGS $RPM_LD_FLAGS"
%ifarch %{ix86}
    CFLAGS="$CFLAGS -fno-lto -march=i686"
    LDFLAGS="$LDFLAGS -fno-lto"
%endif    
CXXFLAGS="$CFLAGS"
export CFLAGS CXXFLAGS LDFLAGS

%cmake --log-level=DEBUG \
 -DENABLE_DEBUGINFOD=1 \
 -DCMAKE_BUILD_TYPE=None \
 -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DINSTALL_CMAKE_DIR:PATH=/usr/lib64/cmake/Dyninst \
 -DCMAKE_INSTALL_PREFIX:PATH=/usr \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=/usr/include/dyninst \
 -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib64/dyninst
%cmake_build -v -v -v

%install

cd %{dyninst_base}
%cmake_install -v -v -v

# move /usr/lib64//dyninst/cmake/Dyninst to /usr/lib64/cmake/Dyninst
mkdir -p %{buildroot}/%{_libdir}/cmake
mv %{buildroot}/%{_libdir}/dyninst/cmake/Dyninst %{buildroot}/%{_libdir}/cmake/Dyninst

# this is a testsuite-like binary, not needed in main package
rm -f "%{buildroot}%{_bindir}/parseThat"

mkdir -p %{buildroot}/etc/ld.so.conf.d
echo "%{_libdir}/dyninst" > %{buildroot}/etc/ld.so.conf.d/%{name}-%{_arch}.conf

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%dir %{_libdir}/dyninst
%{_libdir}/dyninst/*.so.*
# dyninst mutators dlopen the runtime library
%{_libdir}/dyninst/libdyninstAPI_RT.so
%{_libdir}/dyninst/libdyninstAPI_RT.a

%doc %{dyninst_base}/COPYRIGHT
%doc %{dyninst_base}/LICENSE.md

%config(noreplace) /etc/ld.so.conf.d/*

%files doc
%doc %{dyninst_base}/dataflowAPI/doc/dataflowAPI.pdf
%doc %{dyninst_base}/dynC_API/doc/dynC_API.pdf
%doc %{dyninst_base}/dyninstAPI/doc/dyninstAPI.pdf
%doc %{dyninst_base}/instructionAPI/doc/instructionAPI.pdf
%doc %{dyninst_base}/parseAPI/doc/parseAPI.pdf
%doc %{dyninst_base}/patchAPI/doc/patchAPI.pdf
%doc %{dyninst_base}/proccontrol/doc/proccontrol.pdf
%doc %{dyninst_base}/stackwalk/doc/stackwalk.pdf
%doc %{dyninst_base}/symtabAPI/doc/symtabAPI.pdf

%files devel
%{_includedir}/dyninst
%{_libdir}/dyninst/*.so
%{_libdir}/cmake/Dyninst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.0-9
- Prepare for Oreon 11 (RP1)
