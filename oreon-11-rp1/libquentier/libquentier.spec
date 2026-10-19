%global source0_hash 20d81c1658fbcffd8ab78fa5c171c2306c88e21b260000b416706628a6791517
%undefine __cmake_in_source_build
%global commit          04b7e7d8415b2610d30ce727db9cebc77387928e
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20220710
Name:       libquentier
Summary:        Set of Qt/C++ APIs for feature rich desktop clients for Evernote service
Version:    0.5.0
Release:        1%{?dist}
License:    GPL-3.0-only OR LGPL-3.0-only
URL:        https://github.com/d1vanov/libquentier
Source0:        https://github.com/d1vanov/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:     libquentier-4ce8e3b-fix_translations_install.patch
ExclusiveArch: %{qt5_qtwebengine_arches}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(QEverCloud-qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebChannel)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineCore)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(libxml2)
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libtidy-devel
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
%description
This library presents a set of Qt/C++ APIs useful for applications working as
feature rich desktop clients for Evernote service. The most important and
useful components of the library are the following:

 - Local storage - persistence of data downloaded from Evernote service in
   a local SQLite database
 - Synchronization - the logics of exchanging new and/or modified data
   with Evernote service
 - Note editor - the UI component capable for notes displaying and editing

The library is based on the lower level functionality provided by QEverCloud
library. It also serves as the functional core of Quentier application.

%package devel
Summary:       Headers files for developing with %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files for developing applications that use %{name}.

%package doc
Summary: Documentation for %{name}
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

%build

%cmake -DUSE_QT5=1 \
       -DCMAKE_INSTALL_LIBDIR=%{_qt5_libdir} \
       -DQt5_LUPDATE_EXECUTABLE=%{_bindir}/lupdate-qt5 \
       -DQt5_LRELEASE_EXECUTABLE=%{_bindir}/lrelease-qt5 \
       -DUSE_LD_GOLD=0
%cmake_build
cd %{_vpath_builddir}
make lupdate
make lrelease
make doc
%install
%cmake_install
cd %{_vpath_builddir}
mkdir -p %{buildroot}%{_qt5_docdir}/%{name}
cp -aR doc/html/* %{buildroot}%{_qt5_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libquentier-devel -f %{oreon_filedir}/libquentier-devel.list
%files -n libquentier-doc -f %{oreon_filedir}/libquentier-doc.list

%changelog

%autochangelog
