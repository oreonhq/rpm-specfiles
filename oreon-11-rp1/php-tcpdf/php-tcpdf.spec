%global source0_hash 5f205ba455dcdb4d2234a2f009c21c2757c8cb7bcf5be0e7e13fa097064328b1
%global gh_commit    e1e2ade18e574e963473f53271591edd8c0033ec
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     tecnickcom
%global gh_date      2026-03-03
%global gh_project   TCPDF
%global real_name    tcpdf
Name:           php-tcpdf
Summary:        PHP class for generating PDF documents and barcodes
Version:        7.0.10
Release:        1%{?dist}
URL:            http://www.tcpdf.org
License:        LGPL-3.0-or-later
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        %{name}.blacklist
Source2:        _blank.png
BuildArch:      noarch
Requires:       php(language) >= 7.1
Requires:       php-curl
Requires:       php-bcmath
Requires:       php-gd
Requires:       php-json
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-posix
Requires:       php-tidy
Requires:       php-xml
Requires:       php-zlib
Recommends:     php-imagick
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(tecnick.com/tcpdf) = %{version}
Provides:       php-composer(tecnickcom/tcpdf)  = %{version}
# oreon:deps
BuildRequires:  dejavu-lgc-sans-fonts
BuildRequires:  dejavu-lgc-sans-mono-fonts
BuildRequires:  dejavu-lgc-serif-fonts
BuildRequires:  dejavu-sans-fonts
BuildRequires:  dejavu-sans-mono-fonts
BuildRequires:  dejavu-serif-fonts
BuildRequires:  gnu-free-mono-fonts
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
%description
PHP class for generating PDF documents.

* no external libraries are required for the basic functions;
* all standard page formats, custom page formats, custom margins and units
  of measure;
* UTF-8 Unicode and Right-To-Left languages;
* TrueTypeUnicode, OpenTypeUnicode, TrueType, OpenType, Type1 and CID-0 fonts;
* font subsetting;
* methods to publish some XHTML + CSS code, Javascript and Forms;
* images, graphic (geometric figures) and transformation methods;
* supports JPEG, PNG and SVG images natively, all images supported by GD
  (GD, GD2, GD2PART, GIF, JPEG, PNG, BMP, XBM, XPM) and all images supported
  via ImagMagick (http: www.imagemagick.org/www/formats.html)
* 1D and 2D barcodes: CODE 39, ANSI MH10.8M-1983, USD-3, 3 of 9, CODE 93,
  USS-93, Standard 2 of 5, Interleaved 2 of 5, CODE 128 A/B/C, 2 and 5 Digits
  UPC-Based Extention, EAN 8, EAN 13, UPC-A, UPC-E, MSI, POSTNET, PLANET,
  RMS4CC (Royal Mail 4-state Customer Code), CBC (Customer Bar Code),
  KIX (Klant index - Customer index), Intelligent Mail Barcode, Onecode,
  USPS-B-3200, CODABAR, CODE 11, PHARMACODE, PHARMACODE TWO-TRACKS,
  Datamatrix ECC200, QR-Code, PDF417;
* ICC Color Profiles, Grayscale, RGB, CMYK, Spot Colors and Transparencies;
* automatic page header and footer management;
* document encryption up to 256 bit and digital signature certifications;
* transactions to UNDO commands;
* PDF annotations, including links, text and file attachments;
* text rendering modes (fill, stroke and clipping);
* multiple columns mode;
* no-write page regions;
* bookmarks and table of content;
* text hyphenation;
* text stretching and spacing (tracking/kerning);
* automatic page break, line break and text alignments including justification;
* automatic page numbering and page groups;
* move and delete pages;
* page compression (requires php-zlib extension);
* XOBject templates;
* PDF/A-1b (ISO 19005-1:2005) support.

By default, TCPDF uses the GD library which is know as slower than ImageMagick
solution. You can optionally install php-pecl-imagick; TCPDF will use it.

%package dejavu-lgc-sans
Summary:        DejaVu LGC sans-serif fonts for tcpdf
BuildRequires:  dejavu-lgc-sans-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-lgc-sans-fonts
Obsoletes:      %{name}-dejavu-lgc-sans-fonts < 6.11
Provides:       %{name}-dejavu-lgc-sans-fonts = %{version}
%description dejavu-lgc-sans
This package allow to use system DejaVu LGC sans-serif variable-width
font faces in TCPDF.

%package dejavu-lgc-sans-mono
Summary:        DejaVu LGC mono-spaced fonts for tcpdf
BuildRequires:  dejavu-lgc-sans-mono-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-lgc-sans-mono-fonts
Obsoletes:      %{name}-dejavu-lgc-sans-mono-fonts < 6.11
Provides:       %{name}-dejavu-lgc-sans-mono-fonts = %{version}
%description dejavu-lgc-sans-mono
This package allow to use system DejaVu LGC sans-serif mono-spaced
font faces in TCPDF.

%package dejavu-lgc-serif
Summary:        DejaVu LGC serif fonts for tcpdf
BuildRequires:  dejavu-lgc-serif-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-lgc-serif-fonts
Obsoletes:      %{name}-dejavu-lgc-serif-fonts < 6.11
Provides:       %{name}-dejavu-lgc-serif-fonts = %{version}
%description dejavu-lgc-serif
This package allow to use system DejaVu LGC serif variable-width
font faces in TCPDF.

%package dejavu-sans
Summary:        DejaVu sans-serif fonts for tcpdf
BuildRequires:  dejavu-sans-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-sans-fonts
Obsoletes:      %{name}-dejavu-sans-fonts < 6.11
Provides:       %{name}-dejavu-sans-fonts = %{version}
%description dejavu-sans
This package allow to use system DejaVu sans-serif variable-width
font faces in TCPDF.

%package dejavu-sans-mono
Summary:        DejaVu mono-spaced fonts for tcpdf
BuildRequires:  dejavu-sans-mono-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-sans-mono-fonts
Obsoletes:      %{name}-dejavu-sans-mono-fonts < 6.11
Provides:       %{name}-dejavu-sans-mono-fonts = %{version}
%description dejavu-sans-mono
This package allow to use system DejaVu sans-serif mono-spaced
font faces in TCPDF.

%package dejavu-serif
Summary:        DejaVu serif fonts for tcpdf
BuildRequires:  dejavu-serif-fonts
Requires:       %{name} = %{version}-%{release}
Requires:       dejavu-serif-fonts
Obsoletes:      %{name}-dejavu-serif-fonts < 6.11
Provides:       %{name}-dejavu-serif-fonts = %{version}
%description dejavu-serif
This package allow to use system DejaVu serif variable-width
font faces in TCPDF.

%package gnu-free-mono
Summary:        GNU FreeFonts mono-spaced for tcpdf
BuildRequires:  gnu-free-mono-fonts
Requires:       gnu-free-mono-fonts
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-gnu-free-mono-fonts < 6.11
Provides:       %{name}-gnu-free-mono-fonts = %{version}
%description gnu-free-mono
This package allow to use system GNU FreeFonts mono-spaced font faces in TCPDF.

%package gnu-free-sans
Summary:        GNU FreeFonts sans-serif for tcpdf
BuildRequires:  gnu-free-sans-fonts
Requires:       gnu-free-sans-fonts
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-gnu-free-sans-fonts < 6.11
Provides:       %{name}-gnu-free-sans-fonts = %{version}
%description gnu-free-sans
This package allow to use system GNU FreeFont sans-serif font faces in TCPDF.

%package gnu-free-serif
Summary:        GNU FreeFonts serif for tcpdf
BuildRequires:  gnu-free-serif-fonts
Requires:       gnu-free-serif-fonts
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-gnu-free-serif-fonts < 6.11
Provides:       %{name}-gnu-free-serif-fonts = %{version}
%description gnu-free-serif
This package allow to use system GNU FreeFont serif font faces in TCPDF.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

#: Fix version
#sed -e '/tcpdf_version/s/6.6.0/%{version}/' -i include/tcpdf_static.php

: Check version
grep tcpdf_version include/tcpdf_static.php | grep %{version}

: remove bundled fonts
rm -rf fonts/dejavu-fonts-ttf* fonts/freefont-* fonts/ae_fonts_*
for fic in fonts/*.z
do
  rm -f $fic ${fic/.z/.php}
done
ls fonts | sed -e 's|^|%{_datadir}/php/%{real_name}/fonts/|' >corefonts.lst

%build

: empty build section, nothing required
%install
: Library
install -d     %{buildroot}%{_datadir}/php/%{real_name}
cp -a *.php    %{buildroot}%{_datadir}/php/%{real_name}/
cp -a include  %{buildroot}%{_datadir}/php/%{real_name}/
cp -a fonts    %{buildroot}%{_datadir}/php/%{real_name}/
install -d     %{buildroot}%{_datadir}/php/%{real_name}/images
install -m 0644 %{SOURCE2} \
               %{buildroot}%{_datadir}/php/%{real_name}/images/
: Autoloader
php -d memory_limit=2G\
  %{_bindir}/phpab \
    --template fedora \
    --output %{buildroot}%{_datadir}/php/%{real_name}/autoload.php \
    %{buildroot}%{_datadir}/php/%{real_name}
: Configuration
install -d     %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 config/*.php \
               %{buildroot}%{_sysconfdir}/%{name}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/php.d/opcache-%{name}.blacklist
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/php-zts.d/opcache-%{name}.blacklist
: Tools
install -d %{buildroot}%{_bindir}
install -m 0755 tools/%{real_name}_addfont.php \
           %{buildroot}%{_bindir}/%{real_name}_addfont
for ttf in \
    /usr/share/fonts/dejav*/*ttf \
    /usr/share/fonts/gnu-free/*ttf \
; do php -d memory_limit=1G tools/tcpdf_addfont.php \
    --addcbbox \
    --flags 32 \
    --fonts $ttf \
    --link \
    --outpath %{buildroot}%{_datadir}/php/%{real_name}/fonts/
done
ls %{buildroot}%{_datadir}/php/%{real_name}/fonts/dejavuserif* |
    sed -e 's:^%{buildroot}::' | tee dejavu-serif.lst
if [ -f %{buildroot}%{_datadir}/php/%{real_name}/fonts/dejavumathtexgyre ]; then
 ls %{buildroot}%{_datadir}/php/%{real_name}/fonts/dejavumathtexgyre* |
    sed -e 's:^%{buildroot}::' | tee -a dejavu-serif.lst
fi
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

php -r 'require "%{buildroot}%{_datadir}/php/%{real_name}/autoload.php";
  printf("%{name} version %s\n", $ver=TCPDF_STATIC::getTCPDFVersion());
  exit ($ver === "%{version}" ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list
%files -n php-tcpdf-dejavu-lgc-sans -f %{oreon_filedir}/php-tcpdf-dejavu-lgc-sans.list
%files -n php-tcpdf-dejavu-lgc-sans-mono -f %{oreon_filedir}/php-tcpdf-dejavu-lgc-sans-mono.list
%files -n php-tcpdf-dejavu-lgc-serif -f %{oreon_filedir}/php-tcpdf-dejavu-lgc-serif.list
%files -n php-tcpdf-dejavu-sans -f %{oreon_filedir}/php-tcpdf-dejavu-sans.list
%files -n php-tcpdf-dejavu-sans-mono -f %{oreon_filedir}/php-tcpdf-dejavu-sans-mono.list
%files -n php-tcpdf-dejavu-serif -f %{oreon_filedir}/php-tcpdf-dejavu-serif.list
%files -n php-tcpdf-gnu-free-mono -f %{oreon_filedir}/php-tcpdf-gnu-free-mono.list
%files -n php-tcpdf-gnu-free-sans -f %{oreon_filedir}/php-tcpdf-gnu-free-sans.list
%files -n php-tcpdf-gnu-free-serif -f %{oreon_filedir}/php-tcpdf-gnu-free-serif.list

%changelog

%autochangelog
