%global _catalogue /etc/X11/fontpath.d
# NOTE: Fonts strictly intended for X core fonts, should be installed into _x11fontdir.
%global _x11fontdir %{_datadir}/X11/fonts
%global _x11fontencodingsdir %{_x11fontdir}/encodings

# A macro to de-duplicate a set of calls used in multiple fonts.
# Usage: font_update_dirs [-f] [-t] <directory>
#	-f ... run fontscale
# 	-t ... run ttmkfdir
# 	-u ... uninstall mode, only perform actions if the target directory exists
# 	<directory>
%global font_update_dirs(ftu) (							\
if [ -z "%*" ]; then								\
	echo "Missing directory argument";					\
	exit 1;									\
fi										\
fontdir="%{_x11fontdir}/%%1"							\
if [ -z "%%{-u}" -o -d $fontdir ]; then						\
   if [ ! -z "%%{-f}" ]; then							\
	   mkfontscale "$fontdir";						\
   fi										\
   if [ ! -z "%%{-t}" ]; then							\
	ttmkfdir -d "$fontdir" -o "$fontdir/fonts.scale";			\
   fi										\
   mkfontdir "$fontdir";							\
   fc-cache "$fontdir";								\
   mkdir -p "%{_x11fontencodingsdir}/large";					\
   mkfontscale -n -e "%{_x11fontencodingsdir}" -e "%{_x11fontencodingsdir}/large" "%{_x11fontencodingsdir}";	\
fi										\
)

Summary:    X.Org X11 fonts
Name:       xorg-x11-fonts
Version:    7.5
Release:    42%{?dist}
License:    HPND AND Adobe-Utopia AND Cronyx AND MIT AND Lucida-Bitmap-Fonts AND Bitstream-Charter AND X11
URL:        https://www.x.org

BuildArch:  noarch

# Not copyrightable, see fedora-license-data!394
Source0:    https://www.x.org/pub/individual/font/encodings-1.0.5.tar.bz2
# SPDX: HPND
Source1:    https://www.x.org/pub/individual/font/font-adobe-100dpi-1.0.3.tar.bz2
Source2:    https://www.x.org/pub/individual/font/font-adobe-75dpi-1.0.3.tar.bz2
# SPDX: Adobe-Utopia
Source3:    https://www.x.org/pub/individual/font/font-adobe-utopia-100dpi-1.0.4.tar.bz2
Source4:    https://www.x.org/pub/individual/font/font-adobe-utopia-75dpi-1.0.4.tar.bz2
Source5:    https://www.x.org/pub/individual/font/font-adobe-utopia-type1-1.0.4.tar.bz2
# SPDX: Cronyx
Source6:    https://www.x.org/pub/individual/font/font-alias-1.0.3.tar.bz2
# SPDX: MIT
Source7:    https://www.x.org/pub/individual/font/font-arabic-misc-1.0.3.tar.bz2
# SPDX: Lucida-Bitmap-Fonts
Source8:    https://www.x.org/pub/individual/font/font-bh-100dpi-1.0.3.tar.bz2
Source9:    https://www.x.org/pub/individual/font/font-bh-75dpi-1.0.3.tar.bz2
# Not copyrightable, see fedora-license-data#333
Source10:   https://www.x.org/pub/individual/font/font-bh-lucidatypewriter-100dpi-1.0.3.tar.bz2
Source11:   https://www.x.org/pub/individual/font/font-bh-lucidatypewriter-75dpi-1.0.3.tar.bz2
# SPDX: HPND
Source12:   https://www.x.org/pub/individual/font/font-bitstream-100dpi-1.0.3.tar.bz2
Source13:   https://www.x.org/pub/individual/font/font-bitstream-75dpi-1.0.3.tar.bz2
# SPDX: Bitstream-Charter
Source14:   https://www.x.org/pub/individual/font/font-bitstream-type1-1.0.3.tar.bz2
# SPDX: Cronyx
Source15:   https://www.x.org/pub/individual/font/font-cronyx-cyrillic-1.0.3.tar.bz2
# SPDX: LicenseRef-Fedora-UltraPermissive
Source16:   https://www.x.org/pub/individual/font/font-cursor-misc-1.0.3.tar.bz2
# Daewoo-misc has no license terms, just Copyright (#1952723)
# Source17:   https://www.x.org/pub/individual/font/font-daewoo-misc-1.0.3.tar.bz2
# SPDX: HPND for dec/isas
Source18:   https://www.x.org/pub/individual/font/font-dec-misc-1.0.3.tar.bz2
Source19:   https://www.x.org/pub/individual/font/font-isas-misc-1.0.3.tar.bz2
# Not copyrightable, see fedora-license-data#327
Source20:   https://www.x.org/pub/individual/font/font-jis-misc-1.0.3.tar.bz2
# SPDX LicenseRef-Fedora-Public-Domain
Source21:   https://www.x.org/pub/individual/font/font-micro-misc-1.0.3.tar.bz2
# SPDX: Cronyx AND LicenseRef-Fedora-Public-Domain AND LicenseRef-Fedora-UltraPermissive
Source22:   https://www.x.org/pub/individual/font/font-misc-cyrillic-1.0.3.tar.bz2
# SPDX: MIT
Source23:   https://www.x.org/pub/individual/font/font-misc-ethiopic-1.0.3.tar.bz2
# SPDX LicenseRef-Fedora-Public-Domain
Source24:   https://www.x.org/pub/individual/font/font-misc-misc-1.1.2.tar.bz2
# SPDX: MIT
Source25:   https://www.x.org/pub/individual/font/font-mutt-misc-1.0.3.tar.bz2
# SPDX: HPND
Source26:   https://www.x.org/pub/individual/font/font-schumacher-misc-1.1.2.tar.bz2
# SPDX: Cronyx
Source27:   https://www.x.org/pub/individual/font/font-screen-cyrillic-1.0.4.tar.bz2
# SPDX: HPND
Source28:   https://www.x.org/pub/individual/font/font-sony-misc-1.0.3.tar.bz2
# MIT
Source29:   https://www.x.org/pub/individual/font/font-sun-misc-1.0.3.tar.bz2
# SPDX LicenseRef-Fedora-Public-Domain
Source30:   https://www.x.org/pub/individual/font/font-winitzki-cyrillic-1.0.3.tar.bz2
# X11
Source31:   https://www.x.org/pub/individual/font/font-xfree86-type1-1.0.4.tar.bz2
# oreon url source checksums begin
%global source0_sha256 bd96e16143a044b19e87f217cf6a3763a70c561d1076aad6f6d862ec41774a31
%global source0_file encodings-1.0.5.tar.bz2
%global source1_sha256 b2c08433eab5cb202470aa9f779efefce8d9cab2534f34f3aa4a31d05671c054
%global source1_file font-adobe-100dpi-1.0.3.tar.bz2
%global source2_sha256 c6024a1e4a1e65f413f994dd08b734efd393ce0a502eb465deb77b9a36db4d09
%global source2_file font-adobe-75dpi-1.0.3.tar.bz2
%global source3_sha256 d16f5e3f227cc6dd07a160a71f443559682dbc35f1c056a5385085aaec4fada5
%global source3_file font-adobe-utopia-100dpi-1.0.4.tar.bz2
%global source4_sha256 8732719c61f3661c8bad63804ebfd54fc7de21ab848e9a26a19b1778ef8b5c94
%global source4_file font-adobe-utopia-75dpi-1.0.4.tar.bz2
%global source5_sha256 979435105f897a70f8993fa02c8362160b0513366c2ab896965416f96dbb8077
%global source5_file font-adobe-utopia-type1-1.0.4.tar.bz2
%global source6_sha256 8b453b2aae1cfa8090009ca037037b8c5e333550651d5a158b7264ce1d472c9a
%global source6_file font-alias-1.0.3.tar.bz2
%global source7_sha256 505d9b12a7093389e67a925dfda6346bde26d114c67f0cdca7aeda6e5d3344f4
%global source7_file font-arabic-misc-1.0.3.tar.bz2
%global source8_sha256 23c07162708e4b79eb33095c8bfa62c783717a9431254bbf44863734ea239481
%global source8_file font-bh-100dpi-1.0.3.tar.bz2
%global source9_sha256 3486aa51ac92c646a448fe899c5c3dae0024b1fef724d5100d52640d1cac721c
%global source9_file font-bh-75dpi-1.0.3.tar.bz2
%global source10_sha256 62a83363c2536095fda49d260d21e0847675676e4e3415054064cbdffa641fbb
%global source10_file font-bh-lucidatypewriter-100dpi-1.0.3.tar.bz2
%global source11_sha256 4ac16afbe205480cc5572e2977ea63488c543d05be0ea8e5a94c845a6eebcb31
%global source11_file font-bh-lucidatypewriter-75dpi-1.0.3.tar.bz2
%global source12_sha256 ebe0d7444e3d7c8da7642055ac2206f0190ee060700d99cd876f8fc9964cb6ce
%global source12_file font-bitstream-100dpi-1.0.3.tar.bz2
%global source13_sha256 ba3f5e4610c07bd5859881660753ec6d75d179f26fc967aa776dbb3d5d5cf48e
%global source13_file font-bitstream-75dpi-1.0.3.tar.bz2
%global source14_sha256 c6ea0569adad2c577f140328dc3302e729cb1b1ea90cd0025caf380625f8a688
%global source14_file font-bitstream-type1-1.0.3.tar.bz2
%global source15_sha256 6e8631936157677c77ba032b5c7b1fb3cb2ee872dbcea0444f12cd602cd9212a
%global source15_file font-cronyx-cyrillic-1.0.3.tar.bz2
%global source16_sha256 17363eb35eece2e08144da5f060c70103b59d0972b4f4d77fd84c9a7a2dba635
%global source16_file font-cursor-misc-1.0.3.tar.bz2
%global source18_sha256 e19ddf8b5f8de914d81675358fdfe37762e9ce524887cc983adef34f2850ff7b
%global source18_file font-dec-misc-1.0.3.tar.bz2
%global source19_sha256 5824ab4b485951107dd245b8f7717d2822f1a6dbf6cea98f1ac7f49905c0a867
%global source19_file font-isas-misc-1.0.3.tar.bz2
%global source20_sha256 2b18ce10b367ebafe95a17de799b6db9a24e2337188d124adaf68af05b1fac65
%global source20_file font-jis-misc-1.0.3.tar.bz2
%global source21_sha256 9a3381c10f32d9511f0ad4179df395914c50779103c16cddf7017f5220ed8db6
%global source21_file font-micro-misc-1.0.3.tar.bz2
%global source22_sha256 e40fe3e3323c62b738550795457ad555c70c008aa91b5912dfd46f8e745f5e60
%global source22_file font-misc-cyrillic-1.0.3.tar.bz2
%global source23_sha256 53cb1fd83afdbe7939c0eac34003676ee0e6023216892d98054db90b703c98a5
%global source23_file font-misc-ethiopic-1.0.3.tar.bz2
%global source24_sha256 b8e77940e4e1769dc47ef1805918d8c9be37c708735832a07204258bacc11794
%global source24_file font-misc-misc-1.1.2.tar.bz2
%global source25_sha256 bd5f7adb34367c197773a9801df5bce7b019664941900b2a31fbfe1ff2830f8f
%global source25_file font-mutt-misc-1.0.3.tar.bz2
%global source26_sha256 e444028656e0767e2eddc6d9aca462b16a2be75a47244dbc199b2c44eca87e5a
%global source26_file font-schumacher-misc-1.1.2.tar.bz2
%global source27_sha256 824231e8dffe15299454e47259f29d98001c9cf8ad3d6b5171399e4d71705e79
%global source27_file font-screen-cyrillic-1.0.4.tar.bz2
%global source28_sha256 2043a326ba347c9da5ca1e9bc363e2521c3ea40b43b1f9662d333efd4867cff5
%global source28_file font-sony-misc-1.0.3.tar.bz2
%global source29_sha256 481f4fcbbf7005658b080b3cf342c8c76de752e77f47958b2b383de73266d2e0
%global source29_file font-sun-misc-1.0.3.tar.bz2
%global source30_sha256 abd13b63d02fcaec488686c23683e5cf640b43bd32f8ca22eeae6f84df0a36a0
%global source30_file font-winitzki-cyrillic-1.0.3.tar.bz2
%global source31_sha256 caebf42aec7be7f3bd40e0f232d6f34881b853dc84acfcdf7458358701fbe34a
%global source31_file font-xfree86-type1-1.0.4.tar.bz2
# oreon url source checksums end

# Luxi fonts are under a bad license
# http://www.x.org/pub/individual/font/font-bh-ttf-1.0.0.tar.bz2
# http://www.x.org/pub/individual/font/font-bh-type1-1.0.0.tar.bz2

# IBM refused to relicense ibm-type1 fonts with permission to modify
# http://www.x.org/pub/individual/font/font-ibm-type1-1.0.0.tar.bz2

# Meltho Syrian fonts (misc-meltho) have a bad license, upstream did not respond
# to request for relicensing
# http://www.x.org/pub/individual/font/font-misc-meltho-1.0.0.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  bdftopcf mkfontscale
BuildRequires:  font-util >= 1.1.0
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildRequires:  ucs2any

%description
X.Org X Window System fonts.

%package misc
Summary:            misc bitmap fonts for the X Window System
Requires(post):     fontconfig
Requires(post):     mkfontdir
Requires(postun):   fontconfig
Requires(postun):   mkfontdir
# Still required by xfig-common, xosd, xtide
Obsoletes:          xorg-x11-fonts-base <= %{version}-%{release}
Provides:           xorg-x11-fonts-base = %{version}-%{release}

%description misc
This package contains misc bitmap Chinese, Japanese, Korean, Indic, and Arabic
fonts for use with X Window System.

%package Type1
Summary:            Type1 fonts provided by the X Window System
Requires(post):     fontconfig
Requires(post):     mkfontdir
Requires(post):     ttmkfdir
Requires(postun):   fontconfig
Requires(postun):   mkfontdir
Requires(postun):   ttmkfdir

%description Type1
A collection of Type1 fonts which are part of the core X Window System
distribution.

%package ethiopic
Summary:            Ethiopic fonts
Requires(post):     fontconfig
Requires(post):     mkfontdir
Requires(post):     mkfontscale
Requires(post):     ttmkfdir
Requires(postun):   fontconfig
Requires(postun):   mkfontdir
Requires(postun):   mkfontscale
Requires(postun):   ttmkfdir

%description ethiopic
Ethiopic fonts which are part of the core X Window System distribution.

%package 75dpi
Summary:            A set of 75dpi resolution fonts for the X Window System
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description 75dpi
A set of 75 dpi fonts used by the X window system.

%package 100dpi
Summary:            A set of 100dpi resolution fonts for the X Window System
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description 100dpi
A set of 100 dpi fonts used by the X window system.

%package ISO8859-1-75dpi
Summary:            A set of 75dpi ISO-8859-1 fonts for X
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description ISO8859-1-75dpi
Contains a set of 75dpi fonts for ISO-8859-1.

%package ISO8859-1-100dpi
Summary:            A set of 100dpi ISO-8859-1 fonts for X
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description ISO8859-1-100dpi
Contains a set of 100dpi fonts for ISO-8859-1.

%package ISO8859-2-75dpi
Summary:            A set of 75dpi Central European language fonts for X
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description ISO8859-2-75dpi
Contains a set of 75dpi fonts for Central European languages.

%package ISO8859-2-100dpi
Summary:            A set of 100dpi Central European language fonts for X
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description ISO8859-2-100dpi
Contains a set of 100dpi fonts for Central European languages.

%package ISO8859-9-75dpi
Summary:            ISO8859-9-75dpi fonts
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description ISO8859-9-75dpi
Contains a set of 75dpi fonts for the Turkish language.

%package ISO8859-9-100dpi
Summary:            ISO8859-9-100dpi fonts
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description ISO8859-9-100dpi
Contains a set of 100dpi fonts for the Turkish language.

%package ISO8859-14-75dpi
Summary:            ISO8859-14-75dpi fonts
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description ISO8859-14-75dpi
Contains a set of 75dpi fonts in the ISO8859-14 encoding which provide Welsh
support.

%package ISO8859-14-100dpi
Summary:            ISO8859-14-100dpi fonts
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description ISO8859-14-100dpi
Contains a set of 100dpi fonts in the ISO8859-14 encoding which provide Welsh
support.

%package ISO8859-15-75dpi
Summary:            ISO8859-15-75dpi fonts
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description ISO8859-15-75dpi
Contains a set of 75dpi fonts in the ISO8859-15 encoding which provide Euro
support.

%package ISO8859-15-100dpi
Summary:            ISO8859-15-100dpi fonts
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description ISO8859-15-100dpi
Contains a set of 100dpi fonts in the ISO8859-15 encoding which provide Euro
support.

%package cyrillic
Summary:            Cyrillic fonts for X
Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%description cyrillic
Contains a set of Cyrillic fonts.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/encodings-1.0.5.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bd96e16143a044b19e87f217cf6a3763a70c561d1076aad6f6d862ec41774a31" || { echo "oreon: Source0 SHA256 mismatch for encodings-1.0.5.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-adobe-100dpi-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b2c08433eab5cb202470aa9f779efefce8d9cab2534f34f3aa4a31d05671c054" || { echo "oreon: Source1 SHA256 mismatch for font-adobe-100dpi-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-adobe-75dpi-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c6024a1e4a1e65f413f994dd08b734efd393ce0a502eb465deb77b9a36db4d09" || { echo "oreon: Source2 SHA256 mismatch for font-adobe-75dpi-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-adobe-utopia-100dpi-1.0.4.tar.bz2; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d16f5e3f227cc6dd07a160a71f443559682dbc35f1c056a5385085aaec4fada5" || { echo "oreon: Source3 SHA256 mismatch for font-adobe-utopia-100dpi-1.0.4.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-adobe-utopia-75dpi-1.0.4.tar.bz2; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8732719c61f3661c8bad63804ebfd54fc7de21ab848e9a26a19b1778ef8b5c94" || { echo "oreon: Source4 SHA256 mismatch for font-adobe-utopia-75dpi-1.0.4.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-adobe-utopia-type1-1.0.4.tar.bz2; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "979435105f897a70f8993fa02c8362160b0513366c2ab896965416f96dbb8077" || { echo "oreon: Source5 SHA256 mismatch for font-adobe-utopia-type1-1.0.4.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-alias-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8b453b2aae1cfa8090009ca037037b8c5e333550651d5a158b7264ce1d472c9a" || { echo "oreon: Source6 SHA256 mismatch for font-alias-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-arabic-misc-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "505d9b12a7093389e67a925dfda6346bde26d114c67f0cdca7aeda6e5d3344f4" || { echo "oreon: Source7 SHA256 mismatch for font-arabic-misc-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-bh-100dpi-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "23c07162708e4b79eb33095c8bfa62c783717a9431254bbf44863734ea239481" || { echo "oreon: Source8 SHA256 mismatch for font-bh-100dpi-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-bh-75dpi-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3486aa51ac92c646a448fe899c5c3dae0024b1fef724d5100d52640d1cac721c" || { echo "oreon: Source9 SHA256 mismatch for font-bh-75dpi-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-bh-lucidatypewriter-100dpi-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "62a83363c2536095fda49d260d21e0847675676e4e3415054064cbdffa641fbb" || { echo "oreon: Source10 SHA256 mismatch for font-bh-lucidatypewriter-100dpi-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-bh-lucidatypewriter-75dpi-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4ac16afbe205480cc5572e2977ea63488c543d05be0ea8e5a94c845a6eebcb31" || { echo "oreon: Source11 SHA256 mismatch for font-bh-lucidatypewriter-75dpi-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-bitstream-100dpi-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ebe0d7444e3d7c8da7642055ac2206f0190ee060700d99cd876f8fc9964cb6ce" || { echo "oreon: Source12 SHA256 mismatch for font-bitstream-100dpi-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-bitstream-75dpi-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ba3f5e4610c07bd5859881660753ec6d75d179f26fc967aa776dbb3d5d5cf48e" || { echo "oreon: Source13 SHA256 mismatch for font-bitstream-75dpi-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-bitstream-type1-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source14 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c6ea0569adad2c577f140328dc3302e729cb1b1ea90cd0025caf380625f8a688" || { echo "oreon: Source14 SHA256 mismatch for font-bitstream-type1-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-cronyx-cyrillic-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source15 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6e8631936157677c77ba032b5c7b1fb3cb2ee872dbcea0444f12cd602cd9212a" || { echo "oreon: Source15 SHA256 mismatch for font-cronyx-cyrillic-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-cursor-misc-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source16 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "17363eb35eece2e08144da5f060c70103b59d0972b4f4d77fd84c9a7a2dba635" || { echo "oreon: Source16 SHA256 mismatch for font-cursor-misc-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-dec-misc-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source18 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e19ddf8b5f8de914d81675358fdfe37762e9ce524887cc983adef34f2850ff7b" || { echo "oreon: Source18 SHA256 mismatch for font-dec-misc-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-isas-misc-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5824ab4b485951107dd245b8f7717d2822f1a6dbf6cea98f1ac7f49905c0a867" || { echo "oreon: Source19 SHA256 mismatch for font-isas-misc-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-jis-misc-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2b18ce10b367ebafe95a17de799b6db9a24e2337188d124adaf68af05b1fac65" || { echo "oreon: Source20 SHA256 mismatch for font-jis-misc-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-micro-misc-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9a3381c10f32d9511f0ad4179df395914c50779103c16cddf7017f5220ed8db6" || { echo "oreon: Source21 SHA256 mismatch for font-micro-misc-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-misc-cyrillic-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e40fe3e3323c62b738550795457ad555c70c008aa91b5912dfd46f8e745f5e60" || { echo "oreon: Source22 SHA256 mismatch for font-misc-cyrillic-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-misc-ethiopic-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "53cb1fd83afdbe7939c0eac34003676ee0e6023216892d98054db90b703c98a5" || { echo "oreon: Source23 SHA256 mismatch for font-misc-ethiopic-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-misc-misc-1.1.2.tar.bz2; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b8e77940e4e1769dc47ef1805918d8c9be37c708735832a07204258bacc11794" || { echo "oreon: Source24 SHA256 mismatch for font-misc-misc-1.1.2.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-mutt-misc-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bd5f7adb34367c197773a9801df5bce7b019664941900b2a31fbfe1ff2830f8f" || { echo "oreon: Source25 SHA256 mismatch for font-mutt-misc-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-schumacher-misc-1.1.2.tar.bz2; test -f "$f" || { echo "oreon: missing Source26 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e444028656e0767e2eddc6d9aca462b16a2be75a47244dbc199b2c44eca87e5a" || { echo "oreon: Source26 SHA256 mismatch for font-schumacher-misc-1.1.2.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-screen-cyrillic-1.0.4.tar.bz2; test -f "$f" || { echo "oreon: missing Source27 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "824231e8dffe15299454e47259f29d98001c9cf8ad3d6b5171399e4d71705e79" || { echo "oreon: Source27 SHA256 mismatch for font-screen-cyrillic-1.0.4.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-sony-misc-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source28 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2043a326ba347c9da5ca1e9bc363e2521c3ea40b43b1f9662d333efd4867cff5" || { echo "oreon: Source28 SHA256 mismatch for font-sony-misc-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-sun-misc-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source29 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "481f4fcbbf7005658b080b3cf342c8c76de752e77f47958b2b383de73266d2e0" || { echo "oreon: Source29 SHA256 mismatch for font-sun-misc-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-winitzki-cyrillic-1.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source30 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "abd13b63d02fcaec488686c23683e5cf640b43bd32f8ca22eeae6f84df0a36a0" || { echo "oreon: Source30 SHA256 mismatch for font-winitzki-cyrillic-1.0.3.tar.bz2" >&2; exit 1; })
%(f=%{_sourcedir}/font-xfree86-type1-1.0.4.tar.bz2; test -f "$f" || { echo "oreon: missing Source31 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "caebf42aec7be7f3bd40e0f232d6f34881b853dc84acfcdf7458358701fbe34a" || { echo "oreon: Source31 SHA256 mismatch for font-xfree86-type1-1.0.4.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31

%build
# Build all apps
{
    for app in encodings-* font-* ; do
        pushd $app
            autoreconf -vif
            case $app in
                font-adobe-100dpi-*|font-adobe-75dpi-*|font-adobe-utopia-100dpi-*|font-adobe-utopia-75dpi-*|font-bh-*)
                    %configure --with-fontrootdir=%{_x11fontdir} \
                        --disable-iso8859-3 \
                        --disable-iso8859-4 \
                        --disable-iso8859-10 \
                        --disable-iso8859-13
                    ;;
                font-misc-misc-*|font-schumacher-misc-*)
                    %configure --with-fontrootdir=%{_x11fontdir} \
                        --disable-iso8859-3 \
                        --disable-iso8859-4 \
                        --disable-iso8859-10 \
                        --disable-iso8859-11 \
                        --disable-iso8859-13 \
                        --disable-iso8859-16
                    ;;
                *)
                    %configure --with-fontrootdir=%{_x11fontdir}
                    ;;
            esac
            %make_build
        popd
    done
}


%install
# Install all apps
{
    for app in encodings-* font-* ; do
        pushd $app
            %make_install
        popd
    done
}

# Install catalogue symlinks
mkdir -p $RPM_BUILD_ROOT%{_catalogue}
for f in misc:unscaled:pri=10 75dpi:unscaled:pri=20 100dpi:unscaled:pri=30 Type1 TTF OTF cyrillic; do
    ln -fs %{_x11fontdir}/${f%%%%:*} $RPM_BUILD_ROOT%{_catalogue}/xorg-x11-fonts-$f
done

# Create fake ghost files for file manifests.
{
    # Make ghost fonts.alias, fonts.dir, encodings.dir files
    FONTDIR=$RPM_BUILD_ROOT%{_x11fontdir}
    # Create fake %%ghost fonts.alias
    for subdir in TTF OTF ; do
        touch $FONTDIR/$subdir/fonts.{alias,scale}
        chmod 0644 $FONTDIR/$subdir/fonts.{alias,scale}
    done
    # Create fake ghost encodings.dir, fonts.dir, fonts.scale, fonts.cache-*
    for subdir in Type1 TTF OTF 100dpi 75dpi cyrillic misc ; do
        rm -f $FONTDIR/$subdir/{encodings,fonts}.dir
        touch $FONTDIR/$subdir/{encodings,fonts}.dir
        chmod 0644 $FONTDIR/$subdir/{encodings,fonts}.dir
        touch $FONTDIR/$subdir/fonts.scale
        chmod 0644 $FONTDIR/$subdir/fonts.scale

        # Create bogus fonts.cache-* files
        # Create somewhat future-proofed ghosted fonts.cache-* files so that
        # the font packages own these files.
        for fcver in $(seq 1 9) ; do
            touch $FONTDIR/$subdir/fonts.cache-$fcver
            chmod 0644 $FONTDIR/$subdir/fonts.cache-$fcver
        done
    done
}

%post misc
{
# Only run fc-cache in the Type1 dir, gzipped pcf's take forever
  %font_update_dirs misc || :
}

%postun misc
{
  # Rebuild fonts.dir when uninstalling package. (exclude the local, CID dirs)
  if [ "$1" = "0" ]; then
    %font_update_dirs -u misc || :
  fi
}

%post Type1
{
  %font_update_dirs -f Type1 || :
}

%postun Type1
{
  if [ "$1" = "0" ]; then
    %font_update_dirs -u -f Type1 || :
  fi
}

%post ethiopic
{
  %font_update_dirs -t TTF || :
  %font_update_dirs -f OTF || :
}

%postun ethiopic
{
  if [ "$1" = "0" ]; then
    %font_update_dirs -u -t TTF || :
    %font_update_dirs -u -f OTF || :
  fi
}

%post 75dpi
mkfontdir %{_x11fontdir}/75dpi || :

%post 100dpi
mkfontdir %{_x11fontdir}/100dpi || :

%post ISO8859-1-75dpi
mkfontdir %{_x11fontdir}/75dpi || :

%post ISO8859-1-100dpi
mkfontdir %{_x11fontdir}/100dpi || :

%post ISO8859-2-75dpi
mkfontdir %{_x11fontdir}/75dpi || :

%post ISO8859-2-100dpi
mkfontdir %{_x11fontdir}/100dpi || :

%post ISO8859-9-75dpi
mkfontdir %{_x11fontdir}/75dpi || :

%post ISO8859-9-100dpi
mkfontdir %{_x11fontdir}/100dpi || :

%post ISO8859-14-75dpi
mkfontdir %{_x11fontdir}/75dpi || :

%post ISO8859-14-100dpi
mkfontdir %{_x11fontdir}/100dpi || :

%post ISO8859-15-75dpi
mkfontdir %{_x11fontdir}/75dpi || :

%post ISO8859-15-100dpi
mkfontdir %{_x11fontdir}/100dpi || :

%post cyrillic
mkfontdir %{_x11fontdir}/cyrillic || :

%postun 75dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/75dpi ]; then
    mkfontdir %{_x11fontdir}/75dpi || :
  fi
}

%postun 100dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/100dpi ]; then
    mkfontdir %{_x11fontdir}/100dpi || :
  fi
}

%postun ISO8859-1-75dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/75dpi ]; then
    mkfontdir %{_x11fontdir}/75dpi || :
  fi
}

%postun ISO8859-1-100dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/100dpi ]; then
    mkfontdir %{_x11fontdir}/100dpi || :
  fi
}

%postun ISO8859-2-75dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/75dpi ]; then
    mkfontdir %{_x11fontdir}/75dpi || :
  fi
}

%postun ISO8859-2-100dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/100dpi  ]; then
    mkfontdir %{_x11fontdir}/100dpi || :
  fi
}

%postun ISO8859-9-75dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/75dpi ]; then
    mkfontdir %{_x11fontdir}/75dpi || :
  fi
}

%postun ISO8859-9-100dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/100dpi  ]; then
    mkfontdir %{_x11fontdir}/100dpi || :
  fi
}

%postun ISO8859-14-75dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/75dpi ]; then
    mkfontdir %{_x11fontdir}/75dpi || :
  fi
}

%postun ISO8859-14-100dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/100dpi  ]; then
    mkfontdir %{_x11fontdir}/100dpi || :
  fi
}

%postun ISO8859-15-75dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/75dpi ]; then
    mkfontdir %{_x11fontdir}/75dpi || :
  fi
}

%postun ISO8859-15-100dpi
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/100dpi  ]; then
    mkfontdir %{_x11fontdir}/100dpi || :
  fi
}

%postun cyrillic
{
  if [ "$1" = "0" -a -d %{_x11fontdir}/cyrillic ]; then
    mkfontdir %{_x11fontdir}/cyrillic || :
  fi
}


%files misc
%{_catalogue}/xorg-x11-fonts-misc:unscaled:pri=10
%dir %{_x11fontdir}/misc
%{_x11fontdir}/misc/*
%dir %{_x11fontdir}/encodings
%dir %{_x11fontdir}/encodings/large
%{_x11fontdir}/encodings/*.enc.gz
%ghost %verify(not md5 size mtime) %{_x11fontdir}/encodings/encodings.dir
%{_x11fontdir}/encodings/large/*.enc.gz
%ghost %verify(not md5 size mtime) %{_x11fontdir}/encodings/large/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/misc/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/misc/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/misc/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/misc/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/misc/fonts.cache-*

%files ethiopic
%{_catalogue}/xorg-x11-fonts-TTF
%{_catalogue}/xorg-x11-fonts-OTF
# TTF fonts
%dir %{_x11fontdir}/TTF
# font-misc-ethiopic
%{_x11fontdir}/TTF/GohaTibebZemen.ttf
%ghost %verify(not md5 size mtime) %{_x11fontdir}/TTF/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/TTF/fonts.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/TTF/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/TTF/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/TTF/fonts.cache-*
# OTF fonts
%dir %{_x11fontdir}/OTF
%{_x11fontdir}/OTF/GohaTibebZemen.otf
%ghost %verify(not md5 size mtime) %{_x11fontdir}/OTF/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/OTF/fonts.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/OTF/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/OTF/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/OTF/fonts.cache-*

%files 75dpi
%{_catalogue}/xorg-x11-fonts-75dpi:unscaled:pri=20
%dir %{_x11fontdir}/75dpi
# font-adobe-75dpi
%{_x11fontdir}/75dpi/cour[BOR]??.pcf*
%{_x11fontdir}/75dpi/courBO??.pcf*
%{_x11fontdir}/75dpi/helv[BOR]??.pcf*
%{_x11fontdir}/75dpi/helvBO??.pcf*
%{_x11fontdir}/75dpi/ncen[BIR]??.pcf*
%{_x11fontdir}/75dpi/ncenBI??.pcf*
%{_x11fontdir}/75dpi/tim[BIR]??.pcf*
%{_x11fontdir}/75dpi/timBI??.pcf*
%{_x11fontdir}/75dpi/symb??.pcf*
# font-adobe-utopia-75dpi
%{_x11fontdir}/75dpi/UTBI__??.pcf*
%{_x11fontdir}/75dpi/UT[BI]___??.pcf*
%{_x11fontdir}/75dpi/UTRG__??.pcf*
# font-bh-75dpi
%{_x11fontdir}/75dpi/luBIS??.pcf*
%{_x11fontdir}/75dpi/lu[BIR]S??.pcf*
%{_x11fontdir}/75dpi/lub[BIR]??.pcf*
%{_x11fontdir}/75dpi/lubBI??.pcf*
# font-bh-lucidatypewriter-75dpi
%{_x11fontdir}/75dpi/lut[BR]S??.pcf*
# font-bitstream-75dpi
%{_x11fontdir}/75dpi/char[BIR]??.pcf*
%{_x11fontdir}/75dpi/charBI??.pcf*
%{_x11fontdir}/75dpi/tech14.pcf*
%{_x11fontdir}/75dpi/techB14.pcf*
%{_x11fontdir}/75dpi/term14.pcf*
%{_x11fontdir}/75dpi/termB14.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.cache-*

%files 100dpi
%{_catalogue}/xorg-x11-fonts-100dpi:unscaled:pri=30
%dir %{_x11fontdir}/100dpi
# font-adobe-100dpi
%{_x11fontdir}/100dpi/cour[BOR]??.pcf*
%{_x11fontdir}/100dpi/courBO??.pcf*
%{_x11fontdir}/100dpi/helv[BOR]??.pcf*
%{_x11fontdir}/100dpi/helvBO??.pcf*
%{_x11fontdir}/100dpi/ncen[BIR]??.pcf*
%{_x11fontdir}/100dpi/ncenBI??.pcf*
%{_x11fontdir}/100dpi/tim[BIR]??.pcf*
%{_x11fontdir}/100dpi/timBI??.pcf*
%{_x11fontdir}/100dpi/symb??.pcf*
# font-adobe-utopia-100dpi
%{_x11fontdir}/100dpi/UTBI__??.pcf*
%{_x11fontdir}/100dpi/UT[BI]___??.pcf*
%{_x11fontdir}/100dpi/UTRG__??.pcf*
# font-bh-100dpi
%{_x11fontdir}/100dpi/luBIS??.pcf*
%{_x11fontdir}/100dpi/lu[BIR]S??.pcf*
%{_x11fontdir}/100dpi/lub[BIR]??.pcf*
%{_x11fontdir}/100dpi/lubBI??.pcf*
# font-bh-lucidatypewriter-100dpi
%{_x11fontdir}/100dpi/lut[BR]S??.pcf*
# font-bitstream-100dpi
%{_x11fontdir}/100dpi/char[BIR]??.pcf*
%{_x11fontdir}/100dpi/charBI??.pcf*
%{_x11fontdir}/100dpi/tech14.pcf*
%{_x11fontdir}/100dpi/techB14.pcf*
%{_x11fontdir}/100dpi/term14.pcf*
%{_x11fontdir}/100dpi/termB14.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.cache-*

%files ISO8859-1-75dpi
%{_catalogue}/xorg-x11-fonts-75dpi:unscaled:pri=20
%dir %{_x11fontdir}/75dpi
# font-adobe-75dpi
%{_x11fontdir}/75dpi/cour[BOR]??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/courBO??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/helv[BOR]??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/helvBO??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/ncen[BIR]??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/ncenBI??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/tim[BIR]??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/timBI??-ISO8859-1.pcf*
# font-adobe-utopia-75dpi
%{_x11fontdir}/75dpi/UTBI__??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/UT[BI]___??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/UTRG__??-ISO8859-1.pcf*
# font-bh-75dpi
%{_x11fontdir}/75dpi/luBIS??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/lu[BIR]S??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/lub[BIR]??-ISO8859-1.pcf*
%{_x11fontdir}/75dpi/lubBI??-ISO8859-1.pcf*
# font-bh-lucidatypewriter-75dpi
%{_x11fontdir}/75dpi/lut[BR]S??-ISO8859-1.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.cache-*

%files ISO8859-1-100dpi
%{_catalogue}/xorg-x11-fonts-100dpi:unscaled:pri=30
%dir %{_x11fontdir}/100dpi
# font-adobe-100dpi
%{_x11fontdir}/100dpi/cour[BOR]??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/courBO??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/helv[BOR]??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/helvBO??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/ncen[BIR]??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/ncenBI??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/tim[BIR]??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/timBI??-ISO8859-1.pcf*
# font-adobe-utopia-100dpi
%{_x11fontdir}/100dpi/UTBI__??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/UT[BI]___??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/UTRG__??-ISO8859-1.pcf*
# font-bh-100dpi
%{_x11fontdir}/100dpi/luBIS??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/lu[BIR]S??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/lub[BIR]??-ISO8859-1.pcf*
%{_x11fontdir}/100dpi/lubBI??-ISO8859-1.pcf*
# font-bh-lucidatypewriter-100dpi
%{_x11fontdir}/100dpi/lut[BR]S??-ISO8859-1.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.cache-*

%files ISO8859-2-75dpi
%{_catalogue}/xorg-x11-fonts-75dpi:unscaled:pri=20
%dir %{_x11fontdir}/75dpi
# font-adobe-75dpi
%{_x11fontdir}/75dpi/cour[BOR]??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/courBO??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/helv[BOR]??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/helvBO??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/ncen[BIR]??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/ncenBI??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/tim[BIR]??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/timBI??-ISO8859-2.pcf*
# font-adobe-utopia-75dpi
%{_x11fontdir}/75dpi/UTBI__??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/UT[BI]___??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/UTRG__??-ISO8859-2.pcf*
# font-bh-75dpi
%{_x11fontdir}/75dpi/luBIS??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/lu[BIR]S??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/lub[BIR]??-ISO8859-2.pcf*
%{_x11fontdir}/75dpi/lubBI??-ISO8859-2.pcf*
# font-bh-lucidatypewriter-75dpi
%{_x11fontdir}/75dpi/lut[BR]S??-ISO8859-2.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.cache-*

%files ISO8859-2-100dpi
%{_catalogue}/xorg-x11-fonts-100dpi:unscaled:pri=30
%dir %{_x11fontdir}/100dpi
# font-adobe-100dpi
%{_x11fontdir}/100dpi/cour[BOR]??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/courBO??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/helv[BOR]??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/helvBO??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/ncen[BIR]??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/ncenBI??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/tim[BIR]??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/timBI??-ISO8859-2.pcf*
# font-adobe-utopia-100dpi
%{_x11fontdir}/100dpi/UTBI__??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/UT[BI]___??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/UTRG__??-ISO8859-2.pcf*
# font-bh-100dpi
%{_x11fontdir}/100dpi/luBIS??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/lu[BIR]S??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/lub[BIR]??-ISO8859-2.pcf*
%{_x11fontdir}/100dpi/lubBI??-ISO8859-2.pcf*
# font-bh-lucidatypewriter-100dpi
%{_x11fontdir}/100dpi/lut[BR]S??-ISO8859-2.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.cache-*

%files ISO8859-9-75dpi
%{_catalogue}/xorg-x11-fonts-75dpi:unscaled:pri=20
%dir %{_x11fontdir}/75dpi
# font-adobe-75dpi
%{_x11fontdir}/75dpi/cour[BOR]??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/courBO??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/helv[BOR]??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/helvBO??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/ncen[BIR]??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/ncenBI??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/tim[BIR]??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/timBI??-ISO8859-9.pcf*
# font-adobe-utopia-75dpi
%{_x11fontdir}/75dpi/UTBI__??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/UT[BI]___??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/UTRG__??-ISO8859-9.pcf*
# font-bh-75dpi
%{_x11fontdir}/75dpi/luBIS??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/lu[BIR]S??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/lub[BIR]??-ISO8859-9.pcf*
%{_x11fontdir}/75dpi/lubBI??-ISO8859-9.pcf*
# font-bh-lucidatypewriter-75dpi
%{_x11fontdir}/75dpi/lut[BR]S??-ISO8859-9.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.cache-*

%files ISO8859-9-100dpi
%{_catalogue}/xorg-x11-fonts-100dpi:unscaled:pri=30
%dir %{_x11fontdir}/100dpi
# font-adobe-100dpi
%{_x11fontdir}/100dpi/cour[BOR]??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/courBO??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/helv[BOR]??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/helvBO??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/ncen[BIR]??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/ncenBI??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/tim[BIR]??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/timBI??-ISO8859-9.pcf*
# font-adobe-utopia-100dpi
%{_x11fontdir}/100dpi/UTBI__??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/UT[BI]___??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/UTRG__??-ISO8859-9.pcf*
# font-bh-100dpi
%{_x11fontdir}/100dpi/luBIS??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/lu[BIR]S??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/lub[BIR]??-ISO8859-9.pcf*
%{_x11fontdir}/100dpi/lubBI??-ISO8859-9.pcf*
# font-bh-lucidatypewriter-100dpi
%{_x11fontdir}/100dpi/lut[BR]S??-ISO8859-9.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.cache-*

%files ISO8859-14-75dpi
%{_catalogue}/xorg-x11-fonts-75dpi:unscaled:pri=20
%dir %{_x11fontdir}/75dpi
# font-adobe-75dpi
%{_x11fontdir}/75dpi/cour[BOR]??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/courBO??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/helv[BOR]??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/helvBO??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/ncen[BIR]??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/ncenBI??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/tim[BIR]??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/timBI??-ISO8859-14.pcf*
# font-adobe-utopia-75dpi
%{_x11fontdir}/75dpi/UTBI__??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/UT[BI]___??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/UTRG__??-ISO8859-14.pcf*
# font-bh-75dpi
%{_x11fontdir}/75dpi/luBIS??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/lu[BIR]S??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/lub[BIR]??-ISO8859-14.pcf*
%{_x11fontdir}/75dpi/lubBI??-ISO8859-14.pcf*
# font-bh-lucidatypewriter-75dpi
%{_x11fontdir}/75dpi/lut[BR]S??-ISO8859-14.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.cache-*

%files ISO8859-14-100dpi
%{_catalogue}/xorg-x11-fonts-100dpi:unscaled:pri=30
%dir %{_x11fontdir}/100dpi
# font-adobe-100dpi
%{_x11fontdir}/100dpi/cour[BOR]??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/courBO??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/helv[BOR]??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/helvBO??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/ncen[BIR]??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/ncenBI??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/tim[BIR]??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/timBI??-ISO8859-14.pcf*
# font-adobe-utopia-100dpi
%{_x11fontdir}/100dpi/UTBI__??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/UT[BI]___??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/UTRG__??-ISO8859-14.pcf*
# font-bh-100dpi
%{_x11fontdir}/100dpi/luBIS??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/lu[BIR]S??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/lub[BIR]??-ISO8859-14.pcf*
%{_x11fontdir}/100dpi/lubBI??-ISO8859-14.pcf*
# font-bh-lucidatypewriter-100dpi
%{_x11fontdir}/100dpi/lut[BR]S??-ISO8859-14.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.cache-*

%files ISO8859-15-75dpi
%{_catalogue}/xorg-x11-fonts-75dpi:unscaled:pri=20
%dir %{_x11fontdir}/75dpi
# font-adobe-75dpi
%{_x11fontdir}/75dpi/cour[BOR]??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/courBO??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/helv[BOR]??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/helvBO??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/ncen[BIR]??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/ncenBI??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/tim[BIR]??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/timBI??-ISO8859-15.pcf*
# font-adobe-utopia-75dpi
%{_x11fontdir}/75dpi/UTBI__??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/UT[BI]___??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/UTRG__??-ISO8859-15.pcf*
# font-bh-75dpi
%{_x11fontdir}/75dpi/luBIS??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/lu[BIR]S??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/lub[BIR]??-ISO8859-15.pcf*
%{_x11fontdir}/75dpi/lubBI??-ISO8859-15.pcf*
# font-bh-lucidatypewriter-75dpi
%{_x11fontdir}/75dpi/lut[BR]S??-ISO8859-15.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/75dpi/fonts.cache-*

%files ISO8859-15-100dpi
%{_catalogue}/xorg-x11-fonts-100dpi:unscaled:pri=30
%dir %{_x11fontdir}/100dpi
# font-adobe-100dpi
%{_x11fontdir}/100dpi/cour[BOR]??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/courBO??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/helv[BOR]??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/helvBO??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/ncen[BIR]??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/ncenBI??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/tim[BIR]??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/timBI??-ISO8859-15.pcf*
# font-adobe-utopia-100dpi
%{_x11fontdir}/100dpi/UTBI__??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/UT[BI]___??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/UTRG__??-ISO8859-15.pcf*
# font-bh-100dpi
%{_x11fontdir}/100dpi/luBIS??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/lu[BIR]S??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/lub[BIR]??-ISO8859-15.pcf*
%{_x11fontdir}/100dpi/lubBI??-ISO8859-15.pcf*
# font-bh-lucidatypewriter-100dpi
%{_x11fontdir}/100dpi/lut[BR]S??-ISO8859-15.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/100dpi/fonts.cache-*

%files Type1
%{_catalogue}/xorg-x11-fonts-Type1
%dir %{_x11fontdir}/Type1
# font-adobe-utopia-type1
%{_x11fontdir}/Type1/UT??____.[ap]f[ma]
# font-bitstream-type1
%{_x11fontdir}/Type1/c0???bt_.[ap]f[mb]
# font-ibm-type1
# Pulled for licensing reasons (see bz 317641)
# %%{_x11fontdir}/Type1/cour*.afm
# %%{_x11fontdir}/Type1/cour*.pfa
#font-xfree86-type1
%{_x11fontdir}/Type1/cursor.pfa
%ghost %verify(not md5 size mtime) %{_x11fontdir}/Type1/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/Type1/fonts.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/Type1/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/Type1/fonts.cache-*

%files cyrillic
%{_catalogue}/xorg-x11-fonts-cyrillic
%dir %{_x11fontdir}/cyrillic
# font-cronyx-cyrillic
%{_x11fontdir}/cyrillic/crox[1-6]*.pcf*
%{_x11fontdir}/cyrillic/koi10x16b.pcf*
%{_x11fontdir}/cyrillic/koi10x20.pcf*
%{_x11fontdir}/cyrillic/koi6x10.pcf*
%{_x11fontdir}/cyrillic/koinil2.pcf*
# font-misc-cyrillic
%{_x11fontdir}/cyrillic/koi12x24*.pcf*
%{_x11fontdir}/cyrillic/koi6x13.pcf*
%{_x11fontdir}/cyrillic/koi6x13b.pcf*
%{_x11fontdir}/cyrillic/koi6x9.pcf*
%{_x11fontdir}/cyrillic/koi[5789]x*.pcf*
# font-screen-cyrillic
%{_x11fontdir}/cyrillic/screen8x16*.pcf*
# font-winitzki-cyrillic
%{_x11fontdir}/cyrillic/proof9x16.pcf*
%ghost %verify(not md5 size mtime) %{_x11fontdir}/cyrillic/encodings.dir
%ghost %verify(not md5 size mtime) %{_x11fontdir}/cyrillic/fonts.dir
# NOTE: Xorg supplies this fonts.alias, so it is not ghosted
%verify(not md5 size mtime) %{_x11fontdir}/cyrillic/fonts.alias
%ghost %verify(not md5 size mtime) %{_x11fontdir}/cyrillic/fonts.scale
%ghost %verify(not md5 size mtime) %{_x11fontdir}/cyrillic/fonts.cache-*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.5-42
- Prepare for Oreon 11 (RP1)
