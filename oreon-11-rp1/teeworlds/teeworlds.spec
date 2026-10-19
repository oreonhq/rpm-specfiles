%global source2_hash 16c3149245663438773331369dd70302d6ccd879b24159a6bee8bf6205eab4f1
%global source1_hash 323876f791a873fd43633506bd0409cfa20f6c95cb8b7c54d43728e20ee03005
%global source0_hash 6e67846b38750d2a372d7835fa3775db016458a20a85aa52f1c758102ddd4abe
Name:           teeworlds
Version:        0.7.5
Release:        19%{?dist}
Summary:        Online multi-player platform 2D shooter
License:        LicenseRef-Callaway-Teeworlds AND Zlib AND BSD-2-Clause AND BSD-3-Clause
URL:            https://www.teeworlds.com/
Source0:        https://github.com/teeworlds/teeworlds/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/teeworlds/teeworlds-maps/archive/1d3401a37a3334e311faf18a22aeff0e0ac9ee65/%{name}-%{version}-maps.tar.gz
Source2:        https://github.com/teeworlds/teeworlds-translation/archive/4ed69dd7497ca6e04bab0b042f137bf97f3c5d0a/%{name}-%{version}-translation.tar.gz
Source3:        %{name}.png
Source4:        %{name}-server@.service
Source5:        server_dm.cfg
Source6:        server_tdm.cfg
Source7:        server_ctf.cfg
Patch0: 3018.patch
Provides:       bundled(md5)
Provides:       bundled(json-parser)
Requires:       %{name}-data = %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pnglite-devel
BuildRequires:  python3-devel
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
The game features cartoon-themed graphics and physics, 
and relies heavily on classic shooter weaponry and gameplay. 
The controls are heavily inspired by the FPS genre of computer games. 

%package        server
Summary:        Server for %{name}
Requires:       %{name}-data = %{version}
Provides:       bundled(md5)
%{?systemd_requires}
BuildRequires:  systemd
%description    server
Server for %{name}, an online multi-player platform 2D shooter. 

%package        data
Summary:        Data-files for %{name}
License:        CC-BY-SA-4.0
Requires:       font(dejavusans)
BuildArch:      noarch
%description    data
Data-files for %{name}, an online multi-player platform 2D shooter.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a1 -a2
%autopatch -p1
rm -vrf datasrc/{maps,languages}
mv teeworlds-maps-* datasrc/maps
mv teeworlds-translation-* datasrc/languages
# https://github.com/teeworlds/teeworlds/issues/1882
%ifnarch x86_64
sed -i -e "/_mm_pause/d" src/engine/client/client.cpp
%endif
sed -i "s/\/usr/\%{_prefix}/g" src/engine/shared/storage.cpp

# Create a sysusers.d config file
cat >teeworlds.sysusers.conf <<EOF
u teeworlds - '%{name} server daemon account' %{_sysconfdir}/%{name} -
EOF

%build

%cmake . -GNinja -DCMAKE_BUILD_TYPE=RELEASE \
  -DPREFER_BUNDLED_LIBS=OFF \
  -DSERVER_EXECUTABLE=%{name}-srv \
  -DPYTHON_EXECUTABLE=%{__python3} \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  %{nil}
%cmake_build
%install
%cmake_install
install -Dpm0644 -t %{buildroot}%{_datadir}/pixmaps/ %{S:3}
install -Dpm0644 -t %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/ %{S:3}
install -Dpm0644 -t %{buildroot}%{_metainfodir} other/%{name}.appdata.xml
install -Dpm0644 -t %{buildroot}%{_unitdir} %{S:4}
install -Dpm0644 -t %{buildroot}%{_datadir}/applications other/%{name}.desktop
install -Dpm0664 %{S:5} %{buildroot}%{_sysconfdir}/%{name}/dm.cfg
install -Dpm0664 %{S:6} %{buildroot}%{_sysconfdir}/%{name}/tdm.cfg
install -Dpm0664 %{S:7} %{buildroot}%{_sysconfdir}/%{name}/ctf.cfg
ln -sf %{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/DejaVuSans.ttf
install -m0644 -D teeworlds.sysusers.conf %{buildroot}%{_sysusersdir}/teeworlds.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%systemd_post %{name}-server@dm.service
%systemd_post %{name}-server@tdm.service
%systemd_post %{name}-server@ctf.service
%preun server

%systemd_preun %{name}-server@dm.service
%systemd_preun %{name}-server@tdm.service
%systemd_preun %{name}-server@ctf.service
%postun server

%systemd_postun_with_restart %{name}-server@dm.service
%systemd_postun_with_restart %{name}-server@tdm.service
%systemd_postun_with_restart %{name}-server@ctf.service
%files -f %{oreon_filedir}/main.list
%files -n teeworlds-server -f %{oreon_filedir}/teeworlds-server.list
%files -n teeworlds-data -f %{oreon_filedir}/teeworlds-data.list

%changelog

%autochangelog
