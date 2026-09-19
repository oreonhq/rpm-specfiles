%global source0_hash 6365981e018629c7265a64f48b4cec8984bfed0383daea78e936a9310271f5ef

Name:    kpilot
Summary: Sync PIM data with PalmOS devices
Version: 5.3.0
Release: 46%{?dist}

# no pilot-link on S/390
ExcludeArch: s390 s390x

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/4.3.4/src/kdepim-4.3.4.tar.bz2
# translations collected from:
# http://websvn.kde.org/branches/stable/l10n-kde4/*/messages/kdepim
# http://websvn.kde.org/branches/stable/l10n-kde4/*/docs/kdepim
Source1: kpilot-translations-20100115.tar.bz2
Patch0:  kdepim-4.3.4-qtcore-includes.patch
# Remove bad debugging statements to fix FTBFS (#1556010, #1604519)
Patch1:  kdepim-4.3.4-kpilot-remove-bad-debug.patch

BuildRequires: kdelibs4-devel >= 4.3.4
BuildRequires: kdepimlibs-devel >= 4.3.4
BuildRequires: akonadi-devel
BuildRequires: boost-devel
BuildRequires: pilot-link-devel >= 0.12
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: make

Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?fedora} < 13
Conflicts: kdepim < 6:4.3.80
Conflicts: kde-l10n < 4.3.90-3
%endif

%description
Utility to synchronize PIM (Personal Information Management) data with
PalmOS devices.

%package libs
Summary: Runtime libraries for %{name}

%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n kdepim-4.3.4 -a 1
%patch -P0 -p1
%patch -P1 -p1

# FTBFS Workaround for new cmake
echo "cmake_policy(VERSION 3.5)" > cmake4-kde4-compat.cmake
mkdir -p cmake-compat
cp /usr/lib*/automoc4/automoc4.files.in /usr/lib*/automoc4/Automoc4* cmake-compat/
sed -i 's/VERSION 2.6.4 FATAL_ERROR/VERSION 3.5/g' cmake-compat/Automoc4Config.cmake
sed -i 's/CMP0002 OLD/CMP0002 NEW/g' cmake-compat/Automoc4Config.cmake
sed -i '1i cmake_minimum_required(VERSION 3.5)' kpilot/CMakeLists.txt

echo 'add_subdirectory(../doc/kpilot doc)' >>kpilot/CMakeLists.txt
echo 'add_subdirectory(../kpilot-translations-20100115 l10n)' >>kpilot/CMakeLists.txt
pushd kpilot-translations-20100115/doc
for i in *_kpilot ; do
  if [ -e $i/index.docbook ] ; then
    echo "add_subdirectory($i)" >>CMakeLists.txt
    echo 'kde4_create_handbook(index.docbook INSTALL_DESTINATION ${HTML_INSTALL_DIR}/'${i%_kpilot}'/ SUBDIR kpilot)' >$i/CMakeLists.txt
  fi
done
popd

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} -Wno-dev \
 -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES=../cmake4-kde4-compat.cmake \
 -DAutomoc4_DIR=../cmake-compat \
 -DAUTOMOC4_EXECUTABLE=%{_bindir}/automoc4 ../kpilot
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# make symlinks relative
mkdir -p %{buildroot}%{_docdir}/HTML/en/common
pushd %{buildroot}%{_docdir}/HTML/en
for i in *; do
   if [ -d $i -a -L $i/common ]; then
      rm -f $i/common
      ln -nfs ../common $i
   fi
done
popd

# don't package devel files
rm -rf %{buildroot}%{_kde4_includedir}/kpilot/
rm -f %{buildroot}%{_kde4_libdir}/libkpilot.so

%find_lang %{name} --with-kde

%check
for f in %{buildroot}%{_kde4_datadir}/applications/kde4/*.desktop ; do
  desktop-file-validate $f
done

%ldconfig_scriptlets libs

%files -f %{name}.lang
%doc kpilot/COPYING
%doc kpilot/README kpilot/AUTHORS kpilot/ChangeLog kpilot/NEWS kpilot/TODO
%{_kde4_bindir}/kpilot
%{_kde4_bindir}/kpilotDaemon
%{_kde4_datadir}/applications/kde4/kpilot*.desktop
%{_kde4_datadir}/config.kcfg/*.kcfg
%{_kde4_datadir}/kde4/services/*.desktop
%{_kde4_datadir}/kde4/servicetypes/kpilotconduit.desktop
%{_kde4_appsdir}/kconf_update/kpilot.upd
%{_kde4_appsdir}/kpilot/
%{_kde4_iconsdir}/hicolor/*/*/*

%files libs
%{_kde4_libdir}/libkpilot.so.*
%{_kde4_libdir}/libkpilot_*.so
%{_kde4_libdir}/kde4/kcm_kpilot.so
%{_kde4_libdir}/kde4/kpilot_conduit_*.so

%changelog
%autochangelog
