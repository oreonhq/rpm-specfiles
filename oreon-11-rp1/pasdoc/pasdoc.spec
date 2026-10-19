%global source0_hash 63652c09be4fdcae5ac004917bcdc984404514e9b84582ce9583fae140ec7dfa
Name: pasdoc
Summary:        Documentation tool for Pascal and Object Pascal source code
License: GPL-2.0-or-later
%global with_gui 1
%global with_tools 1
%global with_tests 1
Version: 1.0.4
Release:        1%{?dist}
URL: https://github.com/pasdoc/pasdoc
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10: %{name}.man
Source20: pascal_pre_proc.man
Source21: file_to_pascal_data.man
Source30: %{name}-gui.desktop
Source31: %{name}-gui.metainfo.xml
Patch0: 0000-adapt-test-runner.patch
Patch1: 0001-enable-dwarf3-debuginfo.patch
ExclusiveArch: %{fpc_arches}
%if 0%{?with_gui}
%global widgetset gtk2
%endif
%if 0%{?with_tests}
%endif
# oreon:deps
BuildRequires:  /usr/bin/diff
BuildRequires:  /usr/bin/xmllint
BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  lazarus-lcl-gtk2
BuildRequires:  lazarus-tools
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
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
%oreon_prep
%build

mkdir -p build/bin build/obj
%global fpc_flags -g -gl -gw3 -O3 -Mobjfpc -Sh -FE./build/bin -FU./build/obj
fpc %{fpc_flags} \
	-Fu./source/component \
	-Fu./source/component/tipue \
	-Fu./source/console \
	-Fi./source/component \
	-Fi./source/component/images \
	./source/console/pasdoc.dpr
%if 0%{?with_tests}
	fpc %{fpc_flags} "./tests/fpcunit/test_pasdoc.lpr"
	mv ./build/bin/test_pasdoc ./tests/
%endif
%if 0%{?with_tools}
	for TOOL in pascal_pre_proc file_to_pascal_data file_to_pascal_string; do
		fpc %{fpc_flags} "./source/tools/${TOOL}.dpr"
	done
%endif
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
%if 0%{?with_tools}
install -m 644 -p '%{SOURCE20}' "${MANDIR}/pascal_pre_proc.1"
install -m 644 -p '%{SOURCE21}' "${MANDIR}/file_to_pascal_data.1"
ln -sr "${MANDIR}"/file_to_pascal_{data,string}.1
%endif
%if 0%{?with_gui}
install -m 755 ./source/gui/pasdoc_gui %{buildroot}%{_bindir}/%{name}-gui
for SIZE in 16 32 64 128 256; do
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
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
%files -f %{oreon_filedir}/main.list
%files -n pasdoc-gui -f %{oreon_filedir}/pasdoc-gui.list
%files -n pasdoc-tools -f %{oreon_filedir}/pasdoc-tools.list

%changelog

%autochangelog
