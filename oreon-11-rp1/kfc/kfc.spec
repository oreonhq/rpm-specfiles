%global source0_hash 6471c9667dc2242360ba9457821e3a63b41110b32169aa4c7aaf4d465aff205f
Name:           kfc
Version:        0.1.4
Release:        1%{?dist}
Summary:        Terminal-emulator color palette setter written in POSIX C99
License:        MIT
URL:            https://github.com/mcpcpc/kfc
Source0:        https://github.com/mcpcpc/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          %{url}/commit/5c8017255c976ca47bd027dda76df3e07010f667.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
kfc ("KISS for colors") is a terminal-emulator color palette setter written in
POSIX C99. This allows one to achieve consistent colors across all terminal
utilities and applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{build_ldflags}"
%install
%make_install PREFIX="%{_prefix}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
