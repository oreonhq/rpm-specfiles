%global source0_hash 6662039f093314f896950519fa781bc87610f926f64b3d349229002f06ac41a9

%global sphinx_user sphinx
%global sphinx_group sphinx
%global sphinx_home %{_localstatedir}/lib/sphinx

# rpmbuild < 4.6 support
%if ! 0%{?__isa_bits}
%ifarch x86_64 ia64 ppc64 sparc64 s390x alpha ppc64le aarch64
%global __isa_bits 64
%else
%global __isa_bits 32
%endif
%endif

%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
%bcond_with java
%else
%bcond_without java
%endif


Name:		sphinx
Version:	2.2.11
Release:	36%{?dist}
Summary:	Free open-source SQL full-text search engine
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://sphinxsearch.com

Source0:	http://sphinxsearch.com/files/%{name}-%{version}-release.tar.gz
Source1:	searchd.service
Patch0:		%{name}-2.0.3-fix_static.patch
Patch1:		listen_local.patch
Patch2:		sphinx-configure-c99.patch
Patch3:		sphinx-c99.patch

BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:	expat-devel
BuildRequires:	mariadb-connector-c-devel openssl-devel
BuildRequires:	libpq-devel
BuildRequires:	systemd

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

# Users and groups
       

%description
Sphinx is a full-text search engine, distributed under GPL version 2.
Commercial licensing (e.g. for embedded use) is also available upon request.

Generally, it's a standalone search engine, meant to provide fast,
size-efficient and relevant full-text search functions to other
applications. Sphinx was specially designed to integrate well with SQL
databases and scripting languages.

Currently built-in data source drivers support fetching data either via
direct connection to MySQL, or PostgreSQL, or from a pipe in a custom XML
format. Adding new drivers (e.g. native support other DBMSes) is
designed to be as easy as possible.

Search API native ported to PHP, Python, Perl, Ruby, Java, and also
available as a plug-gable MySQL storage engine. API is very lightweight so
porting it to new language is known to take a few hours.

As for the name, Sphinx is an acronym which is officially decoded as SQL
Phrase Index.
For the Sphinx documentation generator, see python-sphinx instead.


%package -n libsphinxclient
Summary:	Pure C search-d client API library


%description -n libsphinxclient
Pure C search-d client API library
Sphinx search engine, http://sphinxsearch.com/


%package -n libsphinxclient-devel
Summary:	Development libraries and header files for libsphinxclient
Requires:	libsphinxclient = %{version}-%{release}


%description -n libsphinxclient-devel
Pure C search-d client API library
Sphinx search engine, http://sphinxsearch.com/


%if %{with java}
%package java
Summary:		Java API for Sphinx
BuildRequires:	java-devel
Requires:		java-headless
Requires:		jpackage-utils


%description java
This package provides the Java API for Sphinx,
the free, open-source full-text search engine,
designed with indexing database content in mind.
%endif

%package php
Summary:	PHP API for Sphinx
Requires:	php-common >= 5.1.6


%description php
This package provides the PHP API for Sphinx,
the free, open-source full-text search engine,
designed with indexing database content in mind.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -qn %{name}-%{version}-release
%patch -P0 -p1 -b .fix_static
%patch -P1 -p1 -b .default_listen
%patch -P2 -p1
%patch -P3 -p1

# Fix wrong-file-end-of-line-encoding
for f in \
	api/java/mk.cmd \
	api/ruby/test.rb \
	api/ruby/spec/%{name}/%{name}_test.sql \
	api/ruby/spec/%{name}/%{name}_test.sql \
; do
	sed -i 's/\r$//' ${f};
done

# Fix file not UTF8
iconv -f iso8859-1 -t utf-8 doc/%{name}.txt > doc/%{name}.txt.conv && mv -f doc/%{name}.txt.conv doc/%{name}.txt

# Create a sysusers.d config file
cat >sphinx.sysusers.conf <<EOF
g sphinx -
u sphinx - 'Sphinx Search' %{sphinx_home} /bin/bash
EOF

%build
%if %{__isa_bits} == 64
%configure --sysconfdir=%{_sysconfdir}/%{name} --with-mysql --with-pgsql --enable-id64
%else
%configure --sysconfdir=%{_sysconfdir}/%{name} --with-mysql --with-pgsql
%endif

make %{?_smp_mflags}

# Build libsphinxclient
pushd api/libsphinxclient
    %configure
    make #%{?_smp_mflags}
popd


%if %{with java}
# make the java api
make -C api/java 
%endif


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p -c"

install -p -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/searchd.service

# Create /var/log/sphinx
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}

# Create /var/run/sphinx
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}

# Create /var/lib/sphinx
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}

# Create sphinx.conf
cp $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}-min.conf.dist \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf
    
# Modify sphinx.conf
sed -i 's|/var/log/searchd.log|%{_localstatedir}/log/%{name}/searchd.log|g' \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf

sed -i 's|/var/log/query.log|%{_localstatedir}/log/%{name}/query.log|g' \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf

sed -i 's|/var/log/searchd.pid|%{_localstatedir}/run/%{name}/searchd.pid|g' \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf

sed -i 's|/var/data|%{_localstatedir}/lib/sphinx|g' \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf

# Create /etc/logrotate.d/sphinx
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name} << EOF
%{_localstatedir}/log/%{name}/*.log {
       weekly
       rotate 10
       copytruncate
       delaycompress
       compress
       notifempty
       missingok
}
EOF

# Create tmpfile run configuration
mkdir -p $RPM_BUILD_ROOT%{_tmpfilesdir}
cat > $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf << EOF
d /run/%{name} 755 %{name} root -
EOF

# Install libsphinxclient
pushd api/libsphinxclient/
    make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p -c"
popd

%if %{with java}
# install the java api
mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -m 0644 api/java/%{name}api.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{_javadir}/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}api.jar
%endif

# install the php api
# "Non-PEAR PHP extensions should put their Class files in /usr/share/php."
# - http://fedoraproject.org/wiki/Packaging:PHP
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/php
install -m 0644 api/%{name}api.php $RPM_BUILD_ROOT%{_datadir}/php

# clean-up .la archives
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# clean-up .a archives
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

install -m0644 -D sphinx.sysusers.conf %{buildroot}%{_sysusersdir}/sphinx.conf



%post
%systemd_post searchd.service

%preun
%systemd_preun searchd.service

%ldconfig_scriptlets -n libsphinxclient

%postun
%systemd_postun_with_restart searchd.service

%posttrans
chown -R %{sphinx_user}:root %{_localstatedir}/log/%{name}/
chown -R %{sphinx_user}:root %{_localstatedir}/run/%{name}/
chown -R %{sphinx_user}:root %{_localstatedir}/lib/%{name}/

%triggerun -- sphinx < 2.0.3-1
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply httpd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save searchd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del searchd >/dev/null 2>&1 || :
/bin/systemctl try-restart searchd.service >/dev/null 2>&1 || :


%files
%doc COPYING doc/sphinx.txt sphinx-min.conf.dist sphinx.conf.dist example.sql
%dir %{_sysconfdir}/sphinx
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%exclude %{_sysconfdir}/%{name}/*.conf.dist
%exclude %{_sysconfdir}/%{name}/example.sql
%{_unitdir}/searchd.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_tmpfilesdir}/%{name}.conf
%{_bindir}/*
%dir %attr(0755, %{sphinx_user}, root) %{_localstatedir}/log/%{name}
%dir %attr(0755, %{sphinx_user}, root) %{_localstatedir}/run/%{name}
%dir %attr(0755, %{sphinx_user}, root) %{_localstatedir}/lib/%{name}
%{_mandir}/man1/*
%{_sysusersdir}/sphinx.conf

%files -n libsphinxclient
%doc COPYING %{?with_java: api/java} api/ruby api/*.php api/*.py api/libsphinxclient/README
%{_libdir}/libsphinxclient-0*.so

%files -n libsphinxclient-devel
%{_libdir}/libsphinxclient.so
%{_includedir}/*

%if %{with java}
%files java
%doc api/java/README COPYING
%{_javadir}/*
%endif

%files php
%doc COPYING
%{_datadir}/php/*

%changelog
%autochangelog
