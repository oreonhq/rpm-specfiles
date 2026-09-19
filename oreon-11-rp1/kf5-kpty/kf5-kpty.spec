%global source0_hash ad4f6322544f65c7c900003d86ffeaac350fd2e2739b4777997ece49d8f04630

%undefine __cmake_in_source_build
%global framework kpty

Name:           kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary:        KDE Frameworks 5 Tier 2 module providing Pty abstraction

License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  libutempter-devel
BuildRequires:  qt5-qtbase-devel

# runtime calls %%_libexexdir/utempter/utempter
Requires:       libutempter

%description
KDE Frameworks 5 tier 2 module providing Pty abstraction.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel >= %{version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
# find_program for utempter is failing for some reason, so
# set path explicitly to known-good value
%cmake_kf5 \
  -DUTEMPTER_EXECUTABLE:PATH=/usr/libexec/utempter/utempter

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-man

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Pty.so.5*

%files devel

%{_kf5_includedir}/KPty/
%{_kf5_libdir}/libKF5Pty.so
%{_kf5_libdir}/cmake/KF5Pty/
%{_kf5_archdatadir}/mkspecs/modules/qt_KPty.pri

%changelog
%autochangelog
