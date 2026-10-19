%global source0_hash 4c31e268579b943388dff31f5f5296496dfa0679a15eefdd3a8f8fe2c41a3f89
Name:           labwc-menu-generator
Version:        0.1.0
Release:        5%{?dist}
Summary:        Menu generator for labwc
SourceLicense:  GPL-2.0-only AND GPL-2.0-or-later
License:        GPL-2.0-only
URL:            https://github.com/labwc/labwc-menu-generator
Source0:        https://github.com/labwc/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Supplements:    labwc
# oreon:deps
BuildRequires:  /usr/bin/prove
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  scdoc
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
