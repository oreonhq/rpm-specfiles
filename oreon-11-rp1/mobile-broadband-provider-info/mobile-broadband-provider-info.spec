%global source0_hash 89bfeff215f4bff8e9c3ff2ec25250fdb080d11e9bfa59c6fc71982ac01c814a
Summary:        Mobile broadband provider database
Name: mobile-broadband-provider-info
Version: 20240407
Release:        1%{?dist}
URL: https://wiki.gnome.org/Projects/NetworkManager/MobileBroadband/ServiceProviders
License: CC-PDDC
Source0:        https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/xmllint
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  gcc
BuildRequires:  meson
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%check

%meson_test
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mobile-broadband-provider-info-devel -f %{oreon_filedir}/mobile-broadband-provider-info-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20240407-5
- Prepare for Oreon 11 (RP1)
