%global source0_hash 9f6cc50182be4d2ece75118aa0b0fd3e9bbad06e94fd6b9eb3a4c08129c2dd26

%{?mingw_package_header}

%global pkgname libimagequant

# does not support out-of-tree builds
%global w64_dir %{_builddir}/mingw64-%{pkgname}-%{version}-%{release}

Name:           mingw-%{pkgname}
Version:        2.17.0
Release:        13%{?dist}
Summary:        MinGW Windows %{pkgname} library

BuildArch:      noarch
# Automatically converted from old format: GPLv3+ and MIT - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL:            https://github.com/ImageOptim/libimagequant
Source0:        %{url}/archive/%{version}/%{pkgname}-%{version}.tar.gz

# MinGW build fixes
Patch0:         libimagequant_mingw.patch

BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libgomp

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libgomp


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{pkgname}-%{version}

cp -a . %{w64_dir}


%build
%mingw32_configure --with-openmp
%mingw32_make dll %{?_smp_mflags}

(
cd %{w64_dir}
%mingw64_configure --with-openmp
%mingw64_make dll %{?_smp_mflags}
)


%install
install -Dpm 0755 %{pkgname}.dll %{buildroot}%{mingw32_bindir}/%{pkgname}.dll
install -Dpm 0755 %{pkgname}.dll.a %{buildroot}%{mingw32_libdir}/%{pkgname}.dll.a
install -Dpm 0644 %{pkgname}.h %{buildroot}%{mingw32_includedir}/%{pkgname}.h

(
cd %{w64_dir}
install -Dpm 0755 %{pkgname}.dll %{buildroot}%{mingw64_bindir}/%{pkgname}.dll
install -Dpm 0755 %{pkgname}.dll.a %{buildroot}%{mingw64_libdir}/%{pkgname}.dll.a
install -Dpm 0644 %{pkgname}.h %{buildroot}%{mingw64_includedir}/%{pkgname}.h
)


%files -n mingw32-%{pkgname}
%license COPYRIGHT
%{mingw32_bindir}/%{pkgname}.dll
%{mingw32_libdir}/%{pkgname}.dll.a
%{mingw32_includedir}/%{pkgname}.h

%files -n mingw64-%{pkgname}
%license COPYRIGHT
%{mingw64_bindir}/%{pkgname}.dll
%{mingw64_libdir}/%{pkgname}.dll.a
%{mingw64_includedir}/%{pkgname}.h

%changelog
%autochangelog
