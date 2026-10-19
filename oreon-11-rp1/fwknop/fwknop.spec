%global source1_hash 587a1c7c07df142fa4be60eff641d29846137b043ae6bb10570549136f179273
%global source0_hash a4ec7c22dd90dd684f9f7b96d3a901c4131ec8c7a3b9db26d0428513f6774c64
Summary:        A Single Packet Authorization (SPA) implementation
Name: fwknop
Version: 2.6.11
Release:        1%{?dist}
License: GPL-2.0-only
Url: http://www.cipherdyne.org/fwknop/
Source0:        http://cipherdyne.org/fwknop/download/fwknop-%{version}.tar.bz2
Source1: http://cipherdyne.org/fwknop/download/fwknop-%{version}.tar.bz2.asc
Source2: fwknopd.service
Requires: logrotate
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  firewalld
BuildRequires:  gcc
BuildRequires:  gpg
BuildRequires:  gpgme-devel
BuildRequires:  iptables
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%package devel
Summary:    The fwknop library, header and API docs
Requires:   gpg, gpgme
Requires: %{name}%{?_isa} >= %{version}-%{release}
%description
fwknop implements an authorization scheme known as Single Packet
Authorization (SPA) that requires only a single encrypted packet to
communicate various pieces of information including desired access through an
iptables policy and/or specific commands to execute on the target system.
The main application of this program is to protect services such as SSH with
an additional layer of security in order to make the exploitation of
vulnerabilities (both 0-day and unpatched code) much more difficult.  The
authorization server passively monitors authorization packets via libpcap and
hence there is no "server" to which to connect in the traditional sense.  Any
service protected by fwknop is inaccessible (by using iptables to
intercept packets within the kernel) before authenticating; anyone scanning for
the service will not be able to detect that it is even listening.  This
authorization scheme offers many advantages over port knocking, include being
non-replayable, much more data can be communicated, and the scheme cannot be
broken by simply connecting to extraneous ports on the server in an effort to
break knock sequences.  The authorization packets can easily be spoofed as
well, and this makes it possible to make it appear as though, say,
www.yahoo.com is trying to authenticate to a target system but in reality the
actual connection will come from a seemingly unrelated IP. Although the
default data collection method is to use libpcap to sniff packets off the
wire, fwknop can also read packets out of a file that is written by the
iptables ulogd pcap writer or by a separate sniffer process.

%description devel
The Firewall Knock Operator library, libfko, provides the Single Packet
Authorization implementation and API for the other fwknop components.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --with-firewall-cmd=/usr/bin/firewall-cmd --with-gpgme
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} -j1 OPTS="$RPM_OPT_FLAGS"
%check

%install
%make_install
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/fwknopd.service
rm $RPM_BUILD_ROOT/%{_libdir}/libfko.{la,a}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post fwknopd.service
%preun

%systemd_preun fwknopd.service
%postun

%systemd_postun_with_restart fwknopd.service
%triggerun -- fwknop < 2.0-2

/usr/bin/systemd-sysv-convert --save fwknopd >/dev/null 2>&1 ||:
/sbin/chkconfig --del fwknopd >/dev/null 2>&1 || :
/bin/systemctl try-restart fwknopd.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list
%files -n fwknop-devel -f %{oreon_filedir}/fwknop-devel.list

%changelog

%autochangelog
