%global source0_hash 528ee5b8ca0a27d8d66128ebf850e23be9571dc130cf2a82dd2463dac7d3a92f
%global forgeurl    https://gitlab.freedesktop.org/upower/%{name}
Version:        0.30
%forgemeta
Name:           power-profiles-daemon
Release:        1%{?dist}
Summary:        Makes power profiles handling available over D-Bus
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        https://gitlab.freedesktop.org/upower/power-profiles-daemon/-/archive/0.30/power-profiles-daemon-0.30.tar.bz2
Provides:       ppd-service
Conflicts:      ppd-service
# oreon:deps
BuildRequires:  argparse-manpage
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(python-dbusmock)
BuildRequires:  python3dist(shtab)
BuildRequires:  systemd-rpm-macros
BuildRequires:  umockdev
# /oreon:deps
%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch
%description docs
This package contains the documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%forgeautosetup

%build

%meson \
    -Dgtk_doc=true \
    -Dpylint=disabled \
    -Dzshcomp=%{zsh_completions_dir} \
%meson_build
%install
%meson_install
mkdir -p %{buildroot}/%{_localstatedir}/lib/power-profiles-daemon
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%define _smp_build_ncpus 1
%meson_test
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n power-profiles-daemon-docs -f %{oreon_filedir}/power-profiles-daemon-docs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.30-1
- Prepare for Oreon 11 (RP1)
