%global source0_hash fce3c603cac3fec9a3f0e101c49785c32ace07b8f60b52739b638d329f43826d

Name:    kmime
Version: 25.12.3
Release: 1%{?dist}
Summary: The KMime Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kcodecs-devel

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Codecs)
Requires:       boost-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
#find ./po -type f -name libkmime5.po -execdir mv {} libkmime6.po \;

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang libkmime6 --with-qt

%files -f libkmime6.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/%{name}.*
%{_kf6_libdir}/libKPim6Mime.so.*

%files devel
%{_includedir}/KPim6/KMime/
%{_kf6_libdir}/libKPim6Mime.so
%{_kf6_libdir}/cmake/KPim6Mime/
%changelog
%autochangelog
