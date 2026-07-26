%global source0_hash 13bbf24b8bb52d9ba9b53929764ec0ea4d5ee26aaf71f01fbd021fc9794cc3e0

# https://bugzilla.redhat.com/show_bug.cgi?id=541154
%global _hardened_build 1
%global upstreamname xfce4-volumed-pulse
%global minorversion 0.2

Name:           xfce4-volumed
Version:        0.2.3
Release:        38%{?dist}
Summary:        Daemon to add additional functionality to the volume keys of the keyboard
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://git.xfce.org/apps/xfce4-volumed-pulse/
Source0:        https://archive.xfce.org/src/apps/%{upstreamname}/%{minorversion}/%{upstreamname}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  xfconf-devel
BuildRequires:  libnotify-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  keybinder3-devel

Provides:       xfce4-volumed-pulse

%description
The xfce4-volumed adds additional functionality to the volume up/down and mute
keys of the keyboard. It makes the keys work without configuration and uses 
the XFCE 4 mixer's defined card and track for choosing which track to act on. 
The volume level is shown in a notification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{upstreamname}-%{version}
echo "Icon=multimedia-volume-control" >> data/%{name}.desktop

%build
%configure
%make_build

%install
%make_install
desktop-file-install \
  --add-category="Utility" \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_sysconfdir}/xdg/autostart/%{upstreamname}.desktop

# one launcher is enough, we don't want to have a daemon in the menu
rm -rf %{buildroot}/%{_datadir}/applications/

%files
%doc AUTHORS ChangeLog README THANKS
%license COPYING
/etc/xdg/autostart/%{upstreamname}.desktop
%{_bindir}/%{upstreamname}

%changelog
%autochangelog
