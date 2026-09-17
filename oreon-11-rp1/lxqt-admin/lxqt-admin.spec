%global source0_hash 42269b012d8d7d32788c2fa8686fab518ce9c30a2eb4a93fcab719f7d9b28d8d

Name:           lxqt-admin
Summary:        LXQt system administration tool
Version:        2.3.0
Release:        2%{?dist}
License:        LGPL-2.1-only
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(lxqt)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(polkit-qt6-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  perl

Requires:       polkit

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

%autosetup -p1

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

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/polkit-1/actions/*.policy

%files l10n -f lxqt-admin-user.lang -f lxqt-admin-time.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-admin-user
%dir %{_datadir}/lxqt/translations/lxqt-admin-time
%{_datadir}/lxqt/translations/lxqt-admin-user/lxqt-admin-user_arn.qm
%{_datadir}/lxqt/translations/lxqt-admin-user/lxqt-admin-user_ast.qm
%{_datadir}/lxqt/translations/lxqt-admin-time/lxqt-admin-time_arn.qm
%{_datadir}/lxqt/translations/lxqt-admin-time/lxqt-admin-time_ast.qm

%changelog
%autochangelog
