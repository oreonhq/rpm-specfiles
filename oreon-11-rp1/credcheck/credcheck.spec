%global source0_hash 549125dd43546c27e1f6db7dfc02f9621be6b459bce9edb561649ca87f88428f
%bcond_without cracklib
%global selinuxtype targeted
%global with_selinux 1
Name: credcheck
Version: 5.0
Release:        1%{?dist}
Summary:        PostgreSQL extension for credential checking
License: PostgreSQL
URL: https://github.com/HexaCluster/%{name}
Source0:        https://github.com/HexaCluster/%{name}/archive/refs/tags/v%{version}.tar.gz
%if %{with cracklib}
Source1: %{name}.cil
Patch0: enable_cracklib.patch
%endif
%if %{with cracklib}
%endif
Requires: postgresql-server
%if %{with cracklib}
Requires: cracklib-dicts
%if 0%{?with_selinux}
Requires: (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif
%endif
# oreon:deps
BuildRequires:  cracklib-devel
BuildRequires:  cracklib-dicts
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  postgresql-server-devel
BuildRequires:  selinux-policy-targeted
# /oreon:deps
%description
The credcheck PostgreSQL extension provides few general credential checks,
which will be evaluated during the user creation, during the password change
and user renaming. By using this extension, we can define a set of rules:

    allow a specific set of credentials
    reject a certain type of credentials
    deny password that can be easily cracked
    enforce use of an expiration date with a minimum of day for a password
    define a password reuse policy
    define the number of authentication failure allowed before a user is banned

This extension provides all the checks as configurable parameters.
The default configuration settings, will not enforce any complex checks
and will try to allow most of the credentials.
By using SET credcheck.<check-name> TO <some value>; command, enforce new
settings for the credential checks. The settings can only be changed 
by a superuser.

%if %{with cracklib} && 0%{?with_selinux}
#The SELinux subpackage
%package selinux
Summary: %{name} SELinux policy
BuildArch: noarch
BuildRequires: selinux-policy-%{selinuxtype}
Requires: selinux-policy-%{selinuxtype}
Recommends: %{name} = %{version}-%{release}
Requires(post): libselinux-utils selinux-policy-%{selinuxtype} policycoreutils
%description selinux
SELinux policy for the %{name} to ensure the dictionaries installed by the
cracklib-dicts package are reachable by this package.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_datadir}/pgsql/extension/%{name}--*--*.sql %{buildroot}%{_datadir}/%{name}
%if %{with cracklib} && 0%{?with_selinux}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.cil
%oreon_autofiles credcheck-selinux usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if %{with cracklib} && 0%{?with_selinux}
%post selinux

%selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.cil
%postun selinux

if [ $1 -eq 0 ]; then
%selinux_modules_uninstall -s %{selinuxtype} %{name}
fi
%endif
%files -f %{oreon_filedir}/main.list
%files -n credcheck-selinux -f %{oreon_filedir}/credcheck-selinux.list

%changelog

%autochangelog
