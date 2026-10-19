%global source0_hash 85faab35915974be1701cbcc6a18606a34e62cc7c86e0336f152acbc6156a8a6
%global fontname lyx
%global _without_included_boost --without-included-boost
%global autotools 0
%global _changelog_trimtime %(date +%s -d "1 year ago")
Name:    lyx
Version: 2.5.3
Release:        1%{?dist}
Summary:        WYSIWYM (What You See Is What You Mean) document processor
License: GPL-2.0-or-later
Url:     https://www.lyx.org/
Source0:        http://ftp.lyx.org/pub/lyx/stable/2.5.x/lyx-%{version}.tar.xz
Source1: lyxrc.dist
Source20: %{fontname}.metainfo.xml
%if 0%{?autotools}
%endif
%if 0%{?_without_included_boost:1}
%endif
Requires: %{name}-common = %{version}-%{release}
Requires: %{fontname}-fonts = %{version}-%{release}
Requires: hicolor-icon-theme
Requires: python3
Requires: ImageMagick
Requires: xdg-utils
Requires: ghostscript
%if %{undefined flatpak}
Requires: tex-dvipdfmx
Requires: tex-epstopdf
Requires: tex-chktex
Requires: tex-dtl
Requires: tex(cprotect.sty)
Requires: tex(dvips)
Requires: tex(esint.sty)
Requires: tex(latex)
Requires: tex(nomencl.sty)
Requires: tex(ulem.sty)
Requires: tex(xcolor.sty)
Recommends: texlive-collection-latexrecommended
%endif
# oreon:deps
BuildRequires:  bc
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  enchant2-devel
BuildRequires:  file-devel
BuildRequires:  fontpackages-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  hunspell-devel
BuildRequires:  make
BuildRequires:  mythes-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  python3-devel
BuildRequires:  tex(dvips)
BuildRequires:  tex(latex)
BuildRequires:  zlib-devel
# /oreon:deps
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
install -p -m644 -D %{SOURCE1} %{buildroot}%{_datadir}/%{name}/lyxrc.dist
mkdir -p %{buildroot}%{_texmf}/tex/latex/
mv %{buildroot}%{_datadir}/%{name}/tex \
   %{buildroot}%{_texmf}/tex/latex/%{name}
install -p -D -m644 lib/images/lyx.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -D -m644 lib/images/lyx.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
touch %{buildroot}%{_datadir}/%{name}/lyxrc.defaults
touch %{buildroot}%{_datadir}/%{name}/{packages,textclass}.lst
install -m 0755 -d %{buildroot}%{_fontdir}
mv %{buildroot}%{_datadir}/%{name}/fonts/*.ttf %{buildroot}%{_fontdir}/
rm -rf %{buildroot}%{_datadir}/%{name}/fonts
install -Dm 0644 -p %{SOURCE20} \
        %{buildroot}%{_metainfodir}/%{fontname}.metainfo.xml
%find_lang %{name}
install -p -D -m 0644 lib/scripts/bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml ||:
make -k check ||:
%files -f %{oreon_filedir}/main.list
%files -n lyx-common -f %{oreon_filedir}/lyx-common.list
%files -n lyx-fonts -f %{oreon_filedir}/lyx-fonts.list

%changelog

%autochangelog
