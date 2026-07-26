%global source0_hash e3a7ea10fc72a74fe9949baa8f2598192c4ee77e50ed229b88d6c3ee34381a39

# Force out of source build
%undefine __cmake_in_source_build

%global commit da33770d22b404d7333e46e26495eaca0c5a6d8a
%global gittag 5.9.0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global baserelease 7

ExclusiveArch:  %{ix86} x86_64 aarch64

# Disable 32-bit builds on architectures with multilibs
# to avoid attempting pulling in 32-bit in to koji build.
%ifarch x86_64
%global disable32bit -Ddisable32bit=ON
%endif
Summary:        Tool to record and replay execution of applications
Name:           rr
Version:        5.9.0
Release:        %{baserelease}%{?dist}
# The entire source code is MIT with the exceptions of
# files in following directories:
#   src/external/tree.h            BSD-2-Clause
#   src/test/dlchecksum.c          Zlib
#   third-party/blake2             CC0-1.0
#   third-party/gdb                FSFAP-no-warranty-disclaimer
#   third-party/proc-service       BSD-2-Clause
#   third-party/zen-pmu-workaround GPL-2.0-only
License:        MIT AND BSD-2-Clause AND Zlib AND CC0-1.0 AND FSFAP-no-warranty-disclaimer and GPL-2.0-only
URL:            http://rr-project.org

Source: https://github.com/rr-debugger/rr/archive/%{gittag}/%{name}-%{version}.tar.gz

Patch1: remove-termio.patch
Patch2: update-cmake-ver.patch
# https://github.com/rr-debugger/rr/issues/4037
Patch3: rr-5.9.0-use-openat2-header.patch

%if  0%{?rhel} == 7
BuildRequires: cmake3
BuildRequires: python36-pexpect
%else
BuildRequires: cmake
BuildRequires: python3-pexpect
%endif
BuildRequires: python3
BuildRequires: make gcc gcc-c++ gdb
BuildRequires: libgcc
BuildRequires: glibc-devel
BuildRequires: libstdc++-devel
BuildRequires: man-pages
BuildRequires: capnproto capnproto-libs capnproto-devel
BuildRequires: patchelf
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
BuildRequires: lldb

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
%if  0%{?rhel} == 7
Requires: python36-pexpect
Requires: cmake3
%else
Requires: python3-pexpect
Requires: cmake
%endif
%description testsuite
rr-testsuite includes compiled test binaries and other files
which are used to test the functionality of rr.
 
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rr-%{gittag}

%build
%if  0%{?rhel} == 7
%cmake3 -DCMAKE_BUILD_TYPE=Release -DINSTALL_TESTSUITE=ON %{?disable32bit}
%cmake3_build
%else
%cmake -DCMAKE_BUILD_TYPE=Release -DINSTALL_TESTSUITE=ON %{?disable32bit}
%cmake_build
%endif

%install
%if  0%{?rhel} == 7
%cmake3_install
%else
%cmake_install
%endif

rm -rf %{buildroot}%{_datadir}/rr/src

# Using a small hack from the Dyninst testsuite which changes file permissions
# to prevent any stripping of debugging information. This is done for libraries
# and executables used by the testsuite.
find %{buildroot}%{_libdir}/rr/testsuite/obj/bin \
  -type f -name '*' -execdir chmod 644 '{}' '+'

find %{buildroot}%{_libdir} \
  -type f -name '*.so' -execdir chmod 644 '{}' '+'

# Some files contain invalid RPATHS.
patchelf --set-rpath '%{_libdir}/rr/' %{buildroot}%{_libdir}/rr/testsuite/obj/bin/constructor
patchelf --set-rpath '%{_libdir}/rr/' %{buildroot}%{_libdir}/rr/testsuite/obj/bin/step_into_lib

%files
%dir %{_libdir}/rr
%{_libdir}/rr/*.so
%exclude %{_libdir}/rr/libtest_lib*.so
%{_bindir}/rr
%{_bindir}/rr_exec_stub*
%{_bindir}/signal-rr-recording.sh
%{_bindir}/rr-collect-symbols.py
%{_datadir}/bash-completion/completions/rr
%{_datadir}/zsh/site-functions/_rr
%dir %{_datadir}/rr
%{_datadir}/rr/*.xml

%attr(755,root,root) %{_libdir}/rr/*.so

%files testsuite
%{_libdir}/rr/libtest_lib*.so
%dir %{_libdir}/rr/testsuite
%{_libdir}/rr/testsuite/*

%attr(755,root,root) %{_libdir}/rr/libtest_lib*.so
%attr(755,root,root) %{_libdir}/rr/testsuite/obj/bin/*

%license LICENSE

%changelog
%autochangelog
