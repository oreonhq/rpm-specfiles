%global source0_hash c6bc8b4252724665297f7cad0c55897285c673f9b8e6db3522ace833593fe0b1
%{?mingw_package_header}
%global pkgname graphite2
Name:          mingw-%{pkgname}
Version:       1.3.15
Release:        1%{?dist}
Summary:        MinGW Windows graphite2 library
License:       LicenseRef-Callaway-LGPLv2+
URL:           https://github.com/silnrsi/graphite
Source0:        https://github.com/silnrsi/graphite/releases/download/%{version}/%{pkgname}-%{version}.tgz
Patch0:        mingw-graphite2_win64.patch
Patch1:        mingw-graphite2_pkgconfig.patch
Patch2:        mingw-graphite2_staticbuild.patch
Patch3:        mingw-graphite2_dllimport-fix.patch
BuildArch:     noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-graphite2 -f %{oreon_filedir}/mingw32-graphite2.list
%files -n mingw32-graphite2-static -f %{oreon_filedir}/mingw32-graphite2-static.list
%files -n mingw64-graphite2 -f %{oreon_filedir}/mingw64-graphite2.list
%files -n mingw64-graphite2-static -f %{oreon_filedir}/mingw64-graphite2-static.list

%changelog

%autochangelog
