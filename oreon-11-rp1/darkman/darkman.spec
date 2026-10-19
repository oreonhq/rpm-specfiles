%global source0_hash 9a83ba1686a5087a7cdb3a6e995c9b90a15318a09076b747b0d0cdd90dde73d9
%bcond check 0
%global goipath         gitlab.com/WhyNotHugo/darkman
%global forgeurl        https://gitlab.com/WhyNotHugo/darkman
Version:                2.3.1
%global tag             v%{version}
%gometa -L -f
Name:           darkman
Release:        1%{?dist}
Summary:        Daemon for dark-mode and light-mode transitions on Linux desktop
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/%{name}-%{tag}.tar.bz2
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       dbus-common
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Daemon for dark-mode and light-mode transitions on Linux desktop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
scdoc < darkman.1.scd > darkman.1
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0644 -Dp contrib/darkman.service     %{buildroot}%{_userunitdir}/darkman.service
install -m 0644 -Dp darkman.1           %{buildroot}%{_mandir}/man1/darkman.1
install -m 0644 -Dp contrib/dbus/nl.whynothugo.darkman.service %{buildroot}%{_datadir}/dbus-1/services/nl.whynothugo.darkman.service
install -m 0644 -Dp contrib/dbus/org.freedesktop.impl.portal.desktop.darkman.service %{buildroot}%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.darkman.service
install -m 0644 -Dp contrib/portal/darkman.portal %{buildroot}%{_datadir}/xdg-desktop-portal/portals/darkman.portal
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%post

%systemd_user_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%postun

%systemd_user_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
