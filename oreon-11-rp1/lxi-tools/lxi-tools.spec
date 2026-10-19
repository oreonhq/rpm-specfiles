%global source2_hash b934b67de8577c8b7cf2e81e9673c5427801c70e9273e7fc6010b78a26855683
%global source1_hash 09abae6b1cd6aa6fe3e37c993ee03d0f310cf65fc65dc4534001a04b120627c8
%global source0_hash 574bf5566517c89d9274a331971fa6eefc6beb48d0882b65105299fd6abbc7c4
Summary:        Tools to manage network attached LXI compatible instruments
Name:           lxi-tools
Version:        2.8
Release:        4%{?dist}
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://lxi-tools.github.io/
Source0:        https://github.com/lxi-tools/lxi-tools/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxi-tools/lxi-tools/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1
Recommends:     bash-completion
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  liblxi-devel
BuildRequires:  lua-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  readline-devel
# /oreon:deps
%description
LXI tools are open source software tools for managing network attached
LXI (LAN eXtensions for Instrumentation) compatible test instruments
such as modern oscilloscopes, power supplies, spectrum analyzers etc.

Features include automatic discovery of test instruments, sending SCPI
commands, grabbing screenshots from supported instruments, benchmarking
SCPI message performance, and powerful scripting for test automation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build

%meson \
  -Dgui=false
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
