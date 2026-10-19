%global source0_hash 75cd971e1b2d6789f9e35b75926b76d037a564ad9291fa852ad9996c8ac40c96
Name: powdertoy
%global rtld_name uk.co.powdertoy.tpt
Summary:        Physics sandbox game
URL: https://powdertoy.co.uk
License: GPL-3.0-only AND Apache-2.0 AND MIT
Version: 100.1.400
Release:        1%{?dist}
%global repo_owner The-Powder-Toy
%global repo_name The-Powder-Toy
Source0:        https://github.com/%{repo_owner}/%{repo_owner}/archive/v%{version}/%{repo_owner}-v%{version}.tar.gz
Patch0: 0000-use-powdertoy-instead-of-powder-as-name.patch
Patch1: 0001-gcc16.patch
%ifnarch ppc64le
%global luaver luajit
%else
%global luaver none
%endif
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libpng-devel
BuildRequires:  lua-devel
BuildRequires:  luajit-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Powder Toy is a free physics sandbox game, which simulates air pressure
and velocity, heat, gravity and a countless number of interactions between
different substances! The game provides you with various building materials,
liquids, gases and electronic components which can be used to construct complex
machines, guns, bombs, realistic terrains and almost anything else.
You can then mine them and watch cool explosions, add intricate wirings,
play with little stickmen or operate your machine. You can also browse and play
thousands of different saves made by the community or upload your own!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo_name}-%{version}

%build

%meson \
	-Dignore_updates=true \
	-Dcan_install=no \
	-Dapp_exe=powdertoy \
	-Dapp_data=powdertoy \
	-Dstatic=none \
	-Dhttp=true \
	-Denforce_https=true \
	-Dlua=%{luaver} \
	-Dx86_sse=auto
%meson_build
%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 %{_vpath_builddir}/powdertoy %{buildroot}%{_bindir}/%{name}
for ICONSET in "icon_exe:apps:powdertoy" "icon_cps:mimetypes:application-vnd.powdertoy.save"; do
	ICON_SRC="$(echo "${ICONSET}" | cut -d: -f1)"
	ICON_CATEGORY="$(echo "${ICONSET}" | cut -d: -f2)"
	ICON_DST="$(echo "${ICONSET}" | cut -d: -f3)"
	ln -sr "resources/generated_icons/${ICON_SRC}.png" "resources/generated_icons/${ICON_SRC}_256.png"
	for ICON_SIZE in 16 32 48 256; do
		ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${ICON_SIZE}x${ICON_SIZE}/${ICON_CATEGORY}"
		install -m 755 -d "${ICON_DIR}"
		install -m 644 -p "resources/generated_icons/${ICON_SRC}_${ICON_SIZE}.png" "${ICON_DIR}/${ICON_DST}.png"
	done
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/scalable/${ICON_CATEGORY}"
	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p "resources/${ICON_SRC}.svg" "${ICON_DIR}/${ICON_DST}.svg"
done
install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p "%{_vpath_builddir}/resources/powder.desktop" "%{buildroot}%{_datadir}/applications/%{rtld_name}.desktop"
install -m 755 -d %{buildroot}%{_metainfodir}/
install -m 644 -p "%{_vpath_builddir}/resources/appdata.xml" "%{buildroot}%{_metainfodir}/%{rtld_name}.metainfo.xml"
install -m 755 -d %{buildroot}%{_datadir}/mime/packages/
install -m 644 resources/save.xml %{buildroot}%{_datadir}/mime/packages/powdertoy-save.xml
install -m 755 -d %{buildroot}%{_mandir}/man6/
install -m 644 resources/powder.man %{buildroot}%{_mandir}/man6/powdertoy.6
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rtld_name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
