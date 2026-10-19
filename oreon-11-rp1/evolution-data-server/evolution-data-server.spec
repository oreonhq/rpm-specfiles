%global source0_hash 78be88e9a511f5afe7ff2e363eade84b622dd0282647fc576edb2d4ff2962cba
%undefine __cmake_in_source_build
%define ldap_support 1
%define static_ldap 0
%define krb5_support 1
%define largefile_support 1
%ifarch i686
%global phonenum_support 0
%else
%global phonenum_support 0%{?fedora}
%endif
%{!?with_docs: %global with_docs 1}
%if 0%{?flatpak}
%global with_docs 0
%endif
%{!?with_webkitgtk: %global with_webkitgtk (%{undefined rhel} || 0%{?rhel} < 10)}
%define glib2_version 2.68
%define gtk3_version 3.20
%define gtk4_version 4.4
%define gtk_doc_version 1.9
%define goa_version 3.8
%define libsecret_version 0.5
%define libgweather_version 4.0
%define libical_version 3.0.16
%define libsoup_version 3.1.1
%define nss_version 3.14
%define sqlite_version 3.7.17
%define webkit2gtk_version 2.34.0
%define webkit2gtk4_version 2.36.0
%define json_glib_version 1.0.4
%define uuid_version 2.0
%define credential_modules_dir %{_libdir}/evolution-data-server/credential-modules
%define camel_provider_dir %{_libdir}/evolution-data-server/camel-providers
%define ebook_backends_dir %{_libdir}/evolution-data-server/addressbook-backends
%define ecal_backends_dir %{_libdir}/evolution-data-server/calendar-backends
%define modules_dir %{_libdir}/evolution-data-server/registry-modules
%define uimodules_dir %{_libdir}/evolution-data-server/ui-modules
%global dbus_service_name_address_book	org.gnome.evolution.dataserver.AddressBook10
%global dbus_service_name_calendar	org.gnome.evolution.dataserver.Calendar8
%global dbus_service_name_sources	org.gnome.evolution.dataserver.Sources5
%global dbus_service_name_user_prompter	org.gnome.evolution.dataserver.UserPrompter0
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name: evolution-data-server
Version: 3.62.0
Release:        1%{?dist}
Summary:        Backend data server for Evolution
License: LGPL-2.0-or-later
URL: https://gitlab.gnome.org/GNOME/evolution/-/wikis/home
Source0:        http://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{version}.tar.xz
Patch100: Make-DBUS_SERVICES_PREFIX-runtime-configurable.patch
Provides: evolution-webcal = %{version}
Obsoletes: evolution-webcal < 2.24.0
Recommends: pinentry-gui
Requires: %{name}-langpacks = %{version}-%{release}
%if %{with_webkitgtk}
%endif
%if %{ldap_support}
%if %{static_ldap}
%endif
%endif
%if %{krb5_support}
%endif
Requires: libical-glib >= %{libical_version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  krb5-devel
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libical-glib)
BuildRequires:  pkgconfig(libsecret-unstable)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  systemd
BuildRequires:  vala
# /oreon:deps
%description
The %{name} package provides a unified backend for programs that work
with contacts, tasks, and calendar information.

It was originally developed for Evolution (hence the name), but is now used
by other packages.

%package devel
Summary: Development files for building against %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig(goa-1.0) >= %{goa_version}
Requires: pkgconfig(gweather4) >= %{libgweather_version}
Requires: pkgconfig(libical-glib) >= %{libical_version}
Requires: pkgconfig(libsecret-unstable) >= %{libsecret_version}
Requires: pkgconfig(libsoup-3.0) >= %{libsoup_version}
Requires: pkgconfig(sqlite3) >= %{sqlite_version}
%if %{with_webkitgtk}
Requires: pkgconfig(webkit2gtk-4.1) >= %{webkit2gtk_version}
Requires: pkgconfig(webkitgtk-6.0) >= %{webkit2gtk4_version}
%endif
Requires: pkgconfig(json-glib-1.0) >= %{json_glib_version}
%description devel
Development files needed for building things which link against %{name}.

%package langpacks
Summary: Translations for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%description langpacks
This package contains translations for %{name}.

%package perl
Summary: Supplemental utilities that require Perl
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: perl-interpreter
%description perl
This package contains supplemental utilities for %{name} that require Perl.

%package tests
Summary: Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -S gendiff -N

# General patches
# %%autopatch -p1 -m 0 -M 99

# Flatpak-specific patches
%if 0%{?flatpak}
%autopatch -p1 -m 100 -M 199
%endif

%build

%if %{ldap_support}
%if %{static_ldap}
%define ldap_flags -DWITH_OPENLDAP=ON -DWITH_STATIC_LDAP=ON
if pkg-config openssl ; then
	export LIBS="-lsasl2 `pkg-config --libs openssl`"
else
	export LIBS="-lsasl2 -lssl -lcrypto"
fi
if pkg-config nss ; then
    export LIBS="$LIBS `pkg-config --libs nss`"
else
    export LIBS="$LIBS -lssl3 -lsmime3 -lnss3 -lnssutil3 -lplds4 -lplc4 -lnspr4"
fi
%else
%define ldap_flags -DWITH_OPENLDAP=ON
%endif
%else
%define ldap_flags -DWITH_OPENLDAP=OFF
%endif
%if %{krb5_support}
%define krb5_flags -DWITH_KRB5=ON
%else
%define krb5_flags -DWITH_KRB5=OFF
%endif
%if %{largefile_support}
%define largefile_flags -DENABLE_LARGEFILE=ON
%else
%define largefile_flags -DENABLE_LARGEFILE=OFF
%endif
%define phonenum_flags -DWITH_PHONENUMBER=OFF
%define ssl_flags -DENABLE_SMIME=ON
%define gtkdoc_flags -DENABLE_GTK_DOC=OFF
%if %{with_webkitgtk}
%define webkitgtk_flags -DENABLE_OAUTH2_WEBKITGTK=ON -DENABLE_OAUTH2_WEBKITGTK4=ON
%else
%define webkitgtk_flags -DENABLE_OAUTH2_WEBKITGTK=OFF -DENABLE_OAUTH2_WEBKITGTK4=OFF
%endif
if ! pkg-config --exists nss; then
  echo "Unable to find suitable version of nss to use!"
  exit 1
fi
export CPPFLAGS="-I%{_includedir}/et"
export CFLAGS="$RPM_OPT_FLAGS -DLDAP_DEPRECATED -fPIC -I%{_includedir}/et -Wno-deprecated-declarations"
%cmake -DENABLE_MAINTAINER_MODE=OFF \
	-DENABLE_FILE_LOCKING=fcntl \
	-DENABLE_DOT_LOCKING=OFF \
	-DENABLE_INTROSPECTION=ON \
	-DENABLE_VALA_BINDINGS=ON \
	-DENABLE_INSTALLED_TESTS=ON \
	-DWITH_LIBDB=OFF \
        -DWITH_SYSTEMDUSERUNITDIR=%{_userunitdir} \
	%ldap_flags %krb5_flags %ssl_flags %webkitgtk_flags \
	%largefile_flags %gtkdoc_flags %phonenum_flags \
	-DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
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
mkdir $RPM_BUILD_ROOT/%{uimodules_dir} || :
mkdir $RPM_BUILD_ROOT/%{credential_modules_dir} || :
find $RPM_BUILD_ROOT -name '*.so.*' -exec chmod +x {} \;
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n evolution-data-server-devel -f %{oreon_filedir}/evolution-data-server-devel.list
%files -n evolution-data-server-langpacks -f %{oreon_filedir}/evolution-data-server-langpacks.list
%files -n evolution-data-server-perl -f %{oreon_filedir}/evolution-data-server-perl.list
%files -n evolution-data-server-tests -f %{oreon_filedir}/evolution-data-server-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.60.0-1
- Prepare for Oreon 11 (RP1)
