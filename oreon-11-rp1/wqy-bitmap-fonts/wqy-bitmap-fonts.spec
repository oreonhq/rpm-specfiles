%global source0_hash af655fedfb490aabbb8ce73602a08a6a847fafc78dc363ff3901aa6c3384ca5d

%define fontname  wqy-bitmap
%define fontconf  61-wqy-bitmapsong.conf
%define wqyroot   wqy-bitmapsong

Name:           %{fontname}-fonts
Version:        1.0.0
Release:        0.31.rc1%{?dist}
Summary:        WenQuanYi Bitmap Chinese Fonts

# Automatically converted from old format: GPLv2 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            http://wenq.org/enindex.cgi
Source0:        http://downloads.sourceforge.net/wqy/wqy-bitmapsong-bdf-1.0.0-RC1.tar.gz
Source1:        61-wqy-bitmapsong.conf

BuildArch:      noarch
BuildRequires: make
BuildRequires:  fontpackages-devel, bdftopcf, perl
Requires:       fontpackages-filesystem

%description
WenQuanYi bitmap fonts include all 20,932 Unicode 5.2
CJK Unified Ideographs (U4E00 - U9FA5) and 6,582
CJK Extension A characters (U3400 - U4DB5) at
5 different pixel sizes (9pt-12X12, 10pt-13X13,
10.5pt-14x14, 11pt-15X15 and 12pt-16x16 pixel).
Use of this bitmap font for on-screen display of Chinese
(traditional and simplified) in web pages and elsewhere
eliminates the annoying "blurring" problems caused by
insufficient "hinting" of anti-aliased vector CJK fonts.
In addition, Latin characters, Japanese Kanas and
Korean Hangul glyphs (U+AC00~U+D7A3) are also included.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{wqyroot}
sed -i 's/shift(ARGV)/shift(@ARGV)/g' bdfmerge.pl

%build
make wqyv1

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.pcf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.pcf
%doc AUTHORS ChangeLog COPYING README LOGO.png

%changelog
%autochangelog
