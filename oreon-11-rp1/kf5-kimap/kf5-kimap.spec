%undefine __cmake_in_source_build
%global framework kimap

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: The KIMAP Library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  boost-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcoreaddons-devel >= 5.23
BuildRequires:  kf5-kdelibs4support-devel >= 5.23
#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  qt5-qtbase-devel
%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

%if ! 0%{?bootstrap}
# runtime sasl plugins
Suggests: cyrus-sasl-gssapi%{?_isa}
Suggests: cyrus-sasl-md5%{?_isa}
Requires: cyrus-sasl-plain%{?_isa}
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-kmime-devel
Requires:       boost-devel
Requires:       cyrus-sasl-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
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
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5IMAP.so.*

%files devel
%{_includedir}/KPim5/KIMAP/
%{_kf5_libdir}/libKPim5IMAP.so
%{_kf5_libdir}/cmake/KF5IMAP/
%{_kf5_libdir}/cmake/KPim5IMAP/
%{_includedir}/KPim5/KIMAPTest/kimaptest/
%{_kf5_libdir}/libkimaptest.a
%{_kf5_archdatadir}/mkspecs/modules/qt_KIMAP.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
