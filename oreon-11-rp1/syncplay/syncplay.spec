%global source0_hash f9d4e4b6d273f08e0c8df3171805c405d8b5d141d4d54f88f391cb645788f6a3
Name:           syncplay
Version:        1.7.6
Release:        1%{?dist}
Summary:        Synchronize playback of various video players via internet
License:        Apache-2.0 AND MIT AND BSD-3-Clause AND CC-BY-3.0
URL:            https://syncplay.pl
Source0:        https://github.com/Syncplay/syncplay/archive/refs/tags/v%{version}/syncplay-%{version}.tar.gz
BuildArch:      noarch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-syncplay = %{version}-%{release}
# /oreon:deps
%description
Solution to synchronize video playback across multiple instances of mpv, VLC,
MPC-HC and MPC-BE over the Internet.
Syncplay synchronizes the position and play state of multiple media players so
that the viewers can watch the same thing at the same time. This means that
when one person pauses/unpauses playback or seeks (jumps position) within their
media player then this will be replicated across all media players connected to
the same server and in the same 'room' (viewing session). When a new person
joins they will also be synchronised. Syncplay also includes text-based chat so
you can discuss a video as you watch it (or you could use third-party Voice
over IP software to talk over a video).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  syncplay/resources/*.desktop
for size in 256 128 96 64 48 32 24 16; do
  install -Dpm 0644 \
    syncplay/resources/hicolor/${size}x${size}/apps/syncplay.png \
    %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/syncplay.png
done
install -Dpm 0644 docs/syncplay.1 %{buildroot}/%{_mandir}/man1/syncplay.1
install -Dpm 0644 docs/syncplay-server.1 %{buildroot}/%{_mandir}/man1/syncplay-server.1
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/syncplay.desktop
%files

%changelog

%autochangelog
