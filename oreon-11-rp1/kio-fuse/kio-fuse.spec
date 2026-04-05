%global         min_qt_version 5.12
%global         min_kf_version 5.66

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:           kio-fuse
Version:        5.1.1
Release:	4%{?dist}
Summary:        KIO FUSE

License:        GPL-3.0-or-later
URL:            https://invent.kde.org/system/kio-fuse
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        gpgkey-21EC3FD75D26B39E820BE6FBD27C2C1AF21D8BAD.gpg

## upstream fixes

BuildRequires:  cmake
BuildRequires:  gnupg2
BuildRequires:  gcc-c++
BuildRequires:  systemd
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules  >= %{min_kf_version}

BuildRequires:  pkgconfig(fuse3)

BuildRequires:  cmake(Qt6Core)       >= %{min_qt_version}
BuildRequires:  cmake(Qt6Test)       >= %{min_qt_version}

BuildRequires:  cmake(KF6KIO)        >= %{min_kf_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{min_kf_version}

%if 0%{?tests}
BuildRequires:  dbus-x11
BuildRequires:  kio-extras
BuildRequires:  fuse3
%endif

Requires:       systemd
Requires:       dbus-common

%description
KioFuse works by acting as a bridge between KDE's KIO filesystem design and
FUSE.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6 -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
	-DQT_MAJOR_VERSION=6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
dbus-launch --exit-with-session \
%ctest --timeout 30 ||:
%endif


%files
%license LICENSES/GPL-3.0-or-later.txt
%doc README.md DESIGN.md
%{_libexecdir}/kio-fuse
%{_userunitdir}/kio-fuse.service
%{_kf6_datadir}/dbus-1/services/org.kde.KIOFuse.service
%{_tmpfilesdir}/%{name}-tmpfiles.conf


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.1-3
- Prepare for Oreon 11 (RP1)
