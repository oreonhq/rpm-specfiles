%global framework ksmtp 

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: KDE SMTP libraries

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

## upstream patches

## upstreamable patches

%global kf5_ver 5.29
BuildRequires: extra-cmake-modules >= %{kf5_ver}
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)

BuildRequires: cmake(Qt5Network)

BuildRequires: kf5-kmime-devel >= %{version}
BuildRequires: cmake(KPim5Mime)

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
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(KPim5Mime)
Requires:       kf5-kmime-devel >= %{version}
%description    devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5SMTP.so.*

%files devel
%{_kf5_libdir}/libKPim5SMTP.so
%{_kf5_libdir}/cmake/KPim5SMTP/
%{_includedir}/KPim5/KSMTP/
%{_kf5_archdatadir}/mkspecs/modules/qt_KSMTP.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
