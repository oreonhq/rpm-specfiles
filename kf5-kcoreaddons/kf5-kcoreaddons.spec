%undefine __cmake_in_source_build
%global framework kcoreaddons

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon with various classes on top of QtCore

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  make
BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  shared-mime-info
BuildRequires:  systemd-devel

%if ! 0%{?bootstrap}
## Drop/omit FAM/gamin support: it is no longer supported upstream,
## e.g. https://bugzilla.gnome.org/show_bug.cgi?id=777997
#BuildRequires:  gamin-devel
%endif
%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:       kf5-filesystem >= %{majmin}

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%{cmake_kf5} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}
%cmake_build


%install
%cmake_install

%find_lang_kf5 kcoreaddons5_qt
%find_lang_kf5 kde5_xml_mimetypes
cat *.lang > all.lang


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
%make_build test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif


%if 0%{?rhel} && 0%{?rhel} < 8
%ldconfig_post

%postun
%{?ldconfig}
if [ $1 -eq 0 ] ; then
update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
update-mime-database %{_datadir}/mime &> /dev/null || :

%else
%ldconfig_scriptlets
%endif

%files -f all.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_bindir}/desktoptojson
%{_kf5_libdir}/libKF5CoreAddons.so.*
%{_kf5_datadir}/mime/packages/kde5.xml
%{_kf5_datadir}/kf5/licenses/

%files devel

%{_kf5_includedir}/KCoreAddons/
%{_kf5_libdir}/libKF5CoreAddons.so
%{_kf5_libdir}/cmake/KF5CoreAddons/
%{_kf5_archdatadir}/mkspecs/modules/qt_KCoreAddons.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
