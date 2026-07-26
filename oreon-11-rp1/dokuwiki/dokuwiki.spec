%global source0_hash 1d10e8dc8ad769b1c56a53a8703db9345070663e8386ee6bded77d4881d090f3

Name:		dokuwiki
Summary:	Standards compliant simple to use wiki
License:	GPL-2.0-only

%global		releasenum 2025-05-14b
%global		releasetag %(rel="%{releasenum}"; echo "${rel//-/}")
Version:	%{releasetag}
Release:	4%{?dist}

%global php_min_version 7.4

URL:		https://www.dokuwiki.org/dokuwiki
Source0:	https://download.dokuwiki.org/src/%{name}/%{name}-%{releasenum}.tgz

#Fedora specific patches to use Fedora packaged libraries
Patch1:		dokuwiki-rm-bundled-libs.patch

BuildArch:	noarch

%global smoke_test 1
%define depends_on(v::) %{expand:
BuildRequires: %{*}

%if 0%{?smoke_test}
Requires: %{*}
%endif
}

%if 0%{?smoke_test}
BuildRequires: php-cli >= %{php_min_version}
%endif

%depends_on php-gd >= %{php_min_version}
%depends_on php-json >= %{php_min_version}
%depends_on php-xml >= %{php_min_version}

# Composer deps
%depends_on php-composer(aziraphale/email-address-validator) >= 2.0.1
%depends_on php-composer(kissifrot/php-ixr) >= 1.8.4
%depends_on php-composer(geshi/geshi) >= 1.0.9.1
%depends_on php-composer(openpsa/universalfeedcreator) >= 1.8.6
%depends_on php-composer(paragonie/constant_time_encoding) >= 2.6.3
%depends_on php-composer(php81_bc/strftime) >= 0.7.6
%depends_on php-composer(phpseclib/phpseclib) >= 3.0.35
# %%depends_on php-composer(simplepie/simplepie) >= 1.8.0
%depends_on php-composer(splitbrain/lesserphp) >= 0.10.0
%depends_on php-composer(splitbrain/php-archive) >= 1.3.1
%depends_on php-composer(splitbrain/php-cli) >= 1.3.1
%depends_on php-composer(splitbrain/php-jsstrip) >= 1.0.1
%depends_on php-composer(splitbrain/slika) >= 1.0.6

# Deps that require extra handling

# Fedora's simplepie package was unfortunately broken for some time
%depends_on php-simplepie >= 1.9.0-2

%description
DokuWiki is a standards compliant, simple to use Wiki, mainly aimed at creating
documentation of any kind. It has a simple but powerful syntax which makes sure
the data-files remain readable outside the Wiki and eases the creation of
structured texts.

All data is stored in plain text files no database is required.

%package selinux
Summary:	SELinux support for dokuwiki
Requires:	%name = %version-%release
Requires:	%{_sbindir}/semanage
Requires:	%{_sbindir}/restorecon
BuildArch:	noarch

%description selinux
Configures DokuWiki to run in SELinux enabled environments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{releasenum}

# Remove bundled code that's available as Fedora packages
#  email-address-validator
rm -r vendor/aziraphale/email-address-validator
rmdir vendor/aziraphale || true
#  geshi
rm -r vendor/geshi/geshi
rmdir vendor/geshi || true
#  kissifrot/php-ixr
rm -r vendor/kissifrot/php-ixr
rmdir vendor/kissifrot || true
#  universalfeedcreator
rm -r vendor/openpsa/universalfeedcreator
rmdir vendor/openpsa || true
#  paragonie
rm -r vendor/paragonie/constant_time_encoding
rm -r vendor/paragonie/random_compat
rmdir vendor/paragonie || true
#  php81bc/strftime
rm -r vendor/php81_bc/strftime
rmdir vendor/php81_bc || true
#  phpseclib
rm -r vendor/phpseclib/phpseclib
rmdir vendor/phpseclib || true
#  simplepie
rm -r vendor/simplepie/simplepie
rmdir vendor/simplepie || true
#  splitbrain/php-archive, splitbrain/php-cli, splitbrain/slika, splitbrain/php-jsstrip, splitbrain/lesserphp
rm -r vendor/splitbrain/php-archive
rm -r vendor/splitbrain/php-cli
rm -r vendor/splitbrain/slika
rm -r vendor/splitbrain/php-jsstrip
rm -r vendor/splitbrain/lesserphp
rmdir vendor/splitbrain || true

%patch -P1 -p1 -b .bundled

mv -f conf/mysql.conf.php.example .

sed -i "s:'./data':'%{_localstatedir}/lib/%{name}/data':" conf/%{name}.php
sed -i "s:ALL        8:ALL        1:" conf/acl.auth.php.dist

cat <<EOF >%{name}.httpd

Alias /%{name} %{_datadir}/%{name}

<Directory %{_datadir}/%{name}>
	<IfModule mod_authz_core.c>
		# Apache 2.4
		Require local
	</IfModule>
	<IfModule !mod_authz_core.c>
		# Apache 2.2
		Options +FollowSymLinks
		Order Allow,Deny
		Allow from 127.0.0.1 ::1
	</IfModule>
</Directory>

<Directory %{_datadir}/%{name}/bin>
	Order Deny,Allow
	Deny from all
</Directory>

<Directory %{_datadir}/%{name}/conf>
	Order Deny,Allow
	Deny from all
</Directory>

<Directory %{_datadir}/%{name}/inc>
	Order Deny,Allow
	Deny from all
</Directory>

<Directory %{_datadir}/%{name}/vendor>
	Order Deny,Allow
	Deny from all
</Directory>

EOF

cat <<EOF >DOKUWIKI-SELINUX.README
%{name}-selinux
====================

This package configures dokuwiki to run in
SELinux enabled environments

EOF

%build
# nothing to do here

%install
install -d -p %{buildroot}%{_sysconfdir}/%{name}
install -d -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -d -p %{buildroot}%{_datadir}/%{name}
install -d -p %{buildroot}%{_datadir}/%{name}/bin
install -d -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/data/{attic,cache,index,locks,log,media,media_attic,media_meta,meta,pages,tmp}
rm -f install.php
rm -f inc/.htaccess
rm -f inc/lang/.htaccess
rm -f vendor/.htaccess
cp -rp data/pages/* %{buildroot}%{_localstatedir}/lib/%{name}/data/pages/
cp -rp conf/* %{buildroot}%{_sysconfdir}/%{name}
cp -rp bin/*  %{buildroot}%{_datadir}/%{name}/bin
cp -rp lib  %{buildroot}%{_datadir}/%{name}/
cp -rp inc  %{buildroot}%{_datadir}/%{name}/
cp -rp vendor  %{buildroot}%{_datadir}/%{name}/
install -p -m0644 *.php %{buildroot}%{_datadir}/%{name}
install -p -m0644 %{name}.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

pushd %{buildroot}%{_sysconfdir}/%{name}
for d in *.dist; do
	d0=`basename $d .dist`
	if [ ! -f "$d0" ]; then
		mv -f $d $d0
	fi
done
popd

pushd %{buildroot}%{_datadir}/%{name}
	ln -sf ../../../etc/%name conf
popd

# Smoke test. Runs the index page script in CLI.
# Should catch some missing or improperly patched dependencies.
%if 0%{?smoke_test}
%check
cat > %{buildroot}%{_datadir}/%{name}/conf/local.php <<'EOF'
<?php
$conf['savedir'] = "%{buildroot}%{_localstatedir}/lib/%{name}/data";
EOF

php %{buildroot}%{_datadir}/%{name}/index.php

rm -f \
	%{buildroot}%{_localstatedir}/lib/%{name}/data/index/page.idx \
	%{buildroot}%{_datadir}/%{name}/conf/local.php
%endif

%post selinux
semanage fcontext -a -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -a -t httpd_sys_content_t '%{_datadir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -a -t httpd_sys_rw_content_t '%{_datadir}/%{name}/lib/plugins(/.*)?' 2>/dev/null || :
restorecon -R '%{_sysconfdir}/%{name}' || :
restorecon -R '%{_datadir}/%{name}' || :

%postun selinux
if [ $1 -eq 0 ] ; then
semanage fcontext -d -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -d -t httpd_sys_content_t '%{_datadir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -d -t httpd_sys_rw_content_t '%{_datadir}/%{name}/lib/plugins(/.*)?' 2>/dev/null || :
fi

%files
%doc COPYING README VERSION mysql.conf.php.example
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %attr(0644,apache,apache) %{_sysconfdir}/%{name}/*
%dir %attr(0755,apache,apache) %{_sysconfdir}/%{name}
%attr(0755,apache,apache) %{_datadir}/%{name}/bin/*.php
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/*.php
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/exe
%{_datadir}/%{name}/lib/images
%{_datadir}/%{name}/lib/index.html
%{_datadir}/%{name}/lib/scripts
%{_datadir}/%{name}/lib/styles
%{_datadir}/%{name}/lib/tpl
%attr(0755,apache,apache) %dir %{_datadir}/%{name}/lib/plugins
%{_datadir}/%{name}/lib/plugins/*
%{_datadir}/%{name}/inc
%{_datadir}/%{name}/vendor
%dir %{_localstatedir}/lib/%{name}
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/attic
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/cache
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/index
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/locks
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/log
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/media
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/media_attic
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/media_meta
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/meta
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/pages
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/pages/wiki
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/tmp
%{_localstatedir}/lib/%{name}/data/pages/*/*

%files selinux
%doc DOKUWIKI-SELINUX.README

%changelog
%autochangelog
