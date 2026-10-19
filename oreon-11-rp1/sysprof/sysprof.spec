%global source0_hash f2c8d9c5c8294ce3fdc8be7d9f4be56a72ed71522cb54987f1723a8cfd91637d
%global glib2_version 2.80.0
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           sysprof
Version:        51.0
Release:        1%{?dist}
Summary:        A system-wide Linux profiler
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND CC-BY-SA-4.0 AND CC0-1.0 AND BSD-2-Clause-Patent
URL:            http://www.sysprof.com
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       hicolor-icon-theme
Requires:       %{name}-cli%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libdebuginfod)
BuildRequires:  pkgconfig(libdex-1)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
# /oreon:deps
%description
Sysprof is a sampling CPU profiler for Linux that collects accurate,
high-precision data and provides efficient access to the sampled
calltrees.

%package        agent
Summary:        Sysprof agent utility
%description    agent
The %{name}-agent package contains the sysprof-agent program. It provides a P2P
D-Bus API to the process which can control subprocesses. It's used by IDE
tooling to have more control across container boundaries.

%package        cli
Summary:        Sysprof command line utility
Requires:       kernel-tools
Requires:       libsysprof%{?_isa} = %{version}-%{release}
%description    cli
The %{name}-cli package contains the sysprof-cli command line utility.

%package     -n libsysprof
Summary:        Sysprof libraries
Obsoletes:      libsysprof-ui < 45.0
%description -n libsysprof
The libsysprof package contains the Sysprof libraries.

%package        capture-devel
Summary:        Development files for sysprof-capture static library
License:        BSD-2-Clause-Patent
Provides:       sysprof-capture-static = %{version}-%{release}
%description    capture-devel
The %{name}-capture-devel package contains the sysprof-capture static library and header files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-capture-devel%{?_isa} = %{version}-%{release}
Requires:       libsysprof%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles libsysprof usr/*/lib*.so.*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n sysprof-agent -f %{oreon_filedir}/sysprof-agent.list
%files -n sysprof-cli -f %{oreon_filedir}/sysprof-cli.list
%files -n libsysprof -f %{oreon_filedir}/libsysprof.list
%files -n sysprof-capture-devel -f %{oreon_filedir}/sysprof-capture-devel.list
%files -n sysprof-devel -f %{oreon_filedir}/sysprof-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
