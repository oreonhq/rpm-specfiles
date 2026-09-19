%global source0_hash a278d9d8f91e8bfb8a1c2f5b73eecab47fd45d0693f5dbea637536413cec2ea5

Name:    heaptrack
Version: 1.5.0
Release: 12%{?dist}
Summary: A heap memory profiler for Linux

License: Apache-2.0 AND BSD-3-Clause AND BSL-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND MIT
URL:     https://invent.kde.org/sdk/heaptrack/

Source0: https://download.kde.org/stable/heaptrack/%{version}/%{name}-%{version}.tar.xz

Patch0:  Support-KChart6-for-KF6.patch
Patch1:  Use-QString-for-KConfigGroup-names.patch

# Upstream Patch: https://invent.kde.org/sdk/heaptrack/-/commit/c6c45f3455a652c38aefa402aece5dafa492e8ab
# Will prolly be unneeded next release.
Patch2:  fix-gcc14-cmake-compat.patch

BuildRequires:  desktop-file-utils

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kitemmodels-devel
BuildRequires:  kf6-threadweaver-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kiconthemes-devel

BuildRequires:  kdiagram-devel

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel

BuildRequires:  boost-devel
BuildRequires:  libunwind-devel
BuildRequires:  libdwarf-devel
BuildRequires:  elfutils-devel
BuildRequires:  libzstd-devel
BuildRequires:  sparsehash-devel
BuildRequires:  zlib-devel

# no libunwind on s390(x)
ExcludeArch:    s390 s390x

%description
Heaptrack traces all memory allocations and annotates these events with stack
traces.Dedicated analysis tools then allow you to interpret the heap memory
profile to:
- find hotspots that need to be optimized to reduce the memory footprint of your
  application
- find memory leaks, i.e. locations that allocate memory which is never
  deallocated
- find allocation hotspots, i.e. code locations that trigger a lot of memory
  allocation calls
- find temporary allocations, which are allocations that are directly followed
  by their deallocation

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6 -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DHEAPTRACK_USE_QT6=1 \
%if "%{?_lib}" == "lib64"
  %{?_cmake_lib_suffix64}
%endif

%cmake_build

%install
%cmake_install

%find_lang heaptrack --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.heaptrack.desktop

%files -f heaptrack.lang
%license LICENSES/GPL-2.0-or-later.txt
%{_bindir}/heaptrack
%{_bindir}/heaptrack_gui
%{_bindir}/heaptrack_print
%{_datadir}/applications/org.kde.heaptrack.desktop
%{_includedir}/heaptrack_api.h
%{_datadir}/metainfo/org.kde.heaptrack.appdata.xml
%dir %{_libdir}/heaptrack/
%{_libdir}/heaptrack/libheaptrack_inject.so
%{_libdir}/heaptrack/libheaptrack_preload.so
%{_libdir}/heaptrack/libexec/heaptrack_interpret
%{_libdir}/heaptrack/libexec/heaptrack_env
%{_datadir}/icons/hicolor/*/apps/heaptrack*

%changelog
%autochangelog
