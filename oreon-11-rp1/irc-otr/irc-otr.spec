%global source0_hash 4619208b9c9171aa97a41960b3e892390b6473e2988a056b9fe8e110daa1ae9c

Name:           irc-otr
Version:        1.0.2
Release:        25%{?dist}
Summary:        Off-The-Record Messaging plugin for irssi
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/cryptodotis/irssi-otr
Source:         https://github.com/cryptodotis/irssi-otr/archive/v%{version}.tar.gz#/irssi-otr-%{version}.tar.gz

Provides:       irssi-otr = %{version}-%{release}
Obsoletes:      irssi-otr < 1.0.0-1

BuildRequires:  glib2-devel >= 2.13
BuildRequires:  irssi-devel >= 0.8.15
BuildRequires:  libotr-devel >= 4.1.0
BuildRequires:  libgcrypt-devel >= 1.5.0
BuildRequires:  pkgconfig
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires: make

%description
This provides modules which implement Off-The-Record (OTR) Messaging
for the irssi IRC client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n irssi-otr-%{version}

%build
./bootstrap
%configure --with-irssi-module-dir=%{_libdir}/irssi/modules
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT%{_libdir}/irssi/modules/libotr.so

%files
%doc README.md ChangeLog
%license LICENSE
%{_libdir}/irssi/modules/libotr.so
%{_datadir}/irssi/help/otr

%changelog
%autochangelog
