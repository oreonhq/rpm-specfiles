%global source0_hash 69b678bf65dde7f2891273d50aea9f5cfd1a96cd208bd063cd4898486c88e6e5
%global svn 144
%global checkout 20240219svn%{svn}
Summary:        Several GUI (Qt) programs and plug-ins for unixODBC
Name: unixODBC-gui-qt
Version: 0^%{checkout}
Release:        1%{?dist}
URL: http://sourceforge.net/projects/unixodbc-gui-qt/
License: GPL-3.0-only AND LGPL-3.0-only
Source0:        %{name}-%{checkout}.tar.gz
Source1: ODBCCreateDataSourceQ5.desktop
Source2: ODBCManageDataSourcesQ5.desktop
Patch0: 0001-Turn-on-soname-versioning.patch
Provides: unixODBC-kde = 2.3.0-1
Obsoletes: unixODBC-kde < 2.3.0-1
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  make
BuildRequires:  qt-assistant-adp-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  unixODBC-devel
# /oreon:deps
%description
unixODBC-gui-qt provides several GUI (Qt) programs and plug-ins.
  * administrator (program)
  * create data source wizard (program)
  * test (program)
  * installer (plug-in)
  * auto test (plug-in)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n %{name}

# Fix hardcoded installation paths
sed -Ei -e 's|(INSTALL_TARGET_BIN)\s*=.*$|\1 = %{_bindir}|' \
        -e 's|(INSTALL_TARGET_LIB)\s*=.*$|\1 = %{_libdir}|' \
        defines.pri

%build

export UNIXODBC_DIR="%{_prefix}" UNIXODBC_LIBDIR="%{_libdir}"
%{qmake_qt5}
%{make_build}
%install
export UNIXODBC_DIR="%{_prefix}" UNIXODBC_LIBDIR="%{_libdir}"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
%{make_install} INSTALL_ROOT="$RPM_BUILD_ROOT"
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
install -p -m 644 odbcinstQ5/ODBCManageDataSources64.xpm \
    $RPM_BUILD_ROOT%{_datadir}/pixmaps/ODBCCreateDataSourceQ5.xpm
install -p -m 644 odbcinstQ5/ODBCManageDataSources64.xpm \
    $RPM_BUILD_ROOT%{_datadir}/pixmaps/ODBCManageDataSourcesQ5.xpm
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
