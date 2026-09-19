%global source0_hash 574bf5566517c89d9274a331971fa6eefc6beb48d0882b65105299fd6abbc7c4

Summary:        Tools to manage network attached LXI compatible instruments
Name:           lxi-tools
Version:        2.8
Release:        4%{?dist}
# src/language-specs/lua-lxi-gui.lang is LGPL-2.1-or-later, rest is BSD-3-Clause
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://lxi-tools.github.io/
Source0:        https://github.com/lxi-tools/lxi-tools/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxi-tools/lxi-tools/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  meson >= 0.53.2
BuildRequires:  readline-devel
BuildRequires:  liblxi-devel >= 1.13
BuildRequires:  lua-devel >= 5.1
BuildRequires:  pkgconfig(bash-completion)
%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires:  glib2-devel >= 2.70
BuildRequires:  gtk4-devel >= 4.6.0
BuildRequires:  gtksourceview5-devel >= 5.4.0
BuildRequires:  json-glib-devel >= 1.4
BuildRequires:  libadwaita-devel >= 1.2
BuildRequires:  %{_bindir}/desktop-file-validate
BuildRequires:  %{_bindir}/appstream-util
%endif
Recommends:     bash-completion

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
%if 0%{?fedora} || 0%{?rhel} > 9
  -Dgui=true
%else
  -Dgui=false
%endif
%meson_build

%install
%meson_install

%if 0%{?fedora} || 0%{?rhel} > 9
%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/io.github.%{name}.lxi-gui.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/io.github.%{name}.lxi-gui.appdata.xml
%endif

%files
%license LICENSE
%doc AUTHORS NEWS README.md
%{_bindir}/lxi
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/lxi*
%{_mandir}/man1/lxi.1*
%if 0%{?fedora} || 0%{?rhel} > 9
%{_bindir}/lxi-gui
%{_datadir}/applications/io.github.%{name}.lxi-gui.desktop
%{_datadir}/glib-2.0/schemas/io.github.%{name}.lxi-gui.gschema.xml
%{_datadir}/icons/hicolor/*/apps/io.github.%{name}.lxi-gui*.svg
%{_metainfodir}/io.github.%{name}.lxi-gui.appdata.xml
%endif

%changelog
%autochangelog
