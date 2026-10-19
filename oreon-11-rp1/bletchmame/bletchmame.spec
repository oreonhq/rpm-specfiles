%global source0_hash a80bea01c0485216a18b7fba5730c58de289c272d3356e752229462003220309
%global forgeurl https://github.com/npwoods/bletchmame
Name:           bletchmame
Version:        2.17
Release:        1%{?dist}
Summary:        MAME emulator frontend
License:        GPL-3.0-or-later
URL:            https://www.bletchmame.org
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          bletchmame-default-paths.patch
Patch:          %{forgeurl}/commit/a72c6cc3b83209c446394528e36cc69b45cb9132.patch
Patch:          %{forgeurl}/commit/b7866b44c8222697ffe3cdc1b101f4d7d7da6bce.patch
Patch:          bletchmame-disable-broken-tests.patch
Recommends:     mame
Recommends:     mame-data-software-lists
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libxkbcommon-devel
BuildRequires:  observable-devel
BuildRequires:  perl
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  quazip-qt6-devel
BuildRequires:  sed
BuildRequires:  zlib-devel
# /oreon:deps
%description
BletchMAME is a new experimental front end for MAME. Unlike existing front ends
(which function as launchers, keeping MAME's internal UI), BletchMAME replaces
the internal MAME UI with a more conventional point and click GUI to provide a
friendlier experience in a number of areas (such as profiles, input
configuration and a number of others). While BletchMAME is intended to support
all machines supported by MAME, it should be particularly suitable to computer
emulation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
# Disable broken tests on 32 bit architectures
%ifarch armv7hl i686 s390x
%patch -P 3 -p1
%endif

cp -p %{SOURCE1} .

# remove bundled libraries
rm -r lib/*
ln -s %{_includedir}/observable lib/observable

# Set build version
mkdir include
echo "v%{version}" | \
  perl scripts/process_version.pl --versionhdr > include/version.gen.h

# Disable -Werror to avoid build failures
sed -i 's/-Werror//' CMakeLists.txt

# Disable broken test due to Qt upgrade
rm src/tests/prefs_test.cpp
sed -i 's:src/tests/prefs_test.cpp::g' CMakeLists.txt

%build

%cmake \
  -DUSE_SHARED_LIBS=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DHAS_VERSION_GEN_H=1
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr plugins %{buildroot}%{_datadir}/%{name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
install -Dpm0644 -t %{buildroot}%{_metainfodir} %{name}.metainfo.xml
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
