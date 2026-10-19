%global source0_hash d41afcbe6cb558f5c8d3d44b1cab19c345817fc3665c039f3b67b11370626f96
%bcond check 1
%global crate startup-disk
%global app_id org.startup_disk.StartupDisk
Name:           rust-startup-disk
Version:        0.1.7
Release:        1%{?dist}
Summary:        Interface to choose the startup volume on Apple Silicon systems
License:        MIT
URL:            https://crates.io/crates/startup-disk
Source0:        https://static.crates.io/crates/startup-disk/startup-disk-%{version}.crate
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Interface to choose the startup volume on Apple Silicon systems
License:        (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT) AND Zlib
Requires:       hicolor-icon-theme
Requires:       polkit
Requires:       sudo
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
make install-data DESTDIR="%{buildroot}" DATADIR="%{_datadir}"
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
make check-data
%endif
%files -f %{oreon_filedir}/main.list
%files -n startup-disk -f %{oreon_filedir}/startup-disk.list

%changelog

%autochangelog
