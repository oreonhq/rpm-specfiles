%global source0_hash 1703a8ac4c4f3469e0d4d7b7e7ebff8d6206e73ec97d2669227a1280202e1396
ExcludeArch:    %{ix86}
Name:           libXISF
Version:        0.2.13
Release:        1%{?dist}
Summary:        Library to load and write XISF format
License:        GPL-3.0-or-later
URL:            https://gitea.nouspiro.space/nou/libXISF
Source0:        https://gitea.nouspiro.space/nou/%{name}/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
LibXISF is C++ library to load and save images in XISF format that
is native format PixInsight astronomical image processing program.
It implements XISF 1.0 specifications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libxisf

# remove bundled libraries
for d in "lz4" "pugixml" "zlib"
do
  rm -rf $d
done

%build

%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DUSE_BUNDLED_LIBS=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libXISF-devel -f %{oreon_filedir}/libXISF-devel.list

%changelog

%autochangelog
