%global source1_hash 4f687c259511ae89ab890bfb778bd2744aefe7e2894c2e4c87dfa89fa75bbd97
%global source0_hash 3142a259ee93b78a9e3f05b371cc94014d121e015ecb6dd26e8b82947f650f33
Name: subscription-manager-cockpit
Version: 13
Release:        1%{?dist}
Summary:        Subscription Manager Cockpit UI
%if 0%{?suse_version}
Group: System Environment/Base
License: LGPLv2
%else
License: LGPL-2.1-or-later
%endif
URL: https://www.candlepinproject.org/
Source0:        https://github.com/cockpit-project/subscription-manager-cockpit/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1: https://github.com/cockpit-project/subscription-manager-cockpit/releases/download/%{version}/%{name}-node-%{version}.tar.xz
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Requires: subscription-manager
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: rhsm-icons
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
Subscription Manager Cockpit UI

%package -n rhsm-icons
Summary: Icons for Red Hat Subscription Management client tools
Conflicts: rhsm-gtk < 1.26.7
Conflicts: subscription-manager-cockpit < 1.26.7
%description -n rhsm-icons
This package contains the desktop icons for the graphical interfaces provided for management
of Red Hat subscriptions: subscription-manager-gui, subscription-manager-cockpit-plugin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%install
%make_install PREFIX=/usr
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose
%oreon_autofiles rhsm-icons usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*
desktop-file-validate %{buildroot}/%{_datadir}/applications/*
%files -f %{oreon_filedir}/main.list
%files -n rhsm-icons -f %{oreon_filedir}/rhsm-icons.list

%changelog

%autochangelog
