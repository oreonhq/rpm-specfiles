%global source0_hash 5935a4cbd47d0dc84122d56e968c8bdd5416f8b9a69b8f97f42f791b526dc3b0
%global stable_kf6 stable
%if !0%{?bootstrap}
%global analitza 1
%global qalculate 1
%global libspectre 1
%ifarch %{arm} %{ix86} x86_64 aarch64
%global luajit 1
%endif
%global python3 1
%endif
%global soname 28
Name:    cantor
Summary:        KDE Frontend to Mathematical Software
Version: 26.08.1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://apps.kde.org/cantor/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Patch2:  cantor-21.04.3-no-julia-internal.patch
%if 0%{?analitza}
%endif
%if 0%{?qalculate}
%endif
%if 0%{?libspectre}
%endif
%if 0%{?luajit}
%endif
%if 0%{?python3}
%endif
Obsoletes: cantor-python3 < 20.04.1
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(Analitza6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Pty)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  python3-devel
# /oreon:deps
%description
%{summary}.

%package  libs
Summary:  Runtime files for %{name}
Conflicts: kdeedu-math-libs < 4.7.0-10
Provides: %{name}-part = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%if ! 0%{?julia}
Obsoletes: %{name}-julia < %{version}-%{release}
%endif
%if ! 0%{?libr}
Obsoletes: %{name}-R < %{version}-%{release}
%endif
%description libs
%{summary}.

%if 0%{?julia}
%package julia
Summary: julia backend for %{name}
BuildRequires: julia-devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Supplements: (%{name} and julia)
%description julia
%{summary}.
%endif

%if 0%{?libr}
%package R
Summary: R backend for %{name}
BuildRequires: pkgconfig(libR)
Obsoletes: kdeedu-math-cantor-R < 4.7.0-10
Provides:  kdeedu-math-cantor-R = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Supplements: (%{name} and R-core)
%description R 
%{summary}.
%endif

%package devel
Summary:  Development files for %{name}
Conflicts: kdeedu-devel < 4.7.0-10
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n cantor-libs -f %{oreon_filedir}/cantor-libs.list
%files -n cantor-devel -f %{oreon_filedir}/cantor-devel.list

%changelog

%autochangelog
