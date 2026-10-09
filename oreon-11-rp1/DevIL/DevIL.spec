%global source0_hash 0075973ee7dd89f0507873e2580ac78336452d29d34a07134b208f44e2feb709

Name:           DevIL
Version:        1.8.0
Release:        %autorelease
Summary:        A cross-platform image library
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://openil.sourceforge.net/
Source0:        https://downloads.sourceforge.net/openil/%{name}-%{version}.tar.gz
# Add solib version numbers to the CMake build (https://github.com/DentonW/DevIL/pull/50)
Patch0:         DevIL-1.8.0-soversion.patch
# Jasper >= 2.0.20 callback API (upstream 42a62648e727e9a0217280474546de3ac69cbff1)
Patch1:         DevIL-1.8.0-jasper.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  lcms2-devel
BuildRequires:  allegro-devel
BuildRequires:  libGLU-devel
BuildRequires:  libICE-devel
BuildRequires:  libXext-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  jasper-devel
BuildRequires:  SDL-devel => 1.2.5
BuildRequires: make

%description
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy for a
developer to learn and use. Ultimate control of images is left to the
developer, so unnecessary conversions, etc. are not performed. DevIL utilizes
a simple, yet powerful, syntax. DevIL can load, save, convert, manipulate,
filter and display a wide variety of image formats.


%package devel
Summary:        Development files for DevIL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for DevIL


%package ILUT
Summary:        The libILUT component of DevIL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description ILUT
The libILUT component of DevIL


%package ILUT-devel
Summary:        Development files for the libILUT component of DevIL
Requires:       %{name}-ILUT%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       allegro-devel libGLU-devel

%description ILUT-devel
Development files for the libILUT component of DevIL


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n DevIL
cd DevIL
iconv -f iso8859-1 CREDITS -t utf8 > CREDITS.conv
touch -r CREDITS CREDITS.conv
mv CREDITS.conv CREDITS
# install into the multilib-correct libdir instead of a hardcoded "lib"
sed -i 's|DESTINATION lib/pkgconfig|DESTINATION ${CMAKE_INSTALL_LIBDIR}/pkgconfig|; s|DESTINATION lib$|DESTINATION ${CMAKE_INSTALL_LIBDIR}|' \
    src-IL/CMakeLists.txt src-ILU/CMakeLists.txt src-ILUT/CMakeLists.txt


%build
cd DevIL
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build


%install
cd DevIL
%cmake_install


%ldconfig_scriptlets
%ldconfig_scriptlets ILUT


%files
%{_libdir}/libIL.so.*
%{_libdir}/libILU.so.*
%license DevIL/COPYING
%doc DevIL/AUTHORS DevIL/ChangeLog DevIL/CREDITS DevIL/README.md DevIL/TODO

%files devel
%{_libdir}/libIL.so.*
%{_libdir}/libILU.so.*
%{_libdir}/pkgconfig/IL.pc
%{_libdir}/pkgconfig/ILU.pc
%dir %{_includedir}/IL
%{_includedir}/IL/il.h
%{_includedir}/IL/ilu.h

%files ILUT
%{_libdir}/libILUT.so.1

%files ILUT-devel
%{_libdir}/libILUT.so
%{_libdir}/pkgconfig/ILUT.pc
%{_includedir}/IL/ilut.h


%changelog
%autochangelog

