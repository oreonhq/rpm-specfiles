%global source0_hash 9d045520a3fb591b67129dc0836726ee3f7922f1e18503495b9423dc62f1c73e
%bcond check 0
%global crate external-editor-revived
%global thunderbird_app_id \{3550f703-e582-4d05-9a08-453d09bdfdc6\}
%global extensions_dir %{_libdir}/mozilla/extensions/%{thunderbird_app_id}
Name:           external-editor-revived
Version:        1.2.0
Release:        1%{?dist}
Summary:        Thunderbird extension that allows editing emails in external editors such as Vim
License:        Apache-2.0 AND MIT AND GPL-3.0-or-later
URL:            https://github.com/Frederick888/external-editor-revived
Source0:        https://github.com/Frederick888/external-editor-revived/archive/refs/tags/v%{version}.tar.gz
ExclusiveArch:  %{rust_arches}
Requires: mozilla-filesystem
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  coreutils
BuildRequires:  rustc
BuildRequires:  sed
BuildRequires:  zip
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license} > LICENSE.dependencies
%cargo_license_summary
pushd $RPM_BUILD_DIR/%{crate}-%{version}/extension
zip -r -FS $RPM_BUILD_DIR/external-editor-revived@tsundere.moe.xpi *
popd
%install
%cargo_install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/mozilla/native-messaging-hosts
$RPM_BUILD_ROOT%{_bindir}/external-editor-revived 2>/dev/null | \
    sed 's|^  "path":.*$|  "path": "%{_bindir}/external-editor-revived",|' > \
    $RPM_BUILD_ROOT%{_libdir}/mozilla/native-messaging-hosts/external_editor_revived.json
mkdir -p $RPM_BUILD_ROOT%{extensions_dir}
cp $RPM_BUILD_DIR/external-editor-revived@tsundere.moe.xpi $RPM_BUILD_ROOT%{extensions_dir}/
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
