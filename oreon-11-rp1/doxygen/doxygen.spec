%global source0_hash a1deed70a6785bbec95a2b2a9e419dc7f7b223a9d74a8644ae611c8e2dcdd354
%global xapian_core_support OFF
%global build_wizard OFF
%global system_spdlog OFF
%global system_fmt OFF
%global build_search %{xapian_core_support}
%global clang_support ON
%global system_sqlite3 ON
%global build_doc OFF
%bcond_with doxygen_latex 0
Summary:        A documentation system for C/C++
Name:    doxygen
Epoch:   2
Version: 1.18.0
Release:        1%{?dist}
License: GPL-2.0-or-later
Url: https://github.com/doxygen
Source0:        https://www.doxygen.nl/files/%{name}-%{version}.src.tar.gz
Source1: doxywizard.desktop
Source2: doxywizard-icons.tar.xz
Source3: README.rpm-packaging
Source4: doxygen-unbundler
%if %{with doxygen_latex}
%endif
Requires: (js-doxygen if redhat-rpm-config)
%if ! 0%{?_module_build} && "%{build_doc}" == "ON"
%endif
%if "%{build_wizard}" == "ON"
%endif
%if "%{?xapian_core_support}" == "ON"
%endif
%if "%{clang_support}" == "ON"
%else
%endif
%if "%{system_spdlog}" == "ON"
%else
Provides: bundled(spdlog) = 1.14.1
%endif
%if "%{system_sqlite3}" == "ON"
%else
Provides: bundled(sqlite) = 3.42.0
%endif
%if "%{system_fmt}" == "ON"
%else
Provides: bundled(fmt) = 10.2.1
%endif
Requires: perl-interpreter
Requires: graphviz
# oreon:deps
BuildRequires:  /usr/bin/python3
BuildRequires:  bison
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  git
BuildRequires:  llvm-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-open
BuildRequires:  sqlite-devel
BuildRequires:  web-assets-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%description latex
%{summary}.
%endif
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}/%{_mandir}/man1
cp doc/*.1 %{buildroot}/%{_mandir}/man1/
%if "%{build_wizard}" == "OFF"
rm -f %{buildroot}/%{_mandir}/man1/doxywizard.1*
%else
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
rm -rf %{buildroot}/%{_docdir}/packages
install -m644 -D --target-directory=%{buildroot}%{_jsdir}/doxygen templates/html/*.js
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.doxygen <<'EOF'
%%doxygen_js_requires() Requires: js-doxygen >= %{version}-%{release}
%%doxygen_unbundle_buildroot() %%{_rpmconfigdir}/redhat/doxygen-unbundler "%{_jsdir}" "%%{buildroot}" %%[ %%# == 0 ? "%%{_docdir}" : "%%1"]
%%doxygen_unbundle() %{_rpmconfigdir}/redhat/doxygen-unbundler "%{_jsdir}" "" %%*
EOF
install -m755 -D --target-directory=%{buildroot}%{_rpmconfigdir}/redhat %{SOURCE4}
%oreon_autofiles js-doxygen usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest -E 012_cite
%files -f %{oreon_filedir}/main.list
%files -n js-doxygen -f %{oreon_filedir}/js-doxygen.list

%changelog

%autochangelog
