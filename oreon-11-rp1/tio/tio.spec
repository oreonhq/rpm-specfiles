%global source2_hash b934b67de8577c8b7cf2e81e9673c5427801c70e9273e7fc6010b78a26855683
%global source1_hash 814fdc1ef57adcef18b5ca752b52fb21bcb1d34605c11a849cb87e7c63d5bc03
%global source0_hash 06fe0c22e3e75274643c017928fbc85e86589bc1acd515d92f98eecd4bbab11b
Summary:        Simple TTY terminal I/O application
Name:           tio
Version:        3.9
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://tio.github.io/
Source0:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  lua-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
# /oreon:deps
%description
Tio is a simple TTY terminal application which features a straightforward
commandline interface to easily connect to TTY devices for basic input/output.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
