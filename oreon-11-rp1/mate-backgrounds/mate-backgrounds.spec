%global source0_hash 50d1afd02486bd07ac22a5a6b6efa3031148f0d48a82e488d909ad57003a6943
Name:          mate-backgrounds
Version:       1.28.0
Release:        1%{?dist}
Summary:        MATE Desktop backgrounds
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
Source1:       default-mate.xml
BuildArch:     noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mate-common
# /oreon:deps
%description
Backgrounds for MATE Desktop

%prep
%oreon_prep
%build

%configure
make %{?_smp_mflags} V=1
%install
%{make_install}
cp -f %{SOURCE1} %{buildroot}%{_datadir}/backgrounds/mate/default-mate.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
