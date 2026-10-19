%global source0_hash 4e83403309e155c707cb5d573981bff8030a71c9112d22a5ec7873d23aa22e8d
%define _legacy_common_support 1
Summary:        Clam Anti-Virus on the KDE Desktop
Name: klamav
Version: 0.46
Release:        49%{?dist}
Source0:        http://downloads.sourceforge.net/klamav/%{name}-%{version}.tar.bz2
Patch0: klamav-0.46-suse-clamav-path.patch
Patch1: klamav-0.41.1-pwd-echo.patch
Patch2: klamav-0.44-no-kde3-mediamanager.patch
Patch3: klamav-0.46-fix-docpath.patch
Patch4: klamav-0.46-gzip-api.patch
Patch5: klamav-0.46-clamav-0.101.patch
Patch6: klamav-clamav-1.0.patch
Patch7: klamav-configure-c99.patch
Patch8: klamav-c99.patch
URL: http://klamav.sourceforge.net
License: GPL-2.0-or-later
Requires: clamav >= 0.93
Requires: clamav-update >= 0.93
# oreon:deps
BuildRequires:  clamav-devel
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gmp-devel
BuildRequires:  kdelibs3-devel
BuildRequires:  make
BuildRequires:  perl(File::Find)
BuildRequires:  sqlite-devel
# /oreon:deps
%description
ClamAV Anti-Virus protection for the KDE desktop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .suse-clamav-path
%patch -P1 -p1 -b .pwd-echo
%patch -P2 -p1 -b .no-kde3-mediamanager
%patch -P3 -p1 -b .fix-docpath
%patch -P4 -p1 -b .gzip-api
%patch -P5 -p1 -b .clamav-0.101
%patch -P6 -p1 -b .clamav-1.0
%patch -P7 -p1 -b .c99
%patch -P8 -p1

# Avoid re-running autoconf.
touch -r aclocal.m4 acinclude.m4 configure*

# Remove staled files (#553807)
%{__rm} -f po/*.gmo

# Fix documentation module name (#553811)
find doc \
    -name 'Makefile.*' -o -name 'index.docbook' \
    -type f | xargs %{__sed} -i -e 's,klamav02,klamav,g'

%build

export CFLAGS="%{optflags} -Wno-error=incompatible-pointer-types"
%configure --disable-rpath --without-included-sqlite --with-disableupdates
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' libtool
%make_build
%install
%make_install
%{__sed} -i.orig -e '/^Terminal/s|^.*$|Terminal=false|' \
    ${RPM_BUILD_ROOT}%{_datadir}/applnk/Utilities/%{name}.desktop
%{__rm} -f ${RPM_BUILD_ROOT}%{_datadir}/applnk/Utilities/%{name}.desktop.orig
desktop-file-install \
    --delete-original \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications/ \
    ${RPM_BUILD_ROOT}%{_datadir}/applnk/Utilities/%{name}.desktop
%find_lang %{name}
chmod 644 src/klammail/*.{c,h}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
