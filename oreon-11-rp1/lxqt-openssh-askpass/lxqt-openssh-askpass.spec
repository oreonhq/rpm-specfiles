%global source0_hash a5a03c3155ac3803e48f3d7966cf1db710ef90a7cabd4d66854db941565e4d49
Name:          lxqt-openssh-askpass
Summary:        Askpass openssh transition dialog for LXQt desktop suite
Version:       2.4.0
Release:        1%{?dist}
License:       LicenseRef-Callaway-LGPLv2+
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       lxqt-openssh-askpass.sh
Source2:       lxqt-openssh-askpass.csh
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description
%{summary}.

%package l10n
Summary:        Translations for lxqt-openssh-askpass
Requires:       lxqt-openssh-askpass
%description l10n
This package provides translations for the lxqt-openssh-askpass package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_libexecdir}/openssh/
mv %{buildroot}/%{_bindir}/lxqt-openssh-askpass %{buildroot}%{_libexecdir}/openssh/
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -p -m0644 %SOURCE1 %SOURCE2 %{buildroot}%{_sysconfdir}/profile.d/
%find_lang lxqt-openssh-askpass --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-openssh-askpass-l10n -f %{oreon_filedir}/lxqt-openssh-askpass-l10n.list

%changelog

%autochangelog
