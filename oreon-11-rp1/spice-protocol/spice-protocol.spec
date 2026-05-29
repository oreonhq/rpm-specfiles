%global source0_hash baf58449f6e89d19f475899ad5fb9196fdc46c03cc53233f4e39cf2978f9cff7

Name:           spice-protocol
Version:        0.14.5
Release:        3%{?dist}
Summary:        Spice protocol header files
# Main headers are BSD, controller / foreign menu are LGPL
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://www.spice-space.org/
Source0:        https://www.spice-space.org/download/releases/%{name}-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  gcc
BuildRequires:  meson

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install


%files
%doc COPYING CHANGELOG.md
%{_includedir}/spice-1
%{_datadir}/pkgconfig/spice-protocol.pc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14.5-3
- Import
