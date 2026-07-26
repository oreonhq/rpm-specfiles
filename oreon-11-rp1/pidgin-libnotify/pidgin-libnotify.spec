%global source0_hash 74f4a9f20e0a483df39974178f1f2380786176189512bcd438e4ada280ec3abe

%global	pidgin_version 2.0.0

Name:		pidgin-libnotify
Version:	0.14
Release:	39%{?dist}
Summary:	Libnotify Pidgin plugin 

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://gaim-libnotify.sourceforge.net/

Source0:	http://downloads.sourceforge.net/gaim-libnotify/%{name}-%{version}.tar.gz
Source1:        pidgin-libnotify.metainfo.xml
Patch0:		pidgin-libnotify-fix-show-button.patch
Patch1:		pidgin-libnotify-0.14-libnotify-0.7.0.patch

# Fix typo in German translation
# https://bugzilla.redhat.com/show_bug.cgi?id=654111
Patch2:		pidgin-libnotify-german-translation-typo.patch

BuildRequires: make
BuildRequires:	gettext
BuildRequires:	libnotify-devel >= 0.3.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	pidgin-devel >= %{pidgin_version}
BuildRequires:	intltool
# For AppData verification
BuildRequires:  libappstream-glib

# In order to enable aarch64 support a more recent autotools
# needs to be used to build this package
# https://bugzilla.redhat.com/show_bug.cgi?id=926114
BuildRequires:  autoconf automake libtool

Requires:	pidgin >= %{pidgin_version}

## Provides a proper upgrade path from gaim-libnotify installations.
Provides:	gaim-libnotify = %{version}-%{release} 
Obsoletes:	gaim-libnotify < %{version}-%{release}

%description
This is a plugin for the open-source Pidgin instant messaging client that uses
libnotify to display graphic notifications of new messages and other events
such as a buddy signing on or off.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n "%{name}-%{version}"

autoreconf -i --force

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p0

%build
%configure --disable-static --disable-deprecated
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/appdata/
cp -p %{SOURCE1} %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.metainfo.xml
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS TODO
%exclude %{_libdir}/purple-2/*.la
%{_libdir}/purple-2/%{name}.so
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
%autochangelog
