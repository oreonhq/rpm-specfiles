%global source0_hash 94d6079060ca5df74542921de4eea38b7d02d07561c919356d95de876f9a6d3a
%global branch 1.28
Name:          mate-icon-theme
Version:       %{branch}.0
Release:        1%{?dist}
Summary:        Icon theme for MATE Desktop
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
BuildArch:     noarch
# oreon:deps
BuildRequires:  icon-naming-utils
BuildRequires:  make
BuildRequires:  mate-common
# /oreon:deps
%description
Icon theme for MATE Desktop

%prep
%oreon_prep
%build

%configure  --enable-icon-mapping
make %{?_smp_mflags} V=1
%install
%{make_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
