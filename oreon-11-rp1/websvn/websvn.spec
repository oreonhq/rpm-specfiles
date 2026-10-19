%global source0_hash a0007c2e7763495cd0f88b8f186f4d7169e3f0637e30088e8b4b851c304b721c
Name:           websvn
Version:        2.9.0
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
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
Requires:       diffutils
%else
Requires:       php-pear(Text_Diff)
%endif
# oreon:deps

# /oreon:deps
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

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -a *.php include javascript languages templates \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT/%{_datadir}/%{name}/include/config.php \
   $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
ln -s ../../../..%{_sysconfdir}/%{name}/config.php \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/include/config.php
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -m 0644 %{SOURCE1} \
                $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/%{name}.conf
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/cache/%{name}
ln -s ../../..%{_localstatedir}/cache/%{name} \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/cache
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/tmp
ln -s ../../..%{_localstatedir}/tmp $RPM_BUILD_ROOT/%{_datadir}/%{name}/temp
ln -s %{_datadir}/%{name}/browse.php %{buildroot}/%{_datadir}/%{name}/wsvn.php
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post selinux

semanage fcontext -a -t httpd_cache_t '%{_localstatedir}/cache/%{name}(/.*)?' 2>/dev/null || :
restorecon -R %{_localstatedir}/cache/%{name} || :
%postun selinux

if [ $1 -eq 0 ] ; then
semanage fcontext -d -t httpd_cache_t '%{_localstatedir}/cache/%{name}(/.*)?' 2>/dev/null || :
fi
%files -f %{oreon_filedir}/main.list
%files -n websvn-selinux -f %{oreon_filedir}/websvn-selinux.list

%changelog

%autochangelog
