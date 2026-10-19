%global source0_hash 7eb26c37ee42b6657526aeddd1bce71c5556e3865772a677f49b68deb46885d6
%if !0%{?bootstrap}
%global mobile 1
%endif
Name:    okular
Summary:        A document viewer
Version: 26.08.1
Release:        1%{?dist}
License: GPL-2.0-only
URL:     https://www.kde.org/applications/graphics/okular/
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires: kf6-purpose%{?_isa}
%if 0%{?chm}
%endif
%if 0%{?ebook}
%endif
%if 0%{?postscript}
%endif
%if !0%{?bootstrap}
%endif
Requires: %{name}-part%{?_isa} = %{version}-%{release}
Requires: kf6-kirigami2%{_isa}
# oreon:deps
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Pty)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(QMobipocket6)
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-purpose-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(phonon4qt6)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
%{summary}.

%if 0%{?mobile}
%package mobile
Summary: Document viewer for plasma mobile
Obsoletes: okular-active < 16.04
Requires: %{name}-part%{?_isa} = %{version}-%{release}
%description mobile
%{summary}.
%endif

%package devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package  libs 
Summary:  Runtime files for %{name} 
%description libs 
%{summary}.

%package part
Summary: Okular kpart plugin
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kdegraphics-mobipocket%{?_isa}
Requires: ebook-tools-libs%{?_isa}
Requires: poppler-qt6%{?_isa}
Requires: libkexiv2-qt6%{?_isa}
Requires: phonon-qt6%{?_isa}
Requires: djvulibre-libs%{?_isa}
Requires: libmarkdown%{?_isa}
Requires: libspectre%{?_isa}
Conflicts: kde-l10n < 17.03
%description part
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%if ! 0%{?mobile}
# disable/omit mobile, it doesn't work -- rex
sed -i -e 's|^add_subdirectory( mobile )|#add_subdirectory( mobile )|' CMakeLists.txt
%endif

%build

%cmake_kf6 -DOKULAR_UI=both \
	-DFORCE_NOT_REQUIRED_DEPENDENCIES="CHM;LibZip;DjVuLibre;EPub;"
%cmake_build
%install
%cmake_install
%find_lang all --all-name --with-html --with-man
grep -v \
  -e %{_mandir} \
  -e %{_kf6_docdir} \
  all.lang > okular-part.lang
cat all.lang okular-part.lang | sort | uniq -u > okular.lang
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.okular.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.okular.appdata.xml
%if 0%{?mobile}
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.okular.kirigami.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.okular.kirigami.appdata.xml
%endif
%files -f %{oreon_filedir}/main.list
%files -n okular-mobile -f %{oreon_filedir}/okular-mobile.list
%files -n okular-devel -f %{oreon_filedir}/okular-devel.list
%files -n okular-libs -f %{oreon_filedir}/okular-libs.list
%files -n okular-part -f %{oreon_filedir}/okular-part.list

%changelog

%autochangelog
