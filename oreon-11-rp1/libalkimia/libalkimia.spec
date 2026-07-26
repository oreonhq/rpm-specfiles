%global source0_hash f921410e180e0a5811e1ee2926954920c6576a72b3b65f53791faa6c85fcb689

# uncomment to enable bootstrap mode
#global bootstrap 1

%if ! 0%{?bootstrap}
#global docs 1
%global tests 1
%endif

Name:    libalkimia
Summary: Financial library
Version: 8.2.1
Release: 3%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://kmymoney.org/
Source0: https://download.kde.org/stable/alkimia/%{version}/alkimia-%{version}.tar.xz

## upstream patches
# https://invent.kde.org/office/alkimia/-/commit/089794942385e4d3fc02e028eab2039bbcaab508
Patch0: alkimia-8.2.1-install-financequote.patch

## upstreamable patches
# https://invent.kde.org/office/alkimia/-/merge_requests/61
Patch100: alkimia-8.2.1-install-python.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkg-config
# KF6
BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(Plasma)
# Qt6
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Test)
%ifarch %{qt6_qtwebengine_arches}
%global webengine 1
BuildRequires: cmake(Qt6WebEngineWidgets)
%endif

# While upstream prefers MPIR over GMP (“MPIR is preferred over GMP” in
# CMakeLists.txt), MPIR is no longer maintained upstream
# (https://groups.google.com/g/mpir-devel/c/qTOaOBuS2E4?hl=en), so we
# unconditionally use GMP instead.
BuildRequires: pkgconfig(gmp)

# financequote.pl
BuildRequires: perl-generators

# gdb.py
BuildRequires: python3-devel

# %%check
%if 0%{?tests}
BuildRequires: xwayland-run
BuildRequires: libEGL
%endif

%if 0%{?docs}
BuildRequires: doxygen
%endif

%description
%{summary}

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gmp-devel
%description devel
%{summary}.

%package        qt6
Summary:        Accounts framework Qt6 bindings
Obsoletes:      %{name}-qt5 < 8.2.1
# financequote.pl
Recommends:     perl(Date::Manip)
Recommends:     perl(Finance::Quote)
Recommends:     perl(LWP)
Recommends:     perl(XML::Parser)
Recommends:     perl(XML::Writer)
%description    qt6
%{summary}.

%package        qt6-devel
Summary:        Development files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
Requires:       gmp-devel
%if 0%{?webengine}
Requires:       cmake(Qt6WebEngineWidgets)
%endif
Obsoletes:      %{name}-qt5-devel < 8.2.1
%description    qt6-devel
%{summary}.

%package        doc
Summary:        API Documentation for %{name}
BuildArch:      noarch
%description    doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n alkimia-%{version} -p1

%build
%cmake_kf6 \
  %{!?plasma:-DBUILD_APPLETS:BOOL=OFF} \
  -DBUILD_WITH_QT6=ON \
  -DBUILD_WITH_WEBENGINE:BOOL=%{?webengine:ON}%{!?webengine:OFF} \
  -DBUILD_WITH_WEBKIT:BOOL=OFF \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DENABLE_FINANCEQUOTE:BOOL=ON

%cmake_build

## docs
%if 0%{?docs}
# auto-update doxygen configuration
doxygen -u %{_target_platform}-qt6/src/libalkimia.doxygen
make libalkimia_apidoc -C %{_target_platform}-qt6
%endif

%install
%cmake_install

%if 0%{?docs}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a %{_target_platform}-qt6/src/apidocs/html/ %{buildroot}%{_pkgdocdir}/
%endif

## unpackaged files
%if ! 0%{?plasma}
rm -fv  %{buildroot}%{_kf6_datadir}/locale/*/LC_MESSAGES/plasma*
%endif

# Perform byte compilation manually on paths outside the usual locations
%py_byte_compile %{python3} %{buildroot}%{_datadir}/gdb

%find_lang %{name} --all-name

%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libalkimia6)" = "%{version}"
%if 0%{?tests}
# some tests require online access, not available in mock builds
# alkonlinequotestest requires a JS-enabled browser backend
%global __ctest xwfb-run -- %{__ctest}
time \
%ctest -E '(download|newstuff|web)engine%{!?webengine:|onlinequotes}'
%endif

%files qt6 -f %{name}.lang
%doc README.md
%license COPYING*
%{_kf6_bindir}/onlinequoteseditor6
%{_kf6_libdir}/libalkimia6.so.8{,.*}
%{_kf6_qmldir}/org/kde/alkimia6/
%{_kf6_datadir}/alkimia6/
%{_kf6_datadir}/applications/org.kde.onlinequoteseditor6.desktop
%{_kf6_datadir}/icons/*/*/apps/onlinequoteseditor6.*
%{_kf6_datadir}/knsrcfiles/*-quotes.knsrc
%{_kf6_metainfodir}/org.kde.onlinequoteseditor6.appdata.xml

%files qt6-devel
%dir %{_includedir}/alkimia/
%{_includedir}/alkimia/Qt6/
%{_kf6_libdir}/libalkimia6.so
%{_kf6_libdir}/pkgconfig/libalkimia6.pc
%{_kf6_libdir}/cmake/LibAlkimia6-*/
%{_kf6_datadir}/gdb/

%if 0%{?docs}
%files doc
%dir %{_pkgdocdir}/
%doc %{_pkgdocdir}/html
%endif

%changelog
%autochangelog
