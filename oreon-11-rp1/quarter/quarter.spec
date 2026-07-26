%global source0_hash 18d9c11c738bd85db782036cfdc7117691928ab62697249621dcd5716acdb1ab

%global sover 20

Name:           quarter
Version:        1.2.3
Release:        4%{?dist}
Summary:        Lightweight glue library between Coin and Qt

License:        BSD-3-Clause 
URL:            https://www.coin3d.org/quarter/
Source0:        https://github.com/coin3d/%{name}/releases/download/v%{version}/%{name}-%{version}-src.tar.gz

BuildRequires:  cmake gcc gcc-c++ doxygen
BuildRequires:  mesa-libGL-devel
BuildRequires:  Coin4-devel
BuildRequires:  qt6-qtbase-devel
# Needed for Cmake UI Config
BuildRequires:  qt6-qttools-static
BuildRequires:  libspnav-devel

%description
Quarter is a light-weight glue library that provides seamless integration
between Systems in Motions's Coin high-level 3D visualization library and
Trolltech's Qt 2D user interface library.

Qt and Coin is a perfect match since they are both open source, widely portable
and easy to use. Quarter has evolved from Systems in Motion's own experiences
using Coin and Qt together in our applications.

The functionality in Quarter revolves around QuarterWidget, a subclass of
QGLWidget. This widget provides functionality for rendering of Coin scenegraphs
and translation of QEvents into SoEvents. Using this widget is as easy as using
any other QWidget.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package doc
Summary:        Development documentation for %{name}
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DQUARTER_BUILD_DOCUMENTATION=ON

%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_libdir}/*.so.%{sover}*
%{_libdir}/qt6/plugins/designer/*

%files devel
%{_includedir}/Quarter/
%{_libdir}/*.so
%{_libdir}/cmake/Quarter-%{version}/
%{_libdir}/pkgconfig/Quarter.pc

%files doc
%{_docdir}/Quarter/

%changelog
%autochangelog
