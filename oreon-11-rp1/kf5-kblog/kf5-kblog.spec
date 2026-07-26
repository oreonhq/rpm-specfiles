%global source0_hash 5932a8ba3ec33f13aec201252abb6d0712740f52af03747e9eb0f6c0764cb9b4

%undefine __cmake_in_source_build
%global framework kblog

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 20.04.3
Release: 15%{?dist}
Summary: The KBlog Library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://cgit.kde.org/%{framework}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# libical (and thus kcalendarcore) not on all arches for RHEL8.
%if 0%{?rhel} == 8
ExclusiveArch: x86_64 ppc64le aarch64 %{arm}
%endif

BuildRequires: make
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcoreaddons-devel >= 5.15
BuildRequires:  kf5-kdelibs4support-devel >= 5.15
BuildRequires:  kf5-kio-devel >= 5.15
BuildRequires:  kf5-kxmlrpcclient-devel >= 5.15
#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
# in kf5 since 5.50.0
BuildRequires:  kf5-syndication-devel >= %{majmin_ver}

BuildRequires:  qt5-qtbase-devel
%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

# upstream dropped support, FTBFS on f28+
%if 0%{?fedora} > 27
Obsoletes: blogilo < 17.08.3-10
Obsoletes: blogilo-libs < 17.08.3-10
%endif

%description
The KBlog library can retrieve, update or create blog posts on various popular
blogging platforms like Wordpress or Blogspot.com.
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kdelibs4support-devel
Requires:       kf5-kcalendarcore-devel
Requires:       kf5-syndication-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test/fast ARGS="--output-on-failure --timeout 10" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKF5Blog.so.*

%files devel
%{_kf5_includedir}/kblog_version.h
%{_kf5_includedir}/KBlog/
%{_kf5_libdir}/libKF5Blog.so
%{_kf5_libdir}/cmake/KF5Blog/
%{_kf5_archdatadir}/mkspecs/modules/qt_KBlog.pri

%changelog
%autochangelog
