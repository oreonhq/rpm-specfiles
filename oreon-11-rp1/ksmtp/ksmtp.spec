%global source0_hash a4a76de3a2471d8828c086ea04633a3de2d9ba135b80c5c0ede7eb285ac45a9e

Name:    ksmtp
Version: 25.12.3
Release: 1%{?dist}
Summary: KDE SMTP libraries

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{name}/

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)

BuildRequires: cmake(Qt6Network)

BuildRequires: cmake(KPim6Mime)

BuildRequires: pkgconfig(libsasl2)

# runtime sasl plugins
Suggests: cyrus-sasl-gssapi%{?_isa}
Recommends: cyrus-sasl-md5%{?_isa}
Requires: cyrus-sasl-plain%{?_isa}

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

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6SMTP.so.*

%files devel
%{_kf6_libdir}/libKPim6SMTP.so
%{_kf6_libdir}/cmake/KPim6SMTP/
%{_includedir}/KPim6/KSMTP/

%files doc

%changelog
%autochangelog
