%global source0_hash 52f536c1bdcf5532fe4aaf6338c5296a8dfd7efe0557c55c55d42b2b5dc3e04c
Summary:        Program for managing links into a DRBD shared partition
Name:              drbdlinks
Version:           1.29
Release:        1%{?dist}
License:           GPL-2.0-only
URL:               https://www.tummy.com/software/drbdlinks/
Source0:        https://github.com/linsomniac/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz
Source1:           drbdlinks.logrotate
Source2:           drbdlinksclean.service
Source3:           drbdlinksclean-wrapper
Requires:          python2
BuildArch:         noarch
%{?systemd_requires}
# oreon:deps
BuildRequires:  make
BuildRequires:  python2
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
sed -e '1 s|^#!.*python|#!%{__python}|g' -i $RPM_BUILD_ROOT%{_sbindir}/%{name}
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
%oreon_autofiles main

%check

make -C tests DRBDLINKS=$RPM_BUILD_ROOT%{_sbindir}/%{name}
%post

%systemd_post drbdlinksclean.service
%preun

%systemd_preun drbdlinksclean.service
%postun

%systemd_postun drbdlinksclean.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
