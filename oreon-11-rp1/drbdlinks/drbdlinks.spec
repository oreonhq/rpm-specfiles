%global source0_hash 52f536c1bdcf5532fe4aaf6338c5296a8dfd7efe0557c55c55d42b2b5dc3e04c

Summary:           Program for managing links into a DRBD shared partition
Name:              drbdlinks
Version:           1.29
Release:           16%{?dist}
License:           GPL-2.0-only
URL:               https://www.tummy.com/software/drbdlinks/
Source0:           https://github.com/linsomniac/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz
Source1:           drbdlinks.logrotate
Source2:           drbdlinksclean.service
Source3:           drbdlinksclean-wrapper
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:          python3
BuildRequires:     python3-devel
%else
Requires:          python2
BuildRequires:     python2
%endif
BuildRequires:     make
BuildRequires:     systemd-rpm-macros
BuildArch:         noarch
%{?systemd_requires}

%description
The drbdlinks program manages links into a DRBD partition which is shared
among several machines. A simple configuration file, "/etc/drbdlinks.conf",
specifies the links. This can be used to manage e.g. links for /etc/httpd,
/var/lib/pgsql and other system directories that need to appear as if they
are local to the system when running applications after the drbd shared
partition has been mounted.

When running drbdlinks with "start" as the mode, drbdlinks will rename the
existing files/directories and then make symbolic links into the DRBD
partition, "stop" does the reverse. By default, rename appends ".drbdlinks"
to the name, but this can be overridden.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-release-%{version}

%build

%install
install -D -p -m 755 %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
%if 0%{?fedora} || 0%{?rhel} >= 8
sed -e '1 s|^#!.*python|#!%{__python3}|g' -i $RPM_BUILD_ROOT%{_sbindir}/%{name}
%else
sed -e '1 s|^#!.*python|#!%{__python}|g' -i $RPM_BUILD_ROOT%{_sbindir}/%{name}
%endif
touch -c -r %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir}/%{name}.d,/usr/lib/ocf/resource.d/tummy}/
ln -s ../../../../..%{_sbindir}/%{name} $RPM_BUILD_ROOT/usr/lib/ocf/resource.d/tummy/%{name}
install -D -p -m 644 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install -D -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/drbdlinksclean.service
install -D -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_libexecdir}/drbdlinksclean
install -D -p -m 644 %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8
install -D -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/configs-to-clean

mv -f README.markdown README

%check
make -C tests DRBDLINKS=$RPM_BUILD_ROOT%{_sbindir}/%{name}

%post
%systemd_post drbdlinksclean.service

%preun
%systemd_preun drbdlinksclean.service

%postun
%systemd_postun drbdlinksclean.service

%files
%license LICENSE
%doc README WHATSNEW
%{_unitdir}/drbdlinksclean.service
%{_libexecdir}/drbdlinksclean
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}.d/
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_sbindir}/%{name}
/usr/lib/ocf/resource.d/tummy/
%{_mandir}/man8/%{name}.8*
%{_localstatedir}/lib/%{name}/

%changelog
%autochangelog
