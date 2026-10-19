%global source0_hash c7954b34da5766288ea19b56026421c9c1fe2c23ef379e57ec209dc0cf13df2b
%global systemd_unit_handover gnome-remote-desktop-handover.service
%global systemd_unit_headless gnome-remote-desktop-headless.service
%global systemd_unit_system gnome-remote-desktop.service
%global systemd_unit_user gnome-remote-desktop.service
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
%bcond rdp %[0%{?fedora} || 0%{?rhel} >= 10]
%bcond vnc %[0%{?fedora} || 0%{?rhel} < 10]
%global libei_version 1.0.901
%global pipewire_version 0.3.49
Name:           gnome-remote-desktop
Version:        51.0
Release:        1%{?dist}
Summary:        GNOME Remote Desktop screen share service
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-remote-desktop
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Patch0:         gnutls-anontls.patch
%if %{with rdp}
%endif
%if %{with vnc}
%endif
Requires:       libei%{?_isa} >= %{libei_version}
Requires:       pipewire%{?_isa} >= %{pipewire_version}
Obsoletes:      vino < 3.22.0-21
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  glslc
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(ffnvcodec)
BuildRequires:  pkgconfig(freerdp3)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libei-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(tss2-mu)
BuildRequires:  pkgconfig(tss2-rc)
BuildRequires:  pkgconfig(tss2-tctildr)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(winpr3)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  spirv-tools
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
GNOME Remote Desktop is a remote desktop and screen sharing service for the
GNOME desktop environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson \
%if %{with rdp}
    -Drdp=true \
%else
    -Drdp=false \
%endif
%if %{with vnc}
    -Dvnc=true \
%else
    -Dvnc=false \
%endif
    -Dsystemd=true \
    -Dtests=false
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%post

%systemd_post %{systemd_unit_system}
%systemd_user_post %{systemd_unit_handover}
%systemd_user_post %{systemd_unit_headless}
%systemd_user_post %{systemd_unit_user}
%preun

%systemd_preun %{systemd_unit_system}
%systemd_user_preun %{systemd_unit_handover}
%systemd_user_preun %{systemd_unit_headless}
%systemd_user_preun %{systemd_unit_user}
%postun

%systemd_postun_with_restart %{systemd_unit_system}
%systemd_user_postun_with_restart %{systemd_unit_handover}
%systemd_user_postun_with_restart %{systemd_unit_headless}
%systemd_user_postun_with_restart %{systemd_unit_user}
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
