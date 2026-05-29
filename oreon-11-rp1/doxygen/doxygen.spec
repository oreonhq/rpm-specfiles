%global source0_hash 201ce33b514ea87cc1697c0dcf829692c2695c1812683a9cc622194b05e263a8

%if 0%{?fedora}
%global xapian_core_support ON
%global build_wizard ON
%global system_spdlog ON
%global system_fmt ON
%else
%global xapian_core_support OFF
%global build_wizard OFF
%global system_spdlog OFF
%global system_fmt OFF
%endif
%global build_search %{xapian_core_support}
%global clang_support ON
%global system_sqlite3 ON
%global build_doc OFF
# Fedora split texlive-* specs are not in oreon-11-rp1 yet; latex meta needs them.
%bcond_with doxygen_latex 0

Summary: A documentation system for C/C++
Name:    doxygen
Epoch:   2
Version: 1.16.1
Release: 3%{?dist}
# No version is specified.
License: GPL-2.0-or-later
Url: https://github.com/doxygen
Source0:        https://www.doxygen.nl/files/doxygen-1.16.1.src.tar.gz
# this icon is part of kdesdk
Source1: doxywizard.desktop
# hicolor PNGs from doxywizard.ico; ship doxywizard-icons.tar.xz next to this spec
Source2: doxywizard-icons.tar.xz
Source3: README.rpm-packaging
Source4: doxygen-unbundler

# upstream fixes

BuildRequires: %{_bindir}/python3
BuildRequires: perl-interpreter, perl-open
%if %{with doxygen_latex}
BuildRequires: texlive-bibtex
%endif
BuildRequires: web-assets-devel
# Building an RPM package typically needs unbundling of Javascript assets.
Requires: (js-doxygen if redhat-rpm-config)

%if ! 0%{?_module_build} && "%{build_doc}" == "ON"
BuildRequires: tex(dvips)
BuildRequires: tex(latex)
# From doc/manual.sty
BuildRequires: tex(helvet.sty)
BuildRequires: tex(sectsty.sty)
BuildRequires: tex(tocloft.sty)
BuildRequires: tex(fontenc.sty)
BuildRequires: tex(fancyhdr.sty)
# From templates/latex/doxygen.sty
BuildRequires: tex(alltt.sty)
BuildRequires: tex(calc.sty)
BuildRequires: tex(float.sty)
BuildRequires: tex(verbatim.sty)
BuildRequires: tex(xcolor.sty)
BuildRequires: tex(fancyvrb.sty)
BuildRequires: tex(tabularx.sty)
BuildRequires: tex(multirow.sty)
BuildRequires: tex(hanging.sty)
BuildRequires: tex(ifpdf.sty)
BuildRequires: tex(adjustbox.sty)
BuildRequires: tex(amssymb.sty)
BuildRequires: tex(stackengine.sty)
BuildRequires: tex(ulem.sty)
# From doc/doxygen_manual.tex
BuildRequires: tex(ifthen.sty)
BuildRequires: tex(array.sty)
BuildRequires: tex(geometry.sty)
BuildRequires: tex(makeidx.sty)
BuildRequires: tex(natbib.sty)
BuildRequires: tex(graphicx.sty)
BuildRequires: tex(multicol.sty)
BuildRequires: tex(float.sty)
BuildRequires: tex(geometry.sty)
BuildRequires: tex(listings.sty)
BuildRequires: tex(color.sty)
BuildRequires: tex(xcolor.sty)
BuildRequires: tex(textcomp.sty)
BuildRequires: tex(wasysym.sty)
BuildRequires: tex(import.sty)
BuildRequires: tex(appendix.sty)
BuildRequires: tex(hyperref.sty)
BuildRequires: tex(pspicture.sty)
BuildRequires: tex(inputenc.sty)
BuildRequires: tex(mathptmx.sty)
BuildRequires: tex(courier.sty)
# From src/latexgen.cpp
BuildRequires: tex(fixltx2e.sty)
BuildRequires: tex(ifxetex.sty)
BuildRequires: tex(caption.sty)
BuildRequires: tex(etoc.sty)
# From src/util.cpp
BuildRequires: tex(newunicodechar.sty)
# From templates/latex/tabu_doxygen.sty
BuildRequires: tex(varwidth.sty)
BuildRequires: tex(xtab.sty)
BuildRequires: tex(tabu.sty)
BuildRequires: /usr/bin/epstopdf
BuildRequires: texlive-epstopdf
BuildRequires: ghostscript
BuildRequires: gettext
BuildRequires: graphviz
%endif

%if "%{build_wizard}" == "ON"
BuildRequires: desktop-file-utils
%endif

BuildRequires: zlib-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: cmake
BuildRequires: git

%if "%{?xapian_core_support}" == "ON"
BuildRequires: xapian-core-devel
%endif

%if "%{clang_support}" == "ON"
BuildRequires: llvm-devel
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++ gcc
%endif

%if "%{system_spdlog}" == "ON"
BuildRequires: spdlog-devel
%else
# SPDLOG_VER* defined in deps/spdlog/include/spdlog/version.h
Provides: bundled(spdlog) = 1.14.1
%endif

%if "%{system_sqlite3}" == "ON"
BuildRequires: sqlite-devel
%else
# SQLITE_VERSION defined in deps/sqlite3/sqlite3.h
Provides: bundled(sqlite) = 3.42.0
%endif

%if "%{system_fmt}" == "ON"
BuildRequires: fmt-devel
%else
# deps/fmt/README.md
Provides: bundled(fmt) = 10.2.1
%endif

Requires: perl-interpreter
Requires: graphviz

%description
Doxygen can generate an online class browser (in HTML) and/or a
reference manual (in LaTeX) from a set of documented source files. The
documentation is extracted directly from the sources. Doxygen can
also be configured to extract the code structure from undocumented
source files.

%package -n js-doxygen
Summary: Javascript files used by Doxygen
Requires: web-assets-filesystem
BuildArch: noarch
%description -n js-doxygen
Javascript files for use by locally installed Doxygen documentation.

%if  "%{build_wizard}" == "ON"
%package doxywizard
Summary: A GUI for creating and editing configuration files
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtsvg-devel

%description doxywizard
Doxywizard is a GUI for creating and editing configuration files that
are used by doxygen.
%endif

%if ! 0%{?_module_build}
%if %{with doxygen_latex}
%package latex
Summary: Support for producing latex/pdf output from doxygen
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: tex(latex)
Requires: tex(dvips)
Requires: texlive-wasy
%if 0%{?fedora} > 17 || 0%{?rhel} > 6
# From doc/manual.sty
Requires: tex(helvet.sty)
Requires: tex(sectsty.sty)
Requires: tex(tocloft.sty)
Requires: tex(fontenc.sty)
Requires: tex(fancyhdr.sty)
# From templates/latex/doxygen.sty
Requires: tex(alltt.sty)
Requires: tex(calc.sty)
Requires: tex(float.sty)
Requires: tex(verbatim.sty)
Requires: tex(xcolor.sty)
Requires: tex(fancyvrb.sty)
Requires: tex(tabularx.sty)
Requires: tex(multirow.sty)
Requires: tex(hanging.sty)
Requires: tex(ifpdf.sty)
Requires: tex(adjustbox.sty)
Requires: tex(amssymb.sty)
Requires: tex(stackengine.sty)
Requires: tex(ulem.sty)
Requires: tex(xltabular.sty)
Requires: tex(tabularray.sty)
Requires: tex(enumitem.sty)
Requires: tex(alphalph.sty)
# From doc/doxygen_manual.tex
Requires: tex(ifthen.sty)
Requires: tex(array.sty)
Requires: tex(geometry.sty)
Requires: tex(makeidx.sty)
Requires: tex(natbib.sty)
Requires: tex(graphicx.sty)
Requires: tex(multicol.sty)
Requires: tex(float.sty)
Requires: tex(geometry.sty)
Requires: tex(listings.sty)
Requires: tex(color.sty)
Requires: tex(xcolor.sty)
Requires: tex(textcomp.sty)
Requires: tex(wasysym.sty)
Requires: tex(import.sty)
Requires: tex(appendix.sty)
Requires: tex(hyperref.sty)
Requires: tex(pspicture.sty)
Requires: tex(inputenc.sty)
Requires: tex(mathptmx.sty)
Requires: tex(courier.sty)
# From src/latexgen.cpp
Requires: tex(fixltx2e.sty)
Requires: tex(ifxetex.sty)
Requires: tex(caption.sty)
Requires: tex(etoc.sty)
# From src/util.cpp
Requires: tex(newunicodechar.sty)
# From templates/latex/tabu_doxygen.sty
Requires: tex(varwidth.sty)
# I'm 99% sure this isn't needed anymore since
# doxygen has a local fork of tabu... but it doesn't seem to be hurting anything.
Requires: tex(tabu.sty)
# There also does not seem to be any references to xtab in the code... but eh.
Requires: tex(xtab.sty)
# Explicitly called binaries
Requires: texlive-bibtex
Requires: texlive-makeindex
Requires: texlive-epstopdf
# fonts
Requires: texlive-collection-fontsrecommended
%endif

%description latex
%{summary}.
%endif
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -a2

cp %{SOURCE3} .

%build
%cmake \
	-Dbuild_wizard=%{build_wizard} \
	-DBUILD_SHARED_LIBS=OFF \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-Dbuild_search=%{build_search} \
	-Duse_libclang=%{clang_support} \
	-DMAN_INSTALL_DIR=%{_mandir}/man1 \
	-Dbuild_doc=%{build_doc} \
	-DPYTHON_EXECUTABLE=%{_bindir}/python3 \
	-Dbuild_xmlparser=ON \
	-Duse_sys_sqlite3=%{system_sqlite3} \
	-Duse_sys_spdlog=%{system_spdlog} \
	-Duse_sys_fmt=%{system_fmt}

%cmake_build %{?_smp_mflags}

%install
%cmake_install

# install man pages
mkdir -p %{buildroot}/%{_mandir}/man1
cp doc/*.1 %{buildroot}/%{_mandir}/man1/

%if "%{build_wizard}" == "OFF"
rm -f %{buildroot}/%{_mandir}/man1/doxywizard.1*
%else
# install icons
icondir=%{buildroot}%{_datadir}/icons/hicolor
mkdir -m755 -p $icondir/{16x16,32x32,48x48,128x128}/apps
install -m644 -p -D doxywizard-6.png $icondir/16x16/apps/doxywizard.png
install -m644 -p -D doxywizard-5.png $icondir/32x32/apps/doxywizard.png
install -m644 -p -D doxywizard-4.png $icondir/48x48/apps/doxywizard.png
install -m644 -p -D doxywizard-3.png $icondir/128x128/apps/doxywizard.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
%endif

%if "%{xapian_core_support}" == "OFF"
rm -f %{buildroot}/%{_mandir}/man1/doxyindexer.1* %{buildroot}/%{_mandir}/man1/doxysearch.1*
%endif

# remove duplicate
rm -rf %{buildroot}/%{_docdir}/packages

# Install the asset files.
install -m644 -D --target-directory=%{buildroot}%{_jsdir}/doxygen templates/html/*.js

# Generate the macros file.  Expand version/release/%%_jsdir.
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.doxygen <<'EOF'
%%doxygen_js_requires() Requires: js-doxygen >= %{version}-%{release}
%%doxygen_unbundle_buildroot() %%{_rpmconfigdir}/redhat/doxygen-unbundler "%{_jsdir}" "%%{buildroot}" %%[ %%# == 0 ? "%%{_docdir}" : "%%1"]
%%doxygen_unbundle() %{_rpmconfigdir}/redhat/doxygen-unbundler "%{_jsdir}" "" %%*
EOF

 # Install the unbundler script.
install -m755 -D --target-directory=%{buildroot}%{_rpmconfigdir}/redhat %{SOURCE4}

%check
%ctest

%files
%doc LANGUAGE.HOWTO README.md README.rpm-packaging
%license LICENSE
%if ! 0%{?_module_build}
%if "%{xapian_core_support}" == "ON"
%{_bindir}/doxyindexer
%{_bindir}/doxysearch*
%endif
%endif
%{_bindir}/doxygen
%{_mandir}/man1/doxygen.1*
%if "%{xapian_core_support}" == "ON"
%{_mandir}/man1/doxyindexer.1*
%{_mandir}/man1/doxysearch.1*
%endif
%{_rpmconfigdir}/macros.d/macros.doxygen
%{_rpmconfigdir}/redhat/doxygen-unbundler
%if "%{build_wizard}" == "ON"
%files doxywizard
%{_bindir}/doxywizard
%{_mandir}/man1/doxywizard*
%{_datadir}/applications/doxywizard.desktop
%{_datadir}/icons/hicolor/*/apps/doxywizard.png
%endif

%files -n js-doxygen
%{_jsdir}/doxygen/*

%if ! 0%{?_module_build}
%if %{with doxygen_latex}
%files latex
# intentionally left blank
%endif
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16.1-3
- Prepare for Oreon 11 (RP1)
