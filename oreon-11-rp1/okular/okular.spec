%global source0_hash 7eb26c37ee42b6657526aeddd1bce71c5556e3865772a677f49b68deb46885d6

## uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%if 0%{?fedora}
%global chm 1
%global ebook 1
%global postscript 1
%endif
# uncomment to include -mobile (currently doesn't work)
# it links libokularpart.so, but fails to file/load at runtime
%global mobile 1
%endif

Name:    okular
Summary: A document viewer
Version: 26.08.1
Release: 1%{?dist}

License: GPL-2.0-only
URL:     https://www.kde.org/applications/graphics/okular/

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches (master branch)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Pty)
BuildRequires: cmake(KF6ThreadWeaver)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WindowSystem)

BuildRequires: qt6-qtbase-private-devel
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)

# okular-mobile
BuildRequires: kf6-purpose-devel
Requires: kf6-purpose%{?_isa}

BuildRequires: pkgconfig(phonon4qt6)
BuildRequires: cmake(Qca-qt6)

## generater/plugin deps
BuildRequires: cmake(KExiv2Qt6)
BuildRequires: cmake(QMobipocket6)
%if 0%{?chm}
BuildRequires: chmlib-devel
BuildRequires: pkgconfig(libzip)
%endif
%if 0%{?ebook}
BuildRequires: ebook-tools-devel
%endif
%if 0%{?postscript}
BuildRequires: pkgconfig(libspectre)
%endif
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(libmarkdown)
BuildRequires: pkgconfig(libspectre)
BuildRequires: pkgconfig(poppler-qt6)
BuildRequires: pkgconfig(zlib)
%if 0%{?fedora}
BuildRequires: pkgconfig(ddjvuapi) 
%endif

%if !0%{?bootstrap}
BuildRequires:  cmake(Qt6TextToSpeech)
%endif

Requires: %{name}-part%{?_isa} = %{version}-%{release}
Requires: kf6-kirigami2%{_isa}

%description
%{summary}.

%if 0%{?mobile}
%package mobile
Summary: Document viewer for plasma mobile
# included last in okular-15.12.3-1.fc23
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
%if 0%{?fedora}
# use Recommends to avoid hard deps -- rex
## lpr
Recommends: cups-client
## ps2pdf,pdf2ps
Recommends: ghostscript-core
%endif
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
# translations moved here
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


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.okular.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.okular.appdata.xml
%if 0%{?mobile}
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.okular.kirigami.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.okular.kirigami.appdata.xml
%endif

%files -f okular.lang
%license LICENSES/*
%{_kf6_bindir}/okular
%{_kf6_datadir}/applications/org.kde.okular.desktop
%{_kf6_metainfodir}/org.kde.okular.appdata.xml
%{_kf6_datadir}/applications/okularApplication_*.desktop
%{_kf6_metainfodir}/org.kde.okular-*.metainfo.xml
%{_kf6_datadir}/okular/
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/okular.1*
%{_kf6_datadir}/qlogging-categories6/okular.categories

%if 0%{?mobile}
%files mobile
%{_kf6_bindir}/okularkirigami
%{_qt6_qmldir}/org/kde/okular/
%{_kf6_metainfodir}/org.kde.okular.kirigami.appdata.xml
%{_kf6_datadir}/applications/org.kde.okular.kirigami.desktop
%{_kf6_datadir}/applications/org.kde.mobile.okular_*.desktop
%endif

%files devel
%{_includedir}/okular/
%{_libdir}/libOkular6Core.so
%{_libdir}/cmake/Okular6/

%ldconfig_scriptlets libs

%files libs
%{_libdir}/libOkular6Core.so.*

%files part -f okular-part.lang
%if 0%{?fedora}
# Disabled upstream?
# %%{_kf6_plugindir}/kio/kio_msits.so
%endif
%{_kf6_datadir}/config.kcfg/*.kcfg
%dir %{_qt6_plugindir}/okular_generators/
%{_qt6_plugindir}/okular_generators/okularGenerator_*.so
%{_kf6_plugindir}/parts/okularpart.so


%changelog
%autochangelog
