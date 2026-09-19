%global source0_hash f0e471c1bf4e7804a6cfb41ea9d13e7d623b2bcc7bc1e2a4dd54951a24d60285

#%%global dev rc1

Name:           civetweb
Summary:        Embedded C/C++ web server
Version:        1.16
Release:        13%{?dev:%{dev}}%{?dist}
License:        MIT
Url:            https://github.com/civetweb/civetweb
Source:         https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:		0001-CMakeLists.txt.patch
Patch:		0002-src-civetweb.c.patch
Patch:		0003-src-civetweb.c.patch
BuildRequires:  cmake make gcc-c++

%description
Civetweb is an easy to use, powerful, C (C/C++) embeddable web server
with optional CGI, SSL and Lua support.

CivetWeb can be used by developers as a library, to add web server
functionality to an existing application. It can also be used by end
users as a stand-alone web server running on a Windows or Linux PC.
It is available as single executable, no installation is required.

%package devel
Summary:        Civetweb Client Library C and C++ header files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Civetweb shared libs and associated header files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{cmake} . \
    -G "Unix Makefiles" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_CONFIG=rpmbuild \
    -DCIVETWEB_ENABLE_CXX:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCIVETWEB_BUILD_TESTING:BOOL=OFF

export GCC_COLORS=
export VERBOSE=1
%cmake_build %{?_smp_mflags}

%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}/civetweb

%files
%{_bindir}/civetweb
%{_libdir}/libcivetweb.so.*
%{_libdir}/libcivetweb-cpp.so.*
%license LICENSE.md
%doc README.md RELEASE_NOTES.md SECURITY.md

%files devel
%{_includedir}/*.h
%{_libdir}/libcivetweb.so
%{_libdir}/libcivetweb-cpp.so
%{_libdir}/cmake/civetweb/*
%{_datadir}/pkgconfig/*

%changelog
%autochangelog
