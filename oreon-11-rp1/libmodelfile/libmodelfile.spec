%global source0_hash 3d9409f22f07d875a54e30b8f495734f734a835d163b360dc856569bc5485ad5

Name:           libmodelfile
Version:        0.1.92
Release:        41%{?dist}
Summary:        Library for accessing various model file formats

License:        Zlib
URL:            http://www.worldforge.org
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.gz
Patch0:         libmodelfile-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  SDL_image-devel libGL-devel libGLU-devel
BuildRequires: make

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

%autosetup -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make %{?_smp_mflags} check

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}-0.2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
