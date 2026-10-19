%global source0_hash none
ExcludeArch: %{ix86}
%bcond check 0
%global crate cosmic-initial-setup
%global commit 9973b0330df4759263b7db350c373f326989a13b
%global commitdatestring 2026-03-23 15:48:15 +0100
%global cosmic_minver 1.0.9
Name:           cosmic-initial-setup
Version: 1.9.0
Release:        1%{?dist}
Summary:        Initial setup application for the COSMIC desktop environment
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSD-3-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR CC0-1.0 OR MIT-0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/pop-os/cosmic-initial-setup
Source0:        cosmic-initial-setup-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Recommends:     PackageKit
Recommends:     flatpak
Requires:       flatpak-libs
Requires:       polkit
Requires:       hicolor-icon-theme
Requires:       cosmic-icon-theme >= %{cosmic_minver}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  flatpak-devel
BuildRequires:  just
BuildRequires:  libinput-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  openssl-devel
BuildRequires:  rustc
BuildRequires:  systemd-devel
# /oreon:deps
%description

%prep
%autosetup -n %{crate} -p1 -a1
if [ -f .cargo/config.toml ]; then
cat %{SOURCE2} >> .cargo/config.toml
echo "Appended %{SOURCE2} to .cargo/config.toml"
else
cat %{SOURCE2} >> .cargo/config
echo "Appended %{SOURCE2} to .cargo/config"
fi
%oreon_vendor_cargo
%build

export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
export DISABLE_IF_EXISTS=/run/rootfsbase
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt
%install
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} prefix=%{_prefix} install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicInitialSetup.desktop
%if %{with check}
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
