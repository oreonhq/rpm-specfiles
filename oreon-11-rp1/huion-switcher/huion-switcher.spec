%global source0_hash a595efecc78ee227bb1ac8ebf48bccea5c2b57a2553e88de3428dbbc3d438c04
%bcond check 0
%global udevdir %(pkg-config --variable=udevdir udev)
%global cargo_install_lib 0
Name:           huion-switcher
Version:        0.5.0
Release:        1%{?dist}
Summary:        Utility to switch Huion tablets into tablet mode
SourceLicense:  GPL-2.0-only
License:        GPL-2.0-only AND MIT AND (MIT OR Apache-2.0)
URL:            https://github.com/whot/huion-switcher
Source0:        https://github.com/whot/huion-switcher/archive/refs/tags/%{version}.tar.gz
Requires:       udev
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(udev)
BuildRequires:  rustc
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -D -m 644 -t %{buildroot}/%{udevdir}/rules.d/ 80-huion-switcher.rules
install -D -m 644  huion-switcher.man %{buildroot}/%{_mandir}/man1/huion-switcher.1
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
