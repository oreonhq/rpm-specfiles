%global source0_hash e947048130f6300e8be86573af8f225b486884fac14fcfe01bd913b41fa73bd3
Name:           xrefresh
Version:        1.1.1
Release:        1%{?dist}
Summary:        Refresh all or part of an X screen
License:        MIT
URL:            https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes:      xorg-x11-server-utils < 7.7-40
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
# /oreon:deps
%description
xrefresh is a simple X program that causes all or part of your screen to be
repainted.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
