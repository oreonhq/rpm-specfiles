%global source0_hash d7ff3c814fbee20128c3f55896deb658c877f33f769ccfbd271e8dd68e3bfbe9
Name:           sddm-conf
Version:	0.3.0
Release:        1%{?dist}
License:	MIT
URL:		https://github.com/qtilities/%{name}
Source0:        https://github.com/qtilities/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Summary:        Qt-based configuration editor for SDDM
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qtilitools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  perl
# /oreon:deps
%description
Configuration editor for SDDM similar to sddm-config-editor, but written in C++.

%package l10n
BuildArch:      noarch
Summary:        Translations for sddm-conf
Requires:       sddm-conf
%description l10n
This package provides translations for the sddm-conf package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DPROJECT_QT_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/sddm_conf.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml ||:
%files -f %{oreon_filedir}/main.list
%files -n sddm-conf-l10n -f %{oreon_filedir}/sddm-conf-l10n.list

%changelog

%autochangelog
