%global source0_hash c3b0900bc539f91e9dfa3fd621a219dd7b44884f2c4b212d84fa98b13262e4cf

%bcond_with nis

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 6
%define ldap_impl openldap
%else
%define ldap_impl mozldap
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 6
%define betxn_opts --enable-be-txns-by-default
%else
%define betxn_opts --disable-be-txns-by-default
%endif

Name:		slapi-nis
Version:	0.70.0
Release:	7%{?dist}
Summary:	Schema Compatibility plugins for Directory Server
License:	GPL-3.0-or-later
URL:		http://pagure.io/slapi-nis/
Source0:        https://releases.pagure.org/slapi-nis/slapi-nis-%{version}.tar.gz
Source1:        https://releases.pagure.org/slapi-nis/slapi-nis-%{version}.tar.gz.asc
Patch0:		slapi-nis-eq_once_rel.patch
Patch1:         slapi-nis-rhbz2341357-fix.patch

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:	389-ds-base-devel >= 1.3.5.6, %{ldap_impl}-devel
BuildRequires:	nspr-devel, nss-devel, /usr/bin/rpcgen
%if 0%{?fedora} > 18 || 0%{?rhel} > 6
BuildRequires:	libsss_nss_idmap-devel > 1.16.0-5
%define sss_nss_opts --with-sss-nss-idmap --with-idviews
%else
%define sss_nss_opts %{nil}
%endif
BuildRequires:	pam-devel
%if %{with nis}
%if (0%{?fedora} > 14 && 0%{?fedora} < 28) || (0%{?rhel} > 6 && 0%{?rhel} < 8)
BuildRequires:	libtirpc-devel
%else
BuildRequires:  libnsl2-devel
%endif
%endif
%if 0%{?fedora} > 27 || 0%{?rhel} >= 9
ExcludeArch: %{ix86}
%endif
Requires: 389-ds-base >= 1.3.5.6

%description
This package provides two plugins for Red Hat and 389 Directory Server.

The NIS Server plugin allows the directory server to act as a NIS server
for clients, dynamically generating and updating NIS maps according to
its configuration and the contents of the DIT, and serving the results to
clients using the NIS protocol as if it were an ordinary NIS server.

The Schema Compatibility plugin allows the directory server to provide an
alternate view of entries stored in part of the DIT, optionally adding,
dropping, or renaming attribute values, and optionally retrieving values
for attributes from multiple entries in the tree.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -p1 -P0
%patch -p1 -P1

%build
autoconf --force
%if %{with nis}
WITH_NIS=--enable-nis=yes
%else
WITH_NIS=--disable-nis
%endif
%configure --disable-static --with-ldap=%{ldap_impl} \
	--with-nsswitch --with-pam --with-pam-service=system-auth \
	%{sss_nss_opts} %{betxn_opts} \
	$WITH_NIS
sed -i -e 's,%{_libdir}/dirsrv/plugins/,,g' -e 's,.so$,,g' doc/examples/*.ldif
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/%{_libdir}/dirsrv/plugins/*.la

%if 0
# ns-slapd doesn't want to start in koji, so no tests get run
%check
make check
%endif

%files
%doc COPYING NEWS README STATUS doc/sch-*.txt doc/examples/sch-*.ldif doc/ipa
%if %{with nis}
%doc doc/nis-*.txt doc/examples/nis-*.ldif
%{_mandir}/man1/*
%{_sbindir}/nisserver-plugin-defs
%endif
%{_libdir}/dirsrv/plugins/*.so

%triggerin -- 389-ds-base
instances=$(/usr/sbin/dsctl -l)
for inst in $instances ; do
    grep -q "cn=NIS server,cn=plugins" /etc/dirsrv/${inst}/dse.ldif
    if test $? -eq 0 ; then
	    /usr/bin/ldapdelete -Y EXTERNAL -H ldapi://%2fvar%2frun%2f${inst}.socket -r "cn=NIS Server,cn=plugins,cn=config" 2>/dev/null
	    result=$?
	    if test $result -eq 255 ; then
		echo "Cannot remove NIS server plugin from LDAP server ${inst} instance. Server will fail to start until it is removed."
		echo "Remove 'cn=NIS Server,cn=plugins,cn=config' entry from /etc/dirsrv/${inst}/dse.ldif"
	    fi
	    if test $result -eq 0 ; then
		/usr/sbin/dsctl "$inst" restart
	    fi
    fi
done


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.70.0-7
- Prepare for Oreon 11 (RP1)
