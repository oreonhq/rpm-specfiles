%global source0_hash 3d9409f22f07d875a54e30b8f495734f734a835d163b360dc856569bc5485ad5
Name:           libmodelfile
Version:        0.1.92
Release:        1%{?dist}
Summary:        Library for accessing various model file formats
License:        Zlib
URL:            http://www.worldforge.org
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.gz
Patch0:         libmodelfile-configure-c99.patch
# oreon:deps
BuildRequires:  SDL_image-devel
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  make
# /oreon:deps
%description
This library is a collection of small clean C libraries for loading 3D
models of various file formats. So far the range of model formats is limited.

%package        devel
Summary:        Development files for libmodelfile
Requires:       pkgconfig %{name} = %{version}-%{release}
%description    devel
This package contains libraries and header files for developing applications
that use libmodelfile.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make %{?_smp_mflags} check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libmodelfile-devel -f %{oreon_filedir}/libmodelfile-devel.list

%changelog

%autochangelog
