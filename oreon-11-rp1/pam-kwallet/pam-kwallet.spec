
%global  base_name kwallet-pam


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    pam-kwallet
Summary: PAM module for KWallet
Version: 6.6.2
Release:	2%{?dist}
License: LGPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{base_name}.git

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

## upstream patches

## upstreamable patches

Provides: %{base_name} = %{version}-%{release}

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: systemd-rpm-macros
BuildRequires: libgcrypt-devel >= 1.5.0
BuildRequires: pam-devel
BuildRequires: cmake(KF6Wallet)
BuildRequires: socat

# https://bugzilla.redhat.com/show_bug.cgi?id=1155873
Requires: socat
# pam module makes little sense without the actually kwallet service
Requires: kf6-kwallet

%description
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%files
%{_sysconfdir}/xdg/autostart/pam_kwallet_init.desktop
%{_userunitdir}/plasma-kwallet-pam.service
%{_libexecdir}/pam_kwallet_init
%{_libdir}/security/pam_kwallet5.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
