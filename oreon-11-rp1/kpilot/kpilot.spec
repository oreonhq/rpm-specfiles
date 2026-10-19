%global source0_hash 6365981e018629c7265a64f48b4cec8984bfed0383daea78e936a9310271f5ef
Name:    kpilot
Summary:        Sync PIM data with PalmOS devices
Version: 5.3.0
Release:        46%{?dist}
ExcludeArch: s390 s390x
License: GPL-2.0-or-later
URL:     http://www.kde.org/
Source0:        ftp://ftp.kde.org/pub/kde/stable/4.3.4/src/kdepim-4.3.4.tar.bz2
Source1: kpilot-translations-20100115.tar.bz2
Patch0:  kdepim-4.3.4-qtcore-includes.patch
Patch1:  kdepim-4.3.4-kpilot-remove-bad-debug.patch
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  akonadi-devel
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  kdepimlibs-devel
BuildRequires:  make
BuildRequires:  pilot-link-devel
# /oreon:deps
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
mkdir -p %{buildroot}%{_docdir}/HTML/en/common
pushd %{buildroot}%{_docdir}/HTML/en
for i in *; do
   if [ -d $i -a -L $i/common ]; then
      rm -f $i/common
      ln -nfs ../common $i
   fi
done
popd
rm -rf %{buildroot}%{_kde4_includedir}/kpilot/
rm -f %{buildroot}%{_kde4_libdir}/libkpilot.so
%find_lang %{name} --with-kde
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for f in %{buildroot}%{_kde4_datadir}/applications/kde4/*.desktop ; do
  desktop-file-validate $f
done
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n kpilot-libs -f %{oreon_filedir}/kpilot-libs.list

%changelog

%autochangelog
