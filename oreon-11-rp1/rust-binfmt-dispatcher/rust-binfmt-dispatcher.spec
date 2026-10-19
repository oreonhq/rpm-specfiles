%global source0_hash 23249357bab9ed0d22c9e648e4e1249a58919ff3095e1f338ac1da01c1b96051
%bcond check 1
%global crate binfmt-dispatcher
Name:           rust-binfmt-dispatcher
Version:        0.1.2
Release:        1%{?dist}
Summary:        Smart dispatcher for binfmt_misc
License:        MIT
URL:            https://crates.io/crates/binfmt-dispatcher
Source0:        https://static.crates.io/crates/binfmt-dispatcher/binfmt-dispatcher-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  make
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Smart dispatcher for binfmt_misc
License:        ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND ISC AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
Requires:       polkit
Requires:       systemd
Recommends:     xdg-terminal-exec
Recommends:     zenity
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
make install-data DESTDIR="%{buildroot}"
install -Ddpm0755 %{buildroot}%{_prefix}/lib/binfmt-dispatcher.d
%ifarch %{ix86} %{x86_64}
rm %{buildroot}%{_binfmtdir}/binfmt-dispatcher-*.conf
rm %{buildroot}%{_sysconfdir}/binfmt-dispatcher.toml
%else
for f in %{buildroot}%{_binfmtdir}/binfmt-dispatcher-*.conf; do mv "$f" "$(dirname "$f")/zz-$(basename "$f")"; done
mv %{buildroot}%{_sysconfdir}/binfmt-dispatcher.toml %{buildroot}%{_prefix}/lib/binfmt-dispatcher.d/00-default.toml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%postun      -n %{crate}

if [ $1 -eq 0 ]; then
/bin/systemctl try-restart systemd-binfmt.service
fi
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n binfmt-dispatcher -f %{oreon_filedir}/binfmt-dispatcher.list

%changelog

%autochangelog
