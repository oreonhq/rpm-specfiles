%global source0_hash 7afbc006d04bb8d976a962661978932660db5689ba946ae56d3f5622e0e06c45
%global selinuxtype targeted
%global modulename bitcoin
Name:           bitcoin-core-selinux
Version:        0.2
Release:        1%{?dist}
Summary:        Bitcoin Core SELinux policy
License:        GPL-3.0-only
URL:            https://github.com/scaronni/%{name}
BuildArch:      noarch
Source0:        https://github.com/scaronni/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
%{?selinux_requires}
# oreon:deps
BuildRequires:  pkgconfig(systemd)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
# /oreon:deps
%description
Bitcoin Core SELinux policy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%install
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%oreon_autofiles main

%pre

%selinux_relabel_pre -s %{selinuxtype}
%post

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
if %{_sbindir}/selinuxenabled ; then
     %{_sbindir}/semanage port -a -t %{modulename}_port_t -p tcp 8332
     %{_sbindir}/semanage port -a -t %{modulename}_port_t -p tcp 8333
     %{_sbindir}/semanage port -a -t %{modulename}_port_t -p tcp 8334
     %{_sbindir}/semanage port -a -t %{modulename}_port_t -p tcp 18332
     %{_sbindir}/semanage port -a -t %{modulename}_port_t -p tcp 18333
fi
%postun

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi
if %{_sbindir}/selinuxenabled ; then
    %{_sbindir}/semanage port -d -t %{modulename}_port_t -p tcp 8332
    %{_sbindir}/semanage port -d -t %{modulename}_port_t -p tcp 8333
    %{_sbindir}/semanage port -d -t %{modulename}_port_t -p tcp 8334
    %{_sbindir}/semanage port -d -t %{modulename}_port_t -p tcp 18332
    %{_sbindir}/semanage port -d -t %{modulename}_port_t -p tcp 18333
fi
%posttrans

%selinux_relabel_post -s %{selinuxtype}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
