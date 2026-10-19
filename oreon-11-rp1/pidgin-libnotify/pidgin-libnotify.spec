%global source0_hash 74f4a9f20e0a483df39974178f1f2380786176189512bcd438e4ada280ec3abe
%global	pidgin_version 2.0.0
Name:		pidgin-libnotify
Version:	0.14
Release:        1%{?dist}
Summary:        Libnotify Pidgin plugin
License:	GPL-2.0-or-later
URL:		http://gaim-libnotify.sourceforge.net/
Source0:        http://downloads.sourceforge.net/gaim-libnotify/%{name}-%{version}.tar.gz
Source1:        pidgin-libnotify.metainfo.xml
Patch0:		pidgin-libnotify-fix-show-button.patch
Patch1:		pidgin-libnotify-0.14-libnotify-0.7.0.patch
Patch2:		pidgin-libnotify-german-translation-typo.patch
Requires:	pidgin >= %{pidgin_version}
Provides:	gaim-libnotify = %{version}-%{release} 
Obsoletes:	gaim-libnotify < %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
BuildRequires:  pidgin-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
