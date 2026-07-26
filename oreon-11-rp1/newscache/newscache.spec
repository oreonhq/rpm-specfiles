%global source0_hash 755cdcac06d40fcca2b221f840e05f89a86298bc3bfc518b51a57b42f0512b19

%define srcnamever	NewsCache-1.2rc6
%define socketver	1.12.13

Name: 		newscache
Summary: 	Free cache server for USENET News
Version: 	1.2
Release: 	0.54.rc6%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/hstraub/NewsCache
Source0: 	http://src.linuxhacker.at/NewsCache/%{srcnamever}.tar.gz
Source1:	http://src.linuxhacker.at/socket++/socket++-%{socketver}.tar.gz
Source2:	%{name}.init
Source3:	%{name}.service
Patch1:		newscache-1.2rc6-config.patch
Patch2:		newscache-1.2rc6-gcc43.patch
Patch3:		socket++-1.12.12-drop_doc.patch
Patch4:		newscache-glibc.patch
BuildRequires: make
BuildRequires: libxcrypt-devel
BuildRequires:  gcc-c++
BuildRequires:	libtool, texinfo, pam-devel
BuildRequires:	systemd-units

Requires(post):	systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
NewsCache is a free cache server for USENET News. NewsCache acts to
news reading clients like a news server, except that it stores only
those articles that have been requested by at least one client.
NewsCache targets problems of the current News System like network
bandwidth consumption or the IO load caused by news clients.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcnamever} -a 1

cp etc/newscache.conf-dist newscache.conf
%patch -P1 -p0
%patch -P2 -p1

#  to satisfy g++ >= 8.0
sed -i 's/^main/int main/' configure.in

#  place socket++ source at least 2 level deeper,
#  to avoid autotools inheritance with the newscache sources...
mkdir -p too/deep
mv socket++-%{socketver} too/deep

pushd too/deep/socket++-%{socketver}
%patch -P3 -p1
popd

%patch -P4 -p1

# Create a sysusers.d config file
cat >newscache.sysusers.conf <<EOF
u news - 'News user' /etc/news -
EOF

%build

# socket++ is a library from the same site as NewScache.
# While it is used by newscache only, there is no reason
# to ship it separately.

pushd too/deep/socket++-%{socketver}
./autogen
%configure --enable-static --disable-shared
make %{?_smp_mflags}
popd

SOCKDIR=$PWD/too/deep/socket++-%{socketver}
export CPPFLAGS=-I$SOCKDIR
export LDFLAGS=-L$SOCKDIR/socket++/.libs 

./autogen
%configure --with-pam
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/newscache.conf-dist
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/newscache.auth-dist

# info stuff is too obsolete
rm -f $RPM_BUILD_ROOT%{_infodir}/*

install -d $RPM_BUILD_ROOT%{_localstatedir}/cache/newscache

install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -m644 -p newscache.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

#install -d $RPM_BUILD_ROOT%{_initrddir}
#install -m755 -p %SOURCE2 $RPM_BUILD_ROOT%{_initrddir}/%{name}

install -d $RPM_BUILD_ROOT%{_unitdir}
install -p -m644 %SOURCE3 $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

install -d $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
pushd $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
cat <<EOF >%{name}
#%PAM-1.0
auth    include		password-auth
account include		password-auth

EOF
popd

install -d $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
pushd $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
cat <<EOF >%{name}
#!/bin/bash
/usr/sbin/newscacheclean

EOF
chmod 755 %{name}
popd

install -m0644 -D newscache.sysusers.conf %{buildroot}%{_sysusersdir}/newscache.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%attr(755,news,news) %dir %{_localstatedir}/cache/newscache
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/cron.daily/*
#%config(noreplace) %{_initrddir}/*
%{_unitdir}/%{name}.service
%{_bindir}/*
%{_sbindir}/*
%doc AUTHORS COPYING NEWS README THANKS TODO
%doc doc/newscache*.txt etc/*-dist
%{_mandir}/*/*
%{_sysusersdir}/newscache.conf

%changelog
%autochangelog
