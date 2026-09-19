%global source0_hash d1f07162f0ee8164b8d3aaf7e3527059a8b0f4bf5dd7a9b815845ef281b316b8

%global srcname SiriKali
%global srcurl  https://github.com/mhogomchungu/%{name}

Name:           sirikali
Version:        1.8.6
Release:        1%{?dist}
Summary:        GUI front end to encfs,cryfs,gocryptfs and securefs
# generally GPLv2+, BSD for tasks and NetworkAccessManager folders
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            http://mhogomchungu.github.io/%{name}

Source0:        %{srcurl}/releases/download/%{version}/%{srcname}-%{version}.tar.xz

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: json-devel
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(lxqt-wallet)

BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Network)

BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
Requires:      hicolor-icon-theme

Recommends:    fuse-encfs

%description
%{srcname} is a Qt/C++ GUI front end to encfs,cryfs,gocryptfs and securefs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n%{srcname}-%{version}
# collect licenses
cp -p src/3rdParty/tasks/LICENSE LICENSE-tasks
# unbundle
pushd src/3rdParty
rm -rv lxqt_wallet
popd
sed -i -r 's:".*(json.hpp)":"\1":' CMakeLists.txt
sed -i 's:3rdParty/json:json:' src/%{name}.cpp

%build
%cmake -DQT5=true -DNOKDESUPPORT=true -DNOSECRETSUPPORT=false \
 -DINTERNAL_LXQT_WALLET=false -DBUILD_WITH_QT6=true \
 -DJSON_HEADER_PATH=/usr/include/nlohmann/json.hpp ..
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.mhogomchungu.sirikali.desktop

%files -f %{name}.lang
%license COPY* LICENSE* GPLv*
%doc README.md ABOUT* changelog
%{_bindir}/%{name}*
%{_datadir}/applications/io.github.mhogomchungu.sirikali.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/%{name}*.1*

%changelog
%autochangelog
