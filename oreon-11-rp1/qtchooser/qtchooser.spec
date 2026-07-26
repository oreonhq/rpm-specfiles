%global source0_hash 4681d0561bf96599bf9bf5eb25103d07ee8f045f31576dc2e72b8529587a67c6

%define git g4717841

Name:	 qtchooser
Summary: Wrapper to select between Qt development binary versions
Version: 39
Release: 35%{?dist}

# Automatically converted from old format: LGPLv2 or GPLv3 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2 OR GPL-3.0-only
URL:	 http://macieira.org/qtchooser
Source0: http://macieira.org/qtchooser/qtchooser-%{version}-%{git}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
## Qt5
BuildRequires: pkgconfig(Qt5Core) pkgconfig(Qt5Test)
## default runtime expected
Recommends: qt5-assistant
Recommends: qt5-designer
Recommends: qt5-linguist
Recommends: qt5-qdbusviewer
Recommends: qt5-qtbase-devel
Recommends: qt5-qtdeclarative-devel
Recommends: qt5-qtquick1-devel
Recommends: qt5-qttools
Recommends: qt5-qtxmlpatterns-devel

## Qt4
#BuildRequires: pkgconfig(QtCore) pkgconfig(QtTest)
## default runtime expected
#Recommends: %{_qt4}-config
#Recommends: %{_qt4}-devel
#Recommends: %{_qt4}-qdbusviewer

# profile.d snippets to add /usr/lib/qthcooser to $PATH
SOURCE10: qtchooser.sh
SOURCE11: qtchooser.csh

%description
Qt Chooser provides a wrapper to switch between versions of Qt development
binaries when multiple versions like 4 and 5 are installed or local Qt builds
are to be used.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n qtchooser-%{version}-%{git}

%build
#PATH="%{_qt5_bindir}:$PATH" ; export PATH
%make_build \
  %{?optflags:CXXFLAGS="%{optflags}"} \
  %{?__global_ldflags:LFLAGS="%{__global_ldflags}"}

%install
make install INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}/etc/xdg/qtchooser

# Install man page not installed by Makefile
install -D -p -m 0644 doc/qtchooser.1 %{buildroot}%{_mandir}/man1/qtchooser.1

## env vars
#QT_SELECT
#QTCHOOSER_RUNTOOL

## HACK ALERT
# so, kde-sig decided putting this into %_bindir and using unconditionally is...
# problematic and unacceptable, so a compromise is to stuff this away so users
# can opt-in to use it
mkdir -p %{buildroot}%{_prefix}/lib/qtchooser
mv %{buildroot}%{_bindir}/* %{buildroot}%{_prefix}/lib/qtchooser/

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m644 -p %{SOURCE10} %{SOURCE11} \
  %{buildroot}%{_sysconfdir}/profile.d/

%check
PATH="%{_qt5_bindir}:$PATH" ; export PATH
make check

%files
%license LGPL_EXCEPTION.txt LICENSE.GPL LICENSE.LGPL
%dir %{_sysconfdir}/xdg/qtchooser
%{_sysconfdir}/profile.d/qtchooser.*
%{_mandir}/man1/qtchooser.1*
%dir %{_prefix}/lib/qtchooser/
%{_prefix}/lib/qtchooser/qtchooser
%{_prefix}/lib/qtchooser/assistant
%{_prefix}/lib/qtchooser/designer
%{_prefix}/lib/qtchooser/lconvert
%{_prefix}/lib/qtchooser/linguist
%{_prefix}/lib/qtchooser/lrelease
%{_prefix}/lib/qtchooser/lupdate
%{_prefix}/lib/qtchooser/moc
%{_prefix}/lib/qtchooser/pixeltool
%{_prefix}/lib/qtchooser/qcollectiongenerator
%{_prefix}/lib/qtchooser/qdbus
%{_prefix}/lib/qtchooser/qdbuscpp2xml
%{_prefix}/lib/qtchooser/qdbusviewer
%{_prefix}/lib/qtchooser/qdbusxml2cpp
%{_prefix}/lib/qtchooser/qdoc
%{_prefix}/lib/qtchooser/qdoc3
%{_prefix}/lib/qtchooser/qglinfo
%{_prefix}/lib/qtchooser/qhelpconverter
%{_prefix}/lib/qtchooser/qhelpgenerator
%{_prefix}/lib/qtchooser/qmake
%{_prefix}/lib/qtchooser/qml
%{_prefix}/lib/qtchooser/qml1plugindump
%{_prefix}/lib/qtchooser/qmlbundle
%{_prefix}/lib/qtchooser/qmlmin
%{_prefix}/lib/qtchooser/qmlplugindump
%{_prefix}/lib/qtchooser/qmlprofiler
%{_prefix}/lib/qtchooser/qmlscene
%{_prefix}/lib/qtchooser/qmltestrunner
%{_prefix}/lib/qtchooser/qmlviewer
%{_prefix}/lib/qtchooser/qtconfig
%{_prefix}/lib/qtchooser/rcc
%{_prefix}/lib/qtchooser/uic
%{_prefix}/lib/qtchooser/uic3
%{_prefix}/lib/qtchooser/xmlpatterns
%{_prefix}/lib/qtchooser/xmlpatternsvalidator

%changelog
%autochangelog
