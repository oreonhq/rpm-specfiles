%global source0_hash e698be8fc0d32c5f0b5b46cafcb8f615accaed524b864e58b99b64b7b5549c2d
Summary:        Compatibility version of Qt Assistant
Name:    qt-assistant-adp
Version: 4.6.3
Release:        1%{?dist}
License: LGPL-2.0-or-later WITH FLTK-exception OR LicenseRef-Callaway-GPLv3-with-exceptions
Url: https://download.qt.io/archive/qt/4.6/
Source0:        https://download.qt.io/archive/qt/4.6/qt-assistant-qassistantclient-library-compat-src-%{version}.tar.gz
Source1: QAssistantClient
Source2: QtAssistant
Patch1: 01_build_system.diff
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt4-devel
# /oreon:deps
%description
The old version of Qt Assistant, based on Assistant Document Profile (.adp)
files, and the associated QtAssistantClient library, for compatibility with
applications providing help in that format.

New applications should use the new version of Qt Assistant introduced in Qt
4.4, based on the Qt Help Framework also introduced in Qt 4.4, instead.

%package devel
Summary: Development files for the compatibility QAssistantClient
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt4-devel
%description devel
This package contains the files necessary to build applications using the
deprecated QAssistantClient class (in the deprecated QtAssistantClient library),
which is used together with the legacy Assistant Document Profile (.adp) version
of Qt Assistant.

This class is obsolete. It is provided to keep old source code working. We
strongly advise against using it in new code. New code should use the Qt Help
Framework introduced in Qt 4.4 and/or the version of Qt Assistant based on it
(also introduced in Qt 4.4) instead.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n qt-assistant-qassistantclient-library-compat-version-%{version}
%patch -P1 -p1 -b .build_system
mkdir include
cp -p %{SOURCE1} %{SOURCE2} include/

%build

%{qmake_qt4} QT_PRODUCT=OpenSource
%make_build
pushd lib
%{qmake_qt4} CONFIG=create_prl
%make_build
popd
pushd translations
lrelease-qt4 assistant_adp_*.ts
popd
%install
make install INSTALL_ROOT=%{buildroot}
make install INSTALL_ROOT=%{buildroot} -C lib
mkdir -p %{buildroot}%{_qt4_translationdir}
install -p -m644 translations/assistant_adp_*.qm \
                 %{buildroot}%{_qt4_translationdir}/
install -D -p -m644 features/assistant.prf \
                    %{buildroot}%{_qt4_datadir}/mkspecs/features/assistant.prf
install -p -m644 include/Q* %{buildroot}%{_qt4_headerdir}/QtAssistant/
sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" %{buildroot}%{_qt4_libdir}/*.prl
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt4_bindir}
mv assistant_adp ../../../bin/
ln -s ../../../bin/assistant_adp .
popd
pushd %{buildroot}%{_qt4_libdir}
echo "INPUT(-lQtAssistantClient)" >libQtAssistantClient_debug.so
popd
%find_lang assistant_adp --with-qt --without-mo
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qt-assistant-adp-devel -f %{oreon_filedir}/qt-assistant-adp-devel.list

%changelog

%autochangelog
