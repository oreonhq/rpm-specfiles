%global source0_hash 7350e29be99a47791b6024200a0baa9a44d76f30d4df8cbe2e1b566e52f7af8a
Name:     tlmi-auth
Version:  1.0.1
Release:        1%{?dist}
Summary:        Utility function for certificate based authentication on Lenovo platforms
License:  GPL-2.0-or-later
URL:      https://www.github.com/lenovo/tlmi-auth/
Source0:        https://www.github.com/lenovo/%{name}//archive/refs/tags/v%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  openssl-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
