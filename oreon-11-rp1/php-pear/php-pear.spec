# Fedora spec file for php-pear
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global peardir %{_datadir}/pear
%global metadir %{_localstatedir}/lib/pear

%global getoptver 1.4.3
%global arctarver 1.6.0
%global structver 1.2.0
%global xmlutil   1.4.5
%global manpages  1.10.0

# Tests are only run with rpmbuild --with tests
# Can't be run in mock / koji because PEAR is the first package
%global with_tests 0%{?_with_tests:1}

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%{!?pecl_xmldir: %global pecl_xmldir %{_sharedstatedir}/php/peclxml}

Summary: PHP Extension and Application Repository framework
Name: php-pear
Version: 1.10.18
Release: 1%{?dist}
Epoch: 1
# BSD-2-Clause: PEAR, PEAR_Manpages, Archive_Tar, Console_Getopt
# BSD-3-Clause: XML_Util
# LGPL-3.0-or-later: Structures_Graph
License: BSD-2-Clause AND BSD-3-Clause AND LGPL-3.0-or-later
URL: http://pear.php.net/package/PEAR
Source0: http://download.pear.php.net/package/PEAR-%{version}%{?pearprever}.tgz
# wget https://raw.githubusercontent.com/pear/pear-core/stable/install-pear.php
Source1: install-pear.php
Source3: cleanup.php
Source10: pear.sh
Source11: pecl.sh
Source12: peardev.sh
Source13: macros.pear
Source21: http://pear.php.net/get/Archive_Tar-%{arctarver}.tgz
Source22: http://pear.php.net/get/Console_Getopt-%{getoptver}.tgz
Source23: http://pear.php.net/get/Structures_Graph-%{structver}.tgz
Source24: http://pear.php.net/get/XML_Util-%{xmlutil}.tgz
Source25: http://pear.php.net/get/PEAR_Manpages-%{manpages}.tgz
# oreon url source checksums begin
%global source21_sha256 f856095f64bb3ffa44f870202ffca8f4e6eceef3cb74674f12be3362faafa7d3
%global source21_file Archive_Tar-1.6.0.tgz
%global source22_sha256 54bdfb7c2c958cbd7e1e8f1b964b95c3bfbf3b2779052523011b4ee49d7dfacd
%global source22_file Console_Getopt-1.4.3.tgz
%global source23_sha256 d8d8996c5d3c68119c00b0724fe20f46ae0aa7795aa71d94e6b0622315e6a9e9
%global source23_file Structures_Graph-1.2.0.tgz
%global source24_sha256 e0f8736cb47ce9dd32814de45425ff03ad55a72ba8bb757e42c456f861feedf6
%global source24_file XML_Util-1.4.5.tgz
%global source25_sha256 503cdd117028458999d62ba1d477a112714fe3f9fb53df94324205b95455a237
%global source25_file PEAR_Manpages-1.10.0.tgz
# oreon url source checksums end

BuildArch: noarch
BuildRequires: php(language) > 5.4
BuildRequires: php-cli
BuildRequires: php-xml
BuildRequires: %{_bindir}/gpg
# For pecl_xmldir macro
BuildRequires: php-devel
%if %{with_tests}
BuildRequires:  %{_bindir}/phpunit7
%endif
%if 0%{?fedora}
BuildRequires:  php-fedora-autoloader-devel
%endif

Provides: php-pear(Console_Getopt) = %{getoptver}
Provides: php-pear(Archive_Tar) = %{arctarver}
Provides: php-pear(PEAR) = %{version}
Provides: php-pear(Structures_Graph) = %{structver}
Provides: php-pear(XML_Util) = %{xmlutil}
Provides: php-pear(PEAR_Manpages) = %{manpages}

Provides: php-composer(pear/console_getopt) = %{getoptver}
Provides: php-composer(pear/archive_tar) = %{arctarver}
Provides: php-composer(pear/pear-core-minimal) = %{version}
Provides: php-composer(pear/structures_graph) = %{structver}
Provides: php-composer(pear/xml_util) = %{xmlutil}
%if 0%{?fedora}
Provides: php-autoloader(pear/console_getopt) = %{getoptver}
Provides: php-autoloader(pear/archive_tar) = %{arctarver}
Provides: php-autoloader(pear/pear-core-minimal) = %{version}
Provides: php-autoloader(pear/structures_graph) = %{structver}
Provides: php-autoloader(pear/xml_util) = %{xmlutil}
%endif

# Archive_Tar requires 5.2
# XML_Util, Structures_Graph require 5.3
# Console_Getopt requires 5.4
# PEAR requires 5.4
Requires:  php(language) > 5.4
Requires:  php-cli
# phpci detected extension
# PEAR (date, spl always builtin):
Requires:  php-ftp
Requires:  php-pcre
Requires:  php-posix
Requires:  php-tokenizer
Requires:  php-xml
Requires:  php-zlib
# Console_Getopt: pcre
# Archive_Tar: pcre, posix, zlib
Requires:  php-bz2
# Structures_Graph: none
# XML_Util: pcre
# optional: overload and xdebug
# for /var/www/html ownership
Requires: httpd-filesystem
%if 0%{?fedora}
Recommends: php-composer(fedora/autoloader)
%endif


%description
PEAR is a framework and distribution system for reusable PHP
components.  This package contains the basic PEAR components.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Archive_Tar-1.6.0.tgz; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f856095f64bb3ffa44f870202ffca8f4e6eceef3cb74674f12be3362faafa7d3" || { echo "oreon: Source21 SHA256 mismatch for Archive_Tar-1.6.0.tgz" >&2; exit 1; })
%(f=%{_sourcedir}/Console_Getopt-1.4.3.tgz; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "54bdfb7c2c958cbd7e1e8f1b964b95c3bfbf3b2779052523011b4ee49d7dfacd" || { echo "oreon: Source22 SHA256 mismatch for Console_Getopt-1.4.3.tgz" >&2; exit 1; })
%(f=%{_sourcedir}/Structures_Graph-1.2.0.tgz; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d8d8996c5d3c68119c00b0724fe20f46ae0aa7795aa71d94e6b0622315e6a9e9" || { echo "oreon: Source23 SHA256 mismatch for Structures_Graph-1.2.0.tgz" >&2; exit 1; })
%(f=%{_sourcedir}/XML_Util-1.4.5.tgz; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e0f8736cb47ce9dd32814de45425ff03ad55a72ba8bb757e42c456f861feedf6" || { echo "oreon: Source24 SHA256 mismatch for XML_Util-1.4.5.tgz" >&2; exit 1; })
%(f=%{_sourcedir}/PEAR_Manpages-1.10.0.tgz; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "503cdd117028458999d62ba1d477a112714fe3f9fb53df94324205b95455a237" || { echo "oreon: Source25 SHA256 mismatch for PEAR_Manpages-1.10.0.tgz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -cT

# Create a usable PEAR directory (used by install-pear.php)
for archive in %{SOURCE0} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25}
do
    tar xzf  $archive --strip-components 1 || tar xzf  $archive --strip-path 1
    file=${archive##*/}
    [ -f LICENSE ] && mv LICENSE LICENSE-${file%%-*}
    [ -f README ]  && mv README  README-${file%%-*}

    tar xzf $archive 'package*xml'
    [ -f package2.xml ] && mv package2.xml ${file%%-*}.xml \
                        || mv package.xml  ${file%%-*}.xml
done
cp %{SOURCE1} .

# apply patches on PEAR needed during install
# other patches applied on installation tree

sed -e 's:@BINDIR@:%{_bindir}:' \
    -e 's:@LIBDIR@:%{_localstatedir}/lib:' \
    %{SOURCE13} > macros.pear


%build
%if 0%{?fedora}
# Create per package autoloader
phpab --template fedora \
      --output PEAR/autoload.php\
      PEAR OS System.php PEAR.php

phpab --template fedora \
      --output Structures/Graph/autoload.php \
      Structures

mkdir Archive/Tar
phpab --template fedora \
      --output Archive/Tar/autoload.php \
      Archive

mkdir Console/Getopt
phpab --template fedora \
      --output Console/Getopt/autoload.php \
      Console

mkdir XML/Util
phpab --template fedora \
      --output XML/Util/autoload.php \
      XML
%endif


%install
export PHP_PEAR_SYSCONF_DIR=%{_sysconfdir}
export PHP_PEAR_SIG_KEYDIR=%{_sysconfdir}/pearkeys
export PHP_PEAR_SIG_BIN=%{_bindir}/gpg
export PHP_PEAR_INSTALL_DIR=%{peardir}

# 1.4.11 tries to write to the cache directory during installation
# so it's not possible to set a sane default via the environment.
# The ${PWD} bit will be stripped via relocate.php later.
export PHP_PEAR_CACHE_DIR=${PWD}%{_localstatedir}/cache/php-pear
export PHP_PEAR_TEMP_DIR=/var/tmp

install -d %{buildroot}%{peardir} \
           %{buildroot}%{_localstatedir}/cache/php-pear \
           %{buildroot}%{_localstatedir}/www/html \
           %{buildroot}%{_localstatedir}/lib/pear/pkgxml \
           %{buildroot}%{_sysconfdir}/pear

export INSTALL_ROOT=%{buildroot}

%{_bindir}/php --version

%{_bindir}/php -dmemory_limit=64M -dshort_open_tag=0 -dsafe_mode=0 \
         -d 'error_reporting=E_ALL&~E_DEPRECATED' -ddetect_unicode=0 \
         install-pear.php --force \
                 --dir      %{peardir} \
                 --cache    %{_localstatedir}/cache/php-pear \
                 --config   %{_sysconfdir}/pear \
                 --bin      %{_bindir} \
                 --www      %{_localstatedir}/www/html \
                 --doc      %{_docdir}/pear \
                 --test     %{_datadir}/tests/pear \
                 --data     %{_datadir}/pear-data \
                 --metadata %{metadir} \
                 --man      %{_mandir} \
                 %{SOURCE0} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25}

# Replace /usr/bin/* with simple scripts:
install -m 755 %{SOURCE10} %{buildroot}%{_bindir}/pear
install -m 755 %{SOURCE11} %{buildroot}%{_bindir}/pecl
install -m 755 %{SOURCE12} %{buildroot}%{_bindir}/peardev

# Sanitize the pear.conf
%{_bindir}/php %{SOURCE3} %{buildroot}%{_sysconfdir}/pear.conf %{_datadir}

# Display configuration for debug
%{_bindir}/php -r "print_r(unserialize(substr(file_get_contents('%{buildroot}%{_sysconfdir}/pear.conf'),17)));"


install -m 644 -D macros.pear \
           %{buildroot}%{macrosdir}/macros.pear

# apply patches on installed PEAR tree
pushd %{buildroot}%{peardir}
  : none
popd

# Why this file here ?
rm -rf %{buildroot}/.depdb* %{buildroot}/.lock %{buildroot}/.channels %{buildroot}/.filemap

# Need for re-registrying XML_Util
install -m 644 *.xml %{buildroot}%{_localstatedir}/lib/pear/pkgxml

%if 0%{?fedora}
# install autoloaders
for i in PEAR/autoload.php Structures/Graph/autoload.php Archive/Tar/autoload.php Console/Getopt/autoload.php XML/Util/autoload.php
do install -Dpm 644 $i %{buildroot}%{peardir}/$i
done
%endif


%check
# Check that no bogus paths are left in the configuration, or in
# the generated registry files.
grep %{buildroot} %{buildroot}%{_sysconfdir}/pear.conf && exit 1
grep %{_libdir} %{buildroot}%{_sysconfdir}/pear.conf && exit 1
grep '"/tmp"' %{buildroot}%{_sysconfdir}/pear.conf && exit 1
grep /usr/local %{buildroot}%{_sysconfdir}/pear.conf && exit 1
grep -rl %{buildroot} %{buildroot} && exit 1


%if %{with_tests}
cp /etc/php.ini .
echo "include_path=.:%{buildroot}%{peardir}:/usr/share/php" >>php.ini
export PHPRC=$PWD/php.ini
LOG=$PWD/rpmlog
ret=0

cd %{buildroot}%{_datadir}/tests/pear/Structures_Graph/tests
phpunit7  \
  --include-path=%{buildroot}%{_datadir}/pear \
  . || ret=1

cd %{buildroot}%{_datadir}/tests/pear/XML_Util/tests
phpunit7 \
   --bootstrap=/usr/share/pear/XML/Util/autoload.php \
   --test-suffix .php . || ret=1

cd %{buildroot}%{_datadir}/tests/pear/Console_Getopt/tests
%{_bindir}/php \
   %{buildroot}/usr/share/pear/pearcmd.php \
   run-tests \
   | tee -a $LOG

grep "FAILED TESTS" $LOG && ret=1

exit $ret
%else
echo 'Test suite disabled (missing "--with tests" option)'
%endif

# Register newly installed PECL packages
%transfiletriggerin -- %{pecl_xmldir}
while read file; do
  %{_bindir}/pecl install --nodeps --soft --force --register-only --nobuild "$file" >/dev/null || :
done

# Unregister to be removed PECL packages
# Reading the xml file to retrieve channel and package name
%transfiletriggerun -- %{pecl_xmldir}
%{_bindir}/php -r '
while ($file=fgets(STDIN)) {
  $file = trim($file);
  $xml = simplexml_load_file($file);
  if (isset($xml->channel) &&  isset($xml->name)) {
    printf("%s/%s\n", $xml->channel, $xml->name);
  } else {
    fputs(STDERR, "Bad pecl package file ($file)\n");
  }
}' | while read  name; do
  %{_bindir}/pecl uninstall --nodeps --ignore-errors --register-only "$name" >/dev/null || :
done


%postun
if [ $1 -eq 0 -a -d %{metadir}/.registry ] ; then
  rm -rf %{metadir}/.registry
fi


%files
%{peardir}
%dir %{metadir}
%{metadir}/.channels
%verify(not mtime size md5) %{metadir}/.depdb
%verify(not mtime)          %{metadir}/.depdblock
%verify(not mtime size md5) %{metadir}/.filemap
%verify(not mtime)          %{metadir}/.lock
%{metadir}/.registry
%{metadir}/pkgxml
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/pear.conf
%{macrosdir}/macros.pear
%dir %{_localstatedir}/cache/php-pear
%dir %{_sysconfdir}/pear
%license LICENSE*
%doc README*
%dir %{_docdir}/pear
%doc %{_docdir}/pear/*
%{_datadir}/tests/pear
%{_datadir}/pear-data
%{_mandir}/man1/pear.1*
%{_mandir}/man1/pecl.1*
%{_mandir}/man1/peardev.1*
%{_mandir}/man5/pear.conf.5*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.18-1
- Prepare for Oreon 11 (RP1)
