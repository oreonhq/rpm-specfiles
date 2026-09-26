%global source0_hash 6949dcde27d41cebad1fd741fcafc36d55a1020d2d872d4a6eb3914caabbada2

%{?mingw_package_header}

%global pkgname fribidi

Name:          mingw-%{pkgname}
Version:       1.0.17
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       LGPL-2.0-or-later
BuildArch:     noarch
URL:           https://github.com/%{pkgname}/%{pkgname}
Source0:       https://github.com/%{pkgname}/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.xz

# Drop bundled gnulib
Patch0:        fribidi-drop-bundled-gnulib.patch

BuildRequires: meson
BuildRequires: gcc

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc

%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
%mingw_meson --default-library=both -Ddocs=false
%mingw_ninja

%install
%mingw_ninja_install

%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/fribidi.exe
%{mingw32_prefix}/share/man/man1/fribidi.1*
%{mingw32_bindir}/libfribidi-0.dll
%{mingw32_includedir}/fribidi
%{mingw32_libdir}/libfribidi.dll.a
%{mingw32_libdir}/pkgconfig/fribidi.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libfribidi.a

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/fribidi.exe
%{mingw64_prefix}/share/man/man1/fribidi.1*
%{mingw64_bindir}/libfribidi-0.dll
%{mingw64_includedir}/fribidi
%{mingw64_libdir}/libfribidi.dll.a
%{mingw64_libdir}/pkgconfig/fribidi.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libfribidi.a

%changelog
%autochangelog
