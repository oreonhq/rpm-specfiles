%global source0_hash 0adb2195139fdc1b5596480e2ed62c87b48d10043147da986053ec41eafb5848
Name:           lxqt-admin
Summary:        LXQt system administration tool
Version:        2.4.0
Release:        1%{?dist}
License:        LGPL-2.1-only
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       polkit
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(lxqt)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(polkit-qt6-1)
# /oreon:deps
%description
This package provides tools to adjust settings of the operating system
LXQt is running on. Both can be launched from GUI "Configuration Center".

GUI "Time and date configuration", binary lxqt-admin-time, can be used
to adjust the system time of the operating system as well as the timezone.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-admin
Requires:       lxqt-admin
%description l10n
This package provides translations for the lxqt-admin package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
for admfile in user time; do
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    --remove-category=Help --add-category=X-Help \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt \
    %{buildroot}%{_datadir}/applications/%{name}-${admfile}.desktop
done
%find_lang lxqt-admin-time --with-qt
%find_lang lxqt-admin-user --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-admin-l10n -f %{oreon_filedir}/lxqt-admin-l10n.list

%changelog

%autochangelog
