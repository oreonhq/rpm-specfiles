%global source0_hash 40736ff326e11a51128c1739051a692ad2c79173fc4b695c8be5ec7a614b4de2

Name:           hikari
Version:        2.3.3
Release:        %autorelease
Summary:        Stacking Wayland compositor with tiling capabilities

License:        BSD-2-Clause
URL:            https://hikari.acmelabs.space/
Source0:        %{url}/releases/%{name}-%{version}.tar.gz

BuildRequires: bmake
BuildRequires: mk-files
BuildRequires: gcc
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(libucl)
BuildRequires: (pkgconfig(wlroots) >= 0.15 with pkgconfig(wlroots) < 0.16)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libevdev)
BuildRequires: glib2-devel
BuildRequires: pixman-devel
BuildRequires: pam-devel
Recommends: xorg-x11-server-Xwayland

%description
Hikari is a stacking Wayland compositor with additional tiling capabilities, it
is heavily inspired by the Calm Window manager (cwm(1)). Its core concepts are
views, groups, sheets and the workspace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

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

# FIXME: fix this in install/bmake process.
for binary in %{buildroot}/usr/bin/hikari %{buildroot}/usr/bin/hikari-unlocker; do
      chmod 0755 "${binary:?}"
done

%files
%license LICENSE
%doc README.md
%config %{_sysconfdir}/pam.d/%{name}-unlocker
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0755, root, root) %{_bindir}/%{name}
%attr(0755, root, root) %{_bindir}/%{name}-unlocker
%{_mandir}/man1/hikari.1*
%{_datadir}/backgrounds/%{name}/hikari_wallpaper.png
%{_datadir}/wayland-sessions/%{name}.desktop

%changelog
%autochangelog
