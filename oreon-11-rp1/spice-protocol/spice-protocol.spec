%global source0_hash baf58449f6e89d19f475899ad5fb9196fdc46c03cc53233f4e39cf2978f9cff7
Name:           spice-protocol
Version:        0.14.5
Release:        1%{?dist}
Summary:        Spice protocol header files
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://www.spice-space.org/
Source0:        https://www.spice-space.org/download/releases/%{name}-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
# /oreon:deps
%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir spice-protocol-0.14.5
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14.5-3
- Import
