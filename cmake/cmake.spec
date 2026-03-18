# Do we add appdata-files?
# consider conditional on whether %%_metainfodir is defined or not instead -- rex
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without appdata
%else
%bcond_with appdata
%endif

# Set to bcond_without or use --with bootstrap if bootstrapping a new release
# or architecture
%bcond_with bootstrap

# Build with Emacs support
%bcond_without emacs

# Run git tests
%bcond_without git_test

# Set to bcond_with or use --without gui to disable qt gui build
%bcond_without gui

# Use ncurses for colorful output
%bcond_without ncurses

# Setting the Python-version used by default
%if 0%{?rhel} && 0%{?rhel} < 8
%bcond_with python3
%else
%bcond_without python3
%endif

# Enable RPM dependency generators for cmake files written in Python
%bcond_without rpm

%bcond_without sphinx

%if !0%{?rhel}
%bcond_with bundled_jsoncpp
%bcond_with bundled_rhash
%else
%bcond_without bundled_jsoncpp
%bcond_without bundled_rhash
%endif

# cppdap is currently shipped as a static lib from upstream,
# so we do not have it in the repos.
%bcond_without bundled_cppdap

# Run tests
# ... except i686.
%ifnarch i686
%bcond_without test
%else
%bcond_with test
%endif

# Enable X11 tests
%bcond_without X11_test

# Do not build non-lto objects to reduce build time significantly.
%global build_cflags   %(echo '%{build_cflags}'   | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')
%global build_cxxflags %(echo '%{build_cxxflags}' | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')
%global build_fflags   %(echo '%{build_fflags}' | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')
%global build_fcflags  %(echo '%{build_fflags}' | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')

# Setup _pkgdocdir if not defined already
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Setup _vpath_builddir if not defined already
%{!?_vpath_builddir:%global _vpath_builddir %{_target_platform}}

%global major_version 4
%global minor_version 2
%global patch_version 3

# For handling bump release by rpmdev-bumpspec and mass rebuild
%global baserelease 2

# Set to RC version if building RC, else comment out.
#%%global rcsuf rc3

%if 0%{?rcsuf:1}
%global pkg_version %{major_version}.%{minor_version}.%{patch_version}~%{rcsuf}
%global tar_version %{major_version}.%{minor_version}.%{patch_version}-%{rcsuf}
%else
%global pkg_version %{major_version}.%{minor_version}.%{patch_version}
%global tar_version %{major_version}.%{minor_version}.%{patch_version}
%endif

# Uncomment if building for EPEL
#global name_suffix %%{major_version}
%global orig_name cmake

Name:           %{orig_name}%{?name_suffix}
Version:        %{pkg_version}
Release:        %{baserelease}%{?dist}
Summary:        Cross-platform make system

# most sources are BSD
# Source/CursesDialog/form/ a bunch is MIT
# Source/kwsys/MD5.c is zlib
# some GPL-licensed bison-generated files, which all include an
# exception granting redistribution under terms of your choice
License:        BSD-3-Clause AND MIT-open-group AND Zlib%{?with_bundled_cppdap: AND Apache-2.0}
URL:            http://www.cmake.org
Source0:        http://www.cmake.org/files/v%{major_version}.%{minor_version}/%{orig_name}-%{tar_version}.tar.gz
Source1:        %{name}-init.el
Source2:        macros.%{name}.in
Source3:        macros.aaa-%{name}-srpm
# See https://bugzilla.redhat.com/show_bug.cgi?id=1202899
Source4:        %{name}.attr
Source5:        %{name}.prov
Source6:        %{name}.req

# Always start regular patches with numbers >= 100.
# We need lower numbers for patches in compat package.
# And this enables us to use %%autosetup
#
# Patch to fix RindRuby vendor settings
# http://public.kitware.com/Bug/view.php?id=12965
# https://bugzilla.redhat.com/show_bug.cgi?id=822796
# TODO: Find better wat to handle this
Patch100:       %{name}-findruby.patch
# apply upstream fix for FindLua.cmake which is ... not getting pulled into their tarballs?!?
Patch101:	https://github.com/Kitware/CMake/commit/261b7b933c6604095687d473503e24bae6ec0d6f.patch

# TODO: Remove this patch
# Patch for renaming on EPEL
%if 0%{?name_suffix:1}
Patch1:         %{name}-rename.patch
%endif

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  sed
%if %{with git_test}
# Tests fail if only git-core is installed, bug #1488830
BuildRequires:  git
%else
BuildConflicts: git-core
%endif
%if %{with X11_test}
BuildRequires:  libX11-devel
%endif
%if %{with ncurses}
BuildRequires:  ncurses-devel
%endif
%if %{with sphinx}
BuildRequires:  %{_bindir}/sphinx-build
%endif
%if %{without bootstrap}
BuildRequires:  bzip2-devel
BuildRequires:  curl-devel
%if %{with bundled_cppdap}
Provides: bundled(cppdap)
%else
BuildRequires:  cppdap-devel
%endif
BuildRequires:  expat-devel
%if %{with bundled_jsoncpp}
Provides: bundled(jsoncpp)
%else
BuildRequires:  jsoncpp-devel
%endif
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  libarchive-devel
%else
BuildRequires:  libarchive3-devel
%endif
BuildRequires:  libuv-devel
%if %{with bundled_rhash}
Provides:  bundled(rhash)
%else
BuildRequires:  rhash-devel
%endif
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  vim-filesystem
%endif
%if %{with emacs}
BuildRequires:  emacs
%endif
BuildRequires:  openssl-devel
%if %{with rpm}
%if %{with python3}
%{!?python3_pkgversion: %global python3_pkgversion 3}
BuildRequires:  python%{python3_pkgversion}-devel
%else
BuildRequires:  python2-devel
%endif
%endif
%if %{with gui}
%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires: pkgconfig(Qt6Widgets)
%elif 0%{?rhel} > 7
BuildRequires: pkgconfig(Qt5Widgets)
%else
BuildRequires: pkgconfig(QtGui)
%endif
BuildRequires: desktop-file-utils
%endif

BuildRequires: pkgconfig(bash-completion)
%global bash_completionsdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo '%{_datadir}/bash-completion/completions')

%if %{without bootstrap}
# Ensure we have our own rpm-macros in place during build.
BuildRequires:  %{name}-rpm-macros
%endif
BuildRequires: make

Requires:       %{name}-data = %{version}-%{release}
Requires:       (%{name}-rpm-macros = %{version}-%{release} if rpm-build)
Requires:       %{name}-filesystem%{?_isa} = %{version}-%{release}

# TODO: Change to the latter design. Currently blocked by various `Requires: make` in dependency chains
#   Also relevant for user configuration: https://gitlab.kitware.com/cmake/cmake/-/issues/26891
Requires:       make

# Explicitly require the generators with ninja-build as the default
# Requires:       (ninja-build or make)
# Suggests:       ninja-build

# Provide the major version name
Provides: %{orig_name}%{major_version} = %{version}-%{release}

# Source/kwsys/MD5.c
# see https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries
Provides: bundled(md5-deutsch)

# https://fedorahosted.org/fpc/ticket/555
Provides: bundled(kwsys)

%description
CMake is used to control the software compilation process using simple
platform and compiler independent configuration files. CMake generates
native makefiles and workspaces that can be used in the compiler
environment of your choice. CMake is quite sophisticated: it is possible
to support complex environments requiring system configuration, preprocessor
generation, code generation, and template instantiation.


%package        data
Summary:        Common data-files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       (%{name}-rpm-macros = %{version}-%{release} if rpm-build)
%if %{with emacs}
%if 0%{?fedora} || 0%{?rhel} >= 7
Requires:       emacs-filesystem%{?_emacs_version: >= %{_emacs_version}}
%endif
%endif
Requires:       vim-filesystem

BuildArch:      noarch

%description    data
This package contains common data-files for %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains documentation for %{name}.


%package        filesystem
Summary:        Directories used by CMake modules

%description    filesystem
This package owns all directories used by CMake modules.


%if %{with gui}
%package        gui
Summary:        Qt GUI for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       shared-mime-info%{?_isa}

%description    gui
The %{name}-gui package contains the Qt based GUI for %{name}.
%endif


%package        rpm-macros
Summary:        Common RPM macros for %{name}
Requires:       rpm
# when subpkg introduced
Conflicts:      cmake-data < 3.10.1-2

# Related to the ninja default generator, see the TODO note above on how this should be changed
# Suggests:       ninja-build
Requires:       ninja-build

BuildArch:      noarch

%description    rpm-macros
This package contains common RPM macros for %{name}.


%package        srpm-macros
Summary:        Common SRPM macros for %{name}
Requires:       rpm

BuildArch:      noarch

%description    srpm-macros
This package contains common SRPM macros for %{name}.


%package -n python3-cmake
Summary:        Python metadata for packages depending on %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch:      noarch

%description -n python3-cmake
Package provides metadata for Python packages depending on cmake.
This is to make automatic dependency resolution work. The package is NOT
using anything from the PyPI package called cmake.


%prep
%autosetup -n %{orig_name}-%{tar_version} -p 1

%if %{with rpm}
%if %{with python3}
echo '#!%{__python3}' > %{name}.prov
echo '#!%{__python3}' > %{name}.req
%else
echo '#!%{__python2}' > %{name}.prov
echo '#!%{__python2}' > %{name}.req
%endif
tail -n +2 %{SOURCE5} >> %{name}.prov
tail -n +2 %{SOURCE6} >> %{name}.req
%endif


%build
%{set_build_flags}
SRCDIR="$(/usr/bin/pwd)"
mkdir %{_vpath_builddir}
pushd %{_vpath_builddir}
$SRCDIR/bootstrap --prefix=%{_prefix} \
                  --datadir=/share/%{name} \
                  --docdir=/share/doc/%{name} \
                  --mandir=/share/man \
                  --%{?with_bootstrap:no-}system-libs \
                  --parallel="$(echo %{?_smp_mflags} | sed -e 's|-j||g')" \
%if %{with bundled_cppdap}
                  --no-system-cppdap \
%endif
%if %{with bundled_rhash}
                  --no-system-librhash \
%endif
%if %{with bundled_jsoncpp}
                  --no-system-jsoncpp \
%endif
%if %{with sphinx}
                  --sphinx-man --sphinx-html \
%else
                  --sphinx-build=%{_bindir}/false \
%endif
                  --%{!?with_gui:no-}qt-gui \
                  -- \
                  -DCMAKE_C_FLAGS_RELEASE:STRING="-O2 -g -DNDEBUG" \
                  -DCMAKE_CXX_FLAGS_RELEASE:STRING="-O2 -g -DNDEBUG" \
                  -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-O2 -g -DNDEBUG" \
                  -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
                  -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \
                  -DCMake_TEST_NO_NETWORK:BOOL=ON
popd
%make_build -C %{_vpath_builddir}

# Provide Python metadata
%global cmake_distinfo cmake-%{major_version}.%{minor_version}.%{patch_version}%{?rcsuf}.dist-info
mkdir %{cmake_distinfo}
cat > %{cmake_distinfo}/METADATA << EOF
Metadata-Version: 2.1
Name: cmake
Version: %{major_version}.%{minor_version}.%{patch_version}%{?rcsuf}
Summary: %{summary}
Description-Content-Type: text/plain

Metadata only package for automatic dependency resolution in the RPM
ecosystem. This package is separate from the PyPI package called cmake.
EOF
echo rpm > %{cmake_distinfo}/INSTALLER


%install
mkdir -p %{buildroot}%{_pkgdocdir}
%make_install -C %{_vpath_builddir} CMAKE_DOC_DIR=%{buildroot}%{_pkgdocdir}
find %{buildroot}%{_datadir}/%{name}/Modules -type f | xargs chmod -x
[ -n "$(find %{buildroot}%{_datadir}/%{name}/Modules -name \*.orig)" ] &&
  echo "Found .orig files in %{_datadir}/%{name}/Modules, rebase patches" &&
  exit 1
# Install major_version name links
%{!?name_suffix:for f in ccmake cmake cpack ctest; do ln -s $f %{buildroot}%{_bindir}/${f}%{major_version}; done}

%if %{with emacs}
# Install emacs cmake mode
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name} %{buildroot}%{_emacs_sitestartdir}
mv %{buildroot}%{_emacs_sitelispdir}/%{name}-mode.el %{buildroot}%{_emacs_sitelispdir}/%{name}
%{_emacs_bytecompile} %{buildroot}%{_emacs_sitelispdir}/%{name}/%{name}-mode.el
install -p -m 0644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}
%else
rm -f %{buildroot}%{_emacs_sitelispdir}
%endif
# RPM macros
install -p -m0644 -D %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.%{name}
install -p -m0644 -D %{SOURCE3} %{buildroot}%{_rpmmacrodir}/macros.aaa-%{name}-srpm
sed -i -e "s|@@CMAKE_VERSION@@|%{version}|" -e "s|@@CMAKE_MAJOR_VERSION@@|%{major_version}|" %{buildroot}%{_rpmmacrodir}/macros.%{name}
touch -r %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.%{name}
%if %{with rpm} && 0%{?_rpmconfigdir:1}
# RPM auto provides
install -p -m0644 -D %{SOURCE4} %{buildroot}%{_prefix}/lib/rpm/fileattrs/%{name}.attr
install -p -m0755 -D %{name}.prov %{buildroot}%{_prefix}/lib/rpm/%{name}.prov
install -p -m0755 -D %{name}.req %{buildroot}%{_prefix}/lib/rpm/%{name}.req
%endif
mkdir -p %{buildroot}%{_libdir}/%{orig_name}
# Install copyright files for main package
find Source Utilities -type f -iname copy\* | while read f
do
  fname=$(basename $f)
  dir=$(dirname $f)
  dname=$(basename $dir)
  cp -p $f ./${fname}_${dname}
done
%if %{with bundled_cppdap}
cp -p Utilities/cmcppdap/LICENSE LICENSE.cppdap
cp -p Utilities/cmcppdap/NOTICE NOTICE.cppdap
%endif
# Cleanup pre-installed documentation
%if %{with sphinx}
mv %{buildroot}%{_docdir}/%{name}/html .
%endif
rm -rf %{buildroot}%{_docdir}/%{name}
# Install documentation to _pkgdocdir
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr %{buildroot}%{_datadir}/%{name}/Help %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_pkgdocdir}/Help %{buildroot}%{_pkgdocdir}/rst
%if %{with sphinx}
mv html %{buildroot}%{_pkgdocdir}
%endif

%if %{with gui}
# Desktop file
desktop-file-install --delete-original \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-gui.desktop

%if %{with appdata}
# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}%{_metainfodir}
cat > %{buildroot}%{_metainfodir}/cmake-gui.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: kitware@kitware.com
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">cmake-gui.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>CMake GUI</name>
  <summary>Create new CMake projects</summary>
  <description>
    <p>
      CMake is an open source, cross platform build system that can build, test,
      and package software. CMake GUI is a graphical user interface that can
      create and edit CMake projects.
    </p>
  </description>
  <url type="homepage">http://www.cmake.org</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/CMake/a.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF
%endif
%endif

# create manifests for splitting files and directories for filesystem-package
find %{buildroot}%{_datadir}/%{name} -type d | \
  sed -e 's!^%{buildroot}!%%dir "!g' -e 's!$!"!g' > data_dirs.mf
find %{buildroot}%{_datadir}/%{name} -type f | \
  sed -e 's!^%{buildroot}!"!g' -e 's!$!"!g' > data_files.mf
find %{buildroot}%{_libdir}/%{orig_name} -type d | \
  sed -e 's!^%{buildroot}!%%dir "!g' -e 's!$!"!g' > lib_dirs.mf
find %{buildroot}%{_libdir}/%{orig_name} -type f | \
  sed -e 's!^%{buildroot}!"!g' -e 's!$!"!g' > lib_files.mf
find %{buildroot}%{_bindir} -type f -or -type l -or -xtype l | \
  sed -e '/.*-gui$/d' -e '/^$/d' -e 's!^%{buildroot}!"!g' -e 's!$!"!g' >> lib_files.mf

# Install Python metadata
mkdir -p %{buildroot}%{python3_sitelib}
cp -a %{cmake_distinfo} %{buildroot}%{python3_sitelib}


%if %{with test}
%check
pushd %{_vpath_builddir}
# CTestTestUpload requires internet access.
NO_TEST="CTestTestUpload"
# Likely failing for hardening flags from system.
NO_TEST="$NO_TEST|CustomCommand|RunCMake.PositionIndependentCode"
# Failing for rpm 4.19
NO_TEST="$NO_TEST|CPackComponentsForAll-RPM-default"
NO_TEST="$NO_TEST|CPackComponentsForAll-RPM-OnePackPerGroup"
NO_TEST="$NO_TEST|CPackComponentsForAll-RPM-AllInOne"
# curl test may fail during bootstrap
%if %{with bootstrap}
NO_TEST="$NO_TEST|curl"
%endif
%ifarch riscv64
# These three tests timeout on riscv64, skip them.
NO_TEST="$NO_TEST|Qt5Autogen.ManySources|Qt5Autogen.MocInclude|Qt5Autogen.MocIncludeSymlink|Qt6Autogen.MocIncludeSymlink"
%endif
%if 0%{?fedora} == 41
# Test failing on Fedora 41, only.
NO_TEST="$NO_TEST|RunCMake.Make|RunCMake.BuildDepends|Qt6Autogen.RerunMocBasic|Qt6Autogen.RerunRccDepends"
%endif
# TODO: check why this fails
NO_TEST="$NO_TEST|RunCMake.ParseImplicitLinkInfo"
bin/ctest%{?name_suffix} %{?_smp_mflags} -V -E "$NO_TEST" --output-on-failure
## do this only periodically, not for every build -- besser82 20221102
# Keep an eye on failing tests
#bin/ctest%{?name_suffix} %{?_smp_mflags} -V -R "$NO_TEST" --output-on-failure || :
popd
%endif


%files -f lib_files.mf
%doc %dir %{_pkgdocdir}
%license Copyright.txt*
%license COPYING*
%if %{with bundled_cppdap}
%license LICENSE.cppdap
%license NOTICE.cppdap
%endif
%if %{with sphinx}
%{_mandir}/man1/c%{name}.1.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/cpack%{?name_suffix}.1.*
%{_mandir}/man1/ctest%{?name_suffix}.1.*
%{_mandir}/man7/*.7.*
%endif


%files data -f data_files.mf
%{_datadir}/aclocal/%{name}.m4
%{bash_completionsdir}/c*
%if %{with emacs}
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_emacs_sitelispdir}/%{name}
%{_emacs_sitestartdir}/%{name}-init.el
%else
%{_emacs_sitelispdir}
%{_emacs_sitestartdir}
%endif
%endif
%{vimfiles_root}/indent/%{name}.vim
%{vimfiles_root}/syntax/%{name}.vim


%files doc
# Pickup license-files from main-pkg's license-dir
# If there's no license-dir they are picked up by %%doc previously
%{?_licensedir:%license %{_datadir}/licenses/%{name}*}
%doc %{_pkgdocdir}


%files filesystem -f data_dirs.mf -f lib_dirs.mf


%if %{with gui}
%files gui
%{_bindir}/%{name}-gui
%if %{with appdata}
%{_metainfodir}/*.appdata.xml
%endif
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/mime/packages
%{_datadir}/icons/hicolor/*/apps/CMake%{?name_suffix}Setup.png
%if %{with sphinx}
%{_mandir}/man1/%{name}-gui.1.*
%endif
%endif


%files rpm-macros
%{_rpmmacrodir}/macros.%{name}
%if %{with rpm} && 0%{?_rpmconfigdir:1}
%{_rpmconfigdir}/fileattrs/%{name}.attr
%{_rpmconfigdir}/%{name}.prov
%{_rpmconfigdir}/%{name}.req
%endif

%files srpm-macros
%{_rpmmacrodir}/macros.aaa-%{name}-srpm


%files -n python3-cmake
%{python3_sitelib}/%{cmake_distinfo}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{pkg_version}-1
- Prepare for Oreon 11 (RP1)
