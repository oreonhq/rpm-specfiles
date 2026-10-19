%global source0_hash 6cdbeb588c636ca2c19511af49ce56c8903ac264fcfed5fd759fdbedfea1b3a0
Name:		maradns
Version:	3.5.0036
Release:        9%{?dist}
Summary:        Authoritative and recursive DNS server made with security in mind
Source0:        http://www.maradns.org/download/3.5/%{version}/%{name}-%{version}.tar.xz
Patch0:		%{name}-0001-add-systemd-unit-files.patch
Patch1:		%{name}-0002-fix-prototypes-and-signal-handlers.patch
License:	BSD-2-Clause
URL:		http://www.maradns.org/
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
MaraDNS is a package that implements the Domain Name Service (DNS), an
essential internet service. MaraDNS has the following advantages:
	* Secure.
	* Supported.
	* Easy to use.
	* Small.
	* Open Source.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch -p1

# Create a sysusers.d config file
cat >maradns.sysusers.conf <<EOF
u maradns - 'MaraDns chroot user' /etc/maradns -
EOF

%build

./configure --ipv6 --libdir=%{_libdir}
pushd deadwood-%{version}/src
make %{?_smp_mflags} FLAGS="%{optflags} -lrt"
popd
make %{?_smp_mflags} FLAGS="%{optflags} -DSELECT_PROBLEM -DAUTHONLY"
%install
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/maradns/logger/
install -p -D -m 0644 doc/en/examples/example_mararc %{buildroot}%{_sysconfdir}/mararc
install -p -D -m 0644 deadwood-%{version}/doc/dwood3rc %{buildroot}%{_sysconfdir}/dwood3rc
install -p -d -m 0755 %{buildroot}/var/cache/deadwood
install -p -D -m 0755 server/maradns %{buildroot}%{_sbindir}/maradns
install -p -D -m 0755 tcp/zoneserver %{buildroot}%{_sbindir}/zoneserver
install -p -D -m 0755 deadwood-%{version}/src/Deadwood %{buildroot}%{_sbindir}/Deadwood
install -p -D -m 0755 tcp/getzone %{buildroot}%{_bindir}/getzone
install -p -D -m 0755 tcp/fetchzone %{buildroot}%{_bindir}/fetchzone
install -p -D -m 0755 tools/askmara %{buildroot}%{_bindir}/askmara
install -p -d -m 0755 %{buildroot}%{_mandir}/man{1,5,8}
install -p -D -m 0644 -t %{buildroot}%{_mandir}/man1/ \
	doc/en/man/askmara.1 \
	doc/en/man/getzone.1 \
	doc/en/man/fetchzone.1
install -p -D -m 0644 -t %{buildroot}%{_mandir}/man1/ \
	deadwood-%{version}/doc/Deadwood.1
install -p -D -m 0644 -t %{buildroot}%{_mandir}/man5/ \
	doc/en/man/csv1.5 \
	doc/en/man/csv2.5 \
	doc/en/man/csv2_txt.5 \
	doc/en/man/mararc.5
install -p -D -m 0644 -t %{buildroot}%{_mandir}/man8/ \
	doc/en/man/maradns.8 \
	doc/en/man/zoneserver.8 \
mkdir -p %{buildroot}%{_unitdir}
install -p -D -m 0644 -t %{buildroot}%{_unitdir}/ \
	build/maradns.service \
	build/maradns-zoneserver.service \
	build/maradns-deadwood.service
install -m0644 -D maradns.sysusers.conf %{buildroot}%{_sysusersdir}/maradns.conf
%oreon_autofiles main

%post

if [ $1 -eq 1 ]; then
	sed --in-place -e "s/^maradns_uid.*/maradns_uid = $(id -u maradns)/" %{_sysconfdir}/mararc
	sed --in-place -e "s/^maradns_gid.*/maradns_gid = $(id -g maradns)/" %{_sysconfdir}/mararc
	sed --in-place -e "s/^maradns_uid.*/maradns_uid = $(id -u maradns)/" %{_sysconfdir}/dwood3rc
	sed --in-place -e "s/^maradns_gid.*/maradns_gid = $(id -g maradns)/" %{_sysconfdir}/dwood3rc
	sed --in-place -e 's@/etc/deadwood@/var/cache/deadwood@' %{_sysconfdir}/dwood3rc
fi
%systemd_post maradns.service maradns-zoneserver.service maradns-deadwood.service
%preun

%systemd_preun maradns.service maradns-zoneserver.service maradns-deadwood.service
%postun

%systemd_postun_with_restart maradns.service maradns-zoneserver.service maradns-deadwood.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
