%global source0_hash a818e9f96715a09360a083685e5eb8eab9af5fc7e58fa92c839fa801912fe32f
ExcludeArch: %{ix86}
%bcond check 0
%global commit d1a69fe1e8c1a0bd6bafc81046e9aa1dc07ed3d9
%global commitdatestring 2026-04-06 16:13:17 -0400
%global cosmic_minver 1.0.9
Name:           cosmic-greeter
Version: 1.9.1
Release:        1%{?dist}
Summary:        Login and display manager for the COSMIC Desktop Environment
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC-PDDC AND CC0-1.0 AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/pop-os/cosmic-greeter
Source0:        https://github.com/pop-os/cosmic-greeter/archive/epoch-%{version}/cosmic-greeter-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Patch:          service.patch
Patch:          include-greetd.patch
%{?sysusers_requires_compat}
Requires:       dbus
Requires:       greetd
Requires:       greetd-selinux
Requires:       fprintd-pam
Requires:       pam
Requires:       cosmic-comp >= %{cosmic_minver}
Requires:       cosmic-icon-theme >= %{cosmic_minver}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  golang
BuildRequires:  just
BuildRequires:  libinput-devel
BuildRequires:  libudev-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  pam-devel
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
BuildRequires:  wayland-devel
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cosmic-greeter-epoch-%{version} -p1 -a1
# Check if .cargo/config.toml exists
if [ -f .cargo/config.toml ]; then
  # If it exists, append the contents of %%{SOURCE2} to .cargo/config.toml
  cat %{SOURCE2} >> .cargo/config.toml
  echo "Appended %{SOURCE2} to .cargo/config.toml"
else
  # If it does not exist, append the contents of %%{SOURCE2} to .cargo/config
  cat %{SOURCE2} >> .cargo/config
  echo "Appended %{SOURCE2} to .cargo/config"
fi

%build

export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
cargo build --release --all --offline --frozen
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt
sed 's/^\([^+]*\)+.*+\([^+]*\)$/\1+\2/' -i cargo-vendor.txt
%install
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
install -Dm0755 target/release/cosmic-greeter %{buildroot}/%{_bindir}/cosmic-greeter
install -Dm0755 target/release/cosmic-greeter-daemon %{buildroot}/%{_bindir}/cosmic-greeter-daemon
install -Dm0755 cosmic-greeter-start.sh %{buildroot}/%{_bindir}/cosmic-greeter-start
install -Dm0644 dbus/com.system76.CosmicGreeter.conf %{buildroot}/%{_datadir}/dbus-1/system.d/com.system76.CosmicGreeter.conf
install -Dm0644 debian/cosmic-greeter.sysusers %{buildroot}/%{_sysusersdir}/cosmic-greeter.conf
install -Dm0644 debian/cosmic-greeter.tmpfiles %{buildroot}/%{_tmpfilesdir}/cosmic-greeter.conf
install -Dm0644 cosmic-greeter.toml %{buildroot}/%{_sysconfdir}/greetd/cosmic-greeter.toml
install -Dm0644 debian/cosmic-greeter.service %{buildroot}/%{_unitdir}/cosmic-greeter.service
install -Dm0644 debian/cosmic-greeter-daemon.service %{buildroot}/%{_unitdir}/cosmic-greeter-daemon.service
install -Dm0644 debian/greetd.pam %{buildroot}/%{_sysconfdir}/pam.d/cosmic-greeter
%oreon_autofiles main
%if %{with check}
%check

export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif
%pre

%sysusers_create_compat debian/cosmic-greeter.sysusers
%post

%systemd_post cosmic-greeter.service
%systemd_post cosmic-greeter-daemon.service
%preun

%systemd_preun cosmic-greeter.service
%systemd_preun cosmic-greeter-daemon.service
%postun

%systemd_postun cosmic-greeter.service
%systemd_postun cosmic-greeter-daemon.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
