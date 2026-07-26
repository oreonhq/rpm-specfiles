%global source0_hash fbddda9230cf6ee2a4f5706b4b11e2190ae45f5eda1f0409dc4f99b35e0a70ee

%global         rc_subver     rc5
%global         optflags      %{optflags} -std=gnu17

Summary:        ASCII art library
Name:           aalib
Version:        1.4.0
Release:        0.58.%{rc_subver}%{?dist}
License:        LGPL-2.1-or-later
URL:            http://aa-project.sourceforge.net/aalib/
Source0:        http://download.sourceforge.net/aa-project/%{name}-1.4%{rc_subver}.tar.gz
Patch0:         aalib-aclocal.patch
Patch1:         aalib-config-rpath.patch
Patch2:         aalib-1.4rc5-bug149361.patch
Patch3:         aalib-1.4rc5-rpath.patch
Patch4:         aalib-1.4rc5-x_libs.patch
Patch5:         aalib-1.4rc5-libflag.patch
Patch6:         aalib-c99.patch
Patch7:         https://gitweb.gentoo.org/repo/gentoo.git/plain/media-libs/aalib/files/aalib-1.4_rc5-free-offset-pointer.patch
Patch8:         https://gitweb.gentoo.org/repo/gentoo.git/plain/media-libs/aalib/files/aalib-1.4_rc5-fix-aarender.patch
# Modern ncurses has an opaque WINDOW structure (you cannot address its members directly)
# Use the getmaxx() and getmaxy() functions provided by ncurses instead.
Patch9:		aalib-1.4rc5-opaque-ncurses-fix.patch

BuildRequires:  autoconf
BuildRequires:  gpm-devel
BuildRequires:  libtool
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  slang-devel

%description
AA-lib is a low level gfx library just as many other libraries are. The
main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with a powerful ASCII art renderer. The API
is designed to be similar to other graphics libraries.

%package libs
Summary:        Library files for aalib
%description libs
This package contains library files for aalib.

%package devel
Summary:        Development files for aalib
Requires:       %{name}-libs = %{version}-%{release}

%description devel
This package contains header files and other files needed to develop
with aalib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p1 -b .bug149361
%patch -P3 -p1 -b .rpath
%patch -P4 -p1 -b .x_libs
%patch -P5 -p0 -b .libflag
%patch -P6 -p1
%patch -P7 -p1 -b .free-offset-pointer
%patch -P8 -p1 -b .fix-aarender
%patch -P9 -p1 -b .opaque-ncurses-fix
# included libtool is too old, we need to rebuild
autoreconf -v -f -i

%build
%configure --disable-static  --with-curses-driver=yes --with-ncurses

%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT{%{_libdir}/libaa.la,%{_infodir}/dir}

# clean up multilib conflicts
touch -r NEWS $RPM_BUILD_ROOT%{_bindir}/aalib-config $RPM_BUILD_ROOT%{_datadir}/aclocal/aalib.m4

%ldconfig_scriptlets libs

%files
%{_bindir}/aafire
%{_bindir}/aainfo
%{_bindir}/aasavefont
%{_bindir}/aatest
%{_mandir}/man1/aafire.1*

%files libs
%doc README ChangeLog NEWS
%license COPYING
%{_libdir}/libaa.so.1*

%files devel
%{_bindir}/aalib-config
%{_mandir}/man3/*
%{_libdir}/libaa.so
%{_includedir}/aalib.h
%{_infodir}/aalib.info*
%{_datadir}/aclocal/aalib.m4

%changelog
%autochangelog
