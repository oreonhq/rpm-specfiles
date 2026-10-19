%global source0_hash c1c93d530b01ff2a7f06127a9a82b0273c4f47a23b0d55f506628069f8e8d5da
%bcond check 1
%global cargo_install_lib 0
Name:           bign-handheld-thumbnailer
Version:        1.2.0
Release:        3%{?dist}
Summary:        Thumbnailer for Nintendo handheld game consoles
SourceLicense:  GPL-2.0-or-later
License:        GPL-2.0-or-later AND MIT AND (0BSD OR Apache-2.0 OR MIT) AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense)
URL:            https://github.com/MateusRodCosta/bign-handheld-thumbnailer
Source0:        https://github.com/MateusRodCosta/bign-handheld-thumbnailer/archive/refs/tags/v%{version}.tar.gz
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  meson
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bign-handheld-thumbnailer-%{version}
%oreon_prep
%build

%meson -Dupdate_mime_database=false -Dgenerate_metainfo=true
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%meson_install
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
