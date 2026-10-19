%global source1_hash 92a094a93ab25dd9fa76d7ad47a7948747885e486fe261506bbc3e8c51c3a985
%global source0_hash deb5698b5682bc15d22446db9cf8641857d0bd7785e145b7b6e9247a68d35fd2
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    ksshaskpass
Version:        6.7.5
Release:        1%{?dist}
Summary:        A ssh-add helper that uses kwallet and kpassworddialog
License: GPL-2.0-only
URL:     https://cgit.kde.org/%{name}.git
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
# oreon:deps
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt6Core)
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang ksshaskpass
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/
cat >    %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/ksshaskpass.sh << EOF
SSH_ASKPASS=%{_kf6_bindir}/ksshaskpass
export SSH_ASKPASS
EOF
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
