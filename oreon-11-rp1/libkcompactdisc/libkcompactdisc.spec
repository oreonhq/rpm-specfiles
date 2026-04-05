Name:    libkcompactdisc 
Version: 25.12.2
Release:	2%{?dist}
Summary: A KDE compact disc library

# License for this library is very nebulous.
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/multimedia/libkcompactdisc

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6I18n)

BuildRequires: cmake(Qt6DBus)

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(phonon4qt6)

# historical conflicts
# when split occured (kdemultimedia to libkcompactdisc)
Conflicts: kdemultimedia-libs < 6:4.8.80
# translations moved here (during kf5-libkcompactdisc)
Conflicts: kde-l10n < 17.03
 # translations conflict with kf5-libkcompactdisc
Conflicts: kf5-libkcompactdisc < 24.01.85
Obsoletes: kf5-libkcompactdisc < 24.01.85

%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: kf5-libkcompactdisc-devel < 24.01.85
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-man

%files -f %{name}.lang
%license COPYING*
%{_kf6_libdir}/libKCompactDisc6.so.5*

%files devel
%{_includedir}/KCompactDisc6/
%{_kf6_libdir}/libKCompactDisc6.so
%{_kf6_libdir}/cmake/KCompactDisc6/
%{_qt6_archdatadir}/mkspecs/modules/qt_KCompactDisc.pri


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.2-1
- Prepare for Oreon 11 (RP1)
