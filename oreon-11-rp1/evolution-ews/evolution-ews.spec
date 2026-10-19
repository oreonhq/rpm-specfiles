%global source0_hash 85b8e7089582d9d5ea6dc1a82325b3e5c4b0396924f7a6e0f743a9128cad73d4
%undefine __cmake_in_source_build
%global json_glib_version 1.0.4
%global libmspack_version 0.4
%global libsoup_version 3.1.1
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name: evolution-ews
Version: 3.62.0
Release:        1%{?dist}
Summary:        Evolution extension for Exchange Web Services
License: LGPL-2.1-or-later
URL: https://gitlab.gnome.org/GNOME/evolution/-/wikis/home
Source0:        http://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{version}.tar.xz
%global eds_evo_version %{version}
Requires: evolution >= %{eds_evo_version}
Requires: evolution-data-server >= %{eds_evo_version}
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-langpacks = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pkgconfig(camel-1.2)
BuildRequires:  pkgconfig(evolution-data-server-1.2)
BuildRequires:  pkgconfig(evolution-mail-3.0)
BuildRequires:  pkgconfig(evolution-shell-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libebackend-1.2)
BuildRequires:  pkgconfig(libebook-1.2)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedata-book-1.2)
BuildRequires:  pkgconfig(libedata-cal-2.0)
BuildRequires:  pkgconfig(libemail-engine)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libmspack)
BuildRequires:  pkgconfig(libsoup-3.0)
# /oreon:deps
%description
This package allows Evolution to interact with Microsoft Exchange servers,
versions 2007 and later, through its Exchange Web Services (EWS) interface.

%package core
Summary: Core files for %{name}
Requires: %{name}-langpacks = %{version}-%{release}
Requires: evolution-data-server >= %{eds_evo_version}
Requires: libmspack >= %{libmspack_version}
%description core
This package contains core files for %{name}, which do not depend on the evolution package.
These files add the functionality for the address books, calendars, task lists and memo lists
without bringing in the evolution package.

%package langpacks
Summary: Translations for %{name}
BuildArch: noarch
Requires: %{name}-core = %{version}-%{release}
%description langpacks
This package contains translations for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="$RPM_OPT_FLAGS -Wno-deprecated-declarations"
%cmake -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
	-DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
	%if "%{?_lib}" == "lib64"
		-DLIB_SUFFIX=64 \
	%endif
	%{nil}
%cmake_build
%install
%cmake_install
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n evolution-ews-core -f %{oreon_filedir}/evolution-ews-core.list
%files -n evolution-ews-langpacks -f %{oreon_filedir}/evolution-ews-langpacks.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.60.0-1
- Prepare for Oreon 11 (RP1)
