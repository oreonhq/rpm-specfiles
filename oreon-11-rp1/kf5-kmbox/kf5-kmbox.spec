%global source0_hash e583b87b0eb995ebfafa67817748c23cbd872108451e6bc8cd9590ba7ecdf400

%undefine __cmake_in_source_build
%global framework kmbox

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: The KMbox Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  qt5-qtbase-devel
%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kmime-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build

%install
%cmake_install

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 120" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5Mbox.so.*

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_KMbox.pri
%{_includedir}/KPim5/KMbox
%{_kf5_libdir}/cmake/KPim5Mbox/
%{_kf5_libdir}/libKPim5Mbox.so

%changelog
%autochangelog
