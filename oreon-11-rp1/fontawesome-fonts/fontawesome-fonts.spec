%global source0_hash d5a20554faa1ad30148b05f090a556e23495c446435c8dfc1624d3c0e3c2640b

Name:		fontawesome-fonts
Summary:	Support files for the FontAwesome fonts
Epoch:		1
Version:	7.3.1
Release:	%autorelease

License:	MIT
URL:		https://fontawesome.com/
VCS:		git:https://github.com/FortAwesome/Font-Awesome.git
BuildArch:	noarch

%global _desc %{expand:Font Awesome gives you scalable vector icons that can instantly be customized
— size, color, drop shadow, and anything that can be done with the power of
CSS.}

%global fontlicense	OFL-1.1-RFN
%global fontlicenses	LICENSE.txt
%global fontdocs	CHANGELOG.md README.md UPGRADING.md
%global fontorg		com.fontawesome

%global fontfamily1	FontAwesome 7 Free
%global fontsummary1	Iconic font set
%global fonts1		otfs/*Free*
%global fontconfs1	%{SOURCE3}
%global fontpkgheader1	%{expand:
# This can be removed when F48 reaches EOL
Obsoletes:	fontawesome-6-free-fonts < 7.0.0
Provides:	fontawesome-6-free-fonts = %{version}-%{release}
Provides:	font(fontawesome6free)
Provides:	font(fontawesome6freeregular)
Provides:	font(fontawesome6freesolid)
}
%global fontdescription1 %{expand:%_desc

The FontAwesome Free Fonts contain large numbers of icons packaged as
font files.}

%global fontfamily2	FontAwesome 7 Brands Regular
%global fontsummary2	Iconic font set
%global fonts2		otfs/*Brands*
%global fontconfs2	%{SOURCE4}
%global fontpkgheader2	%{expand:
# This can be removed when F48 reaches EOL
Obsoletes:	fontawesome-6-brands-fonts < 7.0.0
Provides:	fontawesome-6-brands-fonts = %{version}-%{release}
Provides:	font(fontawesome6brands)
Provides:	font(fontawesome6brandsregular)
}
%global fontdescription2 %{expand:%_desc

The FontAwesome Brand Fonts contain brand logos packaged as font files.}

Source0:        https://github.com/FortAwesome/Font-Awesome/archive/refs/tags/%{version}.tar.gz#/Font-Awesome-%{version}.tar.gz
# Script to generate Source2
Source1:	trademarks.py
Source2:	README-Trademarks.txt
Source3:	60-fontawesome-7-free-fonts.conf
Source4:	60-fontawesome-7-brands-fonts.conf

%description
%_desc

%fontpkg -a
%fontmetapkg -d _desc

%package web
License:	CC-BY-4.0
Summary:	Iconic font set, JavaScript and SVG files

%description web
%_desc

This package contains CSS, SCSS and LESS style files for each of the fonts in
the FontAwesome family, as well as JSON and YAML metadata.  It also contains
JavaScript, SVG, and WOFF2 files, which are typically used on web pages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n Font-Awesome-%{version}
cp -p %SOURCE2 .

%build
%fontbuild -a

%install
%fontinstall -a

# Install the web files
mkdir -p %{buildroot}%{_datadir}/fontawesome
cp -a css js metadata schemas scss sprites* svg* webfonts \
   %{buildroot}%{_datadir}/fontawesome

# Fix up the generated metainfo; see bz 1943727
sed -e 's,<!\[CDATA\[\([^]]*\)\]\]>,\1,g' \
    -i %{buildroot}%{_metainfodir}/*.metainfo.xml

%check
%fontcheck -a

%fontfiles -a

%files web
%doc CHANGELOG.md README.md UPGRADING.md
%license LICENSE.txt
%{_datadir}/fontawesome/

%changelog
%autochangelog
