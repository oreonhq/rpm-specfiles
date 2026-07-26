%global source0_hash 46f850254a67888ce0fe1f67e5022cf1c2a1acac73ad6dc29f85fcfd6ebe7ec8

Name: pasdoc
Summary: Documentation tool for Pascal and Object Pascal source code

# The readme says simply "GNU GPL 2", but license headers in code files
# say "version 2 of the License, or (at your option) any later version".
License: GPL-2.0-or-later

%global with_gui 1
%global with_tools 1
%global with_tests 1

Version: 0.16.0
Release: 15%{?dist}

URL: https://github.com/pasdoc/pasdoc
Source0: %{URL}/archive/v%{version}/pasdoc-%{version}.tar.gz

# Submitted upstream: https://github.com/pasdoc/pasdoc/pull/135
Source10: %{name}.man
Source20: pascal_pre_proc.man
Source21: file_to_pascal_data.man

Source30: %{name}-gui.desktop
Source31: %{name}-gui.metainfo.xml

# The test runner script always rebuilds the program from scratch
# before actually performing any tests.
Patch0: 0000-adapt-test-runner.patch

# Edit the project configuration files to enable DWARF3 debuginfo
Patch1: 0001-enable-dwarf3-debuginfo.patch

ExclusiveArch: %{fpc_arches}

BuildRequires: fpc

%if 0%{?with_gui}
%global widgetset gtk2
BuildRequires: desktop-file-utils
BuildRequires: lazarus-lcl-%{widgetset}
BuildRequires: lazarus-tools
BuildRequires: libappstream-glib
%endif

%if 0%{?with_tests}
BuildRequires: make
BuildRequires: %{_bindir}/diff
BuildRequires: %{_bindir}/xmllint
%endif

%description
PasDoc is a documentation tool for Pascal and Object Pascal source code.
Documentation is generated from comments found in the source code, or from
external files. Numerous formatting @-tags are supported. Many output formats
are supported, including HTML and LaTeX.

%if 0%{?with_gui}
%package gui
Summary: Graphical user interface for the PasDoc documentation generator
Requires: hicolor-icon-theme

%description gui
PasDoc is a documentation tool for Pascal and Object Pascal source code.

This package provides a graphical user interface for PasDoc, allowing to
generate documentation files from previously annotated source code.
%endif

%if 0%{?with_tools}
%package tools
Summary: Helper tools for PasDoc

%description tools
Helper tools useful for analyzing Pascal code
and embedding files (both text and binary) inside Pascal sources.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# The upsteam source contains a Makefile, but it sets many compiler options
# such as range checking code, optimization level, and so on.
#
# Instead of using the Makefile, let's compile manually,
# so that Fedora's default settings for FPC are applied.
mkdir -p build/bin build/obj
%global fpc_flags -g -gl -gw3 -O3 -Mobjfpc -Sh -FE./build/bin -FU./build/obj

fpc %{fpc_flags} \
	-Fu./source/component \
	-Fu./source/component/tipue \
	-Fu./source/console \
	-Fi./source/component \
	-Fi./source/component/images \
	./source/console/pasdoc.dpr

# Build the unit test app
%if 0%{?with_tests}
	fpc %{fpc_flags} "./tests/fpcunit/test_pasdoc.lpr"
	mv ./build/bin/test_pasdoc ./tests/
%endif

# Build the helper tools
%if 0%{?with_tools}
	for TOOL in pascal_pre_proc file_to_pascal_data file_to_pascal_string; do
		fpc %{fpc_flags} "./source/tools/${TOOL}.dpr"
	done
%endif

# Build the gui
%if 0%{?with_gui}
	lazbuild --add-package-link ./source/packages/lazarus/pasdoc_package.lpk
	lazbuild --widgetset=%{widgetset} --recursive ./source/gui/pasdoc_gui.lpi
%endif

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} ./build/bin/*

MANDIR="%{buildroot}%{_mandir}/man1"
install -m 755 -d "${MANDIR}"
install -m 644 -p '%{SOURCE10}' "${MANDIR}/%{name}.1"

# Install man pages for tools.
# file_to_pascal_data and file_to_pascal_string are almost the same,
# so the single man page covers them both.
%if 0%{?with_tools}
install -m 644 -p '%{SOURCE20}' "${MANDIR}/pascal_pre_proc.1"
install -m 644 -p '%{SOURCE21}' "${MANDIR}/file_to_pascal_data.1"
ln -sr "${MANDIR}"/file_to_pascal_{data,string}.1
%endif

%if 0%{?with_gui}
install -m 755 ./source/gui/pasdoc_gui %{buildroot}%{_bindir}/%{name}-gui

for SIZE in 16 32 64 128 256; do
	# Icon files use zero-padded three-digit numbers in their names
	PADSIZ="$(printf '%%03d' "${SIZE}")"
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps"

	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p \
		"./source/gui/icons/PasDoc${PADSIZ}.png" \
		"${ICON_DIR}/%{name}-gui.png"
done

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p -t %{buildroot}%{_datadir}/applications '%{SOURCE30}'

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p -t %{buildroot}%{_metainfodir} '%{SOURCE31}'
%endif

%check
%if 0%{?with_tests}
export PASDOC_BIN="$(pwd)/build/bin/pasdoc"
export USE_DIFF_TO_COMPARE="true"

cd tests/
./test_pasdoc -a
./run_all_tests.sh
%endif

%if 0%{?with_gui}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}-gui.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop
%endif

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%if 0%{?with_tools}
%files tools
%license LICENSE
%{_bindir}/file_to_pascal_data
%{_bindir}/file_to_pascal_string
%{_bindir}/pascal_pre_proc
%{_mandir}/man1/file_to_pascal_data.1*
%{_mandir}/man1/file_to_pascal_string.1*
%{_mandir}/man1/pascal_pre_proc.1*
%endif

%if 0%{?with_gui}
%files gui
%doc source/gui/HISTORY
%doc source/gui/README
%doc source/gui/TODO
%license LICENSE
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}-gui.png
%{_metainfodir}/%{name}-gui.metainfo.xml
%endif

%changelog
%autochangelog
