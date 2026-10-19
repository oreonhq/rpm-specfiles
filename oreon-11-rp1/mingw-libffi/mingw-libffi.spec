%global source0_hash f3a3082a23b37c293a4fcd1053147b371f2ff91fa7ea1b2a52e335676bac82dc
%{?mingw_package_header}
Name:		mingw-libffi
Version:	3.5.2
Release:        2%{?dist}
Summary:        A portable foreign function interface library for MinGW
License:	MIT
URL:		http://sourceware.org/libffi
Source0:        https://github.com/libffi/libffi/releases/download/v%{version}/libffi-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
Foreign function interface library for MinGW.

# Win32
%package -n mingw32-libffi
Summary:	A portable foreign function interface library for MinGW
%description -n mingw32-libffi
Foreign function interface library for MinGW.

# Win32 static
%package -n mingw32-libffi-static
Summary:       A portable foreign function interface static library for MinGW
%description -n mingw32-libffi-static
Foreign function interface static library for MinGW.

# Win64
%package -n mingw64-libffi
Summary:	A portable foreign function interface library for MinGW
%description -n mingw64-libffi
Foreign function interface library for MinGW.

# Win64 static
%package -n mingw64-libffi-static
Summary:       A portable foreign function interface static library for MinGW
%description -n mingw64-libffi-static
Foreign function interface static library for MinGW.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libffi-%{version}
%oreon_prep
%build

%mingw_configure --enable-shared
%mingw_make
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_infodir}
rm -rf %{buildroot}%{mingw64_infodir}
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
find %{buildroot} -name "*.la" -delete
%oreon_autofiles mingw32-libffi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libffi-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libffi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libffi-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libffi -f %{oreon_filedir}/mingw32-libffi.list
%files -n mingw32-libffi-static -f %{oreon_filedir}/mingw32-libffi-static.list
%files -n mingw64-libffi -f %{oreon_filedir}/mingw64-libffi.list
%files -n mingw64-libffi-static -f %{oreon_filedir}/mingw64-libffi-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.5.2-2
- Prepare for Oreon 11 (RP1)
