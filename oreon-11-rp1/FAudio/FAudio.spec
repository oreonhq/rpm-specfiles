%global source0_hash b393b2f90b21e9160fedfd3d0da88c6c449df38c17699790b1df1abbf5751792
Name:     FAudio
Version:  26.09
Release:        1%{?dist}
Summary:        FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries
License:  zlib
URL:      https://fna-xna.github.io/
Source0:        https://github.com/FNA-XNA/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  SDL3-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mingw32-SDL3
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-SDL3
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%package -n libFAudio
Summary:        FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries
%description -n libFAudio
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%package -n libFAudio-devel
Summary:  Development files for the FAudio library
Requires: libFAudio%{?_isa} = %{version}-%{release}
%description -n libFAudio-devel
Development files for the FAudio library.

%package -n mingw32-%{name}
Summary:        FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries
BuildArch:      noarch
%description -n mingw32-%{name}
%{summary}.

%package -n mingw64-%{name}
Summary:        FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries
BuildArch:      noarch
%description -n mingw64-%{name}
%{summary}.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
mkdir ../mingw-build
cp -rp . ../mingw-build

%build

%cmake
%cmake_build
pushd ../mingw-build
%mingw_cmake
%mingw_make %{?_smp_mflags}
popd
%install
%cmake_install
pushd ../mingw-build
%mingw_make_install
%mingw_debug_install_post
popd
%oreon_autofiles libFAudio usr/*/lib*.so.*
%oreon_autofiles libFAudio-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles mingw32-FAudio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-FAudio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libFAudio -f %{oreon_filedir}/libFAudio.list
%files -n libFAudio-devel -f %{oreon_filedir}/libFAudio-devel.list
%files -n mingw32-FAudio -f %{oreon_filedir}/mingw32-FAudio.list
%files -n mingw64-FAudio -f %{oreon_filedir}/mingw64-FAudio.list

%changelog

%autochangelog
