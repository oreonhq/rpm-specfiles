# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 528ee5b8ca0a27d8d66128ebf850e23be9571dc130cf2a82dd2463dac7d3a92f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global forgeurl    https://gitlab.freedesktop.org/upower/%{name}

Version:        0.30
%forgemeta

Name:           power-profiles-daemon
Release:        %autorelease
Summary:        Makes power profiles handling available over D-Bus

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        https://gitlab.freedesktop.org/upower/power-profiles-daemon/-/archive/0.30/power-profiles-daemon-0.30.tar.bz2

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  argparse-manpage
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  python3dist(shtab)
BuildRequires:  systemd-rpm-macros

# Test dependencies
BuildRequires:  umockdev
BuildRequires:  python3dist(python-dbusmock)
BuildRequires:  python3dist(pygobject)

# This is an implementation of the power-profiles-daemon service
Provides:       ppd-service
Conflicts:      ppd-service

%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
This package contains the documentation for %{name}.

%prep
%oreon_verify_sources
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

%check
# Tests may fail when executed in parallel
%define _smp_build_ncpus 1
%meson_test

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/powerprofilesctl
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_datadir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.UPower.PowerProfiles.conf
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/dbus-1/system-services/org.freedesktop.UPower.PowerProfiles.service
%{_datadir}/polkit-1/actions/power-profiles-daemon.policy
%dir %{_localstatedir}/lib/power-profiles-daemon/
%{_mandir}/man1/powerprofilesctl.1.gz
%{bash_completions_dir}/powerprofilesctl
%{zsh_completions_dir}/_powerprofilesctl


%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.30-1
- Prepare for Oreon 11 (RP1)
