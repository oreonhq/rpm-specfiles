%global source0_hash f4b59eef4a94b1d29dbe0c106dd00cdc630e47f18619fc754e5afbf5724ebac4
%global snapshot 0
Summary:        Off-The-Record Messaging plugin for Pidgin
Name: pidgin-otr
Version: 4.0.2
Release:        23%{?dist}
Source0:        http://otr.cypherpunks.ca/%{name}-%{version}.tar.gz
Url: http://otr.cypherpunks.ca/
License: GPL-2.0-only
Provides: gaim-otr = %{version}
Obsoletes: gaim-otr < 3.0.1-0.7.20060712cvs
Requires: pidgin >= 2.0.0, libotr >= 4.1.1
SOURCE1: pidgin-otr.metainfo.xml
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libotr-devel
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
BuildRequires:  pidgin-devel
# /oreon:deps
%description 
This is a Pidgin plugin which implements Off-the-Record (OTR) Messaging.
It is known to work (at least) under the Linux and Windows versions of
Pidgin.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure 
make %{?_smp_mflags} all
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT/%{_libdir}/pidgin/pidgin-otr.la
%find_lang %{name}
mkdir -p %{buildroot}/%{_datadir}/appdata/
cp -a %{SOURCE1} %{buildroot}/%{_datadir}/appdata/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
