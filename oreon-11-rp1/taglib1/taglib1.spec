%global source0_hash c8da2b10f1bfec2cd7dbfcd33f4a2338db0765d851a50583d410bacf055cfd0b
%bcond devel 0
%bcond tests 1
%global common_description %{expand:
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3
files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC,
Speex, WavPack, TrueAudio files, as well as APE Tags.
This is a compatibility version for packages not yet rebuilt for taglib 2.}
Name:       taglib1
Summary:        Audio Meta-Data Library (compat version)
Version:    1.13.1
Release:        1%{?dist}
License:    (LGPL-2.1-only OR MPL-1.1) AND BSD-2-Clause AND LGPL-2.1-only
URL:        https://taglib.github.io/
Source0:        https://taglib.github.io/releases/taglib-%{version}.tar.gz
Patch0:     taglib-1.13.1-multilib.patch
%if %{with tests}
%endif
Conflicts:     taglib < 2.0
Provides:      bundled(utf8cpp)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{common_description}

%if %{with devel}
%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: taglib-devel >= 2.0
%description devel
Files needed when building software with %{name}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n taglib-%{version}%{?beta} -p1

%build

%{cmake} \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
%if %{with tests}
  -DBUILD_TESTS:BOOL=ON \
%endif
  -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build
%install
%cmake_install
%if %{without devel}
rm -f  %{buildroot}%{_bindir}/taglib-config
rm -fr %{buildroot}%{_includedir}/taglib/
rm -f  %{buildroot}%{_libdir}/libtag*.so
rm -f  %{buildroot}%{_libdir}/pkgconfig/*.pc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

%if %{with tests}
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n taglib1-devel -f %{oreon_filedir}/taglib1-devel.list

%changelog

%autochangelog
