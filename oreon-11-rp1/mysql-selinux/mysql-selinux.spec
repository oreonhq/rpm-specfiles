%global source0_hash 2f0cca17bc2a29749c3cc90e1415e4d70fb55b424790df2e61acbe1189e706d3
%global selinuxtype targeted
%global modulename mysql
Name:           mysql-selinux
Version:        1.0.18
Release:        1%{?dist}
License:        GPL-3.0-only
URL:            https://github.com/devexp-db/mysql-selinux
Summary:        SELinux policy modules for MySQL and MariaDB packages
Source0:        https://github.com/devexp-db/mysql-selinux/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
%{?selinux_requires}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
# /oreon:deps
%description
SELinux policy modules for MySQL and MariaDB packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}

%build

make
%install
install -d %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
