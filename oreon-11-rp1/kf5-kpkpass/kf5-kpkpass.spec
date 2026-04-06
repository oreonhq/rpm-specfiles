%undefine __cmake_in_source_build
%global framework kpkpass

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-%{framework}
Version: 23.08.5
Release: 6%{?dist}
Summary: Library to deal with Apple Wallet pass files

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  extra-cmake-modules >= 5.60
BuildRequires:  kf5-rpm-macros

BuildRequires:  cmake(KF5Archive)

BuildRequires:  qt5-qtbase-devel

BuildRequires:  pkgconfig(shared-mime-info)
%if "%(pkg-config --modversion shared-mime-info 2> /dev/null || echo 2.1)" < "2.2"
%global mime 1
%endif

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

#find_lang %%{name} --all-name


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
#xvfb-run -a \
#dbus-launch --exit-with-session \
make test/fast ARGS="--output-on-failure --timeout 10" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/org_kde_%{framework}.*
%if 0%{?mime}
%{_kf5_datadir}/mime/packages/application-vnd-apple-pkpass.xml
%endif
%{_kf5_libdir}/libKPim5PkPass.so.5*

%files devel
%{_includedir}/KPim5/KPkPass/
%{_kf5_libdir}/libKPim5PkPass.so
%{_kf5_libdir}/cmake/KPimPkPass/
%{_kf5_libdir}/cmake/KPim5PkPass/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-6
- Prepare for Oreon 11 (RP1)
