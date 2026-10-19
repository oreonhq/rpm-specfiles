%global source0_hash 276db000b4e0a9388c7f5168522174bae4144c8c411a71d480b82ec25ee3bc8b
%global source21_hash f856095f64bb3ffa44f870202ffca8f4e6eceef3cb74674f12be3362faafa7d3
%global source22_hash 54bdfb7c2c958cbd7e1e8f1b964b95c3bfbf3b2779052523011b4ee49d7dfacd
%global source23_hash d8d8996c5d3c68119c00b0724fe20f46ae0aa7795aa71d94e6b0622315e6a9e9
%global source24_hash e0f8736cb47ce9dd32814de45425ff03ad55a72ba8bb757e42c456f861feedf6
%global source25_hash 503cdd117028458999d62ba1d477a112714fe3f9fb53df94324205b95455a237
%global peardir %{_datadir}/pear
%global metadir %{_localstatedir}/lib/pear
%global getoptver 1.4.3
%global arctarver 1.6.0
%global structver 1.2.0
%global xmlutil   1.4.5
%global manpages  1.10.0
%global with_tests 0%{?_with_tests:1}
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%{!?pecl_xmldir: %global pecl_xmldir %{_sharedstatedir}/php/peclxml}
Summary:        PHP Extension and Application Repository framework
Name: php-pear
Version: 1.10.18
Release:        1%{?dist}
Epoch: 1
License: BSD-2-Clause AND BSD-3-Clause AND LGPL-3.0-or-later
URL: http://pear.php.net/package/PEAR
Source0:        https://download.pear.php.net/package/PEAR-%{version}.tgz
Source1: install-pear.php
Source3: cleanup.php
Source10: pear.sh
Source11: pecl.sh
Source12: peardev.sh
Source13: macros.pear
Source21:        https://pear.php.net/get/Archive_Tar-1.6.0.tgz
Source22:        https://pear.php.net/get/Console_Getopt-1.4.3.tgz
Source23:        https://pear.php.net/get/Structures_Graph-1.2.0.tgz
Source24:        https://pear.php.net/get/XML_Util-1.4.5.tgz
Source25:        https://pear.php.net/get/PEAR_Manpages-1.10.0.tgz
BuildArch: noarch
%if %{with_tests}
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
Requires:  php(language) > 5.4
Requires:  php-cli
Requires:  php-ftp
Requires:  php-pcre
Requires:  php-posix
Requires:  php-tokenizer
Requires:  php-xml
Requires:  php-zlib
Requires:  php-bz2
Requires: httpd-filesystem
# oreon:deps
BuildRequires:  /usr/bin/gpg
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-devel
BuildRequires:  php-xml
# /oreon:deps
%description
PEAR is a framework and distribution system for reusable PHP
components.  This package contains the basic PEAR components.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source21_hash}" = "none" || { f="%{SOURCE21}"; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source21_hash}" || { echo "oreon: Source21 hash mismatch" >&2; exit 1; }; }
test "%{source22_hash}" = "none" || { f="%{SOURCE22}"; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source22_hash}" || { echo "oreon: Source22 hash mismatch" >&2; exit 1; }; }
test "%{source23_hash}" = "none" || { f="%{SOURCE23}"; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source23_hash}" || { echo "oreon: Source23 hash mismatch" >&2; exit 1; }; }
test "%{source24_hash}" = "none" || { f="%{SOURCE24}"; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source24_hash}" || { echo "oreon: Source24 hash mismatch" >&2; exit 1; }; }
test "%{source25_hash}" = "none" || { f="%{SOURCE25}"; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source25_hash}" || { echo "oreon: Source25 hash mismatch" >&2; exit 1; }; }
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

%install
export PHP_PEAR_SYSCONF_DIR=%{_sysconfdir}
export PHP_PEAR_SIG_KEYDIR=%{_sysconfdir}/pearkeys
export PHP_PEAR_SIG_BIN=%{_bindir}/gpg
export PHP_PEAR_INSTALL_DIR=%{peardir}
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
install -m 755 %{SOURCE10} %{buildroot}%{_bindir}/pear
install -m 755 %{SOURCE11} %{buildroot}%{_bindir}/pecl
install -m 755 %{SOURCE12} %{buildroot}%{_bindir}/peardev
%{_bindir}/php %{SOURCE3} %{buildroot}%{_sysconfdir}/pear.conf %{_datadir}
%{_bindir}/php -r "print_r(unserialize(substr(file_get_contents('%{buildroot}%{_sysconfdir}/pear.conf'),17)));"
install -m 644 -D macros.pear \
           %{buildroot}%{macrosdir}/macros.pear
pushd %{buildroot}%{peardir}
  : none
popd
rm -rf %{buildroot}/.depdb* %{buildroot}/.lock %{buildroot}/.channels %{buildroot}/.filemap
install -m 644 *.xml %{buildroot}%{_localstatedir}/lib/pear/pkgxml
%oreon_autofiles main

%check

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
%transfiletriggerin -- %{pecl_xmldir}
while read file; do
  %{_bindir}/pecl install --nodeps --soft --force --register-only --nobuild "$file" >/dev/null || :
done
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
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.18-1
- Prepare for Oreon 11 (RP1)
