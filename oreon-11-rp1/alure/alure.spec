%global source0_hash 465e6adae68927be3a023903764662d64404e40c4c152d160e3a8838b1d70f71
Name:           alure
Version:        1.2
Release:        1%{?dist}
Summary:        Audio Library Tools REloaded
License:        LGPL-2.1-or-later
URL:            http://kcat.strangesoft.net/alure.html
Source0:        https://src.fedoraproject.org/repo/pkgs/alure/alure-1.2.tar.bz2/3088aba074ad02d95ea51e705053b9f5/alure-1.2.tar.bz2
Patch0:         alure-gcc47.patch
Patch1:         alure-1.2-fluidsynth-cflags-fix.patch
Patch2:		alure-1.2-use-unique_ptr.patch
Patch3:		alure-1.2-sndfile-cflags-fix.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dumb-devel
BuildRequires:  flac-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
# /oreon:deps
%description
ALURE is a utility library to help manage common tasks with OpenAL
applications. This includes device enumeration and initialization,
file loading, and streaming.

%package        devel
Summary:        Development files for %{name}
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
rm -rf %{buildroot}%{_docdir}/alure/html
%ldconfig_scriptlets
%oreon_autofiles alure-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n alure-devel -f %{oreon_filedir}/alure-devel.list

%changelog

%autochangelog
