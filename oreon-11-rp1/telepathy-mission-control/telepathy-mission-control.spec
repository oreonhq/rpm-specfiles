%global source0_hash 4c6b433b8b9079fd7df3e29aefcad6755a2081a9a634ffb6b33936c7d0d8bd03

%define tp_glib_ver 0.17.5
%global mc_plugindir %{_libdir}/mission-control-plugins.0

Name:           telepathy-mission-control
Version:        5.16.5
Release:        15%{?dist}
Epoch:          1
Summary:        Central control for Telepathy connection manager

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://telepathy.freedesktop.org/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

# Backported from upstream
# https://github.com/TelepathyIM/telepathy-mission-control/pull/6
Patch0:         6.patch

BuildRequires: make
BuildRequires:  chrpath
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  libxslt-devel
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  pkgconfig
BuildRequires:  telepathy-glib-devel >= %{tp_glib_ver}

%description
Mission Control, or MC, is a Telepathy component providing a way for
"end-user" applications to abstract some of the details of connection
managers, to provide a simple way to manipulate a bunch of connection
managers at once, and to remove the need to have in each program the
account definitions and credentials.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure \
  --disable-static \
  --enable-gtk-doc \
  --with-connectivity=nm

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

%{make_build}

%install
%{make_install}

# create/own plugin dir
mkdir -p %{buildroot}%{mc_plugindir}

# Remove rpaths if present
chrpath --list   %{buildroot}%{_libexecdir}/mission-control-5 && \
chrpath --delete %{buildroot}%{_libexecdir}/mission-control-5
# Remove .la files
find %{buildroot} -type f -name "*.la" -delete

%check
%if %{undefined flatpak}
PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "%{?mc_plugindir}" = "$(pkg-config --variable=plugindir mission-control-plugins 2>/dev/null)"
%endif
make check ||:

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/mc-tool
%{_bindir}/mc-wait-for-name
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.AccountManager.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.MissionControl5.service
%{_datadir}/glib-2.0/schemas/im.telepathy.MissionControl.FromEmpathy.gschema.xml
%{_libdir}/libmission-control-plugins.so.0*
%dir %{mc_plugindir}
%{_libexecdir}/mission-control-5
%{_mandir}/man1/mc-tool.1*
%{_mandir}/man1/mc-wait-for-name.1*

%files devel
%doc %{_datadir}/gtk-doc/html/mission-control-plugins
%{_includedir}/mission-control-5.5/
%{_libdir}/pkgconfig/mission-control-plugins.pc
%{_libdir}/libmission-control-plugins.so
%{_mandir}/man8/mission-control-5.8*

%changelog
%autochangelog
