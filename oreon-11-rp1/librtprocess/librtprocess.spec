%global source0_hash ed6862b1491559e71dbebe8cbb299008fb16e230acf3bb9d42bd52942644c4d9

Name:           librtprocess
Version:        0.12.0
Release:        16%{?dist}
Summary:        RawTherapee's processing algorithms

# The entire source is GPL-3.0-or-later, except:
# - BSL-1.0: src/include/helpersse2.h
#            src/include/sleef.h
#            src/include/sleefsseavx.h
License:        GPL-3.0-or-later AND BSL-1.0
URL:            https://github.com/CarVac/librtprocess
Source:         %{url}/archive/%{version}/librtprocess-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
This is a project that aims to make some of RawTherapee's highly optimized
raw processing routines readily available for other FOSS photo editing
software.

The goal is to move certain source files from RawTherapee into this library.
Thus, any changes to the source can be done here and will be used by the
projects which use librtprocess.

%package devel
Summary:        Libraries, includes, etc. used to develop an application with librtprocess
# Does not include anything derived from the BSL-1.0-licensed headers.
License:        GPL-3.0-or-later
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
These are the files needed to develop an application using librtprocess.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/librtprocess.so.0
%{_libdir}/librtprocess.so.0.0.1

%files devel
%{_includedir}/rtprocess/
%{_libdir}/librtprocess.so
%{_libdir}/pkgconfig/rtprocess.pc
%{_libdir}/cmake/rtprocess/

%changelog
%autochangelog
