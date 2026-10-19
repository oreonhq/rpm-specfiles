%global source0_hash 6a73e41f98388a5348b7902f54b02d177cb73b7e5eb0a7a0dcf688cc2c79b42a
Name:           novnc
Version:        1.7.0
Release:        1%{?dist}
Summary:        VNC client using HTML5 (Web Sockets, Canvas) with encryption support
Requires:       python3-websockify
Requires:       which
License:        GPL-3.0-only
URL:            https://github.com/novnc/noVNC
Source0:        https://github.com/novnc/noVNC/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
# /oreon:deps
%description
noVNC is both a HTML VNC client JavaScript library and an application built on
top of that library. noVNC runs well in any modern browser including mobile
browsers (iOS and Android).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n noVNC-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}/
cp -r * %{buildroot}/%{_datadir}/%{name}/
rm -rf %{buildroot}/%{_datadir}/%{name}/snap/
rm -rf %{buildroot}/%{_datadir}/%{name}/tests/
rm -rf %{buildroot}/%{_datadir}/%{name}/utils/
rm %{buildroot}/%{_datadir}/%{name}/po/Makefile
rm %{buildroot}/%{_datadir}/%{name}/po/po2js
rm %{buildroot}/%{_datadir}/%{name}/po/xgettext-html
install -m 444 vnc.html %{buildroot}/%{_datadir}/%{name}/index.html
install -m 444 vnc_lite.html %{buildroot}/%{_datadir}/%{name}/vnc_auto.html
mkdir -p %{buildroot}/%{_bindir}/
install utils/novnc_proxy  %{buildroot}/%{_bindir}/%{name}_server
install utils/novnc_proxy  %{buildroot}/%{_bindir}/%{name}_proxy
mkdir -p %{buildroot}/%{_mandir}/man1/
install docs/novnc_proxy.1 %{buildroot}/%{_mandir}/man1/%{name}_proxy.1
install docs/novnc_proxy.1 %{buildroot}/%{_mandir}/man1/%{name}_server.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
