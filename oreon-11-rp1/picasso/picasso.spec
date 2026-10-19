%global source0_hash f17db7e14cbb536e6014af3c088c9d71c6a820adac6c54a1f2e7cc334228eb88
Name:           picasso
Version:        2.8.0
Release:        1%{?dist}
Summary:        2D vector graphic rendering library
License:        BSD-3-Clause and LGPL-2.1-or-later
URL:            http://onecoolx.github.io/picasso/
Source0:        picasso-%{version}-clean.tar.gz
Patch:          consistenttypes.patch
Patch:          buildflags.patch
Patch:          getarg.patch
Patch:          installdirs.patch
Requires:       open-sans-fonts
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  gtk2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libwebp-devel
BuildRequires:  zlib-ng-compat-devel
# /oreon:deps
%description
Picasso is a high quality vector graphic rendering library. It has high
performance and low footprint. Picasso provides a set of high level 2D
graphics API, which can be used to a GUI system, rendering postscript,
rendering svg images and so on. It support path, matrix, gradient, pattern,
image and truetype font.

%package devel
Summary: Development headers and libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers and libraries for picasso.

%package demos
Summary: Demonstration programs
Requires: %{name}%{?_isa} = %{version}-%{release}
%description demos
Demonstration programs for picasso.

%package doc
Summary: Documentation in html format
BuildArch:  noarch
%description doc
Documentation for Picasso in html format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n picasso-%{version} -p1
# Replace font with unknown license with one packaged in Fedora
# https://github.com/onecoolx/picasso/issues/14
sed -i 's|sunglobe.ttf|%{_datadir}/fonts/open-sans/OpenSans-Regular.ttf|g' cfg/font_config.cfg
# remove bundled libraries that are not used
rm -r third_party/giflib-5.1.3
rm -r third_party/libpng-1.6.17
rm -r third_party/libwebp-0.5.1
rm -r third_party/libjpeg-turbo-1.4.1
rm -r third_party/zlib-1.2.8
rm -r android

%build

%cmake -DOPT_FAST_COPY="ON"       \
       -DOPT_FONT_CONFIG="ON"     \
       -DOPT_FORMAT_ABGR="ON"     \
       -DOPT_FORMAT_ARGB="ON"     \
       -DOPT_FORMAT_BGR="ON"      \
       -DOPT_FORMAT_BGRA="ON"     \
       -DOPT_FORMAT_RGB="ON"      \
       -DOPT_FORMAT_RGB555="ON"   \
       -DOPT_FORMAT_RGB565="ON"   \
       -DOPT_FORMAT_RGBA="ON"     \
       -DOPT_FREE_TYPE2="ON"      \
       -DOPT_LOW_MEMORY="OFF"     \
       -DOPT_SYSTEM_MALLOC="ON"   \
       -DOPT_SYSTEM_GIF="ON"      \
       -DOPT_SYSTEM_JPEG="ON"     \
       -DOPT_SYSTEM_PNG="ON"      \
       -DOPT_SYSTEM_WEBP="ON"     \
       -DOPT_SYSTEM_ZLIB="ON"     \
       -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_LIBDIR=%{_libdir}  \
       -DCMAKE_SKIP_RPATH=YES
%cmake_build 
doxygen
%install
%cmake_install
mkdir -p %{buildroot}/%{_bindir}
install -pm755 %{__cmake_builddir}/clock %{buildroot}%{_bindir}/picasso-clock
install -pm755 %{__cmake_builddir}/flowers %{buildroot}%{_bindir}/picasso-flowers
install -pm755 %{__cmake_builddir}/subwaymap %{buildroot}%{_bindir}/picasso-subwaymap
install -pm755 %{__cmake_builddir}/tiger %{buildroot}%{_bindir}/picasso-tiger
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n picasso-devel -f %{oreon_filedir}/picasso-devel.list
%files -n picasso-demos -f %{oreon_filedir}/picasso-demos.list
%files -n picasso-doc -f %{oreon_filedir}/picasso-doc.list

%changelog

%autochangelog
