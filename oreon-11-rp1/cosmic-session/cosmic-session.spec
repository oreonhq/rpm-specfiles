%global source0_hash e6d093938ab59baafdccac576cb0bc1a1966c825a5fedf9cb498061d8099ed57
ExcludeArch: %{ix86}
%bcond check 0
%global crate cosmic-session
%global commit 02a4c58c3db83d4ea40834ac3a99f04cd331b0b3
%global commitdatestring 2026-03-18 13:53:58 -0400
%global cosmic_minver 1.0.9
Name:           cosmic-session
Version: 1.9.0
Release:        1%{?dist}
Summary:        Session manager for the COSMIC desktop environment
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-3-Clause AND GPL-3.0-only AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Zlib
URL:            https://github.com/pop-os/cosmic-session
Source0:        https://github.com/pop-os/cosmic-session/archive/epoch-%{version}/cosmic-session-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Source3:        cosmic-dconf-profile.txt
Requires:       cosmic-app-library >= %{cosmic_minver}
Requires:       cosmic-applets >= %{cosmic_minver}
Requires:       cosmic-bg >= %{cosmic_minver}
Requires:       cosmic-comp >= %{cosmic_minver}
Requires:       cosmic-files >= %{cosmic_minver}
Requires:       cosmic-greeter >= %{cosmic_minver}
Requires:       cosmic-icons >= %{cosmic_minver}
Requires:       cosmic-idle >= %{cosmic_minver}
Requires:       cosmic-initial-setup >= %{cosmic_minver}
Requires:       cosmic-launcher >= %{cosmic_minver}
Requires:       cosmic-notifications >= %{cosmic_minver}
Requires:       cosmic-osd >= %{cosmic_minver}
Requires:       cosmic-panel >= %{cosmic_minver}
Requires:       cosmic-randr >= %{cosmic_minver}
Requires:       cosmic-screenshot >= %{cosmic_minver}
Requires:       cosmic-settings >= %{cosmic_minver}
Requires:       cosmic-settings-daemon >= %{cosmic_minver}
Requires:       cosmic-term >= %{cosmic_minver}
Requires:       cosmic-workspaces >= %{cosmic_minver}
Requires:       xdg-desktop-portal-cosmic >= %{cosmic_minver}
Requires:       open-sans-fonts
Requires:       font(notosansmono)
Requires:       xdg-user-dirs
Recommends:     cosmic-wallpapers >= %{cosmic_minver}
Requires:       system-cosmic-config
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  just
BuildRequires:  lld
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-epoch-%{version} -p1 -a1
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
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt
sed 's/^\([^+]*\)+.*+\([^+]*\)$/\1+\2/' -i cargo-vendor.txt
%install
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} install
install -Dm0644 %{SOURCE3} %{buildroot}/%{_datadir}/dconf/profile/cosmic
%oreon_autofiles main
%if %{with check}
%check

export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
