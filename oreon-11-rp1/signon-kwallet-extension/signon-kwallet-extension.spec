%undefine __cmake_in_source_build


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    signon-kwallet-extension
Version: 25.12.3
Release:	2%{?dist}
Summary: KWallet integration for Sign-on framework

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://cgit.kde.org/%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kwallet-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  pkgconfig(signon-plugins)

Supplements:    (kf6-kwallet and signon)

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
    -DQT_MAJOR_VERSION=6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%files
%license COPYING
%{_libdir}/signon/extensions/libkeyring-kwallet.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
