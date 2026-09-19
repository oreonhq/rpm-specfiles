%global source0_hash f4b59eef4a94b1d29dbe0c106dd00cdc630e47f18619fc754e5afbf5724ebac4

%global snapshot 0
Summary: Off-The-Record Messaging plugin for Pidgin
Name: pidgin-otr
Version: 4.0.2
Release: 23%{?dist}
Source: http://otr.cypherpunks.ca/%{name}-%{version}.tar.gz
Url: http://otr.cypherpunks.ca/
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Provides: gaim-otr = %{version}
Obsoletes: gaim-otr < 3.0.1-0.7.20060712cvs
Requires: pidgin >= 2.0.0, libotr >= 4.1.1
BuildRequires: make
BuildRequires:  gcc
BuildRequires: glib2-devel, gtk2-devel, libgcrypt-devel >= 1.2.0
BuildRequires: libgpg-error-devel, libotr-devel >= 4.0.0
BuildRequires: pidgin-devel >= 2.0.0, perl(XML::Parser), gettext
BuildRequires: intltool
%if %{snapshot}
BuildRequires: libtool automake autoconf
%endif

SOURCE1: pidgin-otr.metainfo.xml

%description 
This is a Pidgin plugin which implements Off-the-Record (OTR) Messaging.
It is known to work (at least) under the Linux and Windows versions of
Pidgin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%if %{snapshot}
aclocal
intltoolize --force --copy
autoreconf -s -i
%endif

%build

%configure 
make %{?_smp_mflags} all

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
# libtool insists on creating this
rm $RPM_BUILD_ROOT/%{_libdir}/pidgin/pidgin-otr.la
# locale
%find_lang %{name}
mkdir -p %{buildroot}/%{_datadir}/appdata/
cp -a %{SOURCE1} %{buildroot}/%{_datadir}/appdata/

%files -f %{name}.lang
%doc README COPYING
%{_libdir}/pidgin/pidgin-otr.so
%{_datadir}/appdata/pidgin-otr.metainfo.xml

%changelog
%autochangelog
