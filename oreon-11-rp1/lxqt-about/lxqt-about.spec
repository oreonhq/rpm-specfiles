%global source0_hash fc5dbf055ecf7732191466181d8689f7006032be8eb71fcfffdc75a63bd09702
Name:          lxqt-about
Summary:        About application for LXQt desktop suite
Version:       2.4.0
Release:        1%{?dist}
License:       LicenseRef-Callaway-LGPLv2+
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt)
# /oreon:deps
%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-about
Requires:       lxqt-about
%description l10n
This package provides translations for the lxqt-about package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    --remove-category=Help --add-category=X-Help \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-about-l10n -f %{oreon_filedir}/lxqt-about-l10n.list

%changelog

%autochangelog
