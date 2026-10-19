%global source0_hash 8921fb41be1b1f8bd3498a8c45bd955eff752b188ae67b50f3dd8c22592bcc8e
%global framework khtml
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 4 solution with KHTML, a HTML rendering engine
License: LicenseRef-Callaway-LGPLv2+ AND GPL-3.0-only AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  giflib-devel
BuildRequires:  gperf
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kcodecs-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kjs-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-sonnet-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  openssl-devel
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-interpreter
BuildRequires:  phonon-qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
KHTML is a web rendering engine, based on the KParts technology and using KJS
for JavaScript support.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-ki18n-devel >= %{version}
Requires:       kf5-kio-devel >= %{version}
Requires:       kf5-kjs-devel >= %{version}
Requires:       kf5-kparts-devel >= %{version}
Requires:       qt5-qtbase-devel
Requires:       kf5-ktextwidgets-devel >= %{version}
Requires:       kf5-kcodecs-devel >= %{version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build

%cmake_kf5 \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"
%cmake_build
%install
%cmake_install
%find_lang khtml5_qt --with-qt --all-name
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-khtml-devel -f %{oreon_filedir}/kf5-khtml-devel.list

%changelog

%autochangelog
