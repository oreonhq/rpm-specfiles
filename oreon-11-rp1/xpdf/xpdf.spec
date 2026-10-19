%global source16_hash 4bce35b85b49c8e2698a2e01bede345b8e2936daf9622f8f2f4287e409e26256
%global source15_hash 7b6c4b4c39302b043bb1dbb4567af3233901b5692a4c8883f0b3be14b1db49ac
%global source14_hash 4e61cd67d1de292b4b8a8abe84790eec461be5f59165c605d004f8331eee88a2
%global source13_hash aa71214ce2ac26e0495dfb5a19f918ae21380a5c1bd9721ad028cc134bb0d76a
%global source12_hash 5ac306d5678a72b8907bb920ed4781e7c878de50a0f7043847f9ab4c02010c61
%global source8_hash b013eadae2a765fa43cc97e3443007489236e66168f1bf9e7963bc6d2e113fef
%global source7_hash 50bee3b02b34b03b0be3ca8d08c31663f8e89dac934426b7148eba4e92c1f3a6
%global source6_hash 9e6df03aec105006766423d40889631343ca9864d29326d28ce47912d0ffc32d
%global source5_hash c7f57c32e1634cf11ebe7cb55ea9d27cc9a55d5e7e54d3de7a662f2a8e56707f
%global source4_hash c7b9a71a21bb81cb24078fa67be9ac645501413cd8d20aa589f28160cdf40af2
%global source3_hash f946b8d1659812d7ed25d235ae9d693b37cd6927f34d72f32284d286ce2813b4
%global source1_hash 0d201af0747a49ec1ae0e05fc2dca185ca10754d6960d31392dbf30ce258df8d
%global source0_hash 1c38f527c46caee0f712386d42a885b96a31ed9ce11904e872559859894d137e
%global source2_key_fpr A56006CA75CF8B13FA2F120DF4825F5397271342
%undefine __cmake_in_source_build
Summary:        A PDF file viewer for the X Window System
Name: xpdf
Version: 4.06
Release:        1%{?dist}
License: (GPL-2.0-only OR GPL-3.0-only) AND BSD-3-Clause
Epoch: 1
Url: https://www.xpdfreader.com/
Source0:        https://dl.xpdfreader.com/%{name}-%{version}.tar.gz
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
Patch29: xpdf-4.04-shared-xpdf-lib.patch
Patch101: xpdf-4.02-CVE-2019-12360.patch
Patch200: xpdf-4.06-permissions.patch
Patch203: fix-444648.dpatch
Requires: urw-fonts
Requires: xdg-utils
Requires: poppler-utils
Requires: xorg-x11-fonts-ISO8859-1-75dpi
Requires: xorg-x11-fonts-ISO8859-1-100dpi
Requires: qt5-qtsvg
%if 0%{?fedora} || (0%{?oreon} >= 11)
%else
%endif
Provides:  %{name}-chinese-simplified = %{version}-%{release}
Obsoletes: %{name}-chinese-simplified < %{epoch}:%{version}-%{release}
Provides:  %{name}-chinese-traditional = %{version}-%{release}
Obsoletes: %{name}-chinese-traditional < %{epoch}:%{version}-%{release}
Provides:  %{name}-korean = %{version}-%{release}
Obsoletes: %{name}-korean < %{epoch}:%{version}-%{release}
Provides:  %{name}-japanese = %{version}-%{release}
Obsoletes: %{name}-japanese < %{epoch}:%{version}-%{release}
Requires: %{name}-libs%{_isa} = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gnupg2
BuildRequires:  gpgverify
BuildRequires:  libXpm-devel
BuildRequires:  libpaper-devel
BuildRequires:  libpng-devel
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
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
for file in doc/*.1 doc/*.5 xpdf-*/README; do
  sed -i -e 's:/etc/xpdfrc:%{_sysconfdir}/xpdfrc:g' $file
done
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
mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp -a %{_vpath_builddir}/fofi/libfofi.so* $RPM_BUILD_ROOT%{_libdir}
cp -a %{_vpath_builddir}/goo/libgoo.so* $RPM_BUILD_ROOT%{_libdir}
cp -a %{_vpath_builddir}/splash/libsplash.so* $RPM_BUILD_ROOT%{_libdir}
cp -a %{_vpath_builddir}/xpdf/libxpdfcore.so* $RPM_BUILD_ROOT%{_libdir}
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
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/
cp -a doc/sample-xpdfrc $RPM_BUILD_ROOT%{_sysconfdir}/xpdfrc
sed -i -e 's:/usr/local/share/:%{_datadir}/:g' $RPM_BUILD_ROOT%{_sysconfdir}/xpdfrc
%endif
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?fedora} || (0%{?oreon} >= 11)
%files -f %{oreon_filedir}/main.list
%files -n xpdf-devel -f %{oreon_filedir}/xpdf-devel.list
%files -n xpdf-libs -f %{oreon_filedir}/xpdf-libs.list

%changelog

%autochangelog
%endif
