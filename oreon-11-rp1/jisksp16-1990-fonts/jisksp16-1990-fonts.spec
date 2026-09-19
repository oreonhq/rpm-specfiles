%global source0_hash none

%global	fontname	jisksp16-1990
%global	catalogue	%{_sysconfdir}/X11/fontpath.d

Name:		%{fontname}-fonts
Version:	0.983
Release:	36%{?dist}
Summary:	16x16 JIS X 0212:1990 Bitmap font
License:	LicenseRef-Fedora-Public-Domain

URL:		http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/
Source0:	http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/jisksp16-1990.bdf.Z

BuildArch:	noarch
BuildRequires:	gzip mkfontdir fontpackages-devel

Requires:	fontpackages-filesystem

%description
This package provides 16x16 Japanese bitmap font for JIS X 0212:1990.
JIS X 0212:1990 is a character sets that contains the auxiliary kanji
characters.

%prep
%setup -c -T
gunzip -c %{SOURCE0} > jisksp16-1990.bdf

%build
%{_bindir}/bdftopcf jisksp16-1990.bdf | gzip -9c > jisksp16-1990.pcf.gz

%install
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0755 -d $RPM_BUILD_ROOT%{catalogue}

install -m 0644 -p jisksp16-1990.pcf.gz $RPM_BUILD_ROOT%{_fontdir}/

%{_bindir}/mkfontdir $RPM_BUILD_ROOT%{_fontdir}

# Install catalogue symlink
ln -sf %{_fontdir} $RPM_BUILD_ROOT%{catalogue}/%{name}

%_font_pkg jisksp16-1990.pcf.gz

%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%{catalogue}/*

%changelog
%autochangelog
