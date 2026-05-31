%global source0_hash 34af2f15cf7367513b352bdcd2493ab14ce43692d2dcd9dfc499492966c64dcf

Name:           gflags
Version:        2.2.2
Release:        19%{?dist}
Summary:        Library for commandline flag processing

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://gflags.github.io/gflags/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         gflags-fix_pkgconfig.patch
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
The gflags package contains a library that implements commandline
flags processing. As such it's a replacement for getopt(). It has
increased flexibility, including built-in support for C++ types like
string, and the ability to define flags in the source file in which
they're used.

%package devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%cmake -DBUILD_TESTING:BOOL=ON \
       -DINSTALL_HEADERS:BOOL=ON \
       -DREGISTER_BUILD_DIR:BOOL=OFF \
       -DREGISTER_INSTALL_PREFIX:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets

%files
%license COPYING.txt
%doc AUTHORS.txt ChangeLog.txt README.md
%{_bindir}/gflags_completions.sh
%{_libdir}/libgflags.so.*
%{_libdir}/libgflags_nothreads.so.*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libgflags.so
%{_libdir}/pkgconfig/gflags.pc
%{_libdir}/libgflags_nothreads.so
%{_libdir}/cmake/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.2-19
- Import
