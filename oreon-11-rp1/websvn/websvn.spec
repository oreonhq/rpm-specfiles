%global source0_hash 9f006dba0dd762538f95569bcfe63d2a82fb98afa2e431339104c6227e8fb204

Name:           websvn
Version:        2.8.8
Release:        1%{?dist}
Summary:        Online subversion repository browser

License:        GPL-2.0-or-later
URL:            https://websvnphp.github.io
Source0:        https://github.com/websvnphp/websvn/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        websvn-httpd.conf

BuildArch:      noarch

Requires(pre):  httpd
Requires:       sed
Requires:       enscript
Requires:       php >= 5.4.0
Requires:       php-mbstring
Requires:       php-xml
Requires:       php-geshi
Requires:       php-pear(Archive_Tar)
# Text_Diff is broken with PHP 8.
# Use system diff instead where needed.
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 9
Requires:       diffutils
%else
Requires:       php-pear(Text_Diff)
%endif

%description
WebSVN offers a view onto your subversion repositories that's been designed to
reflect the Subversion methodology. You can view the log of any file or
directory and see a list of all the files changed, added or deleted in any
given revision. You can also view the differences between two versions of a
file so as to see exactly what was changed in a particular revision.

%package selinux
Summary:          SELinux context for %{name}
Requires:         %name = %version-%release
Requires(post):   policycoreutils
Requires(postun): policycoreutils

%description selinux
SElinux context for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
find -name .gitignore -delete

mv include/distconfig.php include/config.php
sed -i -e "s#^\/\/ \$config->useMultiViews();#\$config->useMultiViews();#" \
    include/config.php

%build
# Nothing to build

%install
# Install the code
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -a *.php include javascript languages templates \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}

# Move the conf to the proper place
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT/%{_datadir}/%{name}/include/config.php \
   $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
ln -s ../../../..%{_sysconfdir}/%{name}/config.php \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/include/config.php

# Apache conf
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -m 0644 %{SOURCE1} \
                $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Move the cache dir to a better place
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/cache/%{name}
ln -s ../../..%{_localstatedir}/cache/%{name} \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/cache

# Move the temp dir to a better place
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/tmp
ln -s ../../..%{_localstatedir}/tmp $RPM_BUILD_ROOT/%{_datadir}/%{name}/temp

# Add a compat symlink from removed wsvn.php to new browse.php
# This needs FollowSymlinks option in the httpd conf
ln -s %{_datadir}/%{name}/browse.php %{buildroot}/%{_datadir}/%{name}/wsvn.php

%post selinux
semanage fcontext -a -t httpd_cache_t '%{_localstatedir}/cache/%{name}(/.*)?' 2>/dev/null || :
restorecon -R %{_localstatedir}/cache/%{name} || :

%postun selinux
if [ $1 -eq 0 ] ; then
semanage fcontext -d -t httpd_cache_t '%{_localstatedir}/cache/%{name}(/.*)?' 2>/dev/null || :
fi

%files
%doc README.md changes.txt
%license license.txt
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/config.php
%{_datadir}/%{name}
%attr(-,apache,root) %{_localstatedir}/cache/%{name}

%files selinux

%changelog
%autochangelog
