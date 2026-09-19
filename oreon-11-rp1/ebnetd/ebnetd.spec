%global source0_hash a69e5cbf085abd3d3e72212af787a93eb5b8a2dac8d11a77f753dafb0f527483

%global _hardened_build 1

%global username	ebnetd
%global gecos		EBNET User
%global base_homedir	%{_localstatedir}/lib/
%global homedir		%{base_homedir}%{username}

Name:		ebnetd
Version:	1.0
Release:	56%{?dist}
License:	GPL-2.0-or-later
URL:		http://www.sra.co.jp/people/m-kasahr/ebnetd/
# For systemd.macros
BuildRequires:	systemd
BuildRequires:	eb-devel
BuildRequires:	gcc autoconf automake libtool
BuildRequires: make

Source0:	ftp://ftp.sra.co.jp/pub/misc/eb/%{name}-%{version}.tar.gz
Source1:	ebhttpd-README.dist
Source2:	%{name}-tmpfiles.conf
Source11:	ebnetd.socket
Source12:	ebnetd@.service
Source13:	ebnetd-instances.target
Source21:	ndtpd.socket
Source22:	ndtpd@.service
Source23:	ndtpd-instances.target
Source31:	ebhttpd.socket
Source32:	ebhttpd@.service
Source33:	ebhttpd-instances.target
Patch0:		ebnetd-1.0-info.patch
Patch1:		%{name}-aarch64.patch
Patch2:		%{name}-fix-conflict.patch
Patch3:		%{name}-gcc10.patch
Patch4:		%{name}-fedora-c99.patch
Patch5:		%{name}-fix-build.patch
Patch6:		%{name}-ftbfs.patch

Summary:	EBNET protocol server
Requires:	%{name}-common = %{version}-%{release}

%description
EBNET is a protocol to communicate to the EB library that is a C library
for accessing "CD-ROM books".

This package contains a EBNET protocol server.

%package common
Summary:		Common package for ebnetd families
%{?systemd_requires}

%description common
EBNET is a protocol to communicate to the EB library that is a C library
for accessing "CD-ROM books".

This package contains a bunch of the common programs/files to be shared
by ebnetd families.

%package -n ndtpd
Summary:	Network Dictionary Transfer Protocol server
Requires:	%{name}-common = %{version}-%{release}

%description -n ndtpd
This package contains a daemon program to speak Network Dictionary Transfer
Protocol.

%package -n ebhttpd
Summary:	HTTP server for accessing "CD-ROM books"
Requires:	%{name}-common = %{version}-%{release}

%description -n ebhttpd
This package contains a specialized HTTP server that supports HTTP/1.0 and
HTTP/1.1. which provide a way to access "CD-ROM books" through the EB library.

Note that ebhttpd can't be used for generic WWW purposes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp -p %{SOURCE1} .
autoreconf -i # to remove the unnecessary checking like g++

# Create a sysusers.d config file
cat >ebnetd.sysusers.conf <<EOF
u ebnetd - '%{gecos}' %{homedir} -
EOF

%build
%configure --disable-static --enable-ipv6 --with-eb-conf=%{_libdir}/eb.conf --with-logdir=%{_localstatedir}/log/ebnetd --localstatedir=%{base_homedir}

make

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

install -d $RPM_BUILD_ROOT%{_localstatedir}/run/ebnetd
install -d $RPM_BUILD_ROOT%{_tmpfilesdir}
install -d $RPM_BUILD_ROOT/lib/systemd/system
install -p -m0644 %{SOURCE11} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE21} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE31} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE12} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE22} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE32} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE13} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE23} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE33} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf

# correct timestamp
## for patch0
touch -r doc/ebnetd.info-1 doc/ebnetd.info
touch -r doc-ja/ebnetd-ja.info-1 doc/ebnetd-ja.info

for i in `echo $RPM_BUILD_ROOT%{_infodir}/ebnetd-ja*`; do
	iconv -f euc-jp -t utf-8 $i > $i-utf8 && mv $i-utf8 $i && touch -r doc-ja/`basename $i` $i
done

sed -i	-e 's/^\(user[ 	]*\)[a-z].*$/\1ebnetd/' \
	-e 's/^\(group[ 	]*\)[a-z].*$/\1ebnetd/' \
	-e 's,^\# \(work-path[ 	]*\)[a-z/].*$,\1/var/run/ebnetd,' \
	-e 's/^\(syslog-facility[ 	]*\)[a-z0-9].*$/\1daemon/' \
	-e '/^begin .*$/,/^end$/{D}' $RPM_BUILD_ROOT%{_sysconfdir}/ebnetd.conf.sample && \
mv $RPM_BUILD_ROOT%{_sysconfdir}/ebnetd.conf{.sample,} && \
touch -r ebnetd.conf.sample $RPM_BUILD_ROOT%{_sysconfdir}/ebnetd.conf

mkdir -p $RPM_BUILD_ROOT%{homedir} || :

# remove unnecessary files
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

install -m0644 -D ebnetd.sysusers.conf %{buildroot}%{_sysusersdir}/ebnetd.conf

%post
%systemd_post ebnetd.socket

%preun
%systemd_preun ebnetd.socket ebnetd-instances.target

%postun
%systemd_postun_with_restart ebnetd.socket ebnetd-instances.target

%post	-n ndtpd
%systemd_post ndtpd.socket

%preun	-n ndtpd
%systemd_preun ndtpd.socket ndtpd-instances.target

%postun	-n ndtpd
%systemd_postun_with_restart ndtpd.socket ndtpd-instances.target

%post	-n ebhttpd
%systemd_post ebnttpd.socket

%preun	-n ebhttpd
%systemd_preun ebhttpd.socket ebhttpd-instances.target

%postun	-n ebhttpd
%systemd_postun_with_restart ebhttpd.socket ebhttpd-instances.target

%files
%{_sbindir}/ebnetd
%{_sbindir}/ebncontrol
%{_sbindir}/ebncheck
%{_libexecdir}/ebnstat
/lib/systemd/system/ebnetd.socket
/lib/systemd/system/ebnetd@.service
/lib/systemd/system/ebnetd-instances.target

%files common
%license COPYING
%doc AUTHORS ChangeLog NEWS README UPGRADE
%lang(ja) %doc README-ja UPGRADE-ja
%{_sbindir}/ebndaily
%{_sbindir}/ebnupgrade
%{_infodir}/ebnetd.info*
%lang(ja) %doc %{_infodir}/ebnetd-ja.info*
%config(noreplace) %{_sysconfdir}/ebnetd.conf
%attr (-, ebnetd, ebnetd) %{homedir}
%attr (-, ebnetd, ebnetd) %{_localstatedir}/run/ebnetd
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/ebnetd.conf

%files -n ndtpd
%{_sbindir}/ndtp*
%{_libexecdir}/ndtpstat
/lib/systemd/system/ndtpd.socket
/lib/systemd/system/ndtpd@.service
/lib/systemd/system/ndtpd-instances.target

%files -n ebhttpd
%doc ebhttpd-README.dist
%{_sbindir}/ebht*
%{_libexecdir}/ebhtstat
/lib/systemd/system/ebhttpd.socket
/lib/systemd/system/ebhttpd@.service
/lib/systemd/system/ebhttpd-instances.target

%changelog
%autochangelog
