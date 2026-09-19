%global source0_hash 6c1b769038b60250c88e47380cbb021cfa57a65f872bf4d6c340b5e3057096ac

Name: swayidle
Version: 1.9.0
Release: 2%{?dist}
Summary: An idle daemon for wayland compositors

# Automatically converted from old format: MIT and LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-LGPLv2+
URL: https://github.com/swaywm/swayidle
Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1: %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2: https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

BuildRequires: meson >= 0.59.0
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: pkgconfig(wayland-protocols) >= 1.40
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: scdoc

%description
swayidle is an idle management daemon for Wayland compositors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/fish/vendor_completions.d/swayidle.fish
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
