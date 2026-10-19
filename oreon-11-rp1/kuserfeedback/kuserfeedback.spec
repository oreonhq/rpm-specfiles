%global source1_hash 036b2a03042d78adfc92324f4a07a2a22d3b0c3c76ce0e03529c845de5cac9a1
%global source0_hash c8a463c8e570f6d532cbe150732220575c6385df97c91399b6c84450691771ca
Name:    kuserfeedback
Summary:        Framework for collecting user feedback for apps via telemetry and surveys
Version: 6.30.0
Release:        1%{?dist}
License: MIT
URL:     https://invent.kde.org/libraries/%{name}
Source0:        https://download.kde.org/stable/frameworks/6.30/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/stable/frameworks/6.30/%{name}-%{version}.tar.xz.sig
Source2: gpgkey-E0A3EB202F8E57528E13E72FD7574483BB57B18D.gpg
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Widgets)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        console
Summary:        Analytics and administration tool for UserFeedback servers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtcharts%{?_isa}
%description    console
Analytics and administration tool for UserFeedback servers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%cmake_kf6 \
   -DENABLE_DOCS:BOOL=OFF \
   -DENABLE_CONSOLE:BOOL=ON \
   -DENABLE_PHP:BOOL=OFF \
   -DENABLE_PHP_UNIT:BOOL=OFF
%cmake_build
%install
%cmake_install
%find_lang userfeedbackconsole6 --with-qt
%find_lang userfeedbackprovider6 --with-qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kde.kuserfeedback-console.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kuserfeedback-console.desktop
%files -f %{oreon_filedir}/main.list
%files -n kuserfeedback-devel -f %{oreon_filedir}/kuserfeedback-devel.list
%files -n kuserfeedback-console -f %{oreon_filedir}/kuserfeedback-console.list

%changelog

%autochangelog
