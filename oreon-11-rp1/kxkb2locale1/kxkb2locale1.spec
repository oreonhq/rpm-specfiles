%global source0_hash 21f1e7b123c905b5f5435569bb089e57519e50080b220df892880bb22dbda9ac

Name:           kxkb2locale1
Version:        0.1
Release:        3%{?dist}
Summary:        Watches the KDE keyboard config and applies it to org.freedesktop.locale1
License:        MIT
URL:            https://invent.kde.org/aleasto/%{name}
Source:         https://invent.kde.org/aleasto/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6Config)

Supplements:    (kwin-wayland%{?_isa} and livesys-scripts)

%description
KWin may be configured to read the keyboard configuration from
org.freedesktop.locale1 rather than from Kxkb.
The Keyboard KCM and Plasma Applet however are only configured to use Kxkb.
When kxkb2locale1 is running, the user can use the KCM and Plasma Applet to
configure the keyboard as usual and the effects will be reflected immediately.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kxkb2locale1.desktop
desktop-file-validate %{buildroot}/%{_sysconfdir}/xdg/autostart/kxkb2locale1.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/kxkb2locale1
%{_sysconfdir}/xdg/autostart/kxkb2locale1.desktop
%{_datadir}/applications/kxkb2locale1.desktop

%changelog
%autochangelog
