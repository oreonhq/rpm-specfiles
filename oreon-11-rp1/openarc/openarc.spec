%global source0_hash 6a68ecf6335504438648c93930296d1c2f15a9ad90996d25818e745c8ebdf2bc

%global baserelease 1
#global pre_rel Beta3

Summary: An open source library and milter for providing ARC service
Name: openarc
Version: 1.3.0
Release: %{?pre_rel:0.}%{baserelease}%{?pre_rel:.%pre_rel}%{?dist}
# Automatically converted from old format: BSD and Sendmail - review is highly recommended.
License: LicenseRef-Callaway-BSD AND Sendmail-8.23
URL: https://github.com/flowerysong/OpenARC
Source0: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(libidn2)
BuildRequires: pkgconfig(openssl)
BuildRequires: sendmail-milter-devel
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: systemd-rpm-macros
%else
BuildRequires: systemd
%endif

Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: libopenarc = %{version}-%{release}
%{?systemd_requires}
Requires: group(mail)

%description
The Trusted Domain Project is a community effort to develop and maintain a
C library for producing ARC-aware applications and an open source milter for
providing ARC service through milter-enabled MTAs.

%package -n libopenarc
Summary: An open source ARC library

%description -n libopenarc
This package contains the library files required for running services built
using libopenarc.

%package -n libopenarc-devel
Summary: Development files for libopenarc
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n libopenarc-devel
This package contains the static libraries, headers, and other support files
required for developing applications against libopenarc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Previously, a non-system group was created :(, sysusers does not support this
# Create a sysusers.d config file
cat >openarc.sysusers.conf <<EOF
u openarc - - %{_localstatedir}/lib/%{name} -
m openarc mail
EOF

%build
%if 0%{?fedora} >= 42
# Workaround bug in libmilter/mfapi.h with gcc15
# See https://bugzilla.redhat.com/show_bug.cgi?id=2336394
export CFLAGS="%{optflags} --std=gnu17"
%endif
autoreconf --install
%configure --disable-static
%make_build

%install
%make_install
mkdir -p -m 0700 %{buildroot}%{_sysconfdir}/%{name}
mkdir -p -m 0750 %{buildroot}%{_rundir}/%{name}
rm -r %{buildroot}%{_prefix}/share/doc/openarc
rm %{buildroot}/%{_libdir}/*.la

cat > %{buildroot}%{_sysconfdir}/openarc.conf <<EOF
## See openarc.conf(5) or %{_docdir}/%{name}/openarc.conf.sample for more
#PidFile %{_rundir}/%{name}/%{name}.pid
Syslog  yes
UserID  openarc:openarc
Socket  local:%{_rundir}/%{name}/%{name}.sock
SignHeaders to,subject,message-id,date,from,mime-version,dkim-signature
PeerList %{_sysconfdir}/%{name}/PeerList
MilterDebug 6
EnableCoredumps yes

## After setting Mode to "sv", running
## opendkim-genkey -D %{_sysconfdir}/openarc -s key -d `hostname --domain`
## and putting %{_sysconfdir}/openarc
#Mode                    sv
#Canonicalization        relaxed/simple
#Domain                  example.com # change to domain
#Selector                key
#KeyFile                 %{_sysconfdir}/openarc/key.private
#SignatureAlgorithm rsa-sha256
EOF

# Don't sign or validate connections from localhost
cat > %{buildroot}%{_sysconfdir}/%{name}/PeerList <<EOF
127.0.0.1/32
[::1]/128
EOF
chmod 0640 %{buildroot}%{_sysconfdir}/%{name}/PeerList

install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 contrib/systemd/openarc.service %{buildroot}%{_unitdir}/

install -m0644 -D openarc.sysusers.conf %{buildroot}%{_sysusersdir}/openarc.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%ldconfig_scriptlets -n libopenarc

%files
%license LICENSE LICENSE.Sendmail
%doc README.md CHANGELOG.md %{name}/%{name}.conf.sample
%dir %attr(0755,root,%{name}) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0644,root,%{name}) %{_sysconfdir}/%{name}.conf
%config(noreplace) %attr(0440,%{name},%{name}) %{_sysconfdir}/%{name}/PeerList
%{_unitdir}/%{name}.service
%{_mandir}/man1/openarc-keygen.1*
%{_mandir}/man5/openarc.conf.5*
%{_mandir}/man8/openarc.8*
%{_bindir}/openarc-keygen
%{_sbindir}/openarc
%{_sysusersdir}/openarc.conf

%files -n libopenarc
%license LICENSE LICENSE.Sendmail
%{_libdir}/libopenarc.so.1
%{_libdir}/libopenarc.so.1.1.0

%files -n libopenarc-devel
%{_includedir}/openarc/
%{_libdir}/libopenarc.so
%{_libdir}/pkgconfig/openarc.pc

%changelog
%autochangelog
