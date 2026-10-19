%global source0_hash 5772d4d1830664404d8f6ed96d9c35f6e7a53c60b1ac5571cd2a6183c7e633ed
Name:           mmsd-tng
Version:        2.6.4
Release:        1%{?dist}
Summary:        Multimedia Messaging Service
License:        GPL-2.0-or-later
URL:            https://gitlab.com/kop316/mmsd
Source0:        https://gitlab.com/kop316/mmsd/-/archive/%{version}/mmsd-%{version}.tar.gz
Source1:        mmsd-tng.service
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:    %{ix86}
%endif
Requires:       pkgconfig(mobile-broadband-provider-info)
Requires:       systemd
# oreon:deps
BuildRequires:  cmake(libphonenumber)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  protobuf-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
mmsd-tng is a lower level daemon that transmits and recieves MMSes. It works with
both the Modem Manager stack.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mmsd-%{version}
%oreon_prep
%build

%meson -Dbuild-mmsctl=true
%meson_build
%check

%meson_test
%install
%meson_install
mkdir -p %{buildroot}%{_userunitdir}
install -pDm644 %{SOURCE1} %{buildroot}%{_userunitdir}
%oreon_autofiles main

%preun

%systemd_user_preun mmsd-tng.service
%post

%systemd_user_post mmsd-tng.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
