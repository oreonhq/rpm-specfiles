%global source0_hash ab7f724d7fa719b14dc0d038539eed6931b2b8b646f4e05c2140a018c6052279

%global		priority	69
%global		fontname	knm-new-fixed
%global		fontconf	%{priority}-%{fontname}.conf
%global		catalogue	%{_sysconfdir}/X11/fontpath.d

Name:		%{fontname}-fonts
Version:	1.1
Release:	44%{?dist}

Summary:	12x12 JIS X 0208 Bitmap fonts
License:	GPL-1.0-or-later

## the following upstream URL is a dead link anymore.
#URL:		http://www.din.or.jp/~storm/fonts/
#Source0:	http://www.din.or.jp/~storm/fonts/knm_new.tar.gz
Source0:	knm_new.tar.gz
Source1:	%{name}-fontconfig.conf
BuildArch:	noarch
BuildRequires:	mkfontdir fontpackages-devel

Requires:	fontpackages-filesystem

%description
This package provides 12x12 Japanese bitmap fonts for JIS X 0208.
The JIS X 0208 character set contains the most often used Kanji glyphs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -T -c -a 0

%build

%install
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0755 -d $RPM_BUILD_ROOT%{catalogue}

install -m 0644 -p fonts/*.pcf.gz $RPM_BUILD_ROOT%{_fontdir}/

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir}	\
			$RPM_BUILD_ROOT%{_fontconfig_confdir}
install -m 0644 -p	%{SOURCE1}	\
			$RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}

ln -s	%{_fontconfig_templatedir}/%{fontconf}	\
	$RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

mkfontdir $RPM_BUILD_ROOT%{_fontdir}

# Install catalogue symlink
ln -s -f %{_fontdir} $RPM_BUILD_ROOT%{catalogue}/%{fontname}

%_font_pkg -f %{fontconf} *.pcf.gz

%lang(ja) %doc fonts/readme fonts/changes
%doc fonts/gtkrc.sample
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%{catalogue}/*

%changelog
%autochangelog
