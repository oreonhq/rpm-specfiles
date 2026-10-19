%global source0_hash 76f24f7ffd037e431e8813cd4404d0f0b61c4a0c4fda18d92855a8cae7ea7706
Name:    kmailtransport
Version: 26.08.0
Release:        1%{?dist}
Summary:        The KMailTransport Library
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Conflicts:      kf5-kmailtransport < 23.08.5-2
# oreon:deps
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6GAPI)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6SMTP)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Mime)
Requires:       cmake(KPim6AkonadiMime)
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

# Remove together with move-translations.patch once released
find ./po -type f -name libmailtransport5.po -execdir mv {} libmailtransport6.po \;

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kmailtransport-devel -f %{oreon_filedir}/kmailtransport-devel.list
%files -n kmailtransport-doc -f %{oreon_filedir}/kmailtransport-doc.list

%changelog

%autochangelog
