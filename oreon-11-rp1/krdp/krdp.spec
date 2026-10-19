%global source1_hash f54caef5442495cfbb212c8c592a69d6b5844038e03fc6cef98f28c1167ad07f
%global source0_hash 483fb1d9ffd6954e7b12aa4321763a31726e5c0daac10e135cd13a503ced5330
%global stable_kf6 stable
%global qt6minver 6.6.0
%global kf6minver 6.2
ExcludeArch: %{ix86}
Name:           krdp
Summary:        Desktop sharing using RDP
Version:        6.7.5
Release:        1%{?dist}
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/plasma/krdp
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Requires:       /usr/bin/openssl
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-server < 6.0.90
Provides:       %{name}-server = %{version}-%{release}
Provides:       %{name}-server%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/winpr-makecert
BuildRequires:  cmake
BuildRequires:  cmake(FreeRDP)
BuildRequires:  cmake(FreeRDP-Server)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KPipeWire)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(WinPR)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
%{summary}.

%package libs
Summary:        Library for creating an RDP server
Requires:       /usr/bin/winpr-makecert
Conflicts:      %{name} < 6.0.90
Conflicts:      %{name}-server < 6.0.90
%description libs
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-html --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_user_post app-org.kde.krdpserver.service
%preun

%systemd_user_preun app-org.kde.krdpserver.service
%postun

%systemd_user_postun_with_restart app-org.kde.krdpserver.service
%systemd_user_postun_with_reload app-org.kde.krdpserver.service
%systemd_user_postun app-org.kde.krdpserver.service
%files -f %{oreon_filedir}/main.list
%files -n krdp-libs -f %{oreon_filedir}/krdp-libs.list
%files -n krdp-devel -f %{oreon_filedir}/krdp-devel.list

%changelog

* Tue Mar 17 2026 Steve Cossette <farchord@gmail.com> - 6.6.3-1
- 6.6.3

* Tue Mar 03 2026 Steve Cossette <farchord@gmail.com> - 6.6.2-1
- 6.6.2

* Tue Feb 24 2026 Steve Cossette <farchord@gmail.com> - 6.6.1-1
- 6.6.1

* Thu Feb 12 2026 Steve Cossette <farchord@gmail.com> - 6.6.0-1
- 6.6.0

* Tue Jan 27 2026 Steve Cossette <farchord@gmail.com> - 6.5.91-1
- 6.5.91

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Jan 13 2026 farchord@gmail.com - 6.5.90-1
- 6.5.90

* Tue Jan 13 2026 farchord@gmail.com - 6.5.5-1
- 6.5.5

* Tue Dec 09 2025 Steve Cossette <farchord@gmail.com> - 6.5.4-1
- 6.5.4

* Tue Nov 18 2025 Steve Cossette <farchord@gmail.com> - 6.5.3-1
- 6.5.3

* Tue Nov 04 2025 Steve Cossette <farchord@gmail.com> - 6.5.2-1
- 6.5.2

* Tue Oct 28 2025 Steve Cossette <farchord@gmail.com> - 6.5.1-1
- 6.5.1

* Fri Oct 17 2025 Steve Cossette <farchord@gmail.com> - 6.5.0-1
- 6.5.0

* Thu Oct 02 2025 Steve Cossette <farchord@gmail.com> - 6.4.91-1
- 6.4.91

* Tue Sep 30 2025 Jan Grulich <jgrulich@redhat.com> - 6.4.5-2
- Rebuild (qt6)

* Thu Sep 25 2025 Steve Cossette <farchord@gmail.com> - 6.4.90-1
- 6.4.90

* Tue Sep 16 2025 farchord@gmail.com - 6.4.5-1
- 6.4.5

* Sat Aug 16 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.4.4-2
- Drop i686 support (leaf package)

* Wed Aug 06 2025 Steve Cossette <farchord@gmail.com> - 6.4.4-1
- 6.4.4

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 15 2025 Steve Cossette <farchord@gmail.com> - 6.4.3-1
- 6.4.3

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 6.4.2-1
- 6.4.2

* Tue Jun 24 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.4.1-1
- 6.4.1

* Mon Jun 16 2025 Steve Cossette <farchord@gmail.com> - 6.4.0-1
- 6.4.0

* Sat May 31 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.91-2
- Add signature file

* Fri May 30 2025 Steve Cossette <farchord@gmail.com> - 6.3.91-1
- 6.3.91

* Thu May 15 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.90-1
- 6.3.90

* Tue May 06 2025 Steve Cossette <farchord@gmail.com> - 6.3.5-1
- 6.3.5

* Mon Apr 14 2025 Jan Grulich <jgrulich@redhat.com> - 6.3.4-2
- Rebuild (qt6)

* Wed Apr 02 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.4-1
- 6.3.4

* Tue Mar 25 2025 Jan Grulich <jgrulich@redhat.com> - 6.3.3-2
- Rebuild (qt6)

* Tue Mar 11 2025 Steve Cossette <farchord@gmail.com> - 6.3.3-1
- 6.3.3

* Tue Feb 25 2025 Steve Cossette <farchord@gmail.com> - 6.3.2-1
- 6.3.2

* Wed Feb 19 2025 Steve Cossette <farchord@gmail.com> - 6.3.1-2
- Fix systemd startup

* Tue Feb 18 2025 Steve Cossette <farchord@gmail.com> - 6.3.1-1
- 6.3.1

* Thu Feb 06 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.0-1
- 6.3.0

* Thu Jan 23 2025 Steve Cossette <farchord@gmail.com> - 6.2.91-1
- 6.2.91

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Steve Cossette <farchord@gmail.com> - 6.2.90-1
- Beta 6.2.90

* Tue Dec 31 2024 Steve Cossette <farchord@gmail.com> - 6.2.5-1
- 6.2.5

* Tue Nov 26 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.4-1
- 6.2.4

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 6.2.3-1
- 6.2.3

* Tue Oct 22 2024 Steve Cossette <farchord@gmail.com> - 6.2.2-1
- 6.2.2

* Tue Oct 15 2024 Steve Cossette <farchord@gmail.com> - 6.2.1-1
- 6.2.1

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 6.2.0-2
- Rebuild (qt6)

* Thu Oct 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Thu Sep 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.90-1
- 6.1.90

* Tue Sep 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.5-1
- 6.1.5

* Fri Aug 09 2024 Steve Cossette <farchord@gmail.com> - 6.1.4-1
- 6.1.4

* Wed Jul 24 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.3-3
- rebuilt

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.3-1
- 6.1.3

* Wed Jul 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.2-1
- 6.1.2

* Tue Jun 25 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.1-1
- 6.1.1

* Thu Jun 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Sat Jun 01 2024 Neal Gompa <ngompa@fedoraproject.org> - 6.0.90-2
- Fix required dependencies on winpr-makecert and openssl binaries

* Thu May 30 2024 Neal Gompa <ngompa@fedoraproject.org> - 6.0.90-1
- Rebase to 6.0.90
- Restructure package to more closely match krfb

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 5.27.80~git20240131.f36bf16-6
- Rebuild (qt6)

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 5.27.80~git20240131.f36bf16-5
- Rebuild (qt6)

* Tue Feb 13 2024 Alessandro Astone <ales.astone@gmail.com> - 5.27.80~git20240131.f36bf16-4
- krdp-server requires openssl binary

* Fri Feb 09 2024 Neal Gompa <ngompa@fedoraproject.org> - 5.27.80~git20240131.f36bf16-1
- Bump to new git snapshot
- Restrict to FreeRDP 2.x for now

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~git20231227.4931015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~git20231227.4931015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.27.80~git20231227.4931015-1
- Initial package
