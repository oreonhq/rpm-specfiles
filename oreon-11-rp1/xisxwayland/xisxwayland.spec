%global source0_hash d24d9cdff3e3a7ee9456384eab8caaa1d71530d9d95131a23a243ebbee5da22d
Name:       xisxwayland
Version:    2
Release:        1%{?dist}
Summary:        Tool to check if the X server is XWayland
License:    MIT
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes:  xorg-x11-server-utils < 7.7-40
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
# /oreon:deps
%description
xisxwayland is a tool to be used within shell scripts to determine whether
the X server in use is Xwayland. It exits with status 0 if the server is an
Xwayland server and 1 otherwise.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
