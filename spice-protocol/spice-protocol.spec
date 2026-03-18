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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14.5-3
- Prepare for Oreon 11 (RP1)
