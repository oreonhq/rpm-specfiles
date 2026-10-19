%global source0_hash c33eba486fb14504a37402c208e996078b355d3fd5c3515226f29ce1896ba9ab
Name:          lxqt-policykit
Summary:        PolicyKit agent for LXQt desktop suite
Version:       2.4.0
Release:        1%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Provides: PolicyKit-authentication-agent = %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(polkit-agent-1)
# /oreon:deps
%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-policykit
Requires:       lxqt-policykit
%description l10n
This package provides translations for the lxqt-policykit package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's|=lxqt-policykit-agent|=/usr/libexec/lxqt-policykit-agent|g' autostart/lxqt-policykit-agent.desktop.in

%build

%cmake \
    -DPOLKIT_AGENT_BINARY_DIR=%{_libexecdir}
%cmake_build
%install
%cmake_install
install -d %{buildroot}/%{_sysconfdir}/xdg/autostart
%find_lang lxqt-policykit-agent --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-policykit-l10n -f %{oreon_filedir}/lxqt-policykit-l10n.list

%changelog

%autochangelog
