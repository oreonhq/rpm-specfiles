%global framework kdelibs4support

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 4 module with porting aid from KDELibs 4
# Automatically converted from old format: GPLv2+ and LGPLv2+ and BSD - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/portingAids/%{framework}-%{version}.tar.xz

BuildRequires:  ca-certificates
BuildRequires:  gettext-devel

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kcompletion-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-kcrash-devel >= %{majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{majmin}
BuildRequires:  kf5-kded-devel >= %{majmin}
BuildRequires:  kf5-kdesignerplugin-devel >= %{majmin}
BuildRequires:  kf5-kdoctools-devel >= %{majmin}
BuildRequires:  kf5-kemoticons-devel >= %{majmin}
BuildRequires:  kf5-kglobalaccel-devel >= %{majmin}
BuildRequires:  kf5-kguiaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-knotifications-devel >= %{majmin}
BuildRequires:  kf5-kparts-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-ktextwidgets-devel >= %{majmin}
BuildRequires:  kf5-kunitconversion-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  NetworkManager-libnm-devel
%if 0%{?fedora} == 26
BuildRequires: compat-openssl10-devel
%else
BuildRequires: openssl-devel
%endif
BuildRequires:  perl-generators
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       ca-certificates
Requires:       kde-settings
Requires:       kf5-kded >= %{majmin}

%description
This framework provides code and utilities to ease the transition from kdelibs 4
to KDE Frameworks 5. This includes CMake macros and C++ classes whose
functionality has been replaced by code in CMake, Qt and other frameworks.

%package        libs
Summary:        Runtime libraries for %{name}
Requires:       %{name} = %{version}-%{release}
%description    libs
%{summary}.

%package        doc
Summary:        Documentation and user manuals for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf5-kauth-devel >= %{majmin}
Requires:       kf5-kconfigwidgets-devel >= %{majmin}
Requires:       kf5-kcoreaddons-devel >= %{majmin}
Requires:       kf5-kcrash-devel >= %{majmin}
Requires:       kf5-kdesignerplugin-devel >= %{majmin}
Requires:       kf5-kdoctools-devel >= %{majmin}
Requires:       kf5-kemoticons-devel >= %{majmin}
Requires:       kf5-kguiaddons-devel >= %{majmin}
Requires:       kf5-kiconthemes-devel >= %{majmin}
Requires:       kf5-kinit-devel >= %{majmin}
Requires:       kf5-kitemmodels-devel >= %{majmin}
Requires:       kf5-knotifications-devel >= %{majmin}
Requires:       kf5-kparts-devel >= %{majmin}
Requires:       kf5-ktextwidgets-devel >= %{majmin}
Requires:       kf5-kunitconversion-devel >= %{majmin}
Requires:       kf5-kwindowsystem-devel >= %{majmin}
Requires:       kf5-kdbusaddons-devel >= %{majmin}
Requires:       kf5-karchive-devel >= %{majmin}
Requires:       qt5-qtbase-devel

%if 0%{?fedora} || 0%{?rhel} > 7
%global _with_html --with-html
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
# Set absolute BIN_INSTALL_DIR, otherwise CMake will complain about mixed use of
# absolute and relative paths for some reason
# Remove once fixed upstream
%cmake_kf5 \
        -DBIN_INSTALL_DIR=%{_kf5_bindir}

%cmake_build


%install
%cmake_install

%find_lang all --all-name --with-man %{?_with_html}

%if 0%{?_with_html:1}
grep %{_kf5_docdir} all.lang > doc.lang
sort all.lang doc.lang | uniq -u > %{name}.lang
%else
echo '%{_kf5_docdir}/HTML/*/*' > doc.lang
cp all.lang %{name}.lang
%endif

## use ca-certificates' ca-bundle.crt, symlink as what most other
## distros do these days (http://bugzilla.redhat.com/521902)
if [  -f %{buildroot}%{_kf5_datadir}/kf5/kssl/ca-bundle.crt -a \
      -f /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem ]; then
  ln -sf /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
         %{buildroot}%{_kf5_datadir}/kf5/kssl/ca-bundle.crt
fi

## use kdebugrc from kde-settings instead
rm -fv %{buildroot}%{_kf5_sysconfdir}/xdg/kdebugrc


%files -f %{name}.lang
%doc README.md
%license COPYING.LIB
%{_kf5_bindir}/kf5-config
%{_kf5_mandir}/man1/kf5-config.1*
%{_kf5_bindir}/kdebugdialog5
# fileshareset pulls in perl
%{_kf5_libexecdir}/fileshareset
%{_kf5_libexecdir}/filesharelist
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/qimageioplugins/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/kf5/kdoctools/customization/
%{_kf5_datadir}/kf5/locale/
%{_kf5_datadir}/locale/kf5_all_languages
%{_kf5_datadir}/kf5/widgets/
%config %{_kf5_sysconfdir}/xdg/ksslcalist
%{_kf5_datadir}/kf5/kssl/
%config %{_kf5_sysconfdir}/xdg/colors
%config %{_kf5_sysconfdir}/xdg/kdebug.areas

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libKF5KDELibs4Support.so.*
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/designer/*.so
%{_kf5_plugindir}/kio/metainfo.so
%{_kf5_plugindir}/kded/networkstatus.so

%files doc -f doc.lang

%files devel
%{_kf5_libdir}/libKF5KDELibs4Support.so
%{_kf5_libdir}/cmake/KF5KDELibs4Support/
%{_kf5_libdir}/cmake/KF5KDE4Support/
%{_kf5_libdir}/cmake/KDELibs4/

%{_kf5_includedir}/KDELibs4Support/
%{_kf5_datadir}/dbus-1/interfaces/*.xml


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-7
- Prepare for Oreon 11 (RP1)
