%global source0_hash 04d0af0d0ae1f12e9bfe2ea9980042509b1441be7fb036e66014bfa1327b6271
Name:           alchemyquest
Version:        0.5.4
Release:        1%{?dist}
Summary:        Reflection game
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://identicalsoftware.com/alchemyquest/
Source0:        http://identicalsoftware.com/%{name}//%{name}-%{version}.tgz
Requires:      hicolor-icon-theme
Provides:      openalchemist = 0.4-34
Obsoletes:     openalchemist < 0.4-34
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libgamerzilla-devel
BuildRequires:  libzip-devel
BuildRequires:  make
# /oreon:deps
%description
Alchemy Quest is a new reflection game which looks like classic falling block
games but where you can take your time. Be a crazy alchemist and try to make
new objects from those you get from the sky.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_datadir}/alchemyquest/{CODE-LICENSE,GRAPHICS-LICENSE}
pushd %{buildroot}%{_bindir} && ln -s alchemyquest openalchemist && popd
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
install -p -m 644 icons/16x16/apps/alchemyquest.png \
    %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/alchemyquest.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 icons/32x32/apps/alchemyquest.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/alchemyquest.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 icons/48x48/apps/alchemyquest.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/alchemyquest.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 data/logo_svg.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/openalchemist.svg
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    alchemyquest.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    openalchemist.desktop
mkdir -p %{buildroot}%{_metainfodir}
install -p -m 644 %{name}.appdata.xml \
    %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
install -p -m 644 openalchemist.appdata.xml \
    %{buildroot}%{_metainfodir}/openalchemist.metainfo.xml
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/*.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
