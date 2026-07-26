%global source0_hash 623077e0909d8667202ed2d031aa32c70770652cbca6c48ed8cbcf97c23f0156

Name:     fuelmanager
Version:  0.5.1
Release:  11%{?dist}
Summary:  Manage fuel mileage

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:  GPL-3.0-or-later

URL:     https://gitlab.com/kc8hfi/fuelmanager
Source0: https://gitlab.com/kc8hfi/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: qt5-qtbase-devel
BuildRequires: desktop-file-utils
BuildRequires: make

Requires: hicolor-icon-theme
Requires: qt-assistant

%description
Application that keeps track of four things, miles, gallons, cost, and 
the date of each fill-up.  It generates monthly and yearly summaries of 
miles driven, cost of fuel,how many gallons, and fuel mileage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%{qmake_qt5} %{name}.pro PREFIX=%{_prefix}
make %{?_smp_mflags}

%install

make install INSTALL_ROOT=%{buildroot} 

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop

for s in 16 22 24 32 48 256; do
     %{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
     %{__cp} icons/${s}x${s}/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
%{__cp} %{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# install the AppData file
%__mkdir_p %{buildroot}%{_datadir}/appdata
cp fuelmanager.appdata.xml %{buildroot}%{_datadir}/appdata/

%files
%doc COPYING
%doc documentation/fuelmanager.qhc
%{_bindir}/%{name}
%{_datadir}/appdata/*.*
%{_datadir}/applications/*.*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/256x256/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*

%changelog
%autochangelog
