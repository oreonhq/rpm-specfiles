%global source0_hash b0f6aa5908d336d7f41f9576b2418ac7d27efbc59282aa8c9171d88cea74049e
%global snapshot 0%{?svndate}
%if %{snapshot}
%global svnrelease .%{svndate}svn%{svnrev}
%endif
Name:		codeblocks
Version:	25.03
Release:        5%{?dist}
Summary:        An open source, cross platform, free C++ IDE
License:	GPL-3.0-or-later
URL:		http://www.codeblocks.org/
%if %{snapshot}
Source0:        https://sourceforge.net/projects/%{name}/files/Sources/%{version}/%{name}_%{version}.tar.xz
%else
Source0:        https://sourceforge.net/projects/%{name}/files/Sources/%{version}/%{name}_%{version}.tar.xz
%endif
Patch0:		codeblocks-autorev.patch
Patch1:		codeblocks-flags.patch
Patch2:		codeblocks-fedora.patch
Requires:	%{name}-libs = %{version}-%{release}
Requires:	shared-mime-info
Requires:	xterm
Recommends:	%{name}-contrib
Provides:	bundled(wxScintilla) = 3.53.0
Provides:	bundled(squirrel) = 3.1
%global		pkgdatadir	%{_datadir}/%{name}
%global		pkglibdir	%{_libdir}/%{name}
%global		plugindir	%{pkglibdir}/plugins
%global __provides_exclude_from ^%{plugindir}/.*\\.so$
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  astyle-devel
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  libICE-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  tinyxml-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zip
BuildRequires:  zlib-devel
# /oreon:deps
%description
Code::Blocks is a free C++ IDE built specifically to meet the most demanding
needs of its users. It was designed, right from the start, to be extensible
and configurable. Built around a plug-in framework, Code::Blocks can be
extended with plug-in DLLs. It includes a plugin wizard, so you can compile
your own plug-ins.

%package libs
Summary:	Libraries needed to run Code::Blocks and its plug-ins
%description libs
Libraries needed to run Code::Blocks and its plug-ins.

%package devel
Summary:	Files needed to build Code::Blocks plug-ins
Requires:	%{name}-libs = %{version}-%{release}
Requires:	pkgconfig
%description devel
Development files needed to build Code::Blocks plug-ins.

%package contrib-libs
Summary:	Libraries needed to run Code::Blocks contrib plug-ins
Requires:	%{name}-libs = %{version}-%{release}
%description contrib-libs
Libraries needed to run Code::Blocks contrib plug-ins.

%package contrib-devel
Summary:	Files needed to build Code::Blocks contrib plug-ins
Requires:	%{name}-contrib-libs = %{version}-%{release}
%description contrib-devel
Development files needed to build Code::Blocks contrib plug-ins.

%package contrib
Summary:	Additional Code::Blocks plug-ins
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-contrib-libs = %{version}-%{release}
Recommends:	cppcheck
Recommends:	cscope
Recommends:	valgrind
%description contrib
Additional Code::Blocks plug-ins.

%prep

%if %{snapshot}
%setup -q -n %{name}
%patch -P 0 -p1
%else
%setup -q -n %{name}_%{version}
%endif
%patch -P 1 -p1
%patch -P 2 -p1

%if %{snapshot}
# generate revision.m4
echo "m4_define([SVN_REV], %{svnrev})" > revision.m4
echo "m4_define([SVN_REVISION], svn%{svnrev})" >> revision.m4
echo "m4_define([SVN_DATE], %{svndate})" >> revision.m4

./bootstrap
%else
autoreconf -f -i
%endif

# convert EOLs
find . -type f -and -not -name "*.cpp" -and -not -name "*.h" -and -not -name "*.png" -and -not -name "*.bmp" -and -not -name "*.c" -and -not -name "*.cxx" -and -not -name "*.ico" -exec dos2unix -q --keepdate {} \;

%build

%configure \
    --with-contrib-plugins="all" \
    --with-boost-libdir=%{_libdir}
rm -rf src/include/tinyxml src/base/tinyxml
rm -rf src/plugins/astyle/astyle
rm -rf src/plugins/contrib/SpellChecker/hunspell
rm -rf src/plugins/contrib/devpak_plugin/bzip2
rm -rf src/plugins/contrib/help_plugin/{bzip2,zlib}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.{appdata,metainfo}.xml
desktop-file-validate	%{buildroot}/%{_datadir}/applications/codeblocks.desktop
find %{buildroot} -type f -name "*.la" -delete
/bin/touch -r %{SOURCE0} %{buildroot}/%{pkgdatadir}/*.zip
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}/wxContribItems" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}-contrib-%{_arch}.conf
%ldconfig_scriptlets libs
%ldconfig_scriptlets contrib-libs
rm -f %{buildroot}/%{pkgdatadir}/docs/index.ini
%oreon_autofiles codeblocks-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles codeblocks-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles codeblocks-contrib-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles codeblocks-contrib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles codeblocks-contrib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n codeblocks-libs -f %{oreon_filedir}/codeblocks-libs.list
%files -n codeblocks-devel -f %{oreon_filedir}/codeblocks-devel.list
%files -n codeblocks-contrib-libs -f %{oreon_filedir}/codeblocks-contrib-libs.list
%files -n codeblocks-contrib-devel -f %{oreon_filedir}/codeblocks-contrib-devel.list
%files -n codeblocks-contrib -f %{oreon_filedir}/codeblocks-contrib.list

%changelog

%autochangelog
