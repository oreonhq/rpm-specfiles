%global source0_hash 9df7c9fa27b6acf898598162105d07cfd2c07677dddefacb64e66430f3ebf131
Name:    peazip
%global rtld_name io.github.peazip.PeaZip
Summary:        File archiver utility
License: LGPL-3.0-only AND Zlib AND FTL
Version: 11.2.0
Release:        1%{?dist}
URL:     https://peazip.github.io
Source0:        https://github.com/peazip/PeaZip/releases/download/%{version}/peazip-%{version}.src.zip
Source9: peazip.metainfo.xml
Patch0:  %{name}--paths.patch
%global ws_gtk2 1
%global ws_gtk3 1
%global ws_qt5 1
%global ws_qt6 1
ExclusiveArch: %{fpc_arches}
%global desc %{expand:
PeaZip is fully-featured, user-friendly file archiver utility,
supporting over 180 archive formats. It also contains a powerful and complete
file manager for viewing, browsing and searching archive files.}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  lazarus-lcl-gtk2
BuildRequires:  lazarus-lcl-gtk3
BuildRequires:  lazarus-lcl-qt5
BuildRequires:  lazarus-lcl-qt6
BuildRequires:  lazarus-tools
BuildRequires:  libappstream-glib
# /oreon:deps
%description %{desc}

# -- Subpackages start

%package common
Summary: Data files for PeaZip
BuildArch: noarch
License: LGPL-3.0-only AND GFDL-1.1-or-later
Requires: hicolor-icon-theme
Recommends: %{_bindir}/7z
Recommends: %{_bindir}/arc
Recommends: %{_bindir}/brotli
Recommends: %{_bindir}/upx
Recommends: %{_bindir}/unrar-free
Recommends: %{_bindir}/zpaq
Recommends: %{_bindir}/zstd
%description common
This package provides common data files (icons, translations, etc.)
used by the PeaZip file archiving utility.

# -- Widgetset subpackages start

%if 0%{?ws_gtk2}
%package gtk2
Summary: File archiver utility (GTK2 version)
BuildRequires: lazarus-lcl-gtk2
RemovePathPostfixes: .gtk2
Conflicts: %{name}-gtk3
Conflicts: %{name}-qt5
Conflicts: %{name}-qt6
Requires: %{name}-common = %{version}-%{release}
%description gtk2 %{desc}

This package provides a GTK2 build of the program.
%endif

%if 0%{?ws_gtk3}
%package gtk3
Summary: File archiver utility (GTK3 version)
BuildRequires: lazarus-lcl-gtk3
RemovePathPostfixes: .gtk3
Conflicts: %{name}-gtk2
Conflicts: %{name}-qt5
Conflicts: %{name}-qt6
Requires: %{name}-common = %{version}-%{release}
%description gtk3 %{desc}

This package provides a GTK3 build of the program.
%endif

%if 0%{?ws_qt5}
%package qt5
Summary: File archiver utility (Qt version)
BuildRequires: lazarus-lcl-qt5
RemovePathPostfixes: .qt5
Conflicts: %{name}-gtk2
Conflicts: %{name}-gtk3
Conflicts: %{name}-qt6
Requires: %{name}-common = %{version}-%{release}
%description qt5 %{desc}

This package provides a Qt5 build of the program.
%endif

%if 0%{?ws_qt6}
%package qt6
Summary: File archiver utility (Qt6 version)
BuildRequires: lazarus-lcl-qt6
RemovePathPostfixes: .qt6
Conflicts: %{name}-gtk2
Conflicts: %{name}-gtk3
Conflicts: %{name}-qt5
Requires: %{name}-common = %{version}-%{release}
%description qt6 %{desc}

This package provides a Qt6 build of the program.
%endif

# -- Subpackages end

%global widgetsets %{expand: \\
%if 0%{?ws_gtk2}
	gtk2 \\
%endif
%if 0%{?ws_gtk3}
	gtk3 \\
%endif
%if 0%{?ws_qt5}
	qt5 \\
%endif
%if 0%{?ws_qt6}
	qt6 \\
%endif
}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}.src

# Patch the project configuration files to enable debuginfo generation
for PROJECT in dev/project_pea.lpi dev/project_peach.lpi; do
	sed  \
		-e 's|<GenerateDebugInfo Value="False"[ ]*/>|<GenerateDebugInfo Value="True"/><DebugInfoType Value="dsDwarf2"/>|g'  \
		-e 's|<StripSymbols Value="True"[ ]*/>|<StripSymbols Value="False"/>|g'  \
		-i "${PROJECT}"
done

# Move around some files so it's easier to install them later
mv res/share/batch/freedesktop_integration/peazip.desktop ./
mv dev/copying_we.txt res/share/copying/

# Remove unused files
rm -rf res/share/batch/
rm -rf res/share/copying/third-parties/
rm -rf res/share/lang-wincontext/
find res/bin -name '*.txt' -delete
rm res/portable

%build

lazbuild \
	--add-package dev/metadarkstyle/metadarkstyle.lpk
for WIDGETSET in %{widgetsets}; do
	lazbuild \
		--widgetset="${WIDGETSET}" \
		--lazarusdir="%{_libdir}/lazarus" \
		-B dev/project_pea.lpi dev/project_peach.lpi
	mv ./dev/pea    "./pea.${WIDGETSET}"
	mv ./dev/peazip "./peazip.${WIDGETSET}"
done
%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}%{_metainfodir}
for WIDGETSET in %{widgetsets}; do
	install -m 755 "./pea.${WIDGETSET}"    %{buildroot}%{_bindir}/
	install -m 755 "./peazip.${WIDGETSET}" %{buildroot}%{_bindir}/
	sed -e "s|WIDGETSET|${WIDGETSET}|g" \
		< "%{SOURCE9}" \
		> "%{buildroot}%{_metainfodir}/%{rtld_name}-${WIDGETSET}.metainfo.xml"
done
install -m 755 -d %{buildroot}%{_datadir}/
cp -a res %{buildroot}%{_datadir}/
mv %{buildroot}%{_datadir}/res %{buildroot}%{_datadir}/%{name}
function link_binary() {
	SRC_NAME="$1"
	DST_DIR="$2"
	DST_NAME="$3"
	DST_DIR="%{buildroot}%{_datadir}/%{name}/bin/${DST_DIR}"
	mkdir -m 755 -p "${DST_DIR}"
	ln -srf "%{buildroot}%{_bindir}/${SRC_NAME}" "${DST_DIR}/${DST_NAME}"
}
link_binary 7z 7z 7z
link_binary arc arc arc
link_binary brotli brotli brotli
link_binary upx upx upx
link_binary unrar-free unrar unrar
link_binary zpaq zpaq zpaq
link_binary zstd zstd zstd
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
ln -srf \
	%{buildroot}%{_datadir}/%{name}/share/icons/peazip.png \
	%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -m 755 -d %{buildroot}%{_datadir}/applications/
install -m 655 %{name}.desktop %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.peazip.PeaZip.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rtld_name}-*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n peazip-common -f %{oreon_filedir}/peazip-common.list
%files -n peazip-gtk2 -f %{oreon_filedir}/peazip-gtk2.list
%files -n peazip-gtk3 -f %{oreon_filedir}/peazip-gtk3.list
%files -n peazip-qt5 -f %{oreon_filedir}/peazip-qt5.list
%files -n peazip-qt6 -f %{oreon_filedir}/peazip-qt6.list

%changelog

%autochangelog
