%global source0_hash f921410e180e0a5811e1ee2926954920c6576a72b3b65f53791faa6c85fcb689
%if ! 0%{?bootstrap}
%global tests 1
%endif
Name:    libalkimia
Summary:        Financial library
Version: 8.2.1
Release:        3%{?dist}
License: LicenseRef-Callaway-LGPLv2+
URL:     https://kmymoney.org/
Source0:        https://download.kde.org/stable/alkimia/%{version}/alkimia-%{version}.tar.xz
Patch0: alkimia-8.2.1-install-financequote.patch
Patch100: alkimia-8.2.1-install-python.patch
ExcludeArch: %{ix86}
%ifarch %{qt6_qtwebengine_arches}
%global webengine 1
%endif
%if 0%{?tests}
%endif
%if 0%{?docs}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libEGL
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gmp)
BuildRequires:  python3-devel
BuildRequires:  xwayland-run
# /oreon:deps
%description
%{summary}

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gmp-devel
%description devel
%{summary}.

%package        qt6
Summary:        Accounts framework Qt6 bindings
Obsoletes:      %{name}-qt5 < 8.2.1
Recommends:     perl(Date::Manip)
Recommends:     perl(Finance::Quote)
Recommends:     perl(LWP)
Recommends:     perl(XML::Parser)
Recommends:     perl(XML::Writer)
%description    qt6
%{summary}.

%package        qt6-devel
Summary:        Development files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
Requires:       gmp-devel
%if 0%{?webengine}
Requires:       cmake(Qt6WebEngineWidgets)
%endif
Obsoletes:      %{name}-qt5-devel < 8.2.1
%description    qt6-devel
%{summary}.

%package        doc
Summary:        API Documentation for %{name}
BuildArch:      noarch
%description    doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir alkimia-%{version}
%oreon_prep
%build

%cmake_kf6 \
  %{!?plasma:-DBUILD_APPLETS:BOOL=OFF} \
  -DBUILD_WITH_QT6=ON \
  -DBUILD_WITH_WEBENGINE:BOOL=%{?webengine:ON}%{!?webengine:OFF} \
  -DBUILD_WITH_WEBKIT:BOOL=OFF \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DENABLE_FINANCEQUOTE:BOOL=ON
%cmake_build
%if 0%{?docs}
doxygen -u %{_target_platform}-qt6/src/libalkimia.doxygen
make libalkimia_apidoc -C %{_target_platform}-qt6
%endif
%install
%cmake_install
%if 0%{?docs}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a %{_target_platform}-qt6/src/apidocs/html/ %{buildroot}%{_pkgdocdir}/
%endif
%if ! 0%{?plasma}
rm -fv  %{buildroot}%{_kf6_datadir}/locale/*/LC_MESSAGES/plasma*
%endif
%py_byte_compile %{python3} %{buildroot}%{_datadir}/gdb
%find_lang %{name} --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libalkimia6)" = "%{version}"
%if 0%{?tests}
%global __ctest xwfb-run -- %{__ctest}
time \
%ctest -E '(download|newstuff|web)engine%{!?webengine:|onlinequotes}'
%endif
%files -f %{oreon_filedir}/main.list
%files -n libalkimia-devel -f %{oreon_filedir}/libalkimia-devel.list
%files -n libalkimia-qt6 -f %{oreon_filedir}/libalkimia-qt6.list
%files -n libalkimia-qt6-devel -f %{oreon_filedir}/libalkimia-qt6-devel.list
%files -n libalkimia-doc -f %{oreon_filedir}/libalkimia-doc.list

%changelog

%autochangelog
