%global source0_hash f99d1c13aa5fa296898a181dff9b82fb25f6cc0933dbaa7a475d8109bd54209d

%{?mingw_package_header}

%global pkgname graphite2

Name:          mingw-%{pkgname}
Version:       1.3.14
Release:       17%{?dist}
Summary:       MinGW Windows %{pkgname} library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           https://github.com/silnrsi/graphite
Source0:       https://github.com/silnrsi/graphite/releases/download/%{version}/%{pkgname}-%{version}.tgz

# https://github.com/Alexpux/MINGW-packages/blob/master/mingw-w64-graphite2/001-graphite2-1.3.8-win64.patch
Patch0:        mingw-graphite2_win64.patch
# https://github.com/Alexpux/MINGW-packages/blob/master/mingw-w64-graphite2/002-graphite2-1.2.1-pkgconfig.patch
Patch1:        mingw-graphite2_pkgconfig.patch
# https://github.com/Alexpux/MINGW-packages/blob/master/mingw-w64-graphite2/003-graphite2-1.3.9-staticbuild.patch
Patch2:        mingw-graphite2_staticbuild.patch
# https://github.com/Alexpux/MINGW-packages/blob/master/mingw-w64-graphite2/004-graphite2-1.3.8-dllimport-fix.patch
Patch3:        mingw-graphite2_dllimport-fix.patch
# Drop use of LIB_SUFFIX
Patch4:        graphite2_cmakelibsuffix.patch
# Increase minimum cmake version
Patch5:        graphite2_cmakever.patch
# Fix build with gcc15
Patch6:        graphite2_gcc15.patch

BuildArch:     noarch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-freetype

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-freetype

%description
Graphite2 is a project within SIL’s Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create “smart fonts” capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.

# Win32
%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.

# Win64
%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
%mingw_cmake -DGRAPHITE2_COMPARE_RENDERER=OFF
%mingw_make_build

%install
%mingw_make_install

rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}

# Win32
%files -n mingw32-%{pkgname}
%license LICENSE COPYING
%{mingw32_bindir}/gr2fonttest.exe
%{mingw32_bindir}/lib%{pkgname}.dll
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_libdir}/pkgconfig/%{pkgname}.pc
%{mingw32_includedir}/%{pkgname}/

%files -n mingw32-%{pkgname}-static
%license LICENSE COPYING
%{mingw32_libdir}/lib%{pkgname}.a

# Win64
%files -n mingw64-%{pkgname}
%license LICENSE COPYING
%{mingw64_bindir}/gr2fonttest.exe
%{mingw64_bindir}/lib%{pkgname}.dll
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_libdir}/pkgconfig/%{pkgname}.pc
%{mingw64_includedir}/%{pkgname}/

%files -n mingw64-%{pkgname}-static
%license LICENSE COPYING
%{mingw64_libdir}/lib%{pkgname}.a

%changelog
%autochangelog
