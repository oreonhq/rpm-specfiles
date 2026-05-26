# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 964132c389918e8964d7334936b6dd10ef025b300c6b29e693ba0f29550e3de5
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# These are macros to be usable outside of the build section
%global rpcbind_user_group rpc
%global rpcbind_state_dir %{_rundir}/rpcbind

Name:           rpcbind
Version:        1.2.8
Release:        1%{?dist}
Summary:        Universal Addresses to RPC Program Number Mapper
License:        BSD-3-Clause
URL:            http://nfsv4.bullopensource.org

Source0:        http://downloads.sourceforge.net/rpcbind/%{name}-%{version}.tar.bz2
Source1: %{name}.sysconfig

Requires: glibc-common setup
Requires: libtirpc >= 1.3.5
Conflicts: man-pages < 2.43-12
BuildRequires: make
BuildRequires: automake, autoconf, libtool, systemd, systemd-devel
BuildRequires: libtirpc-devel, quota-devel
Requires(pre): coreutils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd coreutils

Patch100: rpcbind-0.2.3-systemd-tmpfiles.patch
Patch101: rpcbind-0.2.4-systemd-rundir.patch

Provides: portmap = %{version}-%{release}
Obsoletes: portmap <= 4.0-65.3

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/rpcbind
Provides: /usr/sbin/rpcinfo
%endif

%description
The rpcbind utility is a server that converts RPC program numbers into
universal addresses.  It must be running on the host to be able to make
RPC calls on a server on that machine.

%prep
%oreon_verify_sources
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
# The binaries now live in /usr/bin, moving from /usr/sbin
# For compatibility create a couple symlinks. 
cd ${RPM_BUILD_ROOT}%{_sbindir}
ln -sf ../bin/rpcbind
ln -sf ../bin/rpcinfo
%endif

install -m0644 -D rpcbind.sysusers.conf %{buildroot}%{_sysusersdir}/rpcbind.conf

%post
%systemd_post rpcbind.service rpcbind.socket

%preun
%systemd_preun rpcbind.service rpcbind.socket

# NOTE: We only restart rpcbind.socket in the %postun scriptlet in order to
# avoid the race described in:
#
# https://github.com/systemd/systemd/issues/13271
# https://github.com/systemd/systemd/issues/8102
#
# Restarting rpcbind.socket causes rpcbind.service to be restarted automatically
# due to "Requires=rpcbind.socket" in the rpcbind.service unit file.
%postun
%systemd_postun_with_restart rpcbind.socket

%files
%license COPYING
%config(noreplace) /etc/sysconfig/rpcbind
%doc AUTHORS ChangeLog README
%{_bindir}/rpcbind
%{_bindir}/rpcinfo
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/rpcbind
%{_sbindir}/rpcinfo
%endif
%{_mandir}/man8/*
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_tmpfilesdir}/%{name}.conf
%attr(0700, %{rpcbind_user_group}, %{rpcbind_user_group}) %dir %{rpcbind_state_dir}
%{_sysusersdir}/rpcbind.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.8-1
- Prepare for Oreon 11 (RP1)
