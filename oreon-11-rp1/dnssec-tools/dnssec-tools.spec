%global source0_hash c12fe51a94607f3ae340a8f72aa5deb8a846edb3b15e78dbaa3c5ddffca58911

# OpenSSL ENGINE support deprecated in Fedora 41 onwards
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
%if 0%{?fedora} > 40
%global _preprocessor_defines %{?_preprocessor_defines} -DOPENSSL_NO_ENGINE
%endif

Summary: A suite of tools for managing dnssec aware DNS usage
Name: dnssec-tools
Version: 2.2.3
Release: 32%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://www.dnssec-tools.org/
#Source0: https://www.dnssec-tools.org/download/%%{name}-%%{version}.tar.gz
Source0: https://www.hardakers.net/software/%{name}-%{version}.tar.gz
Source1: dnssec-tools-dnsval.conf
Source2: libval-config
# Require note: the auto-detection for perl-Net-DNS-SEC will not work since
# the tools do run time tests for their existence.  But most of the tools
# are much more useful with the modules in place, so we hand require them.
Requires: dnssec-tools-perlmods, bind, perl(Getopt::GUI::Long)
Requires: perl(GraphViz)
BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(Test) perl(ExtUtils::MakeMaker)
BuildRequires: make
# Makes the code installation linux filesystem friendly
Patch5: dnssec-tools-linux-conf-paths-1.13.patch
Patch13: dnssec-tools-2.0-autoconf-for-aarch64.patch
Patch17: dnssec-tools-new-2017-key.patch
Patch18: dnssec-tools-new-openssl-APIs.patch
# Update Makefile to respect users LDFLAGS
# https://github.com/DNSSEC-Tools/DNSSEC-Tools/commit/7287c6b96422e499560fb10b95c1a481ea82656d
Patch19: 7287c6b96422e499560fb10b95c1a481ea82656d.patch
# link libval-threads with libs
Patch20: dnssec-tools-2.2.3-link-libval-threads-with-libs.patch
Patch21: dnssec-tools-2.2.3-add_ifdedf_to_engine.patch

%description

The goal of the DNSSEC-Tools project is to create a set of tools,
patches, applications, wrappers, extensions, and plugins that will
help ease the deployment of DNSSEC-related technologies.

%package perlmods
Summary: Perl modules supporting DNSSEC (needed by the dnssec-tools)
Requires: perl(Getopt::GUI::Long)

%description perlmods

The dnssec-tools project comes with a number of perl modules that are
required by the DNSSEC tools themselves as well as modules that are
useful for other developers.

%package libs
Summary: C-based libraries for dnssec aware tools
Requires: openssl

%description libs
C-based libraries useful for developing dnssec aware tools.

%package libs-devel
Summary: C-based development libraries for dnssec aware tools
Requires: dnssec-tools-libs = %{version}-%{release}

%description libs-devel
C-based libraries useful for developing dnssec aware tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P5 -p0 
#%%patch6 -p2
#%%patch12 -p2
#%%patch13 -p2
#%%patch14 -p2
#%%patch15 -p2
#%%patch16 -p2
#%%patch17 -p2
#%%patch18 -p2
%patch -P19 -p2
%patch -P20 -p1 -b .link-with-libs
%patch -P21 -p1

%build
%configure --with-validator-testcases-file=%{_datadir}/dnssec-tools/validator-testcases --with-perl-build-args="INSTALLDIRS=vendor OPTIMIZE='$RPM_OPT_FLAGS'" --sysconfdir=/etc --with-root-hints=/etc/dnssec-tools/root.hints --with-resolv-conf=/etc/dnssec-tools/resolv.conf --disable-static --with-nsec3 --with-ipv6 --with-dlv --disable-bind-checks
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' validator/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' validator/libtool
# makefile dependencies are broken; we can't use smp_mflags:
#make %%{?_smp_mflags} CCFLAGS="-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"
make CCFLAGS="-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

%install
rm -rf %{buildroot}
make install DESTCONFDIR=%{buildroot}/etc/dnssec-tools/ DESTDIR=%{buildroot} QUIET=

%{__install} -m 644 %{SOURCE1} %{buildroot}/etc/dnssec-tools/dnsval.conf
%{__install} -m 644 validator/etc/root.hints %{buildroot}/etc/dnssec-tools/root.hints

# remove unneeded perl install files
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
# remove empty directories
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*
rm -f %{buildroot}%{_libdir}/*.la

# Move the architecture dependent config file to its own place
# (this allows multiple architecture rpms to be installed at the same time)
mv ${RPM_BUILD_ROOT}/%{_bindir}/libval-config ${RPM_BUILD_ROOT}/%{_bindir}/libval-config-%{_arch}
# Add a new wrapper script that calls the right file at run time
install -m 755 %SOURCE2 ${RPM_BUILD_ROOT}/%{_bindir}/libval-config

%ldconfig_scriptlets libs

%files
%doc README.md INSTALL COPYING

%dir %{_sysconfdir}/dnssec-tools/
%config(noreplace) %{_sysconfdir}/dnssec-tools/dnssec-tools.conf

%{_bindir}/dnspktflow
%{_bindir}/donuts
%{_bindir}/donutsd
%{_bindir}/drawvalmap
%{_bindir}/expchk
%{_bindir}/genkrf
%{_bindir}/getdnskeys
%{_bindir}/getds
%{_bindir}/lskrf
%{_bindir}/maketestzone
%{_bindir}/mapper
%{_bindir}/zonesigner
# this doesn't use %%{_datadir} because patch6 above uses this exact path
/usr/share/dnssec-tools
#/usr/share/dnssec-tools/donuts
#/usr/share/dnssec-tools/donuts/rules
#/usr/share/dnssec-tools/donuts/rules/*

%{_bindir}/dtck
%{_bindir}/dtconfchk
%{_bindir}/dtconf
%{_bindir}/dtdefs
%{_bindir}/dtinitconf
%{_bindir}/fixkrf
%{_bindir}/tachk
%{_bindir}/timetrans

%{_bindir}/lsroll
%{_bindir}/rollchk
%{_bindir}/rollctl
%{_bindir}/rollerd
%{_bindir}/rollinit
%{_bindir}/rollset
%{_bindir}/keyarch
%{_bindir}/cleanarch

%{_bindir}/dt-libval_check_conf
%{_bindir}/dt-validate
# configure above 
#%%{_datadir}/dnssec-tools/validator-testcases
%{_bindir}/dt-getaddr
%{_bindir}/dt-gethost
%{_bindir}/dt-getname
%{_bindir}/dt-getquery
%{_bindir}/dt-getrrset
%{_bindir}/dt-danechk

%{_bindir}/trustman
%{_bindir}/blinkenlights
%{_bindir}/lights
%{_bindir}/cleankrf
%{_bindir}/krfcheck
%{_bindir}/rolllog
%{_bindir}/signset-editor
%{_bindir}/rollrec-editor

# new in 1.13
%{_bindir}/buildrealms
%{_bindir}/check-zone-expiration
%{_bindir}/dtrealms
%{_bindir}/grandvizier
%{_bindir}/keymod
%{_bindir}/lsrealm
%{_bindir}/realmchk
%{_bindir}/realmctl
%{_bindir}/realminit
%{_bindir}/realmset

%{_bindir}/lsdnssec

%{_bindir}/bubbles
%{_bindir}/convertar

%{_mandir}/man1/dnssec-tools.1.gz
%{_mandir}/man1/dnspktflow.1.gz
%{_mandir}/man1/donuts.1.gz
%{_mandir}/man1/donutsd.1.gz
%{_mandir}/man1/drawvalmap.1.gz
%{_mandir}/man1/expchk.1.gz
%{_mandir}/man1/genkrf.1.gz
%{_mandir}/man1/getdnskeys.1.gz
%{_mandir}/man1/getds.1.gz
%{_mandir}/man1/lskrf.1.gz
%{_mandir}/man1/keyarch.1.gz
%{_mandir}/man1/maketestzone.1.gz
%{_mandir}/man1/mapper.1.gz
%{_mandir}/man1/zonesigner.1.gz
%{_mandir}/man1/dt-validate.1.gz
%{_mandir}/man1/dt-getaddr.1.gz
%{_mandir}/man1/dt-gethost.1.gz
%{_mandir}/man1/dt-getname.1.gz
%{_mandir}/man1/dt-getquery.1.gz
%{_mandir}/man1/dt-getrrset.1.gz

%{_mandir}/man1/dtconfchk.1.gz
%{_mandir}/man1/dtdefs.1.gz
%{_mandir}/man1/dtinitconf.1.gz
%{_mandir}/man1/fixkrf.1.gz
%{_mandir}/man1/tachk.1.gz
%{_mandir}/man1/timetrans.1.gz

%{_mandir}/man1/bubbles.1.gz
%{_mandir}/man1/convertar.1.gz

%{_mandir}/man1/lsroll.1.gz
%{_mandir}/man1/rollchk.1.gz
%{_mandir}/man1/rollctl.1.gz
%{_mandir}/man1/rollerd.1.gz
%{_mandir}/man1/rollinit.1.gz
%{_mandir}/man1/rollset.1.gz
%{_mandir}/man1/lsdnssec.1.gz
%{_mandir}/man1/cleanarch.1.gz
%{_mandir}/man1/blinkenlights.1.gz
%{_mandir}/man1/lights.1.gz
%{_mandir}/man1/cleankrf.1.gz
%{_mandir}/man1/krfcheck.1.gz
%{_mandir}/man1/rolllog.1.gz
%{_mandir}/man1/signset-editor.1.gz
%{_mandir}/man1/trustman.1.gz
%{_mandir}/man1/dtck.1.gz
%{_mandir}/man1/dtconf.1.gz
%{_mandir}/man1/rollrec-editor.1.gz
%{_mandir}/man3/p_ac_status.3.gz
%{_mandir}/man3/p_val_status.3.gz

# new in 1.13
%{_mandir}/man1/buildrealms.1.gz
%{_mandir}/man1/check-zone-expiration.1.gz
%{_mandir}/man1/dt-libval_check_conf.1.gz
%{_mandir}/man1/dtrealms.1.gz
%{_mandir}/man1/grandvizier.1.gz
%{_mandir}/man1/keymod.1.gz
%{_mandir}/man1/lsrealm.1.gz
%{_mandir}/man1/realmchk.1.gz
%{_mandir}/man1/realmctl.1.gz
%{_mandir}/man1/realminit.1.gz
%{_mandir}/man1/realmset.1.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::realm.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::realmmgr.3pm.gz

%files perlmods
# perl-Net-DNS-SEC is noarch and cannot own this directory:
%dir %{perl_vendorarch}/Net/DNS/SEC

%{perl_vendorarch}/Net/DNS/SEC/Tools
%{perl_vendorarch}/Net/addrinfo*
%{perl_vendorarch}/Net/DNS/SEC/*.pm
%{perl_vendorarch}/Net/DNS/SEC/*.pl
%{perl_vendorarch}/auto/Net/DNS/SEC/Validator
%{perl_vendorarch}/auto/Net/addrinfo/
%{perl_vendorarch}/Net/DNS/ZoneFile/
%{perl_vendorlib}/Net/DNS/SEC/Tools/

%{_mandir}/man3/Net::DNS::SEC::Tools::QWPrimitives.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::BootStrap.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::conf.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::keyrec.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::rollmgr.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::rollrec.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::defaults.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::timetrans.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::tooloptions.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::dnssectools.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Validator.3pm.gz
%{_mandir}/man3/Net::addrinfo.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::Donuts::Rule.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::rolllog.3pm.gz

%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Bind.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Csv.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Dns.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Dump.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Itar.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Libval.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Mf.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Secspider.3pm.gz

# obsolete module still in upstream source:
%{_mandir}/man3/Net::DNS::ZoneFile::Fast.3pm.gz

%files libs
%{_libdir}/*.so.*
%config(noreplace) %{_sysconfdir}/dnssec-tools
#%%config(noreplace) %%{_sysconfdir}/dnssec-tools/dnsval.conf
#%%config(noreplace) %%{_sysconfdir}/dnssec-tools/root.hints

%files libs-devel
%{_includedir}/validator
%{_libdir}/*.so

%{_bindir}/libval-config*

%{_mandir}/man3/libval.3.gz
%{_mandir}/man3/libval_shim.3.gz
%{_mandir}/man3/val_free_answer_chain.3.gz
%{_mandir}/man3/val_get_rrset.3.gz
%{_mandir}/man3/val_getaddrinfo.3.gz
%{_mandir}/man3/val_gethostbyname.3.gz
%{_mandir}/man3/dnsval.conf.3.gz
%{_mandir}/man3/dnsval_conf_get.3.gz
%{_mandir}/man3/dnsval_conf_set.3.gz
%{_mandir}/man3/libsres.3.gz
%{_mandir}/man3/root_hints_get.3.gz
%{_mandir}/man3/root_hints_set.3.gz
%{_mandir}/man3/resolv_conf_get.3.gz
%{_mandir}/man3/resolv_conf_set.3.gz
%{_mandir}/man3/val_create_context.3.gz
%{_mandir}/man3/val_free_context.3.gz
%{_mandir}/man3/val_free_result_chain.3.gz
%{_mandir}/man3/val_istrusted.3.gz
%{_mandir}/man3/val_resolve_and_check.3.gz
%{_mandir}/man3/val_gethostbyaddr.3.gz
%{_mandir}/man3/val_gethostbyaddr_r.3.gz
%{_mandir}/man3/val_gethostbyname2.3.gz
%{_mandir}/man3/val_gethostbyname2_r.3.gz
%{_mandir}/man3/val_gethostbyname_r.3.gz
%{_mandir}/man3/val_getnameinfo.3.gz
%{_mandir}/man3/val_isvalidated.3.gz
%{_mandir}/man3/val_res_query.3.gz
%{_mandir}/man3/val_res_search.3.gz
#%%{_mandir}/man3/val_addrinfo.3.gz
%{_mandir}/man3/val_add_valpolicy.3.gz
%{_mandir}/man3/val_context_setqflags.3.gz
%{_mandir}/man3/val_does_not_exist.3.gz
%{_mandir}/man3/val_free_response.3.gz
%{_mandir}/man3/val_freeaddrinfo.3.gz

# new in 2.1
%{_mandir}/man1/dt-danechk.1.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::Donuts.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::examples.3pm.gz
%{_mandir}/man3/libval_async.3.gz
%{_mandir}/man3/p_dane_error.3.gz
%{_mandir}/man3/val_async_cancel.3.gz
%{_mandir}/man3/val_async_cancel_all.3.gz
%{_mandir}/man3/val_async_check_wait.3.gz
%{_mandir}/man3/val_async_select_info.3.gz
%{_mandir}/man3/val_async_submit.3.gz
%{_mandir}/man3/val_dane_check.3.gz
%{_mandir}/man3/val_dane_match.3.gz
%{_mandir}/man3/val_dane_submit.3.gz
%{_mandir}/man3/val_free_dane.3.gz
%{_mandir}/man3/val_getdaneinfo.3.gz

%changelog
%autochangelog
