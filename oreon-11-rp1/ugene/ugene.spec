%global source0_hash none

%global   use_release_branch  0

%if 0%{?use_release_branch} < 1
# master
%global	gitdate		20260228
%global	gitcommit		77338a76808d0e1b36461a94d16f0a45c83b64e9
# New git commit with non-free part removed using "git filter-branch"
%global	gitcommit_free		6812b00935495786e28ebe901bfb8304dbee457c
%else
# currently 41.0 branch
%global	gitdate		20250313
%global	gitcommit		c0dffab5a15e01c026f80cf0a7033b08112a355f
# New git commit with non-free part using "git filter-branch"
%global	gitcommit_free		b0631c54cc0603a88793ed5d6ee02dec196b823e
%endif

%global	shortcommit	%(c=%{gitcommit}; echo ${c:0:7})
%global	git_version	%{gitdate}git%{shortcommit}

%global	tarballdate	20260301
%global	tarballtime	1637

%global	use_release	1
%global	use_gitbare	0

%if	0%{?use_gitbare} < 1
# force
%global	use_release	1
%endif

%if	0%{?use_release} >= 1
%global	GIT	true
%else
%global	GIT	git
%endif

%global	mainver		53.1
%undefine	prever

%if		0%{?use_release} >= 1
%global	fedoraver		%{mainver}%{?prever:~%{prerpmver}}
%endif
%if		0%{?use_gitbare} >= 1
%global	fedoraver		%{mainver}%{?git_version:^%{git_version}}
%endif

Name:		ugene
Summary:	Integrated bioinformatics toolkit

Version:	%{fedoraver}
Release:	1%{?dist}

#The entire source code is GPLv2+ except:
#file src/libs_3rdparty/qtbindings_core/src/qtscriptconcurrent.h which is GPLv2
#files in src/plugins_3rdparty/script_debuger/src/qtscriptdebug/ which are GPLv2
# Automatically converted from old format: GPLv2+ and GPLv2 - review is highly recommended.
License:	GPL-2.0-or-later AND GPL-2.0-only
URL:		http://ugene.net
%if	0%{?use_release} >= 1
#Source0:	https://github.com/ugeneunipro/ugene/archive/%{mainver}.tar.gz/#/%{name}-%{mainver}.tar.gz
# Removing non-free part
Source0:	%{name}-free-%{mainver}.tar.gz
# Source0 is created by # env VERSION=%%{mainver} source ./%{SOURCE1}
%endif
%if	0%{?use_gitbare} >= 1
Source0:	%{name}-free-%{tarballdate}T%{tarballtime}.tar.gz
%endif
Source1:	create-ugene-free-tarball.sh
Source2:	create-%{name}-git-bare-tarball.sh
# This is not installed
Source10:	ugene.wrapper
Patch1:	ugene-49.1-narrowing-for-unsigned-char.patch
Patch3:	ugene-52.1.x-QObject-connect-overload.patch
# Currently distro-specific
Patch102:	ugene-44.x-libs_3rdparty-breakpad-sys_mmap_use_system_mmap.patch
Patch103:	ugene-40.1-libs_3rdparty-breakpad-unwind-nonsupported-arch.patch
Patch104:	ugene-47.x-plugins_3rdparty-hmm2-nosse-arch.patch
Patch105:	ugene-40.1-libs_3rdparty-breakpad-arch-port.patch
Patch106:	ugene-47.x-git-plgins-smith_waterman-nonsse2-arch.patch
Patch107:	ugene-40.1-qbswap-bigendian-workaround.patch
Patch109:	ugene-50.x-aarch64-neon-impl-not-yet.patch
Patch110:	ugene-52.x-s390x-platform-macro.patch

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils

%if		0%{?use_gitbare} >= 1
BuildRequires:	%{_bindir}/git
%endif

BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5NetworkAuth)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebSockets)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(zlib)

Provides:		bundled(samtools) = 0.1.18

%description
Unipro UGENE is a cross-platform visual environment for DNA and protein
sequence analysis. UGENE integrates the most important bioinformatics
computational algorithms and provides an easy-to-use GUI for performing
complex analysis of the genomic data. One of the main features of UGENE
is a designer for custom bioinformatics workflows.

%prep
%if		0%{?use_release} >= 1
%setup -q
%endif

%if		0%{?use_gitbare} >= 1
%setup -q -c -n %{name}-%{mainver}%{?git_version:-%{git_version}} -T -a 0
git clone ./%{name}.git/
cd %{name}
cp -a [A-Z]* ..

git checkout -b %{mainver}-fedora %{gitcommit_free}
git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"
%endif
%patch -P1 -p1 -b .narrow
	%GIT commit -m "Fix narrowing on arch where default char is unsigned" -a
%patch -P3 -p1 -b .include
	%GIT commit -m "RegionSelectorController: specify overloaded function" -a
%patch -P102 -p1 -b .sys_mmap -Z
	%GIT commit -m "libs_3rdparty/breakpad: use C function instead of directly using syscall assemble code" -a
%patch -P103 -p1 -b .unwind -Z
	%GIT commit -m "libs_3rdparty/breakpad: workaround for arch not supporting unwind" -a
%patch -P104 -p1 -b .sse -Z
	%GIT commit -m "plugins_3rdparty/hmm2: support architecture not supporting SSE2" -a
%patch -P105 -p1 -b .port -Z
	%GIT commit -m "libs_3rdparty/breakpad: workaround for arch not ported by the upstream" -a
%patch -P106 -p1 -b .sse_2 -Z
	%GIT	commit -m "plugins/smith_waterman: support architecture not supporting SSE2" -a
%patch -P107 -p1 -b .char_bigen -Z
	%GIT	commit -m "src/corelibs/U2Core et al.: Workaround for Qt qbswap issue on Q_BIG_ENDIAN" -a
%if 1
%patch -P109 -p1 -b .neon -Z
	%GIT commit -m "neon impl not yet available" -a
%endif
%patch -P110 -p1 -b .s390x_macro -Z
	%GIT commit -m "define s390x related macro" -a

# Kill system-provided 3rd-party libs
sed -i CMakeLists.txt \
	-e '\@add_subdirectory.*libs_3rdparty/sqlite3@d' \
	-e '\@add_subdirectory.*libs_3rdparty/zlib@d' \
	%{nil}
rm -rf src/libs_3rdparty/{sqlite3,zlib}
rm -rf src/include/3rdparty/{sqlite3,zlib}
	%GIT rm -r -f src/libs_3rdparty/{sqlite3,zlib} || true
	%GIT rm -r -f src/include/3rdparty/{sqlite3,zlib} || true
	%GIT commit -m "kill system-provided 3rd-party libs" -a
grep -rl --exclude-dir=.git 3rdparty/zlib/zlib.h . | \
	xargs sed -i 's|3rdparty/zlib/zlib.h|zlib.h|'
grep -rl --exclude-dir=.git 3rdparty/sqlite3/sqlite3.h . | \
	xargs sed -i 's|3rdparty/sqlite3/sqlite3.h|sqlite3.h|'
find . -name CMakeLists.txt | \
	xargs sed -i \
		-e 's|zlib|z|' \
		-e 's|ugenedb|sqlite3|' \
		%{nil}
	%GIT commit -m "fix system provided header path" -a

sed -i.nonfree CMakeLists.txt -e '\@add_subdirectory.*plugins_3rdparty/psipred@d'
	%GIT commit -m "remove nonfree code" -a

# Remove -Werror
sed -i CMakeLists.txt -e '\@" -Werror=@d'
	%GIT commit -m "remove -Werror" -a

# Enable some deprecated API
sed -i CMakeLists.txt -e '\@QT_DISABLE_DEPRECATED_BEFORE=@s|0x050F00|0x050000|'
	%GIT commit -m "enable some deprecated API" -a

%build
%if		0%{?use_gitbare} >= 1
cd %{name}
%endif

export QT_DIR=%{_libdir}/qt5
export LD_LIBRARY_PATH=$(pwd)/%{_vpath_builddir}/dist

%cmake \
	-DCMAKE_SKIP_RPATH=TRUE \
	%{nil}
%cmake_build

%install
%if		0%{?use_gitbare} >= 1
cd %{name}
%endif

%cmake_install

# Install all files manually...
# 0. Documents
cp -a \
	LICENSE.3rd_party.txt \
	LICENSE.txt \
	..

pushd %_vpath_builddir

# 1-0 bindir
mkdir -p %{buildroot}%{_bindir}
install -cpm 0755 %{SOURCE10} %{buildroot}%{_bindir}/%{name}

# 1-1 libraries
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -a dist/* %{buildroot}%{_libdir}/%{name}/
rm -f  %{buildroot}%{_libdir}/%{name}/*.a

# Back to the top directory
popd

# 1-2 data files
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a data %{buildroot}%{_datadir}/%{name}
ln -sf ../../../%{_datadir}/%{name}/data %{buildroot}%{_libdir}/%{name}/data

pushd ./etc/shared
# 1-11 hicolor
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/mimetypes/
cp -p application-x-ugene-ext.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/mimetypes/

# 1-12 mime
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p application-x-ugene.xml %{buildroot}/%{_datadir}/mime/packages

# 1-13 man file
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{name}.1* %{buildroot}/%{_mandir}/man1

# 1-14 desktop files
mkdir -p %{buildroot}%{_datadir}/applications/
cp -p %{name}.desktop %{buildroot}/%{_datadir}/applications/

# 1-15 icons
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p %{name}.{png,xpm} %{buildroot}%{_datadir}/pixmaps
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license	LICENSE.txt
%license	LICENSE.3rd_party.txt

%{_bindir}/%{name}

%dir	%{_libdir}/%{name}/
%{_libdir}/%{name}/lib*.so

%dir	%{_libdir}/%{name}/plugins/
%{_libdir}/%{name}/plugins/*.license
%{_libdir}/%{name}/plugins/*.plugin
%{_libdir}/%{name}/plugins/lib*.so

%{_libdir}/%{name}/transl_*.qm

%{_libdir}/%{name}/%{name}
%{_libdir}/%{name}/%{name}cl
%{_libdir}/%{name}/%{name}m
%{_libdir}/%{name}/%{name}ui
%{_libdir}/%{name}/plugins_checker

%dir	%{_datadir}/%{name}/
%{_datadir}/%{name}/data/
%{_libdir}/%{name}/data

%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ugene.*
%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-ugene-ext.png

%{_datadir}/mime/packages/*.xml
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
