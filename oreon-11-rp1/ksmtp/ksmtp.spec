%global stable_kf6 stable
%global source0_hash a4a76de3a2471d8828c086ea04633a3de2d9ba135b80c5c0ede7eb285ac45a9e
Name:    ksmtp
Version: 25.12.3
Release:        1%{?dist}
Summary:        KDE SMTP libraries
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{name}/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Suggests: cyrus-sasl-gssapi%{?_isa}
Recommends: cyrus-sasl-md5%{?_isa}
Requires: cyrus-sasl-plain%{?_isa}
# oreon:deps
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(libsasl2)
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KPim6Mime)
%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libksmtp5.po -execdir mv {} libksmtp6.po \;

%build

%cmake_kf6 -DBUILD_QCH=OFF
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ksmtp-devel -f %{oreon_filedir}/ksmtp-devel.list
%files -n ksmtp-doc -f %{oreon_filedir}/ksmtp-doc.list

%changelog

%autochangelog
