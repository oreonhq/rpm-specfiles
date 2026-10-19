%global source0_hash c30cb40b8177112c821753a95134ba82e64dfd8230f5c371a1c89a4b0d066309
ExcludeArch: %{ix86}
%bcond check 0
%global crate cosmic-files
%global build_rustflags %{?build_rustflags} --cfg=io_uring_skip_arch_check
%global commit d38d55525b5610e555e11a9c8ebc3bc8507d5480
%global commitdatestring 2026-04-06 18:08:44 -0600
%global cosmic_minver 1.0.9
Name:           cosmic-files
Version: 1.9.0
Release:        1%{?dist}
Summary:        Libcosmic file manager
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSD-3-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR CC0-1.0 OR MIT-0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/pop-os/cosmic-files
Source0:        https://github.com/pop-os/cosmic-files/archive/epoch-%{version}/cosmic-files-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Requires:       gvfs
Requires:       gvfs-fuse
Recommends:     gvfs-nfs
Recommends:     gvfs-smb
Requires:       xdg-utils
Requires:       cosmic-icon-theme >= %{cosmic_minver}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  just
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  rustc
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
%cargo_build -- --package cosmic-files-applet
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt
sed 's/^\([^+]*\)+.*+\([^+]*\)$/\1+\2/' -i cargo-vendor.txt
%install
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} prefix=%{_prefix} install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicFiles.desktop
%if %{with check}
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
( %cargo_test ) || :
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
