%global source0_hash 04d5f9f7ecb96585d64bb563171c5e1f590ca3c70740eb674c94208f86a2b1bf
%global sover 10
%bcond_without check
%bcond_with all_tests
Name:           qxmpp
Version:        1.16.3
Release:        1%{?dist}
Summary:        Cross-platform C++ XMPP client and server library
License:        LGPL-2.1-or-later AND CC0-1.0 AND CC-BY-SA-4.0
URL:            https://invent.kde.org/libraries/qxmpp
Source0:        https://invent.kde.org/libraries/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libomemo-c-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  protobuf-c-devel
BuildRequires:  qca-qt6-devel
# /oreon:deps
%description
QXmpp is a cross-platform C++ XMPP client and server library. It is written in
C++ and uses Qt framework.

QXmpp strives to be as easy to use as possible, the underlying TCP socket, the
core XMPP RFCs (RFC6120 and RFC6121) and XMPP extensions have been nicely
encapsulated into classes. QXmpp is ready to build XMPP clients complying with
the XMPP Compliance Suites 2022 for IM and Advanced Mobile. It comes with full
API documentation, automatic tests and some examples.

%package        qt6
Summary:        QXmpp library for Qt6
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  qca-qt6-devel
BuildRequires:  pkgconfig(gstreamer-1.0)
%description    qt6
QXmpp is a cross-platform C++ XMPP client and server library. It is written in
C++ and uses Qt framework.

QXmpp strives to be as easy to use as possible, the underlying TCP socket, the
core XMPP RFCs (RFC6120 and RFC6121) and XMPP extensions have been nicely
encapsulated into classes. QXmpp is ready to build XMPP clients complying with
the XMPP Compliance Suites 2022 for IM and Advanced Mobile. It comes with full
API documentation, automatic tests and some examples.

%package        qt6-devel
Summary:        Development Files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
%description    qt6-devel
This package contains libraries and header files for developing applications
that use %{name}-qt6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir qxmpp-v%{version}
%oreon_prep
%build

OPTIONS=(
    -GNinja \
    -DBUILD_TESTS=ON \
    -DBUILD_DOCUMENTATION=OFF \
    -DBUILD_OMEMO=ON \
    -DWITH_ENCRYPTION=ON \
    -DWITH_GSTREAMER=ON \
)
%global _vpath_builddir %{_target_platform}-qt6
%cmake \
    ${OPTIONS[@]} \
    -DQT_VERSION_MAJOR=6 \
%cmake_build
%install
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%global _vpath_builddir %{_target_platform}-qt6
%if %{with all_tests}
%ctest
%else
SKIP_TESTS='tst_qxmppcallmanager'
SKIP_TESTS+='|tst_qxmppdiscoverymanager'
SKIP_TESTS+='|tst_qxmppiceconnection'
SKIP_TESTS+='|tst_qxmpppubsubmanager'
SKIP_TESTS+='|tst_qxmpprostermanager'
SKIP_TESTS+='|tst_qxmppuserlocationmanager'
SKIP_TESTS+='|tst_qxmppusertunemanager'
SKIP_TESTS+='|tst_qxmppfileencryption'
SKIP_TESTS+='|tst_qxmpptransfermanager'
SKIP_TESTS+='|tst_qxmpphttpuploadmanager'
SKIP_TESTS+='|tst_qxmppjinglemessageinitiationmanager'
%ctest -E "$SKIP_TESTS"
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n qxmpp-qt6 -f %{oreon_filedir}/qxmpp-qt6.list
%files -n qxmpp-qt6-devel -f %{oreon_filedir}/qxmpp-qt6-devel.list

%changelog

%autochangelog

