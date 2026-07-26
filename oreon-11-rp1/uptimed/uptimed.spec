%global source0_hash 2f669d2968ca1d0865b7a97791c9dbcca759631a1afc5d6702964f070a57252b

Summary:	A daemon to record and keep track of system up times
Name:		uptimed
Version:	0.4.7
Release:	4%{?dist}
License:	GPL-2.0-only
URL:		https://github.com/rpodgorny/uptimed/
Source0:	https://github.com/rpodgorny/%{name}/archive/v%{version}.tar.gz
# https://github.com/rpodgorny/uptimed/pull/6
Patch0:		uptimed-0001-systemd-unit-run-as-daemon-user-not-root.patch
%{?systemd_requires}
BuildRequires: make
BuildRequires: systemd
BuildRequires:	autoconf, automake, libtool

%description
Uptimed is an up time record daemon keeping track of the highest
up times the system ever had.

Uptimed has the ability to inform you of records and milestones
though syslog and e-mail, and comes with a console front end to
parse the records, which can also easily be used to show your
records on your Web page

%package devel
Summary:	Development header and library for uptimed
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development header and library for uptimed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# remove bundled getopt
rm -rf src/getopt.[ch]
sed --in-place -e 's/AC_REPLACE_FUNCS(getopt)//' configure.ac
%patch -P0 -p1

%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# remove superfluous file
rm %{buildroot}/%{_libdir}/libuptimed.la
# Debian ships urec.h as uptimed.h since 2005
mkdir %{buildroot}%{_includedir}
cp libuptimed/urec.h %{buildroot}%{_includedir}/uptimed.h
install -m 755 -d %{buildroot}%{_pkgdocdir}/sample-cgi
install -m 644 sample-cgi/uprecords.* %{buildroot}%{_pkgdocdir}/sample-cgi
mv %{buildroot}/etc/uptimed.conf-dist %{buildroot}/%{_sysconfdir}/uptimed.conf
mkdir -p %{buildroot}%{_localstatedir}/spool/uptimed

%post
%systemd_post %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%preun
%systemd_preun %{name}.service

%files
%doc AUTHORS CREDITS ChangeLog INSTALL.cgi INSTALL.upgrade README.md README.unsupported TODO sample-cgi/
%license COPYING
%config(noreplace) %{_sysconfdir}/uptimed.conf
%{_sbindir}/uptimed
%{_bindir}/uprecords
%{_mandir}/*/*
%{_libdir}/libuptimed.so.*
%{_unitdir}/uptimed.service
%dir %attr(-,daemon,daemon) %{_localstatedir}/spool/uptimed

%files devel
%{_libdir}/libuptimed.so
%{_includedir}/uptimed.h

%changelog
%autochangelog
