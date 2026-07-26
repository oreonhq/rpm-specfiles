%global source0_hash db21c6b89c2804968a1eada43ecb6a9093994b6b42c7adb09ea82ad870879f2a

%global forgeurl https://github.com/bk138/gromit-mpx
Version:        1.8.0
%global tag %{version}
%forgemeta

Name:           gromit-mpx
Release:        %autorelease
Summary:        An on-screen annotation tool
License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  gettext
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(liblz4)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
Gromit-MPX is an on-screen annotation tool that works with any Unix desktop
environment under X11 as well as Wayland.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \

%cmake_build

%install
%cmake_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml

%files -f %{name}.lang
%license COPYING
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.cfg
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/net.christianbeier.Gromit-MPX.desktop
%{_metainfodir}/net.christianbeier.Gromit-MPX.appdata.xml
%{_mandir}/man1/gromit-mpx.1*
%{_datadir}/doc/%{name}/

%changelog
%autochangelog
