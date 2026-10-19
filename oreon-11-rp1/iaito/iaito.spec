%global source1_hash 11f170b87045b5bec23e398ba04994719a72f4573d4391396a3ac0011792e14a
%global source0_hash 11f170b87045b5bec23e398ba04994719a72f4573d4391396a3ac0011792e14a
Name:           iaito
Summary:        GUI for radare2 reverse engineering framework
Version:        6.2.2
URL:            https://radare.org/n/iaito.html
%global         urlvcs          https://github.com/radareorg/iaito
VCS:            git:%{urlvcs}
%bcond_without     releasetag
%global         gituser         radareorg
%global         gitname         iaito
%global         gitdate         20241121
%global         commit          465cf40df7642fe708ab41f66a5aeff127098cc6
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         iaito_translations_gitdate      20221114
%global         iaito_translations_commit       e66b3a962a7fc7dfd730764180011ecffbb206bf
%global         iaito_translations__shortcommit %(c=%{iaito_translations_commit}; echo ${c:0:7})
%if %{with releasetag}
Release:        1%{?dist}
Source0:        %{urlvcs}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Release:        1%{?dist}
%endif
License:        GPL-3.0-only AND CC-BY-SA-3.0 AND CC0-1.0
Source1:        https://github.com/radareorg/iaito-translations/archive/%{iaito_translations_commit}.tar.gz#/iaito-translations-git%{iaito_translations_gitdate}.tar.gz
Patch0:         iaito-5.8.8-norpath.patch
%ifarch %{qt5_qtwebengine_arches}
%endif
Requires:       hicolor-icon-theme
Obsoletes:      r2cutter < 5.2.0
Provides:       r2cutter%{?_isa} = %{version}-%{release}
Obsoletes:      iaito-doc < 5.6.0-0.3.20220303gitafaa7df
Obsoletes:      iaito-devel < 5.6.0-0.6
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  kf5-syntax-highlighting-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  radare2-devel
# /oreon:deps
%description
iaito is a Qt and C++ GUI for radare2.
It is the continuation of Cutter before the fork to keep radare2 as backend.
Its goal is making an advanced, customizable and FOSS reverse-engineering
platform while keeping the user experience at mind.
The iaito is created by reverse engineers for reverse engineers.
Focus on supporting latest version of radare2.
Recommend the use of system installed libraries/radare2.
Closer integration between r2 and the UI.

%package devel
Summary:        Development files for the iaito package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      r2cutter-devel < 5.2.0
Provides:       r2cutter-devel%{?_isa} = %{version}-%{release}
%description devel
Development files for the iaito package. See iaito package for more
information.

# %%package doc
# Summary:        Documentation for the iaito package
# BuildArch:      noarch
# Requires:       %%{name} = %%{version}-%%{release}

# %%description doc
# Documentation for the iaito package. See iaito package for more
# information.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with releasetag}
# Build from git release version
%autosetup -p1 -n %{gitname}-%{version}
%else
%autosetup -p1 -n %{gitname}-%{commit}
# Rename internal "version-git" to "version"
sed -i -e "s|%{version}-git|%{version}|g;" configure configure.acr
%endif

# RHEL up to 9 doesn't know url type of vcs-browser

# RHEL up to 8 doesn't know url type of bugtracker, contact

[ -d src/translations ] || mkdir -p src/translations
tar --strip-component=1 -xvf %{SOURCE1} -C src/translations

# Honor parallel jobs number
sed -i Makefile -e '\@MAKE@s|-j4|%_smp_mflags|'

# Honor Fedora compiler flags
sed -i src/Iaito.pro \
    -e 's|^QMAKE_CXXFLAGS +=.*$|QMAKE_CXXFLAGS += %build_cxxflags\nQMAKE_LFLAGS += %build_ldflags|' \
    %{nil}

# Change prefix
sed -i src/Iaito.pro -e 's|/usr/local|%_prefix|'

# Tweak path to find qmake, lrelease with -qt5 suffix
mkdir TMPBINDIR
cd TMPBINDIR
ln -sf %_bindir/qmake-qt5 qmake
ln -sf %_bindir/lrelease-qt5 lrelease
cd ..

%build

export PATH=$(pwd)/TMPBINDIR:$PATH
%configure
%make_build
%install
export PATH=$(pwd)/TMPBINDIR:$PATH
%make_install STRIP=true
make install-translations DESTDIR=%{?buildroot}
%find_lang %name --with-qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n iaito-devel -f %{oreon_filedir}/iaito-devel.list

%changelog

%autochangelog
