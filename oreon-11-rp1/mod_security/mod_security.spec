%global source0_hash 1fe16eb96b6093f062cef73ec8b7ae481a59813766d49a7f5e4d1b85900e239e
%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn 0-0}}
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}
%bcond_without mlogc
%bcond ssdeep %{undefined rhel}
%bcond yajl %[0%{?rhel} < 10]
Summary:        Security module for the Apache HTTP Server
Name: mod_security
Version: 2.9.11
Release:        1%{?dist}
License: Apache-2.0
URL: http://www.modsecurity.org/
Source0:        https://github.com/owasp-modsecurity/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz
Source1: mod_security.conf
Source2: 10-mod_security.conf
Source3: modsecurity_localrules.conf
Patch1: modsecurity-2.9.3-apulibs.patch
Patch2: mod_security-2.9.3-remote-rules-timeout.patch
Patch3: mod_security-2.9.7-send_error_bucket.patch
Patch4: mod_security-2.9.7-pipedlogs.patch
Requires: httpd httpd-mmn
%if 0%{?fedora} || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
Requires(pre): httpd-filesystem
%endif
%if %{with ssdeep}
%endif
%if %{with yajl}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  httpd-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(yajl)
BuildRequires:  ssdeep-devel
# /oreon:deps
%description
ModSecurity is an open source intrusion detection and prevention engine
for web applications. It operates embedded into the web server, acting
as a powerful umbrella - shielding web applications from attacks.

%if %{with mlogc}
%package        mlogc
Summary:        ModSecurity Audit Log Collector
Requires:       mod_security
%if 0%{?fedora} || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
Requires(pre):  httpd-filesystem
%endif
%description mlogc
This package contains the ModSecurity Audit Log Collector.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n modsecurity-v%{version} -S git

: Building with YAJL=%{with yajl} ssdeep=%{with ssdeep}

%build

./autogen.sh
%configure --enable-pcre-match-limit=1000000 \
           --enable-pcre-match-limit-recursion=1000000 \
           --with-apxs=%{_httpd_apxs} \
           --with-yajl \
           --with-pcre2 \
           --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{_smp_mflags}
%check

%install
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_httpd_moddir}
install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/
install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules
install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/local_rules
install -m0755 apache2/.libs/mod_security2.so %{buildroot}%{_httpd_moddir}/mod_security2.so
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_httpd_modconfdir}/10-mod_security.conf
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_httpd_confdir}/mod_security.conf
sed  -i 's/Include/IncludeOptional/'  %{buildroot}%{_httpd_confdir}/mod_security.conf
%else
install -d -m0755 %{buildroot}%{_httpd_confdir}
cat %{SOURCE2} %{SOURCE1} > %{buildroot}%{_httpd_confdir}/mod_security.conf
%endif
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}
install -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/local_rules/
%if %{with mlogc}
install -d %{buildroot}%{_localstatedir}/log/mlogc
install -d %{buildroot}%{_localstatedir}/log/mlogc/data
install -m0755 mlogc/mlogc %{buildroot}%{_bindir}/mlogc
install -m0755 mlogc/mlogc-batch-load.pl %{buildroot}%{_bindir}/mlogc-batch-load
install -m0644 mlogc/mlogc-default.conf %{buildroot}%{_sysconfdir}/mlogc.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n mod_security-mlogc -f %{oreon_filedir}/mod_security-mlogc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.11-3
- Import
