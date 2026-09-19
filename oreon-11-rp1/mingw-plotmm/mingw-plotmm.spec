%global source0_hash 896bb729eb9cad5f3188d72304789dd7a86fdae66020ac0632fe3bc66abe9653

%?mingw_package_header

Name:           mingw-plotmm
Version:        0.1.2
Release:        45%{?dist}
Summary:        MinGW GTKmm plot widget for scientific applications
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://plotmm.sourceforge.net/
Source0:        http://download.sourceforge.net/plotmm/plotmm-%{version}.tar.gz
# Fix code to build against libsigc++20
# Upstream:
# https://sourceforge.net/tracker/?func=detail&atid=632478&aid=2082337&group_id=102665
Patch0:         plotmm-0.1.2-libsigc++20.patch
Patch1:         mingw32-plotmm-ac.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 68
BuildRequires:  mingw64-filesystem >= 68
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gtkmm24 >= 2.4.0
BuildRequires:  mingw64-gtkmm24 >= 2.4.0
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf

%description
This package provides an extension to the mingw32 gtkmm library.  It
contains widgets which are primarily useful for technical and
scientifical purposes.  Initially, this is a 2-D plotting widget.

# Win32
%package -n mingw32-plotmm
Summary:        MinGW GTKmm plot widget for scientific applications for the win32 target
Requires:       pkgconfig

%description -n mingw32-plotmm
This package provides an extension to the mingw32 gtkmm library.  It
contains widgets which are primarily useful for technical and
scientifical purposes.  Initially, this is a 2-D plotting widget.

%package -n mingw32-plotmm-static
Summary:        Static version of the MinGW Windows PlotMM library
Requires:       mingw32-plotmm = %{version}-%{release}

%description -n mingw32-plotmm-static
Static version of the MinGW Windows PlotMM library.

# Win64
%package -n mingw64-plotmm
Summary:        MinGW GTKmm plot widget for scientific applications for the win64 target
Requires:       pkgconfig

%description -n mingw64-plotmm
This package provides an extension to the mingw64 gtkmm library.  It
contains widgets which are primarily useful for technical and
scientifical purposes.  Initially, this is a 2-D plotting widget.

%package -n mingw64-plotmm-static
Summary:        Static version of the MinGW Windows PlotMM library
Requires:       mingw64-plotmm = %{version}-%{release}

%description -n mingw64-plotmm-static
Static version of the MinGW Windows PlotMM library.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n plotmm-%{version}
%patch -P0 -p1 -b .libsigc++20
%patch -P1 -p0 -b .mingw
# update autotools, distributed files are so old they do not
# get compiling dlls right
libtoolize --force --copy
aclocal
autoconf
automake -a -c

%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -std=gnu++11"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -std=gnu++11"
%mingw_configure
%mingw_make

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{mingw32_bindir}/curves.exe
rm $RPM_BUILD_ROOT%{mingw64_bindir}/curves.exe
rm $RPM_BUILD_ROOT%{mingw32_bindir}/simple.exe
rm $RPM_BUILD_ROOT%{mingw64_bindir}/simple.exe

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-plotmm
%doc AUTHORS COPYING ChangeLog README
%{mingw32_bindir}/libplotmm-0.dll
%{mingw32_libdir}/libplotmm.dll.a
%{mingw32_libdir}/pkgconfig/plotmm.pc
%{mingw32_includedir}/plotmm

%files -n mingw32-plotmm-static
%{mingw32_libdir}/libplotmm.a

%files -n mingw64-plotmm
%doc AUTHORS COPYING ChangeLog README
%{mingw64_bindir}/libplotmm-0.dll
%{mingw64_libdir}/libplotmm.dll.a
%{mingw64_libdir}/pkgconfig/plotmm.pc
%{mingw64_includedir}/plotmm

%files -n mingw64-plotmm-static
%{mingw64_libdir}/libplotmm.a

%changelog
%autochangelog
