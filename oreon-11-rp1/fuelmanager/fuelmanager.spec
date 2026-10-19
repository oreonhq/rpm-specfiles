%global source0_hash 4e63f2cf4f0062bb2d075bef29507f18f801ae8d4dbb5f36ffdad651058f50c9
Name:     fuelmanager
Version:  0.5.1
Release:        1%{?dist}
Summary:        Manage fuel mileage
License:  GPL-3.0-or-later
URL:     https://gitlab.com/kc8hfi/fuelmanager
Source0:        https://gitlab.com/kc8hfi/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Requires: hicolor-icon-theme
Requires: qt-assistant
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
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
%__mkdir_p %{buildroot}%{_datadir}/appdata
cp fuelmanager.appdata.xml %{buildroot}%{_datadir}/appdata/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
