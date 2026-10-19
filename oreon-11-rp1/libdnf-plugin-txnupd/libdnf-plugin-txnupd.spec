%global source0_hash 342006cf822830d9b03ad346c7753ba4f5f5d6ffd980435159f54d7d121314d9
%global libdnf5_minver 5.2.17.0
%global tukit_minver 3.6.2
Name:           libdnf-plugin-txnupd
Version:        0.3.0
Release:        1%{?dist}
Summary:        libdnf5 plugin to implement transactional updates
License:        LGPL-2.1-or-later
URL:            https://gitlab.com/VelocityLimitless/Projects/libdnf-plugin-txnupd
Source0:        https://gitlab.com/VelocityLimitless/Projects/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch1001:      libdnf-plugin-txnupd-Downgrade-dnf5-dependency.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(libdnf5)
BuildRequires:  pkgconfig(tukit)
# /oreon:deps
%description
This package contains the plugin to implement transactional updates
as a libdnf5 plugin. This plugin hooks into libdnf5 for DNF and
PackageKit to enable this functionality in normal use.

%package -n libdnf5-plugin-txnupd
Summary:        libdnf5 plugin to implement transactional updates
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libdnf5%{?_isa} >= %{libdnf5_minver}
Requires:       libtukit%{?_isa} >= %{tukit_minver}
Requires:       dracut-transactional-update
Requires:       dnf-data
Recommends:     (dnf5 or PackageKit)
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
mkdir -p %{buildroot}%{_sysconfdir}/dnf/protected.d
echo "libdnf5-plugin-txnupd" > %{buildroot}%{_sysconfdir}/dnf/protected.d/txnupd.conf
%oreon_autofiles libdnf5-plugin-txnupd usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libdnf5-plugin-txnupd -f %{oreon_filedir}/libdnf5-plugin-txnupd.list

%changelog

%autochangelog
