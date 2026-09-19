%global source0_hash 1c38f527c46caee0f712386d42a885b96a31ed9ce11904e872559859894d137e
%global source2_key_fpr A56006CA75CF8B13FA2F120DF4825F5397271342

%undefine __cmake_in_source_build

Summary: A PDF file viewer for the X Window System
Name: xpdf
Version: 4.06
Release: 2%{?dist}
License: (GPL-2.0-only OR GPL-3.0-only) AND BSD-3-Clause
Epoch: 1
Url: https://www.xpdfreader.com/

Source0: https://dl.xpdfreader.com/%{name}-%{version}.tar.gz
Source1: https://dl.xpdfreader.com/%{name}-%{version}.tar.gz.sig
Source2: gpg-key.txt
Source3: https://dl.xpdfreader.com/xpdf-chinese-simplified.tar.gz
Source4: https://dl.xpdfreader.com/xpdf-chinese-traditional.tar.gz
Source5: https://dl.xpdfreader.com/xpdf-japanese.tar.gz
Source6: https://dl.xpdfreader.com/xpdf-korean.tar.gz
Source7: https://dl.xpdfreader.com/xpdf-cyrillic.tar.gz
Source8: https://dl.xpdfreader.com/xpdf-thai.tar.gz
Source10: xpdf.desktop
Source11: xpdf.png
Source12: https://dl.xpdfreader.com/xpdf-arabic.tar.gz
Source13: https://dl.xpdfreader.com/xpdf-greek.tar.gz
Source14: https://dl.xpdfreader.com/xpdf-hebrew.tar.gz
Source15: https://dl.xpdfreader.com/xpdf-latin2.tar.gz
Source16: https://dl.xpdfreader.com/xpdf-turkish.tar.gz

Patch3: xpdf-4.01-ext.patch
Patch9: xpdf-3.00-papersize.patch
Patch11: xpdf-4.01-crash.patch
Patch12: xpdf-4.01-64bit.patch
Patch15: xpdf-3.04-nocmap.patch
Patch25: xpdf-4.00-versionedlib.patch
Patch26: xpdf-4.06-urw-base35-fonts.patch
Patch28: xpdf-4.04-GlobalParams-null-fix.patch
# https://forum.xpdfreader.com/viewtopic.php?t=42521
Patch29: xpdf-4.04-shared-xpdf-lib.patch

# Security patches
# Based on
# https://gitlab.freedesktop.org/poppler/poppler/commit/cdb7ad95f7c8fbf63ade040d8a07ec96467042fc
# https://gitlab.freedesktop.org/poppler/poppler/commit/bf4aae25a244b1033a2479b9a8f633224f7d5de5
Patch101: xpdf-4.02-CVE-2019-12360.patch
# merged in 4.06
# Patch102: xpdf-4.05-CVE-2024-4141.patch

# Debian patches
Patch200: xpdf-4.06-permissions.patch
# Proper stream encoding on 64bit platforms
Patch203: fix-444648.dpatch

Requires: urw-fonts
Requires: xdg-utils
Requires: poppler-utils
Requires: xorg-x11-fonts-ISO8859-1-75dpi
Requires: xorg-x11-fonts-ISO8859-1-100dpi
Requires: qt5-qtsvg

%if 0%{?fedora} || (0%{?oreon} >= 11)
BuildRequires: qt5-qtbase-devel, cmake
BuildRequires: freetype-devel >= 2.1.7
BuildRequires: fontconfig-devel
BuildRequires: desktop-file-utils
BuildRequires: libpaper-devel
BuildRequires: libpng-devel
BuildRequires: libXpm-devel
BuildRequires: cups-devel
%else
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: freetype-devel >= 2.1.7
BuildRequires: fontconfig-devel
BuildRequires: libpng-devel
%endif
BuildRequires: gpgverify
BuildRequires: gnupg2

Provides:  %{name}-chinese-simplified = %{version}-%{release}
Obsoletes: %{name}-chinese-simplified < %{epoch}:%{version}-%{release}
Provides:  %{name}-chinese-traditional = %{version}-%{release}
Obsoletes: %{name}-chinese-traditional < %{epoch}:%{version}-%{release}
Provides:  %{name}-korean = %{version}-%{release}
Obsoletes: %{name}-korean < %{epoch}:%{version}-%{release}
Provides:  %{name}-japanese = %{version}-%{release}
Obsoletes: %{name}-japanese < %{epoch}:%{version}-%{release}

Requires: %{name}-libs%{_isa} = %{epoch}:%{version}-%{release}

%description
Xpdf is an X Window System based viewer for Portable Document Format
(PDF) files. Xpdf is a small and efficient program which uses
standard X fonts.

%package devel
%if 0%{?fedora} || (0%{?oreon} >= 11)
Requires: %{name}%{_isa} = %{epoch}:%{version}-%{release}
Requires: libpaper-devel
%endif
Requires: fontconfig-devel, freetype-devel
Requires: libpng-devel
Summary: Development files for xpdf libraries

%description devel
Development files for xpdf libraries.

%package libs
Summary: Libraries from xpdf

%description libs
Libraries from xpdf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
%gpgverify -k2 -s1 -d0
%if 0%{?fedora} || (0%{?oreon} >= 11) 
%setup -q -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 12 -a 13 -a 14 -a 15 -a 16
%else
%setup -q
%endif
rm -f xpdf-chinese-simplified/CMap/Adobe-GB1-UCS2 \
      xpdf-chinese-simplified/CMap/GBK-EUC-UCS2 \
      xpdf-chinese-simplified/CMap/GBpc-EUC-UCS2 \
      xpdf-chinese-simplified/CMap/GBpc-EUC-UCS2C \
      xpdf-chinese-traditional/CMap/Adobe-CNS1-UCS2 \
      xpdf-chinese-traditional/CMap/B5pc-UCS2 \
      xpdf-chinese-traditional/CMap/B5pc-UCS2C \
      xpdf-chinese-traditional/CMap/ETen-B5-UCS2 \
      xpdf-japanese/CMap/90ms-RKSJ-UCS2 \
      xpdf-japanese/CMap/90pv-RKSJ-UCS2 \
      xpdf-japanese/CMap/90pv-RKSJ-UCS2C \
      xpdf-japanese/CMap/Adobe-Japan1-UCS2 \
      xpdf-korean/CMap/Adobe-Korea1-UCS2 \
      xpdf-korean/CMap/KSCms-UHC-UCS2 \
      xpdf-korean/CMap/KSCpc-EUC-UCS2 \
      xpdf-korean/CMap/KSCpc-EUC-UCS2C
%patch -P3 -p1 -b .ext
%patch -P9 -p1 -b .papersize
%patch -P11 -p1 -b .crash
%patch -P12 -p1 -b .alloc
%patch -P25 -p1 -b .versionedlib
%patch -P26 -p1 -b .urw-font-fix
%patch -P28 -p1 -b .GlobalParams-null-fix
%patch -P29 -p1 -b .shared-xpdf-lib

# security patches
%patch -P101 -p1 -b .CVE-2019-12360
# %%patch -P102 -p1 -b .CVE-2024-4141

# debian patches
%patch -P200 -p1 -b .permissions
%patch -P203 -p1 -b .64bit-stream

# Comment out unused urlCommand option
sed -i 's|urlCommand|#urlCommand|g' doc/sample-xpdfrc

%build
find -name "*orig" | xargs rm -f

%if 0%{?fedora} || (0%{?oreon} >= 11)
# This may seem pointless, but in the unlikely event that _sysconfdir != /etc ...
for file in doc/*.1 doc/*.5 xpdf-*/README; do
  sed -i -e 's:/etc/xpdfrc:%{_sysconfdir}/xpdfrc:g' $file
done
# Same action for _datadir.
for file in xpdf-*/README xpdf-*/add-to-xpdfrc; do
  sed -i -e 's:/usr/share/:%{_datadir}/:g' $file
  sed -i -e 's:/usr/local/share/:%{_datadir}/:g' $file
done
%endif

export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -Wno-deprecated -fPIC"
%cmake -DMULTITHREADED=ON -DOPI_SUPPORT=ON -DXPDFWIDGET_PRINTING=1 -DSYSTEM_XPDFRC="%{_sysconfdir}/xpdfrc" -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build
%if 0%{?fedora} || (0%{?oreon} >= 11)
%cmake_build --target xpdf
%endif

%install
%if 0%{?fedora} || (0%{?oreon} >= 11)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xpdf/arabic \
         $RPM_BUILD_ROOT%{_datadir}/xpdf/chinese-simplified \
         $RPM_BUILD_ROOT%{_datadir}/xpdf/chinese-traditional \
         $RPM_BUILD_ROOT%{_datadir}/xpdf/cyrillic \
         $RPM_BUILD_ROOT%{_datadir}/xpdf/greek \
         $RPM_BUILD_ROOT%{_datadir}/xpdf/hebrew \
         $RPM_BUILD_ROOT%{_datadir}/xpdf/japanese \
         $RPM_BUILD_ROOT%{_datadir}/xpdf/korean \
         $RPM_BUILD_ROOT%{_datadir}/xpdf/latin2 \
         $RPM_BUILD_ROOT%{_datadir}/xpdf/thai \
         $RPM_BUILD_ROOT%{_datadir}/xpdf/turkish \
         $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

%cmake_install
%endif

# Y U NO INSTALL LIBS?!?
mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp -a %{_vpath_builddir}/fofi/libfofi.so* $RPM_BUILD_ROOT%{_libdir}
cp -a %{_vpath_builddir}/goo/libgoo.so* $RPM_BUILD_ROOT%{_libdir}
cp -a %{_vpath_builddir}/splash/libsplash.so* $RPM_BUILD_ROOT%{_libdir}
cp -a %{_vpath_builddir}/xpdf/libxpdfcore.so* $RPM_BUILD_ROOT%{_libdir}

# headers
mkdir -p $RPM_BUILD_ROOT%{_includedir}/xpdf/fofi
mkdir -p $RPM_BUILD_ROOT%{_includedir}/xpdf/goo
mkdir -p $RPM_BUILD_ROOT%{_includedir}/xpdf/splash
cp -a fofi/*.h $RPM_BUILD_ROOT%{_includedir}/xpdf/fofi/
cp -a goo/*.h $RPM_BUILD_ROOT%{_includedir}/xpdf/goo/
cp -a splash/*.h $RPM_BUILD_ROOT%{_includedir}/xpdf/splash/
cp -a xpdf/*.h $RPM_BUILD_ROOT%{_includedir}/xpdf/
cp -a %{__cmake_builddir}/aconf.h $RPM_BUILD_ROOT%{_includedir}/xpdf/

%if 0%{?fedora} || (0%{?oreon} >= 11)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
%if 0%{?rhel} > 5 || 0%{?fedora} || 0%{?oreon} >= 11
desktop-file-install            \
%else
desktop-file-install --vendor "fedora"                  \
%endif
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        --add-category X-Fedora                         \
        %{SOURCE10}
install -m 0644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/xpdf.png

cp -pr xpdf-arabic/* $RPM_BUILD_ROOT%{_datadir}/xpdf/arabic/
cp -pr xpdf-chinese-simplified/* $RPM_BUILD_ROOT%{_datadir}/xpdf/chinese-simplified/
cp -pr xpdf-chinese-traditional/* $RPM_BUILD_ROOT%{_datadir}/xpdf/chinese-traditional/
cp -pr xpdf-cyrillic/* $RPM_BUILD_ROOT%{_datadir}/xpdf/cyrillic/
cp -pr xpdf-greek/* $RPM_BUILD_ROOT%{_datadir}/xpdf/greek/
cp -pr xpdf-hebrew/* $RPM_BUILD_ROOT%{_datadir}/xpdf/hebrew/
cp -pr xpdf-japanese/* $RPM_BUILD_ROOT%{_datadir}/xpdf/japanese/
cp -pr xpdf-korean/* $RPM_BUILD_ROOT%{_datadir}/xpdf/korean/
cp -pr xpdf-latin2/* $RPM_BUILD_ROOT%{_datadir}/xpdf/latin2/
cp -pr xpdf-thai/* $RPM_BUILD_ROOT%{_datadir}/xpdf/thai/
cp -pr xpdf-turkish/* $RPM_BUILD_ROOT%{_datadir}/xpdf/turkish/

# poppler provides all utilities now
# http://bugzilla.redhat.com/bugzillA/SHow_bug.cgi?id=177446
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=219032
%if 0%{?rhel} > 6 || 0%{?fedora} || 0%{?oreon} >= 11
rm $RPM_BUILD_ROOT%{_bindir}/pdfdetach
%endif
rm $RPM_BUILD_ROOT%{_bindir}/pdffonts
rm $RPM_BUILD_ROOT%{_bindir}/pdfimages
rm $RPM_BUILD_ROOT%{_bindir}/pdfinfo
rm $RPM_BUILD_ROOT%{_bindir}/pdftohtml
rm $RPM_BUILD_ROOT%{_bindir}/pdftops
rm $RPM_BUILD_ROOT%{_bindir}/pdftotext
%if 0%{?rhel} > 5 || 0%{?fedora} > 6 || 0%{?oreon} >= 11
rm $RPM_BUILD_ROOT%{_bindir}/pdftoppm
rm $RPM_BUILD_ROOT%{_mandir}/man1/pdftoppm.1*
%endif
%if 0%{?rhel} > 6 || 0%{?fedora} || 0%{?oreon} >= 11
rm $RPM_BUILD_ROOT%{_mandir}/man1/pdfdetach.1*
%endif
rm $RPM_BUILD_ROOT%{_mandir}/man1/pdffonts.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/pdfimages.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/pdfinfo.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/pdftohtml.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/pdftops.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/pdftotext.1*

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xpdf/
for i in arabic chinese-simplified chinese-traditional cyrillic greek hebrew japanese korean latin2 thai turkish; do
     mv $RPM_BUILD_ROOT%{_datadir}/%{name}/$i/README README.$i
     mv $RPM_BUILD_ROOT%{_datadir}/%{name}/$i/add-to-xpdfrc $RPM_BUILD_ROOT%{_sysconfdir}/xpdf/add-to-xpdfrc.$i
done

# xpdfrc cleanup
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/
cp -a doc/sample-xpdfrc $RPM_BUILD_ROOT%{_sysconfdir}/xpdfrc
sed -i -e 's:/usr/local/share/:%{_datadir}/:g' $RPM_BUILD_ROOT%{_sysconfdir}/xpdfrc
%endif

%ldconfig_scriptlets

%if 0%{?fedora} || (0%{?oreon} >= 11)
%files
%license COPYING COPYING3
%doc CHANGES README README.*
%{_bindir}/xpdf
%{_bindir}/pdftopng
%{_libdir}/lib*.so.*
%{_mandir}/man?/pdftopng*
%{_mandir}/man?/xpdf*
%if 0%{?rhel} > 5 || 0%{?fedora} > 6 || 0%{?oreon} >= 11
# Do Nothing.
%else
%{_bindir}/pdftoppm
%{_mandir}/man?/pdftoppm*
%endif
%if 0%{?rhel}
%if 0%{?rhel} < 7
%{_bindir}/pdfdetach
%{_mandir}/man?/pdfdetach*
%endif
%endif
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdfrc
%dir %{_sysconfdir}/xpdf
%lang(ar) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.arabic
%lang(zh_CN) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.chinese-simplified
%lang(zh_TW) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.chinese-traditional
%lang(el) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.greek
%lang(iw) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.hebrew
%lang(ja) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.japanese
%lang(ko) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.korean
%lang(th) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.thai
%lang(tr) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.turkish
# cyrillic and latin2 are not langs, many languages are cyrillic/latin2
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.cyrillic
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xpdf/add-to-xpdfrc.latin2
%{_datadir}/icons/hicolor/48x48/apps/xpdf.png
%dir %{_datadir}/xpdf
%{_datadir}/applications/*
%lang(ar) %{_datadir}/xpdf/arabic
%lang(zh_CN) %{_datadir}/xpdf/chinese-simplified
%lang(zh_TW) %{_datadir}/xpdf/chinese-traditional
%lang(el) %{_datadir}/xpdf/greek
%lang(iw) %{_datadir}/xpdf/hebrew
%lang(ja) %{_datadir}/xpdf/japanese
%lang(ko) %{_datadir}/xpdf/korean
%lang(th) %{_datadir}/xpdf/thai
%lang(tr) %{_datadir}/xpdf/turkish
%{_datadir}/xpdf/cyrillic
%{_datadir}/xpdf/latin2
%endif

%files devel
%{_includedir}/xpdf/
%{_libdir}/lib*.so

%files libs
%{_libdir}/lib*.so.*

%changelog
%autochangelog
