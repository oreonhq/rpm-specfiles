%global source0_hash cf181ed248f6bf12233b459e4a504fab645b3ce8040b6855a073453756311166
%if 0%{?suse_version}
  %bcond_with bugzilla
  %define dbus_devel dbus-1-devel
  %define libjson_devel libjson-devel
%else
  %bcond_without bugzilla
  %define dbus_devel dbus-devel
  %define libjson_devel json-c-devel
%endif
%define glib_ver 2.43.4
Summary:        Generic library for reporting various problems
Name: libreport
Version: 2.17.15
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://abrt.readthedocs.org/
Source0:        https://github.com/abrt/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if 0%{?fedora} >= 24 || 0%{?rhel} > 7 || 0%{?oreon} >= 11
%endif
%if %{with bugzilla}
%endif
Requires: libreport-filesystem = %{version}-%{release}
Requires: satyr%{?_isa} >= 0.38
Requires: glib2%{?_isa} >= %{glib_ver}
Requires: libarchive%{?_isa}
%if 0%{?_module_build}
%endif
Obsoletes: %{name}-compat < 2.13.2
Obsoletes: %{name}-plugin-rhtsupport < 2.13.2
Obsoletes: %{name}-rhel < 2.13.2
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  augeas
BuildRequires:  augeas-devel
BuildRequires:  curl-devel
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  glibc-all-langpacks
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  json-c-devel
BuildRequires:  libarchive-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  newt-devel
BuildRequires:  python3-devel
BuildRequires:  satyr-devel
BuildRequires:  systemd-devel
BuildRequires:  texinfo
BuildRequires:  xmlrpc-c-devel
BuildRequires:  xmlto
# /oreon:deps
%description
Libraries providing API for reporting different problems in applications
to different bug targets like Bugzilla, ftp, trac, etc...

%package filesystem
Summary: Filesystem layout for libreport
BuildArch: noarch
%description filesystem
Filesystem layout for libreport

%package devel
Summary: Development libraries and headers for libreport
Requires: libreport = %{version}-%{release}
%description devel
Development libraries and headers for libreport

%package web
Summary: Library providing network API for libreport
Requires: libreport = %{version}-%{release}
%description web
Library providing network API for libreport

%package web-devel
Summary: Development headers for libreport-web
Requires: libreport-web = %{version}-%{release}
%description web-devel
Development headers for libreport-web

%package -n python3-libreport
Summary: Python 3 bindings for report-libs
%if 0%{?_module_build}
%global distfreerelease %(echo %{release}|sed 's/%{?dist}$//'||echo 0)
Requires: libreport >= %{version}-%{distfreerelease}
%else
Requires: libreport = %{version}-%{release}
%endif
Requires: python3-dnf
Requires: python3-requests
Requires: python3-urllib3
%{?python_provide:%python_provide python3-libreport}
%description -n python3-libreport
Python 3 bindings for report-libs.

%package cli
Summary: %{name}'s command line interface
Requires: %{name} = %{version}-%{release}
%description cli
This package contains simple command line tool for working
with problem dump reports

%package newt
Summary: %{name}'s newt interface
Requires: %{name} = %{version}-%{release}
Provides: report-newt = 0:0.23-1
Obsoletes: report-newt < 0:0.23-1
%description newt
This package contains a simple newt application for reporting
bugs

%package gtk
Summary: GTK front-end for libreport
Requires: libreport = %{version}-%{release}
Requires: libreport-plugin-reportuploader = %{version}-%{release}
Provides: report-gtk = 0:0.23-1
Obsoletes: report-gtk < 0:0.23-1
%description gtk
Applications for reporting bugs using libreport backend

%package gtk-devel
Summary: Development libraries and headers for libreport
Requires: libreport-gtk = %{version}-%{release}
%description gtk-devel
Development libraries and headers for libreport-gtk

%package plugin-kerneloops
Summary: %{name}'s kerneloops reporter plugin
Requires: curl
Requires: %{name} = %{version}-%{release}
Requires: libreport-web = %{version}-%{release}
%description plugin-kerneloops
This package contains plugin which sends kernel crash information to specified
server, usually to kerneloops.org.

%package plugin-logger
Summary: %{name}'s logger reporter plugin
Requires: %{name} = %{version}-%{release}
%description plugin-logger
The simple reporter plugin which writes a report to a specified file.

%package plugin-systemd-journal
Summary: %{name}'s systemd journal reporter plugin
Requires: %{name} = %{version}-%{release}
%description plugin-systemd-journal
The simple reporter plugin which writes a report to the systemd journal.

%package plugin-mailx
Summary: %{name}'s mailx reporter plugin
Requires: %{name} = %{version}-%{release}
Requires: /usr/bin/mailx
%description plugin-mailx
The simple reporter plugin which sends a report via mailx to a specified
email address.

%if %{with bugzilla}
%package plugin-bugzilla
Summary: %{name}'s bugzilla plugin
Requires: %{name} = %{version}-%{release}
Requires: libreport-web = %{version}-%{release}
Requires: python3-libreport = %{version}-%{release}
%description plugin-bugzilla
Plugin to report bugs into the bugzilla.
%endif

%package plugin-mantisbt
Summary: %{name}'s mantisbt plugin
Requires: %{name} = %{version}-%{release}
Requires: libreport-web = %{version}-%{release}
%description plugin-mantisbt
Plugin to report bugs into the mantisbt.

%package centos
Summary: %{name}'s CentOS Bug Tracker workflow
Requires: %{name} = %{version}-%{release}
Requires: libreport-web = %{version}-%{release}
Requires: libreport-plugin-mantisbt = %{version}-%{release}
%description centos
Workflows to report issues into the CentOS Bug Tracker.

%package plugin-ureport
Summary: %{name}'s micro report plugin
BuildRequires: %{libjson_devel}
Requires: %{name} = %{version}-%{release}
Requires: libreport-web = %{version}-%{release}
%description plugin-ureport
Uploads micro-report to abrt server

%package plugin-reportuploader
Summary: %{name}'s reportuploader plugin
Requires: %{name} = %{version}-%{release}
Requires: libreport-web = %{version}-%{release}
%description plugin-reportuploader
Plugin to report bugs into anonymous FTP site associated with ticketing system.

%if %{with bugzilla}
%package anaconda
Summary: Default configuration for reporting anaconda bugs
Requires: %{name} = %{version}-%{release}
Requires: libreport-plugin-reportuploader = %{version}-%{release}
%description anaconda
Default configuration for reporting Anaconda problems or uploading the gathered
data over ftp/scp...
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure \
%if %{without bugzilla}
        --without-bugzilla \
%endif
        --enable-doxygen-docs \
        --disable-silent-rules
%make_build
%install
%make_install \
%if %{with python3}
             PYTHON=%{__python3} \
%endif
             mandir=%{_mandir}
%find_lang %{name}
find %{buildroot} -name "*.py[co]" -delete
find %{buildroot} -name '*.la' -or -name '*.a' | xargs rm -f
mkdir -p %{buildroot}/%{_initrddir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/events.d/
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/events/
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/workflows.d/
mkdir -p %{buildroot}/%{_datadir}/%{name}/events/
mkdir -p %{buildroot}/%{_datadir}/%{name}/workflows/
rm -f %{buildroot}/%{_infodir}/dir
%oreon_autofiles python3-libreport usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%check

make check|| {
    find tests/testsuite.dir -name "testsuite.log" -print -exec cat '{}' \;
    exit 1
}
%ldconfig_scriptlets
%ldconfig_scriptlets web
%files -f %{oreon_filedir}/main.list
%files -n libreport-filesystem -f %{oreon_filedir}/libreport-filesystem.list
%files -n libreport-devel -f %{oreon_filedir}/libreport-devel.list
%files -n libreport-web -f %{oreon_filedir}/libreport-web.list
%files -n libreport-web-devel -f %{oreon_filedir}/libreport-web-devel.list
%files -n python3-libreport -f %{oreon_filedir}/python3-libreport.list
%files -n libreport-cli -f %{oreon_filedir}/libreport-cli.list
%files -n libreport-newt -f %{oreon_filedir}/libreport-newt.list
%files -n libreport-gtk -f %{oreon_filedir}/libreport-gtk.list
%files -n libreport-gtk-devel -f %{oreon_filedir}/libreport-gtk-devel.list
%files -n libreport-plugin-kerneloops -f %{oreon_filedir}/libreport-plugin-kerneloops.list
%files -n libreport-plugin-logger -f %{oreon_filedir}/libreport-plugin-logger.list
%files -n libreport-plugin-systemd-journal -f %{oreon_filedir}/libreport-plugin-systemd-journal.list
%files -n libreport-plugin-mailx -f %{oreon_filedir}/libreport-plugin-mailx.list
%files -n libreport-plugin-bugzilla -f %{oreon_filedir}/libreport-plugin-bugzilla.list
%files -n libreport-plugin-mantisbt -f %{oreon_filedir}/libreport-plugin-mantisbt.list
%files -n libreport-centos -f %{oreon_filedir}/libreport-centos.list
%files -n libreport-plugin-ureport -f %{oreon_filedir}/libreport-plugin-ureport.list
%files -n libreport-plugin-reportuploader -f %{oreon_filedir}/libreport-plugin-reportuploader.list
%files -n libreport-anaconda -f %{oreon_filedir}/libreport-anaconda.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.15-10
- Prepare for Oreon 11 (RP1)
