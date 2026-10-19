%global source0_hash ce5f1a87c566ef0b2897a28f50a75c1dc23fec413a46a7f4183423b6b6aa991b
%global rpcbind_user_group rpc
%global rpcbind_state_dir %{_rundir}/rpcbind
Name:           rpcbind
Version:        1.2.9
Release:        1%{?dist}
Summary:        Universal Addresses to RPC Program Number Mapper
License:        BSD-3-Clause
URL:            http://nfsv4.bullopensource.org
Source0:        https://downloads.sourceforge.net/rpcbind/%{name}-%{version}.tar.bz2
Source1: %{name}.sysconfig
Requires: glibc-common setup
Requires: libtirpc >= 1.3.5
Conflicts: man-pages < 2.43-12
Requires(pre): coreutils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd coreutils
Patch100: rpcbind-0.2.3-systemd-tmpfiles.patch
Patch101: rpcbind-0.2.4-systemd-rundir.patch
Provides: portmap = %{version}-%{release}
Obsoletes: portmap <= 4.0-65.3
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/rpcbind
Provides: /usr/sbin/rpcinfo
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  quota-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
%description
The rpcbind utility is a server that converts RPC program numbers into
universal addresses.  It must be running on the host to be able to make
RPC calls on a server on that machine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Create a sysusers.d config file
cat >rpcbind.sysusers.conf <<EOF
u rpc 32 'Rpcbind Daemon' /var/lib/rpcbind -
EOF

%build

autoreconf -fisv
%configure \
    --enable-warmstarts \
    --with-statedir="%rpcbind_state_dir" \
    --with-rpcuser="%rpcbind_user_group" \
    --with-nss-modules="files altfiles" \
    --sbindir=%{_bindir} \
    --enable-rmtcalls \
    --enable-debug
make all
%install
mkdir -p %{buildroot}{%{_sbindir},%{_bindir},/etc/sysconfig}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{rpcbind_state_dir}
make DESTDIR=$RPM_BUILD_ROOT install
install -m644 %{SOURCE1} %{buildroot}/etc/sysconfig/rpcbind
%if "%{_sbindir}" != "%{_bindir}"
cd ${RPM_BUILD_ROOT}%{_sbindir}
ln -sf ../bin/rpcbind
ln -sf ../bin/rpcinfo
%endif
install -m0644 -D rpcbind.sysusers.conf %{buildroot}%{_sysusersdir}/rpcbind.conf
%oreon_autofiles main

%post

%systemd_post rpcbind.service rpcbind.socket
%preun

%systemd_preun rpcbind.service rpcbind.socket
%postun

%systemd_postun_with_restart rpcbind.socket
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
