%global source0_hash 83f686fe3ea699b7e67d1c7b4f9aee4930b6b87fb2f5267a221785672d08092b
Name:           lbdb
Summary:        Address Database for mutt
Version:        0.41
Release:        23%{?dist}
License:        GPL-2.0-or-later
Url:            http://www.spinnaker.de/lbdb/
Source0:        http://www.spinnaker.de/debian/lbdb_%{version}.tar.gz
Patch0: 0001-Change-default-methods.patch
Patch1: 0002-Look-up-evolution-addressbook-export-in-libexec-rath.patch
Patch2: 0003-Fix-hostname-lookup-if-multiple-domains-are-listed-i.patch
Requires:       perl(Net::LDAP)
Requires:       perl(Getopt::Long)
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  abook
BuildRequires:  finger
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
The Little Brother's Database (lbdb) consists of a set of small tools
that collect mail addresses from several sources and offer these
addresses to the external query feature of the Mutt mail reader.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lbdb-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

%configure --libdir=%{_libexecdir}/lbdb --with-evolution-addressbook-export=auto --with-gpg=/usr/bin/gpg2
make %{?_smp_mflags}
%install
BUILD_ROOT=${RPM_BUILD_ROOT} make \
        install_prefix=${RPM_BUILD_ROOT} \
        sysconfdir=%{_sysconfdir} \
        mandir=%{_mandir} \
        libdir=%{_libexecdir}/lbdb \
        install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
