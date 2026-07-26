%global source0_hash 1d4b8cc58142a88b4b1603129eb9307e6256aa0146c88d515a09a58dbfa39169

%global srcname spf-engine

Name:           pypolicyd-spf
Version:        3.1.0
Release:        8%{?dist}
Summary:        SPF Policy Server for Postfix (Python implementation)

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://launchpad.net/%{srcname}
Source0:        https://launchpad.net/%{srcname}/3.1/%{version}/+download/%{srcname}-%{version}.tar.gz
Source1:        %{name}-tmpfiles.conf
Patch0:         pypolicyd-spf-3.0.4-service.patch

BuildArch:      noarch
Requires:       postfix
Requires:       python3-pyspf
Requires:       python3-authres

BuildRequires:  systemd
BuildRequires:  python3-devel

BuildRequires:  systemd-rpm-macros
%if 0%{?fedora} < 42 || 0%{?rhel}
%{?sysusers_requires_compat}
%endif

%generate_buildrequires
%pyproject_buildrequires

%package milter
Summary:        Milter for pypolicyd-spf (spf-engine).
Requires:       %{name} = %{version}-%{release}
Requires:       python3-pymilter

%description
pypolicyd-spf (spf-engine) is a Postfix policy engine for Sender Policy
Framework (SPF) checking. It is implemented in pure Python and uses the
python-spf (pyspf) module.

This SPF policy server implementation provides flexible options for different
receiver policies and sender whitelisting to enable it to support a very wide
range of requirements.

%description milter
Milter for pypolicyd-spf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Move doc files
%{__mv} data/share/doc/python-policyd-spf/README.per_user_whitelisting .
%{__mv} data/etc/python-policyd-spf/policyd-spf.conf.commented .

# Create a sysusers.d config file
cat >pypolicyd-spf.sysusers.conf <<EOF
u pyspf-milter - - /run/pyspf-milter -
EOF

%build
%pyproject_wheel

%install
%pyproject_install

# We want the binary in Postfix libexec directory
%{__mkdir_p} %{buildroot}%{_libexecdir}/postfix
%{__mv} %{buildroot}%{_bindir}/policyd-spf %{buildroot}%{_libexecdir}/postfix

# Move etc
%{__mv} %{buildroot}%{_prefix}/etc %{buildroot}%{_sysconfdir}
%{__sed} -i -e 's/^HELO_reject = SPF_Not_Pass$/HELO_reject = Fail/' \
               %{buildroot}%{_sysconfdir}/python-policyd-spf/policyd-spf.conf

# Remove SysV init
%{__rm} -rf %{buildroot}%{_sysconfdir}/init.d

# Temporary files for milter
%{__mkdir_p} %{buildroot}%{_tmpfilesdir}
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

install -m0644 -D pypolicyd-spf.sysusers.conf %{buildroot}%{_sysusersdir}/pypolicyd-spf.conf

%if 0%{?fedora} < 42 || 0%{?rhel}
%pre
%sysusers_create_compat pypolicyd-spf.sysusers.conf
%endif

 
%files
%doc README.txt README.per_user_whitelisting CHANGES COPYING
%doc policyd-spf.conf.commented
%dir %{_sysconfdir}/python-policyd-spf
%config(noreplace) %{_sysconfdir}/python-policyd-spf/policyd-spf.conf
%{_libexecdir}/postfix/policyd-spf
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man1/*
%{_mandir}/man5/*
%dir %{python3_sitelib}/spf_engine
%{python3_sitelib}/spf_engine-%{version}.dist-info/
%pycached %{python3_sitelib}/spf_engine/__init__.py
%pycached %{python3_sitelib}/spf_engine/policy*.py
%pycached %{python3_sitelib}/spf_engine/config.py
%{_sysusersdir}/pypolicyd-spf.conf

%files milter
%dir %{_sysconfdir}/pyspf-milter
%config(noreplace) %{_sysconfdir}/pyspf-milter/pyspf-milter.conf
%{_bindir}/pyspf-milter
%{_unitdir}/pyspf-milter.service
%{_mandir}/man8/*
%pycached %{python3_sitelib}/spf_engine/milter*.py
%pycached %{python3_sitelib}/spf_engine/util.py

%changelog
%autochangelog
