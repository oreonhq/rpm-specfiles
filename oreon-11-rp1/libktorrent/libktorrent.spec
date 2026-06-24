%global source0_hash none

Name:           libktorrent
Summary:        Torrent downloading library for KDE 6 applications
Version:        26.04.2
Release:        1%{?dist}
# CC0 is only for CI tooling, BSD3 for cmake macros, MIT for win32 support code
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/network/%{name}
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)

BuildRequires:  boost-devel >= 1.71.0
BuildRequires:  gmp-devel >= 6.0.0
BuildRequires:  libgcrypt-devel >= 1.4.5

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       libgcrypt-devel%{?_isa}
Requires:       cmake(KF6Archive)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6KIO)
Requires:       cmake(Qt6Network)

%description devel
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang libktorrent6


%files -f libktorrent6.lang
%doc ChangeLog
%license LICENSES/GPL*.txt
%{_kf6_libdir}/libKTorrent6.so.6
%{_kf6_libdir}/libKTorrent6.so.%{version}

%files devel
%{_kf6_includedir}/libktorrent/
%{_kf6_libdir}/libKTorrent6.so
%{_kf6_libdir}/cmake/KTorrent6/


%changelog
%autochangelog

