%global source0_hash dddcb43c58acb334b529387da8f3abfee57346099dce8f438a167f5ebc34a9da
Name:           switcheroo-control
Version:        3.0
Release:        1%{?dist}
Summary:        D-Bus service to check the availability of dual-GPU
License:        GPL-3.0-only
URL:            https://gitlab.freedesktop.org/hadess/switcheroo-control/
Source0:        https://gitlab.freedesktop.org/hadess/switcheroo-control/-/releases/3.0/downloads/switcheroo-control-3.0.tar.xz
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  kernel-headers
BuildRequires:  libdrm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  python3-dbusmock
BuildRequires:  systemd
BuildRequires:  umockdev
# /oreon:deps
%description
D-Bus service to check the availability of dual-GPU.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch
%description docs

This package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

if [ $1 -eq 2 ] && [ -x /usr/bin/systemctl ] ; then
    /usr/bin/systemctl daemon-reload
fi
%systemd_post switcheroo-control.service
%udev_hwdb_update
%udev_rules_update
%preun

%systemd_preun switcheroo-control.service
%postun

%systemd_postun_with_restart switcheroo-control.service
%udev_hwdb_update
%udev_rules_update
%files -f %{oreon_filedir}/main.list
%files -n switcheroo-control-docs -f %{oreon_filedir}/switcheroo-control-docs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0-1
- Prepare for Oreon 11 (RP1)
