# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a1deed70a6785bbec95a2b2a9e419dc7f7b223a9d74a8644ae611c8e2dcdd354
%global source2_hash 3a7bf3435f7c2ff0beba96422c3356396bcc6601a808e186d9ef6ad1231ebdf9

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global xapian_core_support ON
%global build_wizard ON
%global system_spdlog ON
%global system_fmt ON
%global build_search %{xapian_core_support}
%global clang_support ON
%global system_sqlite3 ON
%global build_doc OFF

Summary: A documentation system for C/C++
Name:    doxygen
Epoch:   2
Version:        1.18.0
Release:        2%{?dist}
# No version is specified.
License: GPL-2.0-or-later
Url: https://github.com/doxygen
Source0:        https://www.doxygen.nl/files/doxygen-%{version}.src.tar.gz
# this icon is part of kdesdk
Source1: doxywizard.desktop
# these icons are part of doxygen and converted from doxywizard.ico
Source2: doxywizard-icons.tar.bz2
Source3: README.rpm-packaging
Source4: doxygen-unbundler

# upstream fixes

BuildRequires: %{_bindir}/python3
BuildRequires: perl-interpreter, perl-open
BuildRequires: web-assets-devel
# Building an RPM package typically needs unbundling of Javascript assets.
Requires: (js-doxygen if oreon-rpm-config)


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
BuildRequires:  oreon-rpm-macros

%description doxywizard
Doxywizard is a GUI for creating and editing configuration files that
are used by doxygen.
%endif



%prep
%oreon_sha256
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -

%autosetup -p1 -a2
rm -f testing/012_cite.dox

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
%if "%{build_doc}" == "ON"
%cmake_build %{?_smp_mflags} --target docs
%endif

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
%%doxygen_unbundle_buildroot() %%{_rpmconfigdir}/oreon/doxygen-unbundler "%{_jsdir}" "%%{buildroot}" %%[ %%# == 0 ? "%%{_docdir}" : "%%1"]
%%doxygen_unbundle() %{_rpmconfigdir}/oreon/doxygen-unbundler "%{_jsdir}" "" %%*
EOF

 # Install the unbundler script.
install -m755 -D --target-directory=%{buildroot}%{_rpmconfigdir}/oreon %{SOURCE4}

%check
%ctest

%files
%doc LANGUAGE.HOWTO README.md README.rpm-packaging
%if "%{build_doc}" == "ON"
%doc %{__cmake_builddir}/latex/doxygen_manual.pdf
%doc %{__cmake_builddir}/html
%endif
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
%{_rpmconfigdir}/oreon/doxygen-unbundler
%if "%{build_wizard}" == "ON"
%files doxywizard
%{_bindir}/doxywizard
%{_mandir}/man1/doxywizard*
%{_datadir}/applications/doxywizard.desktop
%{_datadir}/icons/hicolor/*/apps/doxywizard.png
%endif

%files -n js-doxygen
%{_jsdir}/doxygen/*



%changelog
%autochangelog
