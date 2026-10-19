%global source0_hash e3a7ea10fc72a74fe9949baa8f2598192c4ee77e50ed229b88d6c3ee34381a39
%undefine __cmake_in_source_build
%global commit da33770d22b404d7333e46e26495eaca0c5a6d8a
%global gittag 5.9.0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global baserelease 7
ExclusiveArch:  %{ix86} x86_64 aarch64
%ifarch x86_64
%global disable32bit -Ddisable32bit=ON
%endif
Summary:        Tool to record and replay execution of applications
Name:           rr
Version:        5.9.0
Release:        7%{?dist}
License:        MIT AND BSD-2-Clause AND Zlib AND CC0-1.0 AND FSFAP-no-warranty-disclaimer and GPL-2.0-only
URL:            http://rr-project.org
Source0:        https://github.com/%{name}-debugger/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1: remove-termio.patch
Patch2: update-cmake-ver.patch
Patch3: rr-5.9.0-use-openat2-header.patch
# oreon:deps
BuildRequires:  capnproto
BuildRequires:  capnproto-devel
BuildRequires:  capnproto-libs
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  glibc-devel
BuildRequires:  libgcc
BuildRequires:  libstdc++-devel
BuildRequires:  libzstd-devel
BuildRequires:  lldb
BuildRequires:  make
BuildRequires:  man-pages
BuildRequires:  patchelf
BuildRequires:  python3
BuildRequires:  python3-pexpect
BuildRequires:  zlib-devel
# /oreon:deps
%description
rr is a lightweight tool for recording and replaying execution
of applications (trees of processes and threads).
For more information, please visit http://rr-project.org

%package testsuite
Summary: Testsuite for checking rr functionality
Requires: rr
Requires: gdb
Requires: lldb
Requires: python3
Requires: python3-pexpect
Requires: cmake
%description testsuite
rr-testsuite includes compiled test binaries and other files
which are used to test the functionality of rr.
 
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rr-%{gittag}

%build

%cmake -DCMAKE_BUILD_TYPE=Release -DINSTALL_TESTSUITE=ON %{?disable32bit}
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/rr/src
find %{buildroot}%{_libdir}/rr/testsuite/obj/bin \
  -type f -name '*' -execdir chmod 644 '{}' '+'
find %{buildroot}%{_libdir} \
  -type f -name '*.so' -execdir chmod 644 '{}' '+'
patchelf --set-rpath '%{_libdir}/rr/' %{buildroot}%{_libdir}/rr/testsuite/obj/bin/constructor
patchelf --set-rpath '%{_libdir}/rr/' %{buildroot}%{_libdir}/rr/testsuite/obj/bin/step_into_lib
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rr-testsuite -f %{oreon_filedir}/rr-testsuite.list

%changelog

%autochangelog
