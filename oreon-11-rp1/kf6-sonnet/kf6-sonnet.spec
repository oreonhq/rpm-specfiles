%global source1_hash 63efdd1365fceb31543d18efeba5546bc1a38dac85e979e352c8e6428b8423a8
%global source0_hash 1574ef5c17f38e315de104b94580ccc1b7ec1db2650cb4bace2e14159bf61e10
%global		framework sonnet
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:		kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 solution for spell checking
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Patch0:		sonnet6-default-list.patch
Requires:	kf6-filesystem
Recommends:	%{name}-hunspell
# oreon:deps
BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hspell-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig(aspell)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libvoikko)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
KDE Frameworks 6 Tier 1 solution for spell checking.

%package	aspell
Summary:	aspell plugin for %{name}
Requires:	%{name} = %{version}-%{release}
%description	aspell
The %{name}-aspell package contains the aspell spellchecking
plugin for %{name}.

%package	hunspell
Summary:	hunspell plugin for %{name}
Requires:	%{name} = %{version}-%{release}
%description	hunspell
The %{name}-hunspell package contains the hunspell spellchecking
plugin for %{name}.

%package	hspell
Summary:	hspell plugin for %{name}
Supplements:	(%{name} and langpacks-he)
Requires:	%{name} = %{version}-%{release}
Requires:	hunspell-he
%description	hspell
The %{name}-hspell package contains the Hebrew hspell spellchecking
plugin for %{name}.

%package	voikko
Summary:	voikko plugin for %{name}
Supplements:	(%{name} and langpacks-fi)
Requires:	%{name} = %{version}-%{release}
%description	voikko
The %{name}-voikko package contains the Finnish voikko spellchecking
plugin for %{name}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang_kf6 sonnet6_qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-sonnet-aspell -f %{oreon_filedir}/kf6-sonnet-aspell.list
%files -n kf6-sonnet-hunspell -f %{oreon_filedir}/kf6-sonnet-hunspell.list
%files -n kf6-sonnet-hspell -f %{oreon_filedir}/kf6-sonnet-hspell.list
%files -n kf6-sonnet-voikko -f %{oreon_filedir}/kf6-sonnet-voikko.list
%files -n kf6-sonnet-devel -f %{oreon_filedir}/kf6-sonnet-devel.list

%changelog

%autochangelog
