%global source0_hash 205e6752e3cb024bcce0583b43dafc9b89490c0016daa91d2486891edcf2cfc1

%define _legacy_common_support 1
Name:           MagicPoint
Version:        1.13a
Release:        45%{?dist}
Summary:        X based presentation software
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://member.wide.ad.jp/wg/mgp/
Source0:        ftp://sh.wide.ad.jp/WIDE/free-ware/mgp/magicpoint-%{version}.tar.gz
Patch0:         magicpoint-1.11b-debian.patch
Patch1:         magicpoint-1.11b-64bit.patch
Patch2:         magicpoint-1.11b-embed.patch
Patch3:         magicpoint-1.13a-gcc-warnings.patch
Patch4:         magicpoint-1.13a-xwintoppm.patch
Patch5:         magicpoint-1.13a-no-m17n-config.patch
Patch6:         magicpoint-1.13a-mng.patch
Patch7:         magicpoint-1.13a-honor-cflags-for-unimap.patch
# giflib-5.x compatibility
Patch8:         magicpoint-1.13a-giflib5.patch
# libpng > 1.5.0 compatibility
Patch9:         magicpoint-1.13a-libpng.patch
Patch10:        magicpoint-1.13a-libmng-lib64.patch
Patch11:        MagicPoint-c99.patch
Patch12:        magicpoint-1.13a-function-proto.patch
BuildRequires:  make gcc
BuildRequires:  giflib-devel libpng-devel libmng-devel fontconfig-devel 
BuildRequires:  libXmu-devel libXft-devel m17n-lib-devel
BuildRequires:  imake bison flex perl-interpreter perl-generators sharutils
Requires:       sharutils
Obsoletes:      mgp < %{version}-%{release}, magicpoint < %{version}-%{release}
Provides:       mgp = %{version}-%{release}, magicpoint = %{version}-%{release}

%description
MagicPoint is an X11 based presentation tool. MagicPoint's
presentation files (typically .mgp files) are plain text so you can
create presentation files quickly with your favorite editor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n magicpoint-%{version}
iconv -f iso8859-1 -t utf8 sample/sample-fr.mgp > sample/sample-fr.mgp.utf8
touch -r sample/sample-fr.mgp sample/sample-fr.mgp.utf8
mv sample/sample-fr.mgp.utf8 sample/sample-fr.mgp

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign -Wno-unused-variable -Wno-unused-but-set-variable -Wno-unused-function -Wno-old-style-definition -Wno-stringop-truncation -Wno-stringop-overflow -D_DEFAULT_SOURCE"
export CFLAGS="$RPM_OPT_FLAGS"
# Stop configure from checking for non-existing m17n-config shell script
export HAVE_M17NLIB="yes"
%configure --enable-locale --enable-xft2 --enable-gif --with-m17n-lib
xmkmf -a
# LIBDIR is used by the makefile to determine where to install data files
make CDEBUGFLAGS="$RPM_OPT_FLAGS" EXTRA_LDOPTIONS="$LDFLAGS" LIBDIR=%{_datadir}

%install
make install install.man DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_datadir}
install -m 755 contrib/mgp2html.pl $RPM_BUILD_ROOT%{_bindir}/mgp2html
install -m 755 contrib/mgp2latex.pl $RPM_BUILD_ROOT%{_bindir}/mgp2latex
# stop these from ending up in %%doc
rm sample/.cvsignore sample/*akefile*

%files
%doc README SYNTAX USAGE sample
%license COPYRIGHT
%{_bindir}/*
%{_datadir}/mgp
%{_mandir}/*/*

%changelog
%autochangelog
