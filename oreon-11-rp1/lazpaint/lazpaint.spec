%global source0_hash 05da51650f7220b8674083c37857e9fc3686a7f1cabc41bfe4417d6f07632d25

Name: lazpaint
%global name_pretty LazPaint
%global name_rtld io.github.bgrabitmap.LazPaint

Summary: Simple image editor
URL: https://lazpaint.github.io

# LazPaint itself is GPLv3
# BGRABitmap and BGRAControls libraries are modified LGPLv2 (allow static linking in closed-source programs)
# BGRAControls also borrows some Boost-licensed code
License: GPL-3.0-only AND LGPL-3.0-only

Version: 7.3
Release: 4%{?dist}

# Versions taken from lazpaint/lazpaint.lpi
%global bitmap_version   11.6.6
%global controls_version 9.0.2

%global github https://github.com/bgrabitmap
Source0: %{github}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10: %{github}/bgrabitmap/archive/v%{bitmap_version}/bgrabitmap-%{bitmap_version}.tar.gz
Source20: %{github}/bgracontrols/archive/v%{controls_version}/bgracontrols-%{controls_version}.tar.gz

# Fix build with FPC 3.2.4
Patch0000: 0000-fpc-3.2.4.patch

%global widgetset gtk2

BuildRequires: desktop-file-utils
BuildRequires: file
BuildRequires: fpc
BuildRequires: fpc-srpm-macros
BuildRequires: lazarus-lcl-%{widgetset}
BuildRequires: lazarus-tools
BuildRequires: libappstream-glib

BuildRequires: dos2unix
%if %{defined flatpak}
BuildRequires: xmlstarlet
%endif

Requires: hicolor-icon-theme

ExclusiveArch: %{fpc_arches}

%description
%{name_pretty} is a simple image editor, like PaintBrush or Paint.Net,
written in Lazarus (Free Pascal), using the BGRABitmap library.

It supports a variety of file formats, including layered bitmaps
and even 3D files.

%{name_pretty} also offers a command-line interface for using it from a terminal,
as well as a Python script system that allows the user
to write their own layer effects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# unpack BGRABitmap
tar xzf %{SOURCE10}
rmdir use/bgrabitmap
mv bgrabitmap-%{bitmap_version}/bgrabitmap  use/bgrabitmap
rm -rf bgrabitmap-%{bitmap_version}/

# unpack BGRAControls
tar xzf %{SOURCE20}
rmdir use/bgracontrols
mv bgracontrols-%{controls_version}  use/bgracontrols
rm -rf bgracontrols-%{controls_version}/

# Apply patches.
# We do it only now, and not right after %%setup, since some patches affect bgrabitmap/bgracontrols, too.
%patch -p1 -P0000

# Some of the .po files have DOS line endings. Fix those.
dos2unix lazpaint/release/bin/i18n/*.po

%global laz_packages  %{expand:
	use/bgrabitmap/bgrabitmappack.lpk
	use/bgracontrols/bgracontrols.lpk
	lazpaintcontrols/lazpaintcontrols.lpk
}

%global laz_projects  %{expand:
	%{laz_packages}
	lazpaint/lazpaint.lpi
}

# Patch the project configuration files to enable debuginfo generation
LAZ_PROJECTS=(%{laz_projects})
for PROJECT in ${LAZ_PROJECTS[@]}; do
	sed  \
		-e 's|<GenerateDebugInfo Value="False"[ ]*/>|<GenerateDebugInfo Value="True"/>\n\t\t\t<DebugInfoType Value="dsDwarf2"/>|g'  \
		-e 's|<StripSymbols Value="True"[ ]*/>|<StripSymbols Value="False"/>|g'  \
		-i "${PROJECT}"
done

%if %{defined flatpak}
# gtk2 is not part of the runtime and is built in /app for flatpaks
xmlstarlet edit --inplace \
	-s '/CONFIG/ProjectOptions/BuildModes/Item2/CompilerOptions' -t elem -n Other \
	-s '$prev' -t elem -n CustomOptions \
	-i '$prev' -t attr -n Value -v '-k-L%{_libdir}' \
	lazpaint/lazpaint.lpi
%endif

%build
LAZ_PACKAGES=(%{laz_packages})
LAZ_PROJECTS=(%{laz_projects})

# Inform lazbuild where to look for dependencies
for PACKAGE in ${LAZ_PACKAGES[@]}; do
	lazbuild --add-package-link "${PACKAGE}"
done

# lazbuild has a "--recursive" option for automatically compiling dependencies,
# but using this option triggers random crashes during the build.
# See: - https://bugs.freepascal.org/view.php?id=36318
#      - https://bugs.freepascal.org/view.php?id=36959
#
# As a workaround, we build everything manually in order.
for PROJECT in ${LAZ_PROJECTS[@]}; do
	lazbuild --build-mode=Release --widgetset=%{widgetset} --skip-dependencies "${PROJECT}"
done

# Upstream provides a desktop file, but it's a bit of a mess
# and doesn't pass desktop-file-validate.
# Instead of trying to fix it, let's just write a desktop file ourselves.
cat > lazpaint/release/%{name_rtld}.desktop << EOF
[Desktop Entry]
Type=Application
Name=%{name_pretty}
GenericName=Image editor
Comment=%{summary}
Icon=%{name}
Exec=%{_bindir}/%{name}
Terminal=false
Categories=Graphics
EOF

%install
# -- executable
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 lazpaint/release/bin/%{name} %{buildroot}%{_bindir}/

# -- run-time resources

RESDIR="%{buildroot}%{_datadir}/%{name}"
install -m 755 -d "${RESDIR}"
cp -a lazpaint/release/bin/models/ "${RESDIR}/models"

cp -a resources/scripts/ "${RESDIR}/scripts"
rm -rf "${RESDIR}/scripts/test/"

install -m 755 -d "${RESDIR}/i18n"
install -m 644 lazpaint/release/bin/i18n/*.po "${RESDIR}/i18n/"

# -- icons

for ICON_SIZE in 16 20 24 32 40 48 64 96 128 256 512 1024 2048; do
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${ICON_SIZE}x${ICON_SIZE}/apps"
	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p "resources/icon/${ICON_SIZE}x${ICON_SIZE}.png" "${ICON_DIR}/%{name}.png"
done

# -- desktop file and appstream data

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p lazpaint/release/%{name_rtld}.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p Install/flatpak/%{name_rtld}.metainfo.xml %{buildroot}%{_metainfodir}/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name_rtld}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name_rtld}.metainfo.xml

%files
%license COPYING.txt
%license use/bgracontrols/docs/COPYING.LGPL.txt
%license use/bgracontrols/docs/COPYING.modifiedLGPL.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name_rtld}.desktop
%{_datadir}/icons/hicolor/**/apps/%{name}.png
%{_metainfodir}/%{name_rtld}.metainfo.xml

%changelog
%autochangelog
