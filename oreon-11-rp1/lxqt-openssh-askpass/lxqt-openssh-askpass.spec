%global source0_hash c17f7370b99569ec0867ee3c9a104c687721501e8feb09717fe4d7188bfdbf54

Name:          lxqt-openssh-askpass
Summary:       Askpass openssh transition dialog for LXQt desktop suite
Version:       2.3.0
Release:       2%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       lxqt-openssh-askpass.sh
Source2:       lxqt-openssh-askpass.csh
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: perl

%description
%{summary}.

%package l10n
Summary:        Translations for lxqt-openssh-askpass
Requires:       lxqt-openssh-askpass
%description l10n
This package provides translations for the lxqt-openssh-askpass package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

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

%files
%{_libexecdir}/openssh/lxqt-openssh-askpass
%config(noreplace) %{_sysconfdir}/profile.d/*
%{_datadir}/lxqt/translations/%{name}
%{_mandir}/man1/%{name}*

%files l10n -f lxqt-openssh-askpass.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-openssh-askpass

%changelog
%autochangelog
