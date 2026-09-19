%global source0_hash 4e83403309e155c707cb5d573981bff8030a71c9112d22a5ec7873d23aa22e8d

%define _legacy_common_support 1
Summary: Clam Anti-Virus on the KDE Desktop
Name: klamav
Version: 0.46
Release: 49%{?dist}
Source0: http://downloads.sourceforge.net/klamav/%{name}-%{version}.tar.bz2
Patch0: klamav-0.46-suse-clamav-path.patch
# Upstream notified via mailing list:
# http://sourceforge.net/mailarchive/message.php?msg_name=20080123100636.GC1177%40serv.smile.org.ua
Patch1: klamav-0.41.1-pwd-echo.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=483518
Patch2: klamav-0.44-no-kde3-mediamanager.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=553811
Patch3: klamav-0.46-fix-docpath.patch
# fix pointless gzip API abuse causing FTBFS
Patch4: klamav-0.46-gzip-api.patch
# fix FTBFS against clamav 0.101 (#1604507)
Patch5: klamav-0.46-clamav-0.101.patch
# fix build with clamav 1.0
Patch6: klamav-clamav-1.0.patch
Patch7: klamav-configure-c99.patch
Patch8: klamav-c99.patch

URL: http://klamav.sourceforge.net
License: GPL-2.0-or-later
Requires: clamav >= 0.93
Requires: clamav-update >= 0.93
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: kdelibs3-devel >= 3.5.2
BuildRequires: clamav-devel >= 0.93
BuildRequires: curl-devel
BuildRequires: gmp-devel
BuildRequires: desktop-file-utils
BuildRequires: sqlite-devel >= 3.0
BuildRequires: gettext
BuildRequires: make
BuildRequires: perl(File::Find)

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
# fix FTBFS (#2261284, #2300872, #2340698)
export CFLAGS="%{optflags} -Wno-error=incompatible-pointer-types"
%configure --disable-rpath --without-included-sqlite --with-disableupdates
# kill rpath harder, inspired by https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Removing_Rpath
# other more standard variants didnt work or caused other problems
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' libtool
%make_build

%install
%make_install

# Fix Terminal value in desktop-file
%{__sed} -i.orig -e '/^Terminal/s|^.*$|Terminal=false|' \
    ${RPM_BUILD_ROOT}%{_datadir}/applnk/Utilities/%{name}.desktop
%{__rm} -f ${RPM_BUILD_ROOT}%{_datadir}/applnk/Utilities/%{name}.desktop.orig

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
    --vendor fedora \
%endif
    --delete-original \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications/ \
    ${RPM_BUILD_ROOT}%{_datadir}/applnk/Utilities/%{name}.desktop

%find_lang %{name}

# satisfy rpmlint claim on debuginfo subpackage
chmod 644 src/klammail/*.{c,h}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_datadir}/doc/HTML/en/klamav
%{_bindir}/klamav
%{_bindir}/klammail
%{_bindir}/klamarkollon
%attr(755,root,root) %{_bindir}/ScanWithKlamAV
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/apps/klamav
%{_datadir}/apps/konqueror/servicemenus/klamav-dropdown.desktop
%{_datadir}/config.kcfg/klamavconfig.kcfg
%{_datadir}/icons/*/*x*/apps/klamav.png

%changelog
%autochangelog
