%global source0_hash da0e11160b2a36fe6260acf62b4190e29755fd5df130818157a04883c1eb7237

Name:           zeitgeist
Version:        1.0.4
Release:        23%{?dist}
Summary:        Framework providing Desktop activity awareness

# data/ontology/*.trig	BSD-3-Clause OR CC-BY-SA-3.0 -> main
#   Original: https://sourceforge.net/projects/oscaf/files/shared-desktop-ontologies/0.7/shared-desktop-ontologies-0.7.1.tar.bz2/
#   See: LICENSE.CC-BY in the above tarball
# data/ontology2code	 LGPL-2.0-or-later
# datahub/	 LGPL-3.0-or-later -> main
# doc/libzeitgeist/docs_vala/scripts.js	LGPL-2.0-or-later
# examples/c/	 GPL-3.0-only
# extensions/*.c	LGPL-2.0-or-later
# extensions/fts++/	GPL-2.0-or-later -> main
# libzeitgeist/		LGPL-2.0-or-later
# python/*.py	LGPL-2.0-or-later
# src/	(except for some files) LGPL-2.0-or-later
# src/notify.vala	GPL-2.0-or-later -> main
# test/c/	GPL-3.0-only
# test/	(other files) LGPL-2.0-or-later
# tools/	(except for some files) LGPL-2.0-or-later
# tools/zeitgeist-explorer/	GPL-2.0-or-later

# SPDX confirmed
License:        LGPL-2.0-or-later AND LGPL-3.0-or-later AND GPL-2.0-or-later AND (BSD-3-Clause OR CC-BY-SA-3.0)

URL:            https://launchpad.net/zeitgeist
Source0:        %{url}/1.0/%{version}/+download/%{name}-%{version}.tar.xz
# https://bugzilla.redhat.com/show_bug.cgi?id=1779103
# https://gitlab.freedesktop.org/zeitgeist/zeitgeist/issues/19
Patch1:         %{name}-1.0.4-0001-datahub-Fix-wrong-parameter-for-Event.full-ctor.patch

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-rdflib
BuildRequires:  systemd
BuildRequires:  vala
BuildRequires:  xapian-core-devel

BuildRequires:  pkgconfig(dee-icu-1.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(telepathy-glib)

BuildRequires:	/usr/bin/dbus-run-session

%{?systemd_requires}

Requires:       dbus
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      zeitgeist-datahub < 0.9.5-4
Obsoletes:      python2-%{name} < 1.0.2-1

%description
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and
makes relevant information available to other applications.
Note that this package only contains the daemon, which you can use
together with several different user interfaces.

%package -n python3-zeitgeist
Summary:        Python 3 bindings for zeitgeist
License:        LGPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

# manually specify runtime dependencies (no metadata)
Requires:       python3dist(dbus-python)

%description -n python3-zeitgeist
This package contains the Python 3 bindings for zeitgeist.

%package        libs
Summary:        Client library for interacting with the Zeitgeist daemon
License:        LGPL-2.0-or-later

%description    libs
Libzeitgeist is a client library for interacting with the Zeitgeist
daemon.

%package        devel
Summary:        Development files for %{name}
License:        LGPL-2.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Regenerate C source from vala source
find -name '*.vala' -exec touch {} \;

## nuke unwanted rpaths, see also
## https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure

# The following two are hard to get enabled...
%if 0
sed -i.disable test/direct/Makefile.in \
	-e 's|log-test\$(EXEEXT) \\|\\|'
sed -i.disable test/c/Makefile.in \
	-e 's|test-log\$(EXEEXT) \\|\\|'
%endif

# python 3.11 removes inspect.getargspec (bug 2159916)
# https://gitlab.freedesktop.org/zeitgeist/zeitgeist/-/issues/26
# https://docs.python.org/3.11/whatsnew/3.11.html#removed
sed -i.py311 python/client.py \
	-e 's|inspect.getargspec|inspect.getfullargspec|'

%build
%configure --enable-fts --enable-datahub --disable-silent-rules
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete -print

# We install AUTHORS and NEWS with %%doc instead
rm -frv %{buildroot}%{_datadir}/zeitgeist/doc

%check
cat > test-script <<EOF
#!/bin/bash
set -x

PATH_ORIG=\${PATH}
export PATH=\${PATH_ORIG}:%{buildroot}%{_bindir}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}

zeitgeist-daemon &
exec make check
EOF

chmod 0700 ./test-script
dbus-run-session -- ./test-script

%post
%systemd_user_post %{name}.service
%systemd_user_post %{name}-fts.service

%preun
%systemd_user_preun %{name}.service
%systemd_user_preun %{name}-fts.service

%ldconfig_scriptlets libs

%files
%doc AUTHORS
%doc NEWS
%license COPYING
%license COPYING.GPL

%{_bindir}/zeitgeist-daemon
%{_bindir}/zeitgeist-datahub
%dir	%{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/zeitgeist-fts

%dir	%{_datadir}/%{name}/
%dir	%{_datadir}/%{name}/ontology/
%{_datadir}/%{name}/ontology/*.trig
%{_datadir}/dbus-1/services/org.gnome.zeitgeist*.service
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/zeitgeist-daemon
%{_mandir}/man1/zeitgeist-*.*

%config(noreplace) %{_sysconfdir}/xdg/autostart/zeitgeist-datahub.desktop
%{_userunitdir}/%{name}.service
%{_userunitdir}/%{name}-fts.service

%files -n python3-zeitgeist
%{python3_sitelib}/zeitgeist/

%files libs
%license COPYING
%{_libdir}/girepository-1.0/Zeitgeist-2.0.typelib
%{_libdir}/libzeitgeist-2.0.so.*

%files devel
%{_includedir}/zeitgeist-2.0/
%{_libdir}/libzeitgeist-2.0.so
%{_libdir}/pkgconfig/zeitgeist-2.0.pc

%{_datadir}/gir-1.0/Zeitgeist-2.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/zeitgeist-2.0.deps
%{_datadir}/vala/vapi/zeitgeist-2.0.vapi
%{_datadir}/vala/vapi/zeitgeist-datamodel-2.0.vapi

%changelog
%autochangelog
