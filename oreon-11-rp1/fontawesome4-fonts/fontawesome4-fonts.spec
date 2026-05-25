%global fontname fontawesome4
%global fontconf 60-fontawesome.conf
%global _fontdir %{_fontbasedir}/fontawesome

Name:		fontawesome4-fonts
Epoch:		1
Version:	4.7.0
Release:	26%{?dist}

Summary:	Iconic font set
License:	OFL-1.1-RFN
URL:		http://fontawesome.io
Source0:	http://fontawesome.io/assets/font-awesome-%{version}.zip
Source1:	%{name}-fontconfig.conf
Source2:	README-Trademarks.txt
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	ttembed
Requires:	fontpackages-filesystem

# This can be removed when F42 reaches EOL
Obsoletes:      fontawesome-fonts < 1:4.7.0-16
Provides:       fontawesome-fonts = 1:%{version}-%{release}

%description
Font Awesome gives you scalable vector icons that can instantly be customized
— size, color, drop shadow, and anything that can be done with the power of
CSS.

This package contains OpenType and TrueType font files which are typically
used locally.

%package web
License:	OFL-1.1-RFN AND MIT
Requires:	%{fontname}-fonts = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:	Iconic font set, web files

%description web
Font Awesome gives you scalable vector icons that can instantly be customized
— size, color, drop shadow, and anything that can be done with the power of
CSS.

This package contains CSS, SCSS and LESS style files as well as Web Open Font
Format versions 1 and 2, Embedded OpenType and SVG font files which are
typically used on the web.

%prep
%autosetup -n font-awesome-%{version}
cp -p %SOURCE2 .

%build
ttembed fonts/*.ttf fonts/*.otf

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/*.ttf fonts/*.otf fonts/*.woff fonts/*.svg \
		fonts/*.woff2 fonts/*.eot %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

mkdir -p %{buildroot}%{_datadir}/font-awesome-web/
cp -a css less scss %{buildroot}%{_datadir}/font-awesome-web/

# files:
%_font_pkg -f %{fontconf} *.ttf *.otf
%exclude %{_fontdir}/fontawesome-webfont.svg
%exclude %{_fontdir}/fontawesome-webfont.woff
%exclude %{_fontdir}/fontawesome-webfont.woff2
%exclude %{_fontdir}/fontawesome-webfont.eot

%doc README-Trademarks.txt

%files web
%{_datadir}/font-awesome-web/
%{_fontdir}/fontawesome-webfont.svg
%{_fontdir}/fontawesome-webfont.woff
%{_fontdir}/fontawesome-webfont.woff2
%{_fontdir}/fontawesome-webfont.eot

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:4.7.0-26
- Import
