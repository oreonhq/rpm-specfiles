%global source0_hash d09c44ebc3bd5bee7021c79f922fe8fb2fb57f7320f55e97ff9914d2346a591c

%{?mingw_package_header}

Name:           mingw-pixman
Version:        0.46.4
Release:        2%{?dist}
Summary:        MinGW Windows Pixman library

License:        MIT
URL:            http://cgit.freedesktop.org/pixman/

Source0:        http://cairographics.org/releases/pixman-0.46.4.tar.gz
Source1:        make-pixman-snapshot.sh

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libgomp

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-libgomp

BuildRequires:  gcc
BuildRequires:  meson


%description
MinGW Windows Pixman library.


# Win32
%package -n mingw32-pixman
Summary:        MinGW Windows Pixman library

%description -n mingw32-pixman
MinGW Windows Pixman library.


%package -n mingw32-pixman-static
Summary:        Static version of the MinGW Windows Pixman library
Requires:       mingw32-pixman = %{version}-%{release}

%description -n mingw32-pixman-static
Static version of the MinGW Windows Pixman library.

# Win64
%package -n mingw64-pixman
Summary:        MinGW Windows Pixman library

%description -n mingw64-pixman
MinGW Windows Pixman library.

%package -n mingw64-pixman-static
Summary:        Static version of the cross compiled Pixman library
Requires:       mingw64-pixman = %{version}-%{release}

%description -n mingw64-pixman-static
Static version of the cross compiled Pixman library.


%{?mingw_debug_package}


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n pixman-%{version}


%build
# Uses GTK for its testsuite, so disable this otherwise we have a chicken & egg problem on mingw
%mingw_meson --default-library=both -Dgtk=disabled
%mingw_ninja


%install
%mingw_ninja_install


# Win32
%files -n mingw32-pixman
%license COPYING
%{mingw32_bindir}/libpixman-1-0.dll
%{mingw32_includedir}/pixman-1
%{mingw32_libdir}/libpixman-1.dll.a
%{mingw32_libdir}/pkgconfig/pixman-1.pc

%files -n mingw32-pixman-static
%{mingw32_libdir}/libpixman-1.a

# Win64
%files -n mingw64-pixman
%license COPYING
%{mingw64_bindir}/libpixman-1-0.dll
%{mingw64_includedir}/pixman-1
%{mingw64_libdir}/libpixman-1.dll.a
%{mingw64_libdir}/pkgconfig/pixman-1.pc

%files -n mingw64-pixman-static
%{mingw64_libdir}/libpixman-1.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.46.4-2
- Prepare for Oreon 11 (RP1)
