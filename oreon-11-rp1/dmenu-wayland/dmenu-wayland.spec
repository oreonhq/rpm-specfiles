%global source0_hash 56340e198a2c58468c6109f3bb07ab8a074487e67b0758b29c9d4fdce7c4d594
%global commit a380201dff5bfac2dace553d7eaedb6cea6855f9
%global short_commit %(c=%{commit}; echo ${c:0:7})
Name:           dmenu-wayland
Version:        0.1^20241231.%{short_commit}
Release:        1%{?dist}
Summary:        An efficient dynamic menu for wayland (wlroots)
License:        MIT
URL:            https://github.com/nyyManni/dmenu-wayland
Source0:        https://github.com/nyyManni/%{name}/archive/%{commit}/%{name}-%{short_commit}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
%description
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

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
