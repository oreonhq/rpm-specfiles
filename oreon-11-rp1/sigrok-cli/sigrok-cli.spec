%global source0_hash 71d0443f36897bf565732dec206830dbea0f2789b6601cf10536b286d1140ab8

Name:           sigrok-cli
Version:        0.7.2
Release:        12%{?dist}
Summary:        Basic hardware access drivers for logic analyzers
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.sigrok.org
Source0:        %{url}/download/source/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
# libsigrok+decode minor versions have a significantly different API
BuildRequires:  pkgconfig(libsigrok)       >= 0.5.0
BuildRequires:  pkgconfig(libsigrokdecode) >= 0.5.0

%description
%{name} is a command-line tool written in C, which uses both libsigrok and
libsigrokdecode to provide the basic sigrok functionality from the
command-line. Among other things, it's useful for scripting purposes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%doc NEWS README
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/applications/org.sigrok.%{name}.desktop
%{_datadir}/icons/*/*/*/%{name}.svg

%changelog
%autochangelog
