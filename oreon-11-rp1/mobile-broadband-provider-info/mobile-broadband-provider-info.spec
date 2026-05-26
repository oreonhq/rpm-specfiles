Summary: Mobile broadband provider database
Name: mobile-broadband-provider-info
Version: 20240407
Release: 5%{?dist}
URL: https://wiki.gnome.org/Projects/NetworkManager/MobileBroadband/ServiceProviders
License: CC-PDDC
Source: https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 89bfeff215f4bff8e9c3ff2ec25250fdb080d11e9bfa59c6fc71982ac01c814a
%global source0_file mobile-broadband-provider-info-20240407.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/mobile-broadband-provider-info-20240407.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "89bfeff215f4bff8e9c3ff2ec25250fdb080d11e9bfa59c6fc71982ac01c814a" || { echo "oreon: Source0 SHA256 mismatch for mobile-broadband-provider-info-20240407.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
