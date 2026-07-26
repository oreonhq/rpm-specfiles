%global source0_hash c9b84be49cc40d712ec152f7fa3d6987a856b2703c44cbb5bfec29fce0f125b6

%global forgeurl https://gitlab.com/ubports/development/core/gsettings-qt
%global date 20220807
%global commit d5e002d7e0bce46c315bcc99a44a8bd51f49f488
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta

%global __provides_exclude ^libGSettingsQmlPlugin\\.so.*$

Name:           gsettings-qt
Version:        0.2
Release:        %autorelease
Summary:        Qt/QML bindings for GSettings
License:        LGPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  glib2-devel
BuildRequires:  gcc-c++
BuildRequires:  make

%description
Qt/QML bindings for GSettings.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?isa}

%description    devel
Header files and libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# remove test
rm -rf %{buildroot}%{_qt5_prefix}/tests -rf
find %{buildroot} -iname test* -exec rm -f {} \;
find %{buildroot} -iname cpptest* -exec rm -f {} \;

%files
%license COPYING
%{_libdir}/lib%{name}.so.1*
%dir %{_qt5_qmldir}/GSettings.1.0/
%{_qt5_qmldir}/GSettings.1.0/libGSettingsQmlPlugin.so
%{_qt5_qmldir}/GSettings.1.0/plugins.qmltypes
%{_qt5_qmldir}/GSettings.1.0/qmldir

%files devel
%dir %{_qt5_headerdir}/QGSettings/
%{_qt5_headerdir}/QGSettings/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
