%global source0_hash 47d8bd5d862e7e9cf02674bfe8e35d0ccbfc680072ede501d287d6cac96e57e7

# Minimum compatible version
%global libdnf5_minver 5.2.17.0
%global tukit_minver 3.6.2

Name:           libdnf-plugin-txnupd
Version:        0.2.0
Release:        1%{?dist}
Summary:        libdnf5 plugin to implement transactional updates

License:        LGPL-2.1-or-later
URL:            https://gitlab.com/VelocityLimitless/Projects/libdnf-plugin-txnupd
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

# Temporary until all supported releases have DNF 5.4+
Patch1001:      libdnf-plugin-txnupd-Downgrade-dnf5-dependency.patch

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdnf5) >= %{libdnf5_minver}
BuildRequires:  pkgconfig(tukit) >= %{tukit_minver}

%description
This package contains the plugin to implement transactional updates
as a libdnf5 plugin. This plugin hooks into libdnf5 for DNF and
PackageKit to enable this functionality in normal use.

%package -n libdnf5-plugin-txnupd
Summary:        libdnf5 plugin to implement transactional updates

# Replace the old plugin
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}%{?_isa} = %{version}-%{release}

# We need a minimum version of these libraries beyond soname for working APIs
Requires:       libdnf5%{?_isa} >= %{libdnf5_minver}
Requires:       libtukit%{?_isa} >= %{tukit_minver}

# We need the transactional update dracut module
Requires:       dracut-transactional-update

# To ensure directories for configuration files are in place
Requires:       dnf-data

# This is intended to be used alongside DNF5 and PackageKit
Recommends:     (dnf5 or PackageKit)

# Do not permit normal DNF snapper plugin on the same system
Conflicts:      dnf5-actions-snapper

%description -n libdnf5-plugin-txnupd
This package contains the plugin to implement transactional updates
as a libdnf5 plugin. This plugin hooks into libdnf5 for DNF5 and
PackageKit to enable this functionality in normal use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
%meson

%build
%meson_build

%install
%meson_install

# Add configuration to mark this package as protected by libdnf
mkdir -p %{buildroot}%{_sysconfdir}/dnf/protected.d
echo "libdnf5-plugin-txnupd" > %{buildroot}%{_sysconfdir}/dnf/protected.d/txnupd.conf

%files -n libdnf5-plugin-txnupd
%license LICENSE
%doc README.md
%{_libdir}/libdnf5/plugins/txnupd.so
%{_sysconfdir}/dnf/protected.d/txnupd.conf
%{_sysconfdir}/dnf/libdnf5-plugins/txnupd.conf

%changelog
%autochangelog
