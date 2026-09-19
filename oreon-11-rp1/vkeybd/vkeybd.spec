%global source0_hash 96461670943c482ea3dd062a1ba59741bf9a1a9daed6bebf1b6ba5178943d37c

%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
%global with_desktop_vendor_tag 1
%else
%global with_desktop_vendor_tag 0
%endif

Summary:      Virtual MIDI keyboard
Name:         vkeybd
Version:      0.1.18f
Release:      3%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:      GPL-2.0-or-later
URL:          https://github.com/tiwai/%{name}
Source0:      https://github.com/tiwai/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:      vkeybd.png
Source2:      vkeybd.desktop
Patch0:       vkeybd-makefile.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: tk-devel >= 1:9.0
BuildRequires: lash-devel

BuildRequires: desktop-file-utils

Requires: tk >= 1:9.0
Requires: hicolor-icon-theme

%description
This is a virtual keyboard for AWE, MIDI and ALSA drivers.
It's a simple fake of a MIDI keyboard on X-windows system.
Enjoy a music with your mouse and "computer" keyboard :-)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i -e 's|-Wall -O|$(RPM_OPT_FLAGS)|' Makefile

%build
%make_build USE_AWE=0 TCL_VERSION=9.0 PREFIX=%{_prefix}

%install
%make_install USE_AWE=0 PREFIX=%{_prefix}
%make_install USE_AWE=0 PREFIX=%{_prefix} install-man
chmod 644 %{buildroot}/%{_mandir}/man1/*
chmod 755 %{buildroot}/%{_datadir}/vkeybd/vkeybd.tcl

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/vkeybd.png

mkdir -p %{buildroot}/%{_datadir}/applications
desktop-file-install \
%if 0%{?with_desktop_vendor_tag}
  --vendor fedora            \
%endif
  --dir %{buildroot}/%{_datadir}/applications \
  --add-category X-Fedora                       \
  %{SOURCE2}

%files
%doc README ChangeLog
%{_bindir}/vkeybd
%{_bindir}/sftovkb
%{_datadir}/vkeybd/
%{_mandir}/man1/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/vkeybd.png

%changelog
%autochangelog
