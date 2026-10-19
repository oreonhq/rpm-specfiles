%global source0_hash ed915dd146eb10262816da62904d04f78dacf9595d44d400dd1644d21c10c1e4
%global framework kdelibs4support
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 4 module with porting aid from KDELibs 4
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       ca-certificates
Requires:       kde-settings
Requires:       kf5-kded >= %{majmin}
# oreon:deps
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  ca-certificates
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-devel
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kded-devel
BuildRequires:  kf5-kdesignerplugin-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kemoticons-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kunitconversion-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
# /oreon:deps
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
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

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
if [  -f %{buildroot}%{_kf5_datadir}/kf5/kssl/ca-bundle.crt -a \
      -f /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem ]; then
  ln -sf /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
         %{buildroot}%{_kf5_datadir}/kf5/kssl/ca-bundle.crt
fi
rm -fv %{buildroot}%{_kf5_sysconfdir}/xdg/kdebugrc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kdelibs4support-libs -f %{oreon_filedir}/kf5-kdelibs4support-libs.list
%files -n kf5-kdelibs4support-doc -f %{oreon_filedir}/kf5-kdelibs4support-doc.list
%files -n kf5-kdelibs4support-devel -f %{oreon_filedir}/kf5-kdelibs4support-devel.list

%changelog

%autochangelog
