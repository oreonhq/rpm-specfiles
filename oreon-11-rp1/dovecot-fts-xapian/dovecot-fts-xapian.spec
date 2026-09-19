%global source0_hash b2ab1623d45d19f3086e8044957b1572d65659849ccc19bd6b276dac07f98df7

Name:           dovecot-fts-xapian
Version:        1.9.3
Release:        1%{?dist}
Summary:        Dovecot FTS plugin based on Xapian

# From the source code it isn't clear whether this is -only or -or-later, so
# I'm defaulting to the conservative choice here.
License:        LGPL-2.1-only
URL:            https://github.com/grosjo/fts-xapian
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  xapian-core-devel, libicu-devel, dovecot-devel, sqlite-devel, glibc-devel, libstdc++-devel
BuildRequires:  gcc, gcc-c++, make, automake, autoconf, libtool, libgcc
Requires:       dovecot

# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# dovecot does not ship i386
ExcludeArch:    %{ix86}

%description
This project intends to provide a straightforward, simple and
maintenance free, way to configure FTS plugin for Dovecot, 
leveraging the efforts by the Xapian.org team.

This effort came after Dovecot team decided to deprecate 
"fts_squat" included in the dovecot core, and due to the 
complexity of the Solr plugin capabilities, unneeded for most
users.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fts-xapian-%{version}
autoreconf -vi

%build
%configure --enable-static=no --with-dovecot=%{_libdir}/dovecot
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/dovecot/lib21_fts_xapian_plugin.la

%files
%license COPYING
%doc AUTHORS README.md
%{_libdir}/dovecot/lib21_fts_xapian_plugin.so
%{_libdir}/dovecot/settings/lib21_fts_xapian_settings.so
%{_libdir}/dovecot/settings/lib21_fts_xapian_settings.so.0
%{_libdir}/dovecot/settings/lib21_fts_xapian_settings.so.0.0.0

%changelog
%autochangelog
