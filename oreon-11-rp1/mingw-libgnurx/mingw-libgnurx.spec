%global source0_hash 7147b7f806ec3d007843b38e19f42a5b7c65894a57ffc297a76b0dcd5f675d76

%?mingw_package_header

Name:           mingw-libgnurx
Version:        2.5.1
Release:        40%{?dist}
Summary:        MinGW Regex library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://mingw.sourceforge.net/
Source0:        http://kent.dl.sourceforge.net/sourceforge/mingw/mingw-libgnurx-%{version}-src.tar.gz
Source1:        mingw32-libgnurx-configure.ac
Source2:        mingw32-libgnurx-Makefile.am
Patch0:         mingw32-libgnurx-honor-destdir.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  autoconf automake libtool

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

%description
MinGW Windows regular expression library.

# Win32
%package -n mingw32-libgnurx
Summary:        MinGW Regex library

%description -n mingw32-libgnurx
MinGW Windows regular expression library.

%package -n mingw32-libgnurx-static
Summary:        Static version of the MinGW Windows regular expression library
Requires:       mingw32-libgnurx = %{version}-%{release}

%description -n mingw32-libgnurx-static
Static version of the MinGW Windows regular expression library.

# Win64
%package -n mingw64-libgnurx
Summary:        MinGW Regex library

%description -n mingw64-libgnurx
MinGW Windows regular expression library.

%package -n mingw64-libgnurx-static
Summary:        Static version of the MinGW Windows regular expression library
Requires:       mingw64-libgnurx = %{version}-%{release}

%description -n mingw64-libgnurx-static
Static version of the MinGW Windows regular expression library.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mingw-libgnurx-%{version}
%patch -P0 -p0

# The Makefile which is delivered with this package can't create static
# libraries and misnames the resulting import libraries
# So replace the buildsystem by a more proper one
cp %{SOURCE1} configure.ac
cp %{SOURCE2} Makefile.am
touch NEWS
touch AUTHORS
libtoolize --copy
aclocal
autoconf
automake --add-missing

%build
# The upstream code hasn't been updated in 18 years and uses some
# old-style C assumptions, in particular assuming that 'false' and
# 'true' are not keywords.  Hence use C99:
%global mingw32_cppflags -std=c99
%global mingw64_cppflags -std=c99
%mingw_configure --enable-static --enable-shared
%mingw_make %{?_smp_mflags}

%install
# make install expects %{mingw32_includedir} to exist
mkdir -p $RPM_BUILD_ROOT%{mingw32_includedir} $RPM_BUILD_ROOT%{mingw64_includedir}

%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# make install installs two import libraries named libgnurx.a and
# libgnurx.dll.a. As most applications requiring regex functions
# try to perform 'gcc -lregex' we rename the import libraries for this to work
mv $RPM_BUILD_ROOT%{mingw32_libdir}/libgnurx.a $RPM_BUILD_ROOT%{mingw32_libdir}/libregex.a
mv $RPM_BUILD_ROOT%{mingw64_libdir}/libgnurx.a $RPM_BUILD_ROOT%{mingw64_libdir}/libregex.a
mv $RPM_BUILD_ROOT%{mingw32_libdir}/libgnurx.dll.a $RPM_BUILD_ROOT%{mingw32_libdir}/libregex.dll.a
mv $RPM_BUILD_ROOT%{mingw64_libdir}/libgnurx.dll.a $RPM_BUILD_ROOT%{mingw64_libdir}/libregex.dll.a

# Drop the man pages
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Win32
%files -n mingw32-libgnurx
%doc COPYING.LIB
%{mingw32_bindir}/libgnurx-0.dll
%{mingw32_includedir}/regex.h
%{mingw32_libdir}/libregex.dll.a

%files -n mingw32-libgnurx-static
%{mingw32_libdir}/libregex.a

# Win64
%files -n mingw64-libgnurx
%doc COPYING.LIB
%{mingw64_bindir}/libgnurx-0.dll
%{mingw64_includedir}/regex.h
%{mingw64_libdir}/libregex.dll.a

%files -n mingw64-libgnurx-static
%{mingw64_libdir}/libregex.a

%changelog
%autochangelog
