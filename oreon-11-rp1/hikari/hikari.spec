%global source0_hash 40736ff326e11a51128c1739051a692ad2c79173fc4b695c8be5ec7a614b4de2
Name:           hikari
Version:        2.3.3
Release:        1%{?dist}
Summary:        Stacking Wayland compositor with tiling capabilities
License:        BSD-2-Clause
URL:            https://hikari.acmelabs.space/
Source0:        https://%{name}.acmelabs.space//releases/%{name}-%{version}.tar.gz
Recommends: xorg-x11-server-Xwayland
# oreon:deps
BuildRequires:  (pkgconfig(wlroots) >= 0.15 with pkgconfig(wlroots) < 0.16)
BuildRequires:  bmake
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  mk-files
BuildRequires:  pam-devel
BuildRequires:  pixman-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libucl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(wayland-protocols)
# /oreon:deps
%description
Hikari is a stacking Wayland compositor with additional tiling capabilities, it
is heavily inspired by the Calm Window manager (cwm(1)). Its core concepts are
views, groups, sheets and the workspace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
export CFLAGS_EXTRA="$CFLAGS"
export LDFLAGS_EXTRA="$LDFLAGS"
bmake WITH_POSIX_C_SOURCE=YES \
      WITH_XWAYLAND=YES \
      WITH_SCREENCOPY=YES \
      WITH_GAMMACONTOL=YES \
      WITH_LAYERSHELL=YES \
      WITH_VIRTUAL_INPUT=YES
%install
bmake DESTDIR=%{buildroot} \
      PREFIX=%{_prefix} \
      ETC_PREFIX="" \
      WITHOUT_SUID=YES \
      install
for binary in %{buildroot}/usr/bin/hikari %{buildroot}/usr/bin/hikari-unlocker; do
      chmod 0755 "${binary:?}"
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
