%global source0_hash none

%global patched_tarball 1

%if %patched_tarball
%global patch_ext .p
%else
%global patch_ext %{nil}
%endif

Summary: High speed arctic racing game
Name: extremetuxracer
Version: 0.8.4
Release: 3%{?dist}
License: GPL-2.0-or-later
URL: http://extremetuxracer.sourceforge.net
# This is really
# http://downloads.sourceforge.net/extremetuxracer/etr-%%{version}.tar.xz, but
# with a badly licensed font file removed. Use etr-clean-tarball.sh to
# regenerate from the upstream tarball.
Source0: etr-%{version}%{patch_ext}.tar.xz
Source1: etr-clean-tarball.sh
Source2: etr.appdata.xml
Source3: %{name}.metainfo.xml
Source4: %{name}-papercuts.metainfo.xml
#Source5: %%{name}-papercuts-outline.metainfo.xml
# manpages courtesy of Debian
Source6: etr.6
Source7: etr.de.6

# Don't reference removed files
#Patch0: etr-0.6.0-clean-tarball.patch

BuildRequires:  gcc-c++
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: SFML-devel
BuildRequires: freetype-devel
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: fontpackages-devel
BuildRequires: symlinks
BuildRequires: make

Requires: opengl-games-utils
Requires: extremetuxracer-common = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: extremetuxracer-papercuts-fonts = %{?epoch:%{epoch}:}%{version}-%{release}
#Requires: extremetuxracer-papercuts-outline-fonts = %%{?epoch:%%{epoch}:}%%{version}-%%{release}
Requires: gnu-free-sans-fonts
Requires: hicolor-icon-theme

Provides:  %{name}-papercuts-outline-fonts = %{version}-%{release}
Obsoletes: %{name}-papercuts-outline-fonts < %{version}-%{release}

%description
Extreme Tux Racer is an open-source downhill racing game starring Tux, the
Linux mascot.

%package common
Summary: Common files for Extreme Tux Racer and its fonts
BuildArch: noarch

%description common
This package consists of files used by other %{name} packages.

%package papercuts-fonts
Summary: PaperCuts 2.0 font
BuildArch: noarch

%description papercuts-fonts
This package contains the PaperCuts 2.0 font which is used by Extreme Tux
Racer.

%_font_pkg -n papercuts pc_20.ttf
%{_datadir}/appdata/%{name}-papercuts.metainfo.xml

#%%package papercuts-outline-fonts
#Summary: PaperCuts Outline 2.0 font
#BuildArch: noarch
#Requires: extremetuxracer-common = %%{?epoch:%%{epoch}:}%%{version}-%%{release}

#%%description papercuts-outline-fonts
#This package contains the PaperCuts Outline 2.0 font which is used by Extreme
#Tux Racer.

#%%_font_pkg -n papercuts-outline pc_outline.ttf
#%%{_datadir}/appdata/%%{name}-papercuts-outline.metainfo.xml

%prep
%setup -q -n etr-%{version}%{?patch_ext}
#%patch0 -p1 -b .clean-tarball
autoreconf -ivf

%build
%configure
make %{?_smp_mflags}

%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/net.sourceforge.extremetuxracer.desktop
ln -snf opengl-game-wrapper.sh %{buildroot}%{_bindir}/etr-wrapper
desktop-file-edit --set-key=Exec --set-value=etr-wrapper \
    %{buildroot}%{_datadir}/applications/net.sourceforge.extremetuxracer.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/pixmaps/etr.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mv %{buildroot}%{_datadir}/pixmaps/etr.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

mkdir -p %{buildroot}%{_fontdir}
pushd %{buildroot}%{_datadir}/etr/fonts
rm -f stdbold.ttf stditalic.ttf std.ttf
for i in *.ttf; do
    mv "$i" %{buildroot}%{_fontdir}/
    ln -s "%{buildroot}%{_fontdir}/$i" "$i"
done
# Trick symlinks into making symlinks relative which are dangling in the
# buildroot
mkdir -p "%{buildroot}%{_fontbasedir}/gnu-free"
for i in FreeSansBold.ttf FreeSansOblique.ttf FreeSans.ttf; do
    touch "%{buildroot}%{_fontbasedir}/gnu-free/$i"
done
ln -s "%{buildroot}%{_fontbasedir}/gnu-free/FreeSansBold.ttf" stdbold.ttf
ln -s "%{buildroot}%{_fontbasedir}/gnu-free/FreeSansOblique.ttf" stditalic.ttf
ln -s "%{buildroot}%{_fontbasedir}/gnu-free/FreeSans.ttf" std.ttf
symlinks -c -s .
rm -rf "%{buildroot}%{_fontbasedir}/gnu-free"
popd
# move docs in correct location
mv -f %{buildroot}%{_docdir}/etr %{buildroot}%{_pkgdocdir}

# install appdata file
install -DT -m0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/etr.appdata.xml

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{name}-papercuts.metainfo.xml
#install -Dm 0644 -p %{SOURCE5} \
#        %{buildroot}%{_datadir}/appdata/%{name}-papercuts-outline.metainfo.xml

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.xml

install -Dm 0644 -p %{SOURCE6} %{buildroot}%{_mandir}/man6/etr.6
install -Dm 0644 -p %{SOURCE7} %{buildroot}%{_mandir}/de/man6/etr.6

%files
%doc %{_pkgdocdir}/*
%{_bindir}/etr
%{_bindir}/etr-wrapper
%{_datadir}/etr
%{_datadir}/appdata/etr.appdata.xml
%{_datadir}/metainfo/net.sourceforge.extremetuxracer.metainfo.xml
%{_datadir}/applications/net.sourceforge.extremetuxracer.desktop
%{_datadir}/icons/hicolor/*/apps/etr.*
%{_mandir}/man6/etr.6*
%lang(de) %{_mandir}/de/man6/etr.6*

%files common
%doc AUTHORS ChangeLog
%license COPYING
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
%autochangelog
