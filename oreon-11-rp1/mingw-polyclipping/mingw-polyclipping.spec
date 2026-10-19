%global source0_hash a14320d82194807c4480ce59c98aa71cd4175a5156645c4e2b3edd330b930627
%{?mingw_package_header}
%global mingw_pkg_name polyclipping
Name:           mingw-%{mingw_pkg_name}
Version:        6.4.2
Release:        1%{?dist}
Summary:        MinGW Windows Polygon clipping library
License:        BSL-1.0
URL:            http://sourceforge.net/projects/polyclipping
Source0:        http://downloads.sourceforge.net/%{mingw_pkg_name}/clipper_ver%{version}.zip
Patch0:         polyclipping.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
This package contains the MinGW windows port of the clipper polygon
clipping library.

This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:                MinGW Windows Polygon clipping library for the win32 target
%description -n mingw32-%{mingw_pkg_name}
This package contains the MinGW win32 port of the clipper polygon
clipping library.

This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:                MinGW Windows Polygon clipping library for the win64 target
%description -n mingw64-%{mingw_pkg_name}
This package contains the MinGW win64 port of the clipper polygon
clipping library.

This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

# Delete binaries
find . \( -name "*.exe" -o -name "*.dll" \) -delete

# Correct line ends and encodings
find . -type f -exec dos2unix -k {} \;

for filename in perl/perl_readme.txt README; do
  iconv -f iso8859-1 -t utf-8 "${filename}" > "${filename}".conv && \
    touch -r "${filename}" "${filename}".conv && \
    mv "${filename}".conv "${filename}"
done

%patch -P0 -p0 -b .mingw

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
pushd cpp
  %mingw_cmake
  %mingw_make %{?_smp_mflags}
popd
%install
pushd cpp
  %mingw_make install DESTDIR=%{buildroot}
%if 0%{?mingw_build_win32} == 1
  install -d %{buildroot}/%{mingw32_libdir}
  install build_win32$MINGW_BUILDDIR_SUFFIX/libpolyclipping.dll.a %{buildroot}/%{mingw32_libdir}
%endif
%if 0%{?mingw_build_win64} == 1
  install -d %{buildroot}/%{mingw64_libdir}
  install build_win64$MINGW_BUILDDIR_SUFFIX/libpolyclipping.dll.a %{buildroot}/%{mingw64_libdir}
%endif
popd
install -d %{buildroot}/%{mingw32_libdir}/pkgconfig
install -d %{buildroot}/%{mingw64_libdir}/pkgconfig
mv %{buildroot}/%{mingw32_datadir}/pkgconfig/polyclipping.pc %{buildroot}/%{mingw32_libdir}/pkgconfig
mv %{buildroot}/%{mingw64_datadir}/pkgconfig/polyclipping.pc %{buildroot}/%{mingw64_libdir}/pkgconfig
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-polyclipping -f %{oreon_filedir}/mingw32-polyclipping.list
%files -n mingw64-polyclipping -f %{oreon_filedir}/mingw64-polyclipping.list

%changelog

%autochangelog
