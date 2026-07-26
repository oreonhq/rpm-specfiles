%global source0_hash 1583bb15673d48794a71fa12c3447f89046a1ff0ad89d414b5b25013b7751a91

Name:           drraw
Version:        2.2
Release:        0.37.b2%{?dist}
Summary:        Web based presentation front-end for RRDtool

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://web.taranis.org/drraw/
Source0:        http://web.taranis.org/drraw/dist/drraw-2.2b2.tar.gz
Source1:        drraw-httpd.conf
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(RRDs)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Requires:       mod_perl 

%description
drraw is a simple web based presentation front-end for RRDtool that allows you
to interactively build graphs of your own design. A graph definition can be
turned into a template which may be applied to many Round Robin Database files.
drraw specializes in providing an easy mean of displaying data stored with
RRDtool and does not care about how the data is collected, making it a great
complement to other RRDtool front-ends.

%package selinux
Summary:          SELinux context for %{name}
Requires:         %name = %version-%release
Requires(post):   policycoreutils
Requires(postun): policycoreutils

%description selinux
SElinux context for drraw.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n drraw-2.2b2
# Set work dirs in conf file
sed -i -e "s|^\$saved_dir = .*|\$saved_dir = '/var/lib/drraw';|" \
       -e "s|^\$tmp_dir = .*|\$tmp_dir = '/var/tmp';|" drraw.conf
# Patch drraw.cgi for conf file location
sed -i -e 's|^my $config = .*|my $config = "/etc/drraw.conf";|' drraw.cgi
# Fix file encoding
iconv -f iso8859-1 -t utf-8 CHANGES > CHANGES.conv && \
touch -r CHANGES CHANGES.conv && \
mv -f CHANGES.conv CHANGES

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 0755 drraw.cgi $RPM_BUILD_ROOT/%{_datadir}/%{name}/drraw.cgi
install -Dp -m 0644 drraw.conf $RPM_BUILD_ROOT/%{_sysconfdir}/drraw.conf
install -Dp -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/drraw.conf
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/%{name}

%post selinux
semanage fcontext -a -t httpd_sys_script_exec_t '%{_datadir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -a -t httpd_sys_rw_content_t '%{_localstatedir}/lib/%{name}(/.*)?' 2>/dev/null || :
restorecon -R %{_datadir}/%{name} %{_localstatedir}/lib/%{name} || :

%postun selinux
if [ $1 -eq 0 ] ; then
semanage fcontext -d -t httpd_sys_script_exec_t '%{_datadir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -d -t httpd_sys_rw_content_t '%{_localstatedir}/lib/%{name}(/.*)?' 2>/dev/null || :
fi

%files
%license LICENSE
%doc README.EVENTS INSTALL CHANGES
%config(noreplace) %{_sysconfdir}/drraw.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/drraw.conf
%{_datadir}/%{name}
%attr(755,apache,root) %{_localstatedir}/lib/%{name}

%files selinux

%changelog
%autochangelog
