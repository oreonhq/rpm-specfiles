%global source0_hash d75ac68dc11fc7efdc05be23095cbeb7ba39edf94c1fe0f6d975167e9e0ce9b5

# General maintainer notes:
#   Fedora guideliens for packaging of SELinux rules:
#     https://fedoraproject.org/wiki/SELinux/IndependentPolicy
#   RHEL instructions regarding Troubleshooting problems related to SELinux:
#     https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_selinux/troubleshooting-problems-related-to-selinux_using-selinux

# defining macros needed by SELinux
%global selinuxtype targeted
%global modulename mysql

Name:           mysql-selinux
Version:        1.0.14
Release:        3%{?dist}

License:        GPL-3.0-only
URL:            https://github.com/devexp-db/mysql-selinux
Summary:        SELinux policy modules for MySQL and MariaDB packages

Source0:        https://github.com/devexp-db/mysql-selinux/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  selinux-policy-devel

%{?selinux_requires}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}

%description
SELinux policy modules for MySQL and MariaDB packages.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}

%build
make

%install
# install policy modules
install -d %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}


%pre
%selinux_relabel_pre -s %{selinuxtype}

%post
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans
%selinux_relabel_post -s %{selinuxtype}


%files
%defattr(-,root,root,0755)
%attr(0644,root,root) %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%ghost %verify(not mode md5 size mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%license COPYING

# Note:
#   we do not pack the *.if file as seen in the example:
#     https://fedoraproject.org/wiki/SELinux/IndependentPolicy#The_%prep_and_%install_Section
#   since we do not have any interface to be shared (and even then it is optional)

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.14-3
- Prepare for Oreon 11 (RP1)
