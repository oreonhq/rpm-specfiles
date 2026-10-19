%global source0_hash dd1fb3949c0df9c5048979f073ac8e88bbb63d28f0e0d65df3ec08077d98cfb4
%global commit 62ece4b929482702f5b2e716e3ee8998a29546cd
%global commitdate 20230224
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if %{defined commit}
%global snapshotversuffix ^git%{commitdate}.%{shortcommit}
%endif
Name:		openssh-ldap-authkeys
Version:	0.2.0%{?commit:%{snapshotversuffix}}
Release:        1%{?dist}
Summary:        Python script to generate SSH authorized_keys files using an LDAP directory
License:	MIT
URL:		https://github.com/fuhry/%{name}
%if %{defined commit}
Source0:        https://github.com/fuhry/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
%endif
BuildArch:	noarch
%if ! (%{defined python_enable_dependency_generator} || %{defined python_disable_dependency_generator})
Requires:	python%{python3_pkgversion}-ldap
Requires:	python%{python3_pkgversion}-dns
Requires:	python%{python3_pkgversion}-yaml
%endif
Requires:	(%{name}-selinux = %{version}-%{release} if selinux-policy)
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
openssh-ldap-authkeys is an implementation of AuthorizedKeysCommand for
OpenSSH 6.9 and newer that allows SSH public keys to be retrieved from
an LDAP source. It's provided for situations where a solution other
than 1:1 mapping is needed for users.

With SSH keys stored centrally in LDAP, revocation of a compromised
key is a quick and painless exercise for the user or IT department.

openssh-ldap-authkeys allows shared accounts to be fully auditable as
to who used them.

%if 0%{?el7}
%post

%sysusers_create %{name}.sysusers.conf
%tmpfiles_create %{name}.tmpfiles.conf
%endif
%package selinux
Summary:	SELinux module for %{name}
BuildRequires:	selinux-policy
BuildRequires:	selinux-policy-devel
BuildRequires:	make
%{?selinux_requires}
%description selinux
This package provides the SELinux policy module to ensure
%{name} runs properly under an environment with
SELinux enabled.

%pre selinux

%selinux_relabel_pre
%post selinux

%selinux_modules_install %{_datadir}/selinux/packages/olak.pp.bz2
%posttrans selinux

if [ $1 -eq 1 ] && /usr/sbin/selinuxenabled ; then
	fixfiles -FR %{name} restore || :
fi
%postun selinux

%selinux_modules_uninstall olak
if [ $1 -eq 0 ]; then
	%selinux_relabel_post
fi
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{defined commit}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif

%build

%py3_build
pushd selinux
make SHARE="%{_datadir}" TARGETS="olak"
popd
%install
%py3_install
touch %{buildroot}%{_sysconfdir}/%{name}/olak.yml
touch %{buildroot}%{_sysconfdir}/%{name}/authmap
rm %{buildroot}%{_sysconfdir}/%{name}/*.example
install -d %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -d %{buildroot}%{_mandir}/man8/
install -m 644 selinux/olak.pp.bz2 %{buildroot}%{_datadir}/selinux/packages
install -m 644 selinux/olak.if  %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -m 644 selinux/olak_selinux.8 %{buildroot}%{_mandir}/man8/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openssh-ldap-authkeys-selinux -f %{oreon_filedir}/openssh-ldap-authkeys-selinux.list

%changelog

%autochangelog
