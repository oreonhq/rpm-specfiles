%global source0_hash c00723c16f932fe27c5763e95271605340998757622d14492f1da154c8b196ad
Name:           ibus-engine-gui-ci
Version:        1.0.0.20220118
Release:        1%{?dist}
Summary:        GUI CI for IBus engines
License:        LGPL-2.0-or-later
URL:            https://github.com/fujiwarat/ibus-engine-gui-ci
Source0:        https://github.com/fujiwarat/ibus-engine-gui-ci/releases/download/%{version}/%{name}-%{version}.tar.gz
Requires:       ibus
Recommends:     ibus-desktop-testing
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  glib2
BuildRequires:  gtk3-devel
BuildRequires:  ibus-devel
BuildRequires:  json-glib-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
GUI CI can run with ibus-desktop-testing-runner and engines get
focus events with the window manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
