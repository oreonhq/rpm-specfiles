%global source0_hash f0f3a2362861fe8976d7d45436aaa0a10de975522b6e8a53d77058a74ffc81e8
ExcludeArch: %{ix86}
%bcond check 0
%global commit 3e84968dacb6a50a82ef5e35c0ac373c38172681
%global commitdatestring 2026-04-07 16:14:52 +0200
%global cosmic_minver 1.0.9
Name:           cosmic-comp
Version: 1.9.0
Release:        1%{?dist}
Summary:        Compositor for the COSMIC Desktop Environment
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR BSD-3-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/pop-os/cosmic-comp
Source0:        https://github.com/pop-os/cosmic-comp/archive/epoch-%{version}/cosmic-comp-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Requires:       libseat%{?_isa}
Requires:       libwayland-server%{?_isa}
Requires:       xorg-x11-server-Xwayland
Requires:       cosmic-icon-theme >= %{cosmic_minver}
Recommends:     cosmic-session
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  libdisplay-info-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libinput-devel
BuildRequires:  libseat-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  make
BuildRequires:  mesa-libgbm-devel
BuildRequires:  pixman-devel
BuildRequires:  rustc
BuildRequires:  wayland-devel
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n cosmic-comp-epoch-%{version} -p1 -a1
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
export GIT_HASH="%{commit}"
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt
sed 's/^\([^+]*\)+.*+\([^+]*\)$/\1+\2/' -i cargo-vendor.txt
%install
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
export GIT_HASH="%{commit}"
make install DESTDIR=%{buildroot} prefix=%{_prefix}
%oreon_autofiles main
%if %{with check}
%check

export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
export GIT_HASH="%{commit}"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
