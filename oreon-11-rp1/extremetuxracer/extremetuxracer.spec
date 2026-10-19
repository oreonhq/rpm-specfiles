%global source0_hash 829b520afe5313865824ced69fb86d50c8b7388e7e643e38d15ecd86c4c4f8a6
%global patched_tarball 1
%if %patched_tarball
%global patch_ext .p
%else
%global patch_ext %{nil}
%endif
Summary:        High speed arctic racing game
Name: extremetuxracer
Version: 0.8.4
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://extremetuxracer.sourceforge.net
Source0:        https://src.fedoraproject.org/repo/pkgs/%{name}/etr-%{version}%{patch_ext}.tar.xz/sha5%{patched_tarball}2/bbf6c308ee3ab2b22626c0%{patched_tarball}25c2757289785b4a7%{patched_tarball}822ee736852b286469d476f469ee9634c5f9be88a928052589cf%{patched_tarball}%{patched_tarball}a2505f8%{patched_tarball}fc2dd0c0f34ae7%{patched_tarball}daef9328b7/etr-%{version}%{patch_ext}.tar.xz
Source1: etr-clean-tarball.sh
Source2: etr.appdata.xml
Source3: %{name}.metainfo.xml
Source4: %{name}-papercuts.metainfo.xml
Source6: etr.6
Source7: etr.de.6
Requires: opengl-games-utils
Requires: extremetuxracer-common = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: extremetuxracer-papercuts-fonts = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: gnu-free-sans-fonts
Requires: hicolor-icon-theme
Provides:  %{name}-papercuts-outline-fonts = %{version}-%{release}
Obsoletes: %{name}-papercuts-outline-fonts < %{version}-%{release}
# oreon:deps
BuildRequires:  SFML2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fontpackages-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  symlinks
# /oreon:deps
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

export PKG_CONFIG_PATH=%{_libdir}/SFML2/pkgconfig
export CXXFLAGS="%{optflags} -I%{_includedir}/SFML2"
export LDFLAGS="%{?build_ldflags} -L%{_libdir}/SFML2"
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
mv -f %{buildroot}%{_docdir}/etr %{buildroot}%{_pkgdocdir}
install -DT -m0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/etr.appdata.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{name}-papercuts.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.xml
install -Dm 0644 -p %{SOURCE6} %{buildroot}%{_mandir}/man6/etr.6
install -Dm 0644 -p %{SOURCE7} %{buildroot}%{_mandir}/de/man6/etr.6
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n extremetuxracer-common -f %{oreon_filedir}/extremetuxracer-common.list
%files -n extremetuxracer-papercuts-fonts -f %{oreon_filedir}/extremetuxracer-papercuts-fonts.list

%changelog

%autochangelog
