%global source0_hash b01be44c101b83adc01a8935f444e2b2f94c94d9ae6131e28483f38971ec12d3

Name:          lxqt-policykit
Summary:       PolicyKit agent for LXQt desktop suite
Version:       2.3.0
Release:       2%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(PolkitQt6-1)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: pkgconfig(lxqt)
BuildRequires: desktop-file-utils
BuildRequires: perl

Provides: PolicyKit-authentication-agent = %{version}

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

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_libexecdir}/lxqt-policykit-agent
%{_sysconfdir}/xdg/autostart/lxqt-policykit-agent.desktop
%{_datadir}/lxqt/translations/%{name}-agent
%{_mandir}/man1/lxqt-policykit*

%files l10n -f lxqt-policykit-agent.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-policykit-agent

%changelog
%autochangelog
