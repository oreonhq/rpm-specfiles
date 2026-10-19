%global source0_hash b1dfff122fa0faf74e1fdb9ef9d417a9a9d0745e2913287ce2c0a6c0027a946c
%bcond check 1
Name:           phrog
Version:        0.50.0
Release:        1%{?dist}
Summary:        Mobile-friendly greeter for greetd
SourceLicense:  GPL-3.0-only AND CC-BY-SA-4.0
License:        %{shrink:
    ((MIT OR Apache-2.0) AND Unicode-3.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    GPL-3.0-only AND
    LGPL-2.1-only AND
    MIT AND
    (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND
    (Unlicense OR MIT)
}
URL:            https://github.com/samcday/phrog
Source0:        https://github.com/samcday/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
ExcludeArch:    ppc64le
ExcludeArch:    s390x
%if %{with check}
%endif
Requires:       accountsservice
Requires:       gnome-session
Requires:       greetd
Requires:       phoc
Requires:       phosh-osk = 1.0
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  foot
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libphosh-0.45)
BuildRequires:  rustc
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Phrog uses Phosh and greetd to provide a graphical login manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%oreon_vendor_cargo
%build

%cargo_build
%cargo_vendor_manifest
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
install -Dpm 0644 data/mobi.phosh.Phrog.service -t %{buildroot}%{_userunitdir}/
install -Dpm 0644 data/mobi.phosh.Phrog.target -t %{buildroot}%{_userunitdir}/
install -Dpm 0644 data/mobi.phosh.phrog.gschema.xml -t %{buildroot}%{_datadir}/glib-2.0/schemas/
install -Dpm 0644 data/phrog.session -t %{buildroot}%{_datadir}/gnome-session/sessions/
install -Dpm 0644 data/mobi.phosh.Phrog.desktop -t %{buildroot}%{_datadir}/applications/
install -Dpm 0644 dist/fedora/greetd-config.toml -t %{buildroot}%{_sysconfdir}/phrog/
install -Dpm 0644 dist/fedora/phrog.service -t %{buildroot}%{_unitdir}/
install -Dpm 0644 data/systemd-session.conf -T %{buildroot}%{_userunitdir}/gnome-session@phrog.target.d/session.conf
install -Dpm 0755 data/phrog-greetd-session -t %{buildroot}%{_libexecdir}/
install -d %{buildroot}%{_datadir}/phrog/autostart
install -d %{buildroot}%{_sysconfdir}/phrog/autostart
install -Dpm 0755 target/rpm/phrog -t %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/mobi.phosh.Phrog.desktop
export XDG_RUNTIME_DIR=/tmp/runtime-dir
mkdir -p ${XDG_RUNTIME_DIR}
chmod 0700 ${XDG_RUNTIME_DIR}
export G_MESSAGES_DEBUG=all
%{shrink:dbus-run-session xvfb-run -a -s -noreset phoc -S -E "%cargo_test"}
%endif
%post

%systemd_post phrog.service
%preun

%systemd_preun phrog.service
%postun

%systemd_postun_with_restart phrog.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
