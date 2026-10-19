%global source0_hash 22cad63d16449f2496374edf866a38bd62187006d0835e3cd1df0e6333e4d61a
Name:    akonadi-search
Version: 26.08.0
Release:        1%{?dist}
Summary:        The Akonadi Search library and indexing agent
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND (MIT OR Apache-2.0) AND MIT
URL:     https://invent.kde.org/pim/%{name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Obsoletes:      kf5-akonadi-search < 24.01.80-1
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  corrosion
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  rust
BuildRequires:  xapian-core-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KPim6Akonadi)
Requires:       cmake(KPim6AkonadiMime)
Requires:       cmake(KF6Contacts)
Requires:       cmake(KPim6Mime)
Requires:       cmake(KF6CalendarCore)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Delete the Cargo.lock (So it doesn't fail building)
find -name "Cargo.lock" -print -delete

%build

cd agent/rs/htmlparser
%cargo_license_summary
%cargo_license
cd ../../..
%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles akonadi-search-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles akonadi-search-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n akonadi-search-devel -f %{oreon_filedir}/akonadi-search-devel.list
%files -n akonadi-search-doc -f %{oreon_filedir}/akonadi-search-doc.list

%changelog

%autochangelog
