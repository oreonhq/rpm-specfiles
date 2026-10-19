%global source0_hash 9a4227ed5b3336130e793232da00765a64fc22207ff8ad43a82ae1918e903e18
Name:		ufdbGuard
Version:	1.35.8
Release:        1%{?dist}
Summary:        A URL filter for squid
URL:		https://www.urlfilterdb.com/
License:	GPL-2.0-only
Source0:        https://www.urlfilterdb.com/files/downloads/%{name}-%{version}.tar.gz
Source1:	ufdbGuard.logrotate
%bcond_with    tmpfiles
Requires: logrotate
# oreon:deps
BuildRequires:  bind-utils
BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  perl-interpreter
BuildRequires:  systemd-rpm-macros
BuildRequires:  wget
BuildRequires:  zlib-devel
# /oreon:deps
%description
ufdbGuard is a free URL filter for Squid with additional features like
SafeSearch enforcement for a large number of search engines, safer HTTPS 
visits and dynamic detection of proxies (URL filter circumventors).

ufdbGuard supports free and commercial URL databases that can be
downloaded from various sites and vendors.
You can also make your own URL database for ufdbGuard.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

iconv -c --from-code=ISO-8859-1 --to-code=UTF-8 -o CHANGELOG.new CHANGELOG
mv CHANGELOG.new CHANGELOG

# Create a sysusers.d config file
cat >ufdbguard.sysusers.conf <<EOF
u ufdb - 'ufdbGuard URL filter' /var/lib/ufdbguard -
EOF

%build

INSTALL_PROGRAM=./install-sh %configure \
	--with-ufdb-user=ufdb \
	--prefix=%{_prefix} \
	--with-ufdb-bindir=%{_sbindir} \
	--with-ufdb-piddir=%{_localstatedir}/run/ufdbguard \
	--with-ufdb-mandir=%{_mandir} \
	--with-ufdb-images_dir=%{_sharedstatedir}/ufdbguard/images \
	--with-ufdb-logdir=%{_localstatedir}/log/ufdbguard \
	--with-ufdb-samplesdir=%{_sharedstatedir}/ufdbguard/samples \
	--with-ufdb-config=%{_sysconfdir}/ufdbguard \
	--with-ufdb-dbhome=%{_sharedstatedir}/ufdbguard/blacklists \
	--with-ufdb-imagesdir=%{_sharedstatedir}/ufdbguard/images
%make_build
%install
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
mkdir -p %{buildroot}%{_sysconfdir}/init.d
mkdir -p %{buildroot}%{_sysconfdir}/ufdbguard
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
%make_install INSTALL="../install-sh -c"
for i in $(find doc/ -type f -name '*.1'); do
    install -p -D -m 0644 $i %{buildroot}%{_mandir}/man1/
done
for i in $(find doc/ -type f -name '*.8'); do
    install -p -D -m 0644 $i %{buildroot}%{_mandir}/man8/
done
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/ufdbGuard
rm -rf %{buildroot}%{_sysconfdir}/rc.d/init.d/ufdb
rm -rf %{buildroot}%{_sysconfdir}/init.d
rm -f %{buildroot}%{_sbindir}/ufdbsignal
mkdir -p %{buildroot}%{_var}/run/ufdbguard
%if %{with tmpfiles}
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
echo 'd /var/run/ufdbguard 0750 ufdb ufdb -' > \
    %{buildroot}/usr/lib/tmpfiles.d/ufdbGuard.conf
%endif
install -m0644 -D ufdbguard.sysusers.conf %{buildroot}%{_sysusersdir}/ufdbguard.conf
%oreon_autofiles main

%post

%systemd_post ufdbguard.service
%preun

%systemd_preun ufdbguard.service
%postun

%systemd_postun_with_restart ufdbguard.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
