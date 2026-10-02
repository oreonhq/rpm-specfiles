%global source0_hash deb5698b5682bc15d22446db9cf8641857d0bd7785e145b7b6e9247a68d35fd2

%global stable_kf6 stable


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    ksshaskpass
Version:        6.7.5
Release: %autorelease
Summary: A ssh-add helper that uses kwallet and kpassworddialog

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://cgit.kde.org/%{name}.git

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  cmake(Qt6Keychain)

%description
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang ksshaskpass

# Setup environment variables
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/
cat >    %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/ksshaskpass.sh << EOF
SSH_ASKPASS=%{_kf6_bindir}/ksshaskpass
export SSH_ASKPASS
EOF


%files -f ksshaskpass.lang
%doc ChangeLog
%license LICENSES/*
%{_kf6_bindir}/ksshaskpass
%{_kf6_datadir}/applications/org.kde.ksshaskpass.desktop
%config(noreplace) %{_sysconfdir}/xdg/plasma-workspace/env/ksshaskpass.sh
%{_mandir}/man1/ksshaskpass.1*


%changelog
%autochangelog
