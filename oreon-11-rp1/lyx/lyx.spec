%global source0_hash none

## lyx-fonts
%global fontname lyx
BuildRequires: fontpackages-devel

%global _without_included_boost --without-included-boost

# Do we need to rebuild configuration files?
%global autotools 0

# Trim changelog to a reasonable size
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    lyx
Version: 2.5.0
Release: 1%{?dist}
Summary: WYSIWYM (What You See Is What You Mean) document processor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url:     https://www.lyx.org/
Source0: http://ftp.lyx.org/pub/lyx/stable/2.5.x/lyx-%{version}.tar.xz

Source1: lyxrc.dist

# font metainfo file
Source20: %{fontname}.metainfo.xml

%if 0%{?autotools}
BuildRequires: automake libtool
%endif
# weird but necessary to compare the supported qt version
# see http://comments.gmane.org/gmane.editors.lyx.devel/137498
BuildRequires: bc

%if 0%{?_without_included_boost:1}
BuildRequires: boost-devel
%endif

%if 0%{?fedora}
BuildRequires: libappstream-glib
%endif

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: enchant2-devel
BuildRequires: file-devel
BuildRequires: gettext
BuildRequires: hunspell-devel
BuildRequires: mythes-devel
BuildRequires: python3-devel

%if 0%{?fedora} || 0%{?rhel} >= 10
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: libxkbcommon-devel
%else
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5X11Extras)
%endif

BuildRequires: tex(dvips)
BuildRequires: tex(latex)
BuildRequires: zlib-devel

Requires: %{name}-common = %{version}-%{release}
Requires: %{fontname}-fonts = %{version}-%{release}
Requires: hicolor-icon-theme
Requires: python3

%if 0%{?fedora}
# convert doc files to lyx (bug #193858)
Requires: wv
%endif

# required for file conversions
Requires: ImageMagick
Requires: xdg-utils
Requires: ghostscript

%if %{undefined flatpak}
## produce PDF files directly from DVI files
Requires: tex-dvipdfmx
## convert eps to pdf
Requires: tex-epstopdf
## checking the quality of the generated latex
Requires: tex-chktex
## instant preview
Requires: tex-dtl
Requires: tex(cprotect.sty)
# LaTeX packages required to compile the User's Manual
Requires: tex(dvips)
Requires: tex(esint.sty)
Requires: tex(latex)
Requires: tex(nomencl.sty)
Requires: tex(ulem.sty)
Requires: tex(xcolor.sty)
Recommends: texlive-collection-latexrecommended
%endif

%description
LyX is a modern approach to writing documents which breaks with the
obsolete "typewriter paradigm" of most other document preparation
systems.

It is designed for people who want professional quality output
with a minimum of time and effort, without becoming specialists in
typesetting.

The major innovation in LyX is WYSIWYM (What You See Is What You Mean).
That is, the author focuses on content, not on the details of formatting.
This allows for greater productivity, and leaves the final typesetting
to the backends (like LaTeX) that are specifically designed for the task.

With LyX, the author can concentrate on the contents of his writing,
and let the computer take care of the rest.

%package common
Summary:  Common files of %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description common
%{Summary}.

%package fonts
Summary: Lyx/MathML fonts
# The actual license says "The author of these fonts, Basil K. Malyshev, has
# kindly granted permission to use and modify these fonts."
# One of the font files (wasy10) is separately licensed GPL+.
License: LicenseRef-Fedora-UltraPermissive AND GPL-1.0-or-later
Requires: fontpackages-filesystem
Provides:  mathml-fonts = 1.0-50
Provides:  lyx-cmex10-fonts = %{version}-%{release}
Provides:  lyx-cmmi10-fonts = %{version}-%{release}
Provides:  lyx-cmr10-fonts = %{version}-%{release}
Provides:  lyx-cmsy10-fonts = %{version}-%{release}
BuildArch: noarch
%description  fonts
A collection of Math symbol fonts for %{name}.

%prep

%autosetup -p1

# prefer xdg-open over alternatives in configuration
for prog in xv firefox kghostview pdfview xdvi
do
    sed -i -e "s/'$prog'/'xdg-open', '$prog'/" lib/configure.py
done

%if 0%{?autotools}
./autogen.sh
%endif

%build
%configure \
  --disable-dependency-tracking \
  --disable-rpath \
  --disable-silent-rules \
  --enable-build-type=release \
  --enable-optimization="%{optflags}" \
  --without-included-boost \
  --with-enchant \
  --with-hunspell

%make_build

%install
%make_install

%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/lyx2lyx

# misc/extras
install -p -m644 -D %{SOURCE1} %{buildroot}%{_datadir}/%{name}/lyxrc.dist

# Set up the lyx-specific class files where TeX can see them
mkdir -p %{buildroot}%{_texmf}/tex/latex/
mv %{buildroot}%{_datadir}/%{name}/tex \
   %{buildroot}%{_texmf}/tex/latex/%{name}

# icon
install -p -D -m644 lib/images/lyx.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

install -p -D -m644 lib/images/lyx.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# ghost'd files
touch %{buildroot}%{_datadir}/%{name}/lyxrc.defaults
touch %{buildroot}%{_datadir}/%{name}/{packages,textclass}.lst

# fonts
install -m 0755 -d %{buildroot}%{_fontdir}
mv %{buildroot}%{_datadir}/%{name}/fonts/*.ttf %{buildroot}%{_fontdir}/
rm -rf %{buildroot}%{_datadir}/%{name}/fonts

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE20} \
        %{buildroot}%{_metainfodir}/%{fontname}.metainfo.xml

%find_lang %{name}

# bash completion
install -p -D -m 0644 lib/scripts/bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml ||:
# tests/test_filetools error bogus ( see http://bugzilla.redhat.com/723938 )
make -k check ||:

%files
%doc ANNOUNCE lib/CREDITS NEWS README
%license COPYING
%{_bindir}/*

%files common -f %{name}.lang
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/%{name}/
%config(noreplace) %{_datadir}/%{name}/lyxrc.dist
%ghost %{_datadir}/%{name}/lyxrc.defaults
%ghost %{_datadir}/%{name}/*.lst
%{_texmf}/tex/latex/%{name}/
%{_metainfodir}/org.%{name}.LyX.metainfo.xml
%{_sysconfdir}/bash_completion.d/%{name}

%files fonts
%{_fontdir}/*.ttf
%license lib/fonts/BaKoMaFontLicense.txt
%{_metainfodir}/%{fontname}.metainfo.xml

%changelog
%autochangelog
