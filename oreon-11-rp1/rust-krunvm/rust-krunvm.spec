%global source0_hash 5e522404f87f4cd04c8cd0eed0f192d06dc78eae46406a9f4822b531d0abfbdd
%bcond check 0
%global crate krunvm
Name:           rust-krunvm
Version:        0.1.6
Release:        1%{?dist}
Summary:        Create microVMs from OCI images
License:        Apache-2.0
URL:            https://crates.io/crates/krunvm
Source0:        https://static.crates.io/crates/krunvm/krunvm-%{version}.crate
Patch:          krunvm-fix-metadata.diff
ExclusiveArch:  x86_64 aarch64
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Create microVMs from OCI images
License:        Apache-2.0 AND MIT AND (MIT OR Apache-2.0) AND (MIT OR X11 OR Apache-2.0)
Requires:       buildah
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
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  target/release/build/%{crate}-*/out/krunvm.1
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  target/release/build/%{crate}-*/out/krunvm-changevm.1
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  target/release/build/%{crate}-*/out/krunvm-config.1
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  target/release/build/%{crate}-*/out/krunvm-create.1
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  target/release/build/%{crate}-*/out/krunvm-delete.1
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  target/release/build/%{crate}-*/out/krunvm-list.1
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  target/release/build/%{crate}-*/out/krunvm-start.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n krunvm -f %{oreon_filedir}/krunvm.list

%changelog

%autochangelog
