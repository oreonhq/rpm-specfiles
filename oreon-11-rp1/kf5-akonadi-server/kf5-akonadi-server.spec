%global source0_hash abdbdb28c1084a6ad119d7292175ad31efb4a7898a32cc32a35aa1485d9c4f38
%global framework akonadi-server
%global _changelog_trimtime %(date +%s -d "1 year ago")
%global mysql mysql
%if !0%{?bootstrap}
%ifnarch %{arm} s390x
%global tests 0
%endif
%endif
%if 0%{?flatpak}
%global database_backend SQLITE
%endif
Name:    kf5-%{framework}
Summary:        PIM Storage Service
Version: 23.08.5
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/stable/release-service/%{version}/src/akonadi-%{version}.tar.xz
Source10:       akonadiserverrc.mysql
Source11:       akonadiserverrc.sqlite
Patch0:   akonadi-adapt-to-kaccounts-api-change.patch
%define mysql_conf_timestamp 20170512
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
%if ! 0%{?bootstrap}
%endif
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
%if 0%{?tests}
%if ! 0%{?flatpak}
%endif
%endif
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%if ! 0%{?flatpak}
Recommends:     %{name}-mysql = %{version}-%{release}
%endif
Conflicts:      akonadi < 1.13.0-100
Conflicts: kde-l10n < 17.03
Obsoletes: kf5-akonadi-socialutils < 16.07
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtxmlpatterns-devel
# /oreon:deps
%description
%{summary}.

%package libs
Summary:        KDE PIM core libraries
%description libs
%{summary}.

%package devel
Summary:        Developer files for %{name}
Obsoletes:      kf5-akonadi-devel < 16.03
Obsoletes: kf5-akonadi-socialutils-devel < 16.07
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       kf5-kcompletion-devel
Requires:       kf5-kjobwidgets-devel
Requires:       kf5-kservice-devel
Requires:       kf5-solid-devel
Requires:       kf5-kxmlgui-devel
Requires:       kf5-kitemmodels-devel
Requires:       qt5-qtbase-devel
Conflicts:      akonadi-devel
%description devel
%{summary}.

%package mysql
Summary:        Akonadi MySQL backend support
Obsoletes:      akonadi < 1.7.90-2
Obsoletes:      akonadi-mysql < 15.08.0
Provides:       akonadi-mysql = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{mysql}-server
Requires:       qt5-qtbase-mysql%{?_isa}
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
%description mysql
Configures akonadi to use mysql backend by default.

Requires an available instance of mysql server at runtime.
Akonadi can spawn a per-user one automatically if the mysql-server
package is installed on the machine.
See also: %{_sysconfdir}/akonadi/mysql-global.conf

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir akonadi-%{version}
%oreon_prep
%build

%cmake_kf5 \
  %{?database_backend:-DDATABASE_BACKEND=%{database_backend}} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DINSTALL_APPARMOR:BOOL=OFF \
  -DMYSQLD_EXECUTABLE:FILEPATH=%{_libexecdir}/mysqld \
  -DMYSQLD_SCRIPTS_PATH:FILEPATH=%{_bindir}/mysql_install_db \
  -DPOSTGRES_PATH:FILEPATH=%{_bindir}/pg_ctl
%cmake_build
%install
%cmake_install
%find_lang libakonadi5
%find_lang akonadi_knut_resource
install -p -m644 -D %{SOURCE10} %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
install -p -m644 -D %{SOURCE11} %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite
mkdir -p %{buildroot}%{_datadir}/akonadi/agents
touch -d %{mysql_conf_timestamp} \
  %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-global*.conf \
  %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-local.conf
mkdir -p %{buildroot}%{_kf5_datadir}/akonadi/plugins
mkdir -p %{buildroot}%{_kf5_libdir}/akonadi
touch akonadiserverrc
install -p -m644 -D akonadiserverrc %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc
rm -fv %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-global-mobile.conf
rm -fv %{buildroot}%{_kf5_includedir}/AkonadiCore/std_exception.h
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif
%post

%{?ldconfig}
/usr/sbin/update-alternatives \
  --install %{_sysconfdir}/xdg/akonadi/akonadiserverrc \
  akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite \
  8
%postun

%{?ldconfig}
if [ $1 -eq 0 ] ; then
/usr/sbin/update-alternatives \
  --remove akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite
fi
%post mysql

/usr/sbin/update-alternatives \
  --install %{_sysconfdir}/xdg/akonadi/akonadiserverrc \
  akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql \
  10
%postun mysql

if [ $1 -eq 0 ]; then
/usr/sbin/update-alternatives \
  --remove akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
fi
%files -f %{oreon_filedir}/main.list
%files -n kf5-akonadi-server-libs -f %{oreon_filedir}/kf5-akonadi-server-libs.list
%files -n kf5-akonadi-server-devel -f %{oreon_filedir}/kf5-akonadi-server-devel.list
%files -n kf5-akonadi-server-mysql -f %{oreon_filedir}/kf5-akonadi-server-mysql.list

%changelog

%autochangelog
