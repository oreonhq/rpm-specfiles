%global source0_hash 465e6adae68927be3a023903764662d64404e40c4c152d160e3a8838b1d70f71

Name:           alure
Version:        1.2
Release:        37%{?dist}
Summary:        Audio Library Tools REloaded
# ALURE code is LGPLv2+; note -devel subpackage has its own license tag
License:        LGPL-2.1-or-later
URL:            http://kcat.strangesoft.net/alure.html
Source0:        http://kcat.strangesoft.net/%{name}-releases/%{name}-%{version}.tar.bz2
Patch0:         alure-gcc47.patch
Patch1:         alure-1.2-fluidsynth-cflags-fix.patch
Patch2:		alure-1.2-use-unique_ptr.patch
Patch3:		alure-1.2-sndfile-cflags-fix.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake, libvorbis-devel, libsndfile-devel, openal-soft-devel, flac-devel, dumb-devel, fluidsynth-devel

%description
ALURE is a utility library to help manage common tasks with OpenAL
applications. This includes device enumeration and initialization,
file loading, and streaming.

%package        devel
Summary:        Development files for %{name}
# Devel doc includes some files under GPLv2+ from NaturalDocs
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0
%patch -P1 -p1 -b .fluidsynth-cflags-fix
%patch -P2 -p1 -b .unique_ptr
%patch -P3 -p1 -b .sndfile-cflags-fix

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
  %if "%{?_lib}" == "lib64"
    %{?_cmake_lib_suffix64} \
  %endif
  -DBUILD_STATIC:BOOL=OFF
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
# strip installed html doc
rm -rf %{buildroot}%{_docdir}/alure/html

%ldconfig_scriptlets

%files
%doc COPYING
%{_libdir}/*.so.*
%{_bindir}/alure*

%files devel
%doc docs/html examples
%{_includedir}/AL/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
