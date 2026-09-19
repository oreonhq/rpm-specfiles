%global source0_hash 3142a259ee93b78a9e3f05b371cc94014d121e015ecb6dd26e8b82947f650f33

Name: subscription-manager-cockpit
Version: 13
Release: 1%{?dist}
Summary: Subscription Manager Cockpit UI
%if 0%{?suse_version}
Group: System Environment/Base
License: LGPLv2
%else
License: LGPL-2.1-or-later
%endif
URL: https://www.candlepinproject.org/

Source0: https://github.com/cockpit-project/subscription-manager-cockpit/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1: https://github.com/cockpit-project/subscription-manager-cockpit/releases/download/%{version}/%{name}-node-%{version}.tar.xz
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
BuildRequires: make
BuildRequires: libappstream-glib
BuildRequires: gettext
BuildRequires: desktop-file-utils
%if 0%{?rhel} && 0%{?rhel} <= 8
BuildRequires: libappstream-glib-devel
%endif

Requires: subscription-manager
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: rhsm-icons
%if %{defined rhel} && %{undefined centos}
Suggests: insights-client
%endif

%description
Subscription Manager Cockpit UI

%package -n rhsm-icons
Summary: Icons for Red Hat Subscription Management client tools

# As these two packages previously contained the icons now contained in
# rhsm-icons package, we need to specify the logical complement to a
# "Requires", which is "Conflicts". With any luck the underlying
# depsolver will cause the removal of this package if the request
# is to downgrade either of the following to a version below these
# requirements.
Conflicts: rhsm-gtk < 1.26.7
Conflicts: subscription-manager-cockpit < 1.26.7

%description -n rhsm-icons
This package contains the desktop icons for the graphical interfaces provided for management
of Red Hat subscriptions: subscription-manager-gui, subscription-manager-cockpit-plugin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -a 1

%build
# Nothing to build, build is done via the Makefile

%install
%make_install PREFIX=/usr

# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*
desktop-file-validate %{buildroot}/%{_datadir}/applications/*

# this can't be meaningfully tested during package build

%files
%license LICENSE
%dir %{_datadir}/cockpit/subscription-manager
%{_datadir}/applications/*
%{_datadir}/cockpit/subscription-manager/*
%{_datadir}/metainfo/*

%files -n rhsm-icons
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/symbolic/apps/*.svg

%changelog
%autochangelog
