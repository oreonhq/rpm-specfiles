%global source2_hash 1cb07f949cb233a365e927e5f868eceb6e143681208fd917de2a4a53f48001ec
%global source0_hash 6c67f52cae4f139df764ad1cc736562be0f97750791bc212b53f34c06eaf2205
Name:           i3status
Version:        2.15
Release:        1%{?dist}
Summary:        Status bar generator for i3bar, dzen2, xmobar or similar programs
License:        BSD-3-Clause
URL:            https://i3wm.org/i3status/
Source0:        https://i3wm.org/%{name}//%{name}-%{version}.tar.xz
Source1:        %{url}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D#./gpgkey-424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D.gpg
Source3:        fedora-i3-status-config
Recommends:     i3status-config
Requires:       (i3status-config or i3status-config-fedora)
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  perl
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(yajl)
BuildRequires:  xmlto
# /oreon:deps
%description
i3status is a program for generating a status bar for i3bar, dzen2,
xmobar or similar programs. It issues a small number of system
calls, as one generally wants to update such status lines every
second so that the bar is updated even under load. It saves a bit of
energy by being more efficient than shell commands.

%package        config
Summary:        Upstream configuration for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Conflicts:      %{name}-config-fedora
%description    config
This is the upstream/vanilla configuration file of %{name}.

%package        config-fedora
RemovePathPostfixes: .fedora
Summary:        Configuration of %{name} for the Fedora i3 Spin
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Conflicts:      %{name}-config
%description    config-fedora
This is the configuration file of %{name} used for the Fedora i3 Spin.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%meson
%meson_build
%install
%meson_install
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}.conf.fedora
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n i3status-config -f %{oreon_filedir}/i3status-config.list
%files -n i3status-config-fedora -f %{oreon_filedir}/i3status-config-fedora.list

%changelog

%autochangelog
