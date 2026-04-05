
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:          kde-inotify-survey
Version:       25.12.3
Release:	2%{?dist}
Summary:       Monitors inotify limits and lets the user know when exceeded

# Complete license breakdown can be found in the "LICENSE-BREAKDOWN" file
License:       BSD-3-Clause and CC0-1.0 and FSFAP and GPL-2.0-only and GPL-3.0-only
URL:           https://invent.kde.org/system/%{name}

Source:        https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# Updates the dbus service config to use the right policies to satisfy a rpmlint error
# Merge Request: https://invent.kde.org/frameworks/kauth/-/merge_requests/44
Source1:       org.kde.kded.inotify.conf

Requires:      kf6-kded
Requires:      dbus-common
Requires:      polkit
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: qt6-qtbase-devel
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Auth)

%description
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --with-kde --with-man --all-name
rm %{buildroot}%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf
install -m644 -p -D %{SOURCE1} %{buildroot}%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf

%files -f %{name}.lang
%license LICENSES/* screenshot.png.license
%doc README.md screenshot.png
%{_bindir}/kde-inotify-survey
%{_kf6_plugindir}/kded/inotify.so
%{_kf6_libexecdir}/kauth/kded-inotify-helper
%{_datadir}/dbus-1/system-services/org.kde.kded.inotify.service
%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf
%{_datadir}/knotifications6/org.kde.kded.inotify.notifyrc
%{_datadir}/metainfo/org.kde.inotify-survey.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.inotify.policy

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
