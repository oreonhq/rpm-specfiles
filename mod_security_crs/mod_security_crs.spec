%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}

Summary: ModSecurity Core Ruleset
Name: mod_security_crs
Version: 4.15.0
Release: 3%{?dist}
License: Apache-2.0
URL: https://coreruleset.org/
Source: https://github.com/coreruleset/coreruleset/archive/refs/tags/v%{version}.tar.gz
BuildArch: noarch
Requires: mod_security >= 2.9.6
Obsoletes: mod_security_crs-extras < 3.0.0

# Patch0: mod_security_crs-XXX.patch

%description
This package provides the base rules for mod_security.

%prep
%autosetup -p1 -S gendiff -n coreruleset-%{version}

%build

%install
%{__install} -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/
%{__install} -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules
%{__install} -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/plugins
%{__install} -d %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules
%{__install} -d %{buildroot}%{_datarootdir}/mod_modsecurity_crs/plugins

%{__mv} rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf
%{__mv} rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf

%{__install} -m0644 rules/*.conf %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules/
%{__install} -m0644 rules/*.data %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules/
%{__install} -m0644 plugins/* %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/plugins/
%{__mv} crs-setup.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/crs-setup.conf

%post
if [ $1 == 1 ]; then
     # activate base_rules
     for f in `ls %{_datarootdir}/mod_modsecurity_crs/rules/` ; do 
         %{__ln_s} %{_datarootdir}/mod_modsecurity_crs/rules/$f %{_sysconfdir}/httpd/modsecurity.d/activated_rules/$f; 
     done
     %{__sed} -i '/IncludeOptional modsecurity\.d\/\*\.conf/ a\    IncludeOptional modsecurity.d\/plugins\/*-config.conf\n    IncludeOptional modsecurity.d\/plugins\/*-before.conf' %{_httpd_confdir}/mod_security.conf
     %{__sed} -i '/Include modsecurity\.d\/\*\.conf/a\    Include modsecurity.d/plugins/*-config.conf\n    Include modsecurity.d/plugins/*-before.conf' %{_httpd_confdir}/mod_security.conf
     %{__sed} -i '/IncludeOptional modsecurity\.d\/local_rules\/\*\.conf/a\    IncludeOptional modsecurity.d\/plugins\/*-after.conf' %{_httpd_confdir}/mod_security.conf
     %{__sed} -i '/Include modsecurity\.d\/local_rules\/\*\.conf/a\    Include modsecurity.d\/plugins\/*-after.conf' %{_httpd_confdir}/mod_security.conf
fi
exit 0

%preun
if [ $1 == 0 ]; then
     %{__sed} -i -E '/Include(Optional)? modsecurity\.d\/plugins/d' %{_httpd_confdir}/mod_security.conf
     for f in `ls %{_datarootdir}/mod_modsecurity_crs/rules/` ; do 
         %{__rm} %{_sysconfdir}/httpd/modsecurity.d/activated_rules/$f; 
     done
fi
exit 0

%files
%license LICENSE
%doc CHANGES.md README.md
%{_datarootdir}/mod_modsecurity_crs
%{_sysconfdir}/httpd/modsecurity.d/plugins
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/activated_rules/*
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/crs-setup.conf
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/plugins/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.15.0-3
- Prepare for Oreon 11 (RP1)
