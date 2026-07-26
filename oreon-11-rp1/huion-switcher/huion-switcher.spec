%global source0_hash a595efecc78ee227bb1ac8ebf48bccea5c2b57a2553e88de3428dbbc3d438c04

%bcond check 0
%global udevdir %(pkg-config --variable=udevdir udev)

# prevent library files from being installed
%global cargo_install_lib 0

Name:           huion-switcher
Version:        0.5.0
Release:        %autorelease
Summary:        Utility to switch Huion tablets into tablet mode

SourceLicense:  GPL-2.0-only
License:        GPL-2.0-only AND MIT AND (MIT OR Apache-2.0)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/whot/huion-switcher
Source:         https://github.com/whot/huion-switcher/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  cargo
BuildRequires:  pkgconfig(udev) pkgconfig(libusb)
Requires:       udev

%global _description %{expand:
Utility to switch Huion tablets into tablet mode.}

%description %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

install -D -m 644 -t %{buildroot}/%{udevdir}/rules.d/ 80-huion-switcher.rules
install -D -m 644  huion-switcher.man %{buildroot}/%{_mandir}/man1/huion-switcher.1

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/huion-switcher
%{_mandir}/man1/huion-switcher.1*
%{udevdir}/rules.d/80-huion-switcher.rules

%changelog
%autochangelog
