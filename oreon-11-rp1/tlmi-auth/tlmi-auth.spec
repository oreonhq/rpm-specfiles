%global source0_hash 7350e29be99a47791b6024200a0baa9a44d76f30d4df8cbe2e1b566e52f7af8a

Name:     tlmi-auth
Version:  1.0.1
Release:  %autorelease
Summary:  Utility function for certificate based authentication on Lenovo platforms
License:  GPL-2.0-or-later
URL:      https://www.github.com/lenovo/tlmi-auth/
Source:   %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires: gcc
BuildRequires: meson
BuildRequires: openssl-devel

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files 
%license COPYING
%{_bindir}/tlmi-auth
%doc README.md

%check
%meson_test

%changelog
%autochangelog
