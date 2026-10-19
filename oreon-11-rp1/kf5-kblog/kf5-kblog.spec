%global source0_hash 5932a8ba3ec33f13aec201252abb6d0712740f52af03747e9eb0f6c0764cb9b4
%undefine __cmake_in_source_build
%global framework kblog
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{framework}
Version: 20.04.3
Release:        1%{?dist}
Summary:        The KBlog Library
License: LicenseRef-Callaway-LGPLv2+
URL:     https://cgit.kde.org/%{framework}.git
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%global majmin_ver %{version}
%if 0%{?tests}
%endif
Conflicts: kde-l10n < 17.03
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kxmlrpcclient-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-syndication-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test/fast ARGS="--output-on-failure --timeout 10" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-kblog-devel -f %{oreon_filedir}/kf5-kblog-devel.list

%changelog

%autochangelog
