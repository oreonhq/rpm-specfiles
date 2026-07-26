%global source0_hash d41145bd17c0a91006722bc9bd9169de4950359a305b1b97063b0fdd6edbffaa

Name: powdertoy
%global rtld_name uk.co.powdertoy.tpt

Summary: Physics sandbox game
URL: https://powdertoy.co.uk

# Powder Toy itself is GPLv3
# src/bson/ is Apache v2.0
# src/lua/ is MIT
License: GPL-3.0-only AND Apache-2.0 AND MIT

Version: 99.3.384
Release: 5%{?dist}

%global repo_owner The-Powder-Toy
%global repo_name The-Powder-Toy
Source0: https://github.com/%{repo_owner}/%{repo_name}/archive/v%{version}/%{repo_name}-v%{version}.tar.gz

# Upstream defaults to naming the executable just "powder",
# but in Fedora we always used "powdertoy". This patch edits some files
# which refer to "powder" and makes them use "powdertoy" instead.
Patch0: 0000-use-powdertoy-instead-of-powder-as-name.patch

# Fix building with GCC16. Backported from upstream.
# https://github.com/The-Powder-Toy/The-Powder-Toy/commit/2df4e31e5ff526b8871adb0bb62d1b6a8e289255.patch
Patch1: 0001-gcc16.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: meson

BuildRequires: bzip2-devel
BuildRequires: fftw-devel
BuildRequires: jsoncpp-devel
BuildRequires: libcurl-devel
BuildRequires: libpng-devel
BuildRequires: mesa-libGL-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-devel

# luajit is not available on these architectures
%ifnarch ppc64le
BuildRequires: lua-devel
BuildRequires: luajit-devel
%global luaver luajit
%else
%global luaver none
%endif

Requires: hicolor-icon-theme

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
# -Dapp_exe:
#   Upstream defaults to naming the executable file "powder",
#   but in Fedora we always renamed it to "powdertoy".
# -Dapp_data:
#   Before v96, the game stored user data (config etc.) in $PWD.
#   Fedora shipped a patch which put the user data in "$XDG_DATA_HOME/powdertoy".
#   Starting with v96, the game stores its user data in "$XDG_DATA_HOME/The Powder Toy".
#   We modify this value to preserve backwards-compatibility.
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
# Running "%%meson_install" gives "Nothing to install",
# so we gotta do all of this manually.

install -m 755 -d %{buildroot}%{_bindir}
install -m 755 %{_vpath_builddir}/powdertoy %{buildroot}%{_bindir}/%{name}

# -- icons: for the app and for the savefile mimetype
for ICONSET in "icon_exe:apps:powdertoy" "icon_cps:mimetypes:application-vnd.powdertoy.save"; do
	ICON_SRC="$(echo "${ICONSET}" | cut -d: -f1)"
	ICON_CATEGORY="$(echo "${ICONSET}" | cut -d: -f2)"
	ICON_DST="$(echo "${ICONSET}" | cut -d: -f3)"

	# -- png icons
	ln -sr "resources/generated_icons/${ICON_SRC}.png" "resources/generated_icons/${ICON_SRC}_256.png"
	for ICON_SIZE in 16 32 48 256; do
		ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${ICON_SIZE}x${ICON_SIZE}/${ICON_CATEGORY}"
		install -m 755 -d "${ICON_DIR}"
		install -m 644 -p "resources/generated_icons/${ICON_SRC}_${ICON_SIZE}.png" "${ICON_DIR}/${ICON_DST}.png"
	done

	# -- svg icon
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/scalable/${ICON_CATEGORY}"
	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p "resources/${ICON_SRC}.svg" "${ICON_DIR}/${ICON_DST}.svg"
done

# -- .desktop and .appdata.xml file
install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p "%{_vpath_builddir}/resources/powder.desktop" "%{buildroot}%{_datadir}/applications/%{rtld_name}.desktop"

install -m 755 -d %{buildroot}%{_metainfodir}/
install -m 644 -p "%{_vpath_builddir}/resources/appdata.xml" "%{buildroot}%{_metainfodir}/%{rtld_name}.metainfo.xml"

# -- savefile mimetype
install -m 755 -d %{buildroot}%{_datadir}/mime/packages/
install -m 644 resources/save.xml %{buildroot}%{_datadir}/mime/packages/powdertoy-save.xml

# -- man page
install -m 755 -d %{buildroot}%{_mandir}/man6/
install -m 644 resources/powder.man %{buildroot}%{_mandir}/man6/powdertoy.6

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rtld_name}.metainfo.xml

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/mimetypes/application-vnd.powdertoy.save.png
%{_datadir}/icons/hicolor/scalable/mimetypes/application-vnd.powdertoy.save.svg
%{_datadir}/mime/packages/%{name}*
%{_datadir}/applications/%{rtld_name}.desktop
%{_metainfodir}/%{rtld_name}.metainfo.xml
%{_mandir}/man6/%{name}.6*

%changelog
%autochangelog
