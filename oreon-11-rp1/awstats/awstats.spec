%global source0_hash 3ef76ff96c5398477dd8a11134e266e538a487067f6906a3ac8a38bfd11c11e0

Name:       awstats
Version:    8.0
Release:    3%{?dist}
Summary:    Advanced Web Statistics
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
URL:        https://www.awstats.org/
Source0:    https://downloads.sourceforge.net/project/awstats/AWStats/%{version}/awstats-%{version}.tar.gz
Source1:    %{name}.cron
Patch0:     awstats-awredir.pl-sanitize-parameters.patch

# fix configuration for httpd 2.4 (#871366)
Patch1:     awstats-7.9-httpd-2.4.patch

BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  recode
Requires:   perl-Net-IP, perl-Net-DNS, perl-Geo-IP
Requires:   crontabs  
Requires(post): perl-interpreter

# For systemd.macros
BuildRequires:  systemd
Requires(postun): systemd

## SELinux policy is now included upstream
Obsoletes:  awstats-selinux < 6.8-1
Provides:   awstats-selinux = %{version}-%{release}

%description
Advanced Web Statistics is a powerful and full-featured tool that generates
advanced web server graphical statistics. This server log analyzer works
from the command line or as a CGI and shows all information your log contains,
in graphical web pages. It can analyze a lot of web/wap/proxy servers such as
Apache, IIS, Weblogic, Webstar, Squid, ... but also mail or FTP servers.

This program can measure visits, unique visitors, authenticated users, pages,
domains/countries, OS busiest times, robot visits, type of files, search
engines/keywords used, visit duration, HTTP errors and more...
Statistics can be updated from a browser or your scheduler.
The program also supports virtual servers, plugins and a lot of features.

With the default configuration, the statistics are available at:
http://localhost/awstats/awstats.pl

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p 1
%patch -P1 -p 1

# Fix style sheets.
perl -pi -e 's,/icon,/awstatsicons,g' wwwroot/css/*
# Fix some bad file permissions here for convenience.
chmod -x tools/httpd_conf
find tools/xslt -type f | xargs chmod -x
# Remove \r in conf file (file written on MS Windows)
perl -pi -e 's/\r//g' docs/COPYING.TXT docs/LICENSE.TXT docs/pad_awstats.xml docs/awstats_changelog.txt docs/styles.css tools/httpd_conf tools/logresolvemerge.pl tools/awstats_exportlib.pl tools/awstats_buildstaticpages.pl tools/maillogconvert.pl tools/urlaliasbuilder.pl wwwroot/cgi-bin/awredir.pl
# Encoding
recode ISO-8859-1..UTF-8 docs/awstats_changelog.txt
# Stray version control file
rm -f tools/webmin/.gitignore

%install
rm -rf $RPM_BUILD_ROOT

### Create folders
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{httpd/conf.d,%{name},cron.hourly}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

### Install files
cp -pr tools $RPM_BUILD_ROOT%{_datadir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/*.pl
chmod 644 $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/httpd_conf
cp -pr wwwroot $RPM_BUILD_ROOT%{_datadir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/wwwroot/cgi-bin/*.pl
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/wwwroot/classes/src
### We want these outside CGI path.
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/wwwroot/cgi-bin/{lang,lib,plugins}
cp -pr wwwroot/cgi-bin/{lang,lib,plugins} $RPM_BUILD_ROOT%{_datadir}/%{name}

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/wwwroot/cgi-bin/awstats.model.conf

### Commit permanent changes to default configuration
install -p -m 644 wwwroot/cgi-bin/awstats.model.conf \
    $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/%{name}.model.conf
perl -pi -e '
                s|^LogFile=.*$|LogFile="%{_localstatedir}/log/httpd/access_log"|;
                s|^DirData=.*$|DirData="%{_localstatedir}/lib/awstats"|;
                s|^DirCgi=.*$|DirCgi="/awstats"|;
                s|^DirIcons=.*$|DirIcons="/awstatsicons"|;
                s|^SiteDomain=.*$|SiteDomain="localhost.localdomain"|;
                s|^HostAliases=.*$|HostAliases="localhost 127.0.0.1"|;
                s|^EnableLockForUpdate=.*$|EnableLockForUpdate=1|;
                s|^SaveDatabaseFilesWithPermissionsForEveryone=.*$|SaveDatabaseFilesWithPermissionsForEveryone=0|;
                s|^SkipHosts=.*$|SkipHosts="127.0.0.1"|;
                s|^Expires=.*$|Expires=3600|;
            ' $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/%{name}.model.conf
install -p -m 644 $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/%{name}.{model,localhost.localdomain}.conf 

# Fix AWStats path in scripts
perl -pi -e 's|/usr/local/awstats|%{_datadir}/awstats|g' \
             $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/*.pl

# Apache configuration
install -p -m 644 tools/httpd_conf $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Cron job
install -m 0750 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/%{name}

# replace logos with Copyright and Trademark problem by unknown.png
# https://bugzilla.redhat.com/show_bug.cgi?id=1196549
cd $RPM_BUILD_ROOT%{_datadir}/%{name}/wwwroot/icon
for i in browser/adobe.png browser/seamonkey.png os/win*.png os/macos*.png cpu/intel.png cpu/ibm.png; do
  cp -v os/unknown.png $i
done
cd -

%post
if [ $1 -eq 1 ]; then
  if [ ! -f %{_sysconfdir}/%{name}/%{name}.`hostname`.conf ]; then
    %{__cat} %{_sysconfdir}/%{name}/%{name}.model.conf | \
      %{__perl} -p -e 's|^SiteDomain=.*$|SiteDomain="'`hostname`'"|;
                       s|^HostAliases=.*$|HostAliases="REGEX[^.*'${HOSTNAME//./\\\\.}'\$]"|;
                      ' > %{_sysconfdir}/%{name}/%{name}.`hostname`.conf || :
  fi
fi

%postun
%systemd_postun_with_restart httpd.service

%files
# Apache configuration file
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %attr(750,root,root) %{_sysconfdir}/cron.hourly/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/
%{_localstatedir}/lib/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/wwwroot
%{_datadir}/%{name}/tools
%{_datadir}/%{name}/wwwroot/cgi-bin
# Different defattr to fix lots of files which should not be +x.
%defattr(644,root,root,755)
%doc README.md docs/*
%{_datadir}/%{name}/lang
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/wwwroot/classes
%{_datadir}/%{name}/wwwroot/css
%{_datadir}/%{name}/wwwroot/icon
%{_datadir}/%{name}/wwwroot/js

%changelog
%autochangelog
