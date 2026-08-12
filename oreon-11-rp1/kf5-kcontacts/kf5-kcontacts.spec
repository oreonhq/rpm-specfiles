%global source0_hash f107fdec8f52f7362499159c958e57e3b8b1981b0d797a90685c4a604156b4cb

%global framework kcontacts

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Epoch:   1
Version: 5.116.0
Release: 7%{?dist}
Summary: The KContacts Library

License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://projects.kde.org/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcodecs-devel >= %{majmin}

BuildRequires:  qt5-qtbase-devel
BuildRequires:  cmake(Qt5Quick)

%if 0%{?test}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       kf5-kcoreaddons-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKF5Contacts.so.*

%files devel
%{_kf5_includedir}/KContacts/
%{_kf5_libdir}/libKF5Contacts.so
%{_kf5_libdir}/cmake/KF5Contacts/
%{_kf5_archdatadir}/mkspecs/modules/qt_KContacts.pri

%changelog
%autochangelog
