Summary: Mobile broadband provider database
Name: mobile-broadband-provider-info
Version: 20240407
Release: 5%{?dist}
URL: https://wiki.gnome.org/Projects/NetworkManager/MobileBroadband/ServiceProviders
License: CC-PDDC
Source: https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildArch: noarch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: /usr/bin/xmllint
BuildRequires: /usr/bin/xsltproc

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.


%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains files necessary for
developing developing applications that use %{name}.


%prep
%autosetup


%build
%meson
%meson_build


%check
%meson_test


%install
%meson_install


%files
%{_datadir}/%{name}
%doc README
%license COPYING


%files devel
%{_datadir}/pkgconfig/%{name}.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20240407-5
- Prepare for Oreon 11 (RP1)
