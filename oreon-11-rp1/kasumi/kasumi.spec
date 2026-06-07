%global source0_hash none

# anthy-unicode migration
# https://github.com/fcitx/fcitx-anthy/issues/12
# https://osdn.net/projects/scim-imengine/ticket/40956
# https://github.com/uim/uim/issues/166

Name:    kasumi
Version: 2.5
Release: 50%{?dist}

License: GPL-2.0-or-later
URL:     http://kasumi.sourceforge.jp/
%if 0%{?fedora} || (0%{?oreon} >= 11)
BuildRequires: anthy-devel
%endif
BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: gtk3-devel anthy-unicode-devel
Requires: %{name}-common = %{version}-%{release}
Source0:        https://deb.debian.org/debian/pool/main/k/kasumi/kasumi_%{version}+debian2.orig.tar.gz#/kasumi-%{version}.tar.gz
Patch0:        kasumi-853099-manpage.patch
Patch1:        kasumi-1928410-gtk3.patch
Patch2:        kasumi-check-anthy-pkg.patch
Patch3:        kasumi-1938091.patch
Patch4:        kasumi-c89.patch
Patch5:        kasumi-fix-crash-on-close.patch


Summary: An anthy dictionary management tool
%description
Kasumi is a dictionary management tool for Anthy.


%package common
Provides: %{name} = %{version}-%{release}
Summary: Anthy dictionary management common files between kasumi and kasumi-unicode
BuildArch: noarch

%description common
This package contains common files for kasumi and kasumi-unicode.


%package unicode
Requires: %{name}-common = %{version}-%{release}
Summary: An anthy-unicode dictionary management tool

%description unicode
Kasumi-unicode is a dictionary management tool for Anthy-unicode.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n kasumi-2.5+debian2 -p1

%build
sed -i -e '/AM_PATH_GTK_2_0(/i\
PKG_CHECK_MODULES([GTK], [gtk+-3.0])\
CFLAGS="$CFLAGS $GTK_CFLAGS"\
CPPFLAGS="$CPPFLAGS $GTK_CFLAGS"\
LIBS="$LIBS $GTK_LIBS"' \
    -e '/AM_PATH_GTK_2_0(/d' \
    configure.in
autoreconf -f -i
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
echo "# Building kasumi-unicode"
sed -e 's/AC_CHECK_LIB(anthydic,/AC_CHECK_LIB(anthydic-unicode,/' \
    -e 's/AC_CHECK_LIB(anthy,/AC_CHECK_LIB(anthy-unicode,/' \
    -e 's/PKG_CHECK_MODULES(ANTHY, anthy/PKG_CHECK_MODULES(ANTHY, anthy-unicode/' \
    -i.orig configure.in
autoreconf -f -i
%configure
make %{?_smp_mflags}

%if 0%{?fedora} || (0%{?oreon} >= 11)
mv kasumi kasumi-unicode
make clean
cp configure.in.orig configure.in

autoreconf -f -i
echo "# Building kasumi"
%configure
make %{?_smp_mflags}
%endif


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%if 0%{?fedora} || (0%{?oreon} >= 11)
install -pm 755 kasumi-unicode $RPM_BUILD_ROOT%{_bindir}/kasumi-unicode
%else
mv $RPM_BUILD_ROOT%{_bindir}/kasumi $RPM_BUILD_ROOT%{_bindir}/kasumi-unicode
%endif

# remove .desktop file so that kasumi is accessible from scim panel/ibus panel and it's not necessary for other users.
rm -rf $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%find_lang %{name}


%if 0%{?fedora} || (0%{?oreon} >= 11)
%files
%{_bindir}/kasumi
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%endif

%files unicode
%{_bindir}/kasumi-unicode
%doc AUTHORS ChangeLog NEWS README
%license COPYING

%files common -f %{name}.lang
%{_mandir}/man1/kasumi.1*
%{_datadir}/pixmaps/kasumi.png


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5-50
- Import
