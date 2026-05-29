%global source0_hash fdebdf3f1b8641a4b665c61f1f48e482b140a817ce619113559201b8a1fcdd51

Name:		fontawesome-fonts
Summary:	Support files for the FontAwesome fonts
Epoch:		1
Version:	6.7.2
Release:	%autorelease

License:	MIT
URL:		https://fontawesome.com/
VCS:		git:https://github.com/FortAwesome/Font-Awesome.git
BuildArch:	noarch

%global _desc %{expand:
Font Awesome gives you scalable vector icons that can instantly be
customized - size, color, drop shadow, and anything that can be done
with the power of CSS.}

%global fontlicense	OFL-1.1-RFN
%global fontlicenses	LICENSE.txt
%global fontdocs	CHANGELOG.md README.md UPGRADING.md
%global fontorg		com.fontawesome

%global fontfamily1	FontAwesome 6 Free
%global fontsummary1	Iconic font set
%global fonts1		otfs/*Free*
%global fontconfs1	%{SOURCE3}
%global fontpkgheader1	%{expand:
# This can be removed when F42 reaches EOL
Obsoletes:	fontawesome5-free-fonts < 5.15.4-5
Provides:	fontawesome5-free-fonts = %{version}-%{release}
}
%global fontdescription1 %{expand:%_desc

The FontAwesome Free Fonts contain large numbers of icons packaged as
font files.}

%global fontfamily2	FontAwesome 6 Brands Regular
%global fontsummary2	Iconic font set
%global fonts2		otfs/*Brands*
%global fontconfs2	%{SOURCE4}
%global fontpkgheader2	%{expand:
# This can be removed when F42 reaches EOL
Obsoletes:	fontawesome5-brands-fonts < 5.15.4-5
Provides:	fontawesome5-brands-fonts = %{version}-%{release}
}
%global fontdescription2 %{expand:%_desc

The FontAwesome Brand Fonts contain brand logos packaged as font files.}

Source0:        https://github.com/FortAwesome/Font-Awesome/archive/%{version}/Font-Awesome-%{version}.tar.gz
# Script to generate Source2
Source1:	trademarks.py
Source2:	README-Trademarks.txt
Source3:	60-%{fontpkgname1}.conf
Source4:	60-%{fontpkgname2}.conf

# Not for upstream.  This patch modifies the CSS to point to local OpenType
# font files, rather than to the eot, svg, ttf, woff, and woff2 web fonts, as
# required by Fedora's font packaging guidelines.
Patch:          %{name}-opentype-css.patch

%description %_desc

%fontpkg -a

# NOTE: We would like to do this here:
#%%fontmetapkg -d %%_desc
# However, the fontmetapkg macro has no facility for adding Obsoletes and
# Provides, so we expand it by hand.
%package all
Summary:	Metapackage that requires all Font Awesome fonts
Requires:	fontawesome-6-brands-fonts = 1:%{version}-%{release}
Requires:	fontawesome-6-free-fonts = 1:%{version}-%{release}

# This can be removed when F42 reaches EOL
Obsoletes:	fontawesome5-fonts-all < 5.15.4-5
Provides:	fontawesome5-fonts-all = %{version}-%{release}

%description all %_desc

This package is a metapackage that ensures all Font Awesome fonts are
installed.

%package web
License:	CC-BY-4.0
Summary:	Iconic font set, JavaScript and SVG files

# This can be removed when F42 reaches EOL
Obsoletes:	fontawesome5-fonts < 5.15.4-5
Provides:	fontawesome5-fonts = %{version}-%{release}
Obsoletes:	fontawesome5-fonts-web < 5.15.4-5
Provides:	fontawesome5-fonts-web = %{version}-%{release}

%description web %_desc

This package contains CSS, SCSS and LESS style files for each of the
fonts in the FontAwesome family, as well as JSON and YAML metadata.
It also contains JavaScript, TTF, and SVG files, which are typically
used on web pages.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n Font-Awesome-%{version} -p1
cp -p %SOURCE2 .

%build
%fontbuild -a

%install
%fontinstall -a

# Install the web files
mkdir -p %{buildroot}%{_datadir}/fontawesome
cp -a css js less metadata scss sprites svgs webfonts \
   %{buildroot}%{_datadir}/fontawesome

# Fix up the generated metainfo; see bz 1943727
sed -e 's,updatecontact,update_contact,g' \
    -e 's,<!\[CDATA\[\([^]]*\)\]\]>,\1,g' \
    -i %{buildroot}%{_metainfodir}/*.metainfo.xml

%check
%fontcheck -a

%fontfiles -a

%files all

%files web
%doc CHANGELOG.md README* UPGRADING.md
%license LICENSE.txt
%{_datadir}/fontawesome/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:6.7.2-1
- Import
