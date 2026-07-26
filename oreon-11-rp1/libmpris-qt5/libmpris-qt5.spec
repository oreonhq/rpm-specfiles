%global source0_hash 4fa95cadc09110af9aa5454cb28dbf5cb59874026a6428a84bedc6f2755604ec

%global repo qtmpris

Name:           libmpris-qt5
Summary:        Qt and QML MPRIS interface and adaptor
Version:        1.0.0
Release:        16%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://git.merproject.org/mer-core/%{repo}
Source0:        https://git.merproject.org/mer-core/%{repo}/-/archive/%{version}/%{repo}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(dbusextended-qt5)
BuildRequires: make

%description
%{summary}.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{repo}-%{version}

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_libdir}/lib*.so.1*

%files devel
%dir %{_qt5_includedir}/MprisQt/
%{_qt5_includedir}/MprisQt/Mpris
%{_qt5_includedir}/MprisQt/MprisQt
%{_qt5_includedir}/MprisQt/MprisPlayer
%{_qt5_includedir}/MprisQt/MprisController
%{_qt5_includedir}/MprisQt/MprisManager
%{_qt5_includedir}/MprisQt/mpris.h
%{_qt5_includedir}/MprisQt/mprisqt.h
%{_qt5_includedir}/MprisQt/mprisplayer.h
%{_qt5_includedir}/MprisQt/mpriscontroller.h
%{_qt5_includedir}/MprisQt/mprismanager.h
%dir %{_qt5_qmldir}/org/nemomobile/
%dir %{_qt5_qmldir}/org/nemomobile/mpris/
%{_qt5_qmldir}/org/nemomobile/mpris/%{name}-qml-plugin.so
%{_qt5_qmldir}/org/nemomobile/mpris/plugins.qmltypes
%{_qt5_qmldir}/org/nemomobile/mpris/qmldir
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
%autochangelog
