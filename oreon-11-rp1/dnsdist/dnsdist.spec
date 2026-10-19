%global source0_hash 9fcb469d7a1b5116606f2563761343d1c595523c1fd67808835fa4edc03c24ce
%ifarch %{nodejs_arches}
%if "0%{?el7}" == "0"
%global uglify 1
%endif
%endif
Name: dnsdist
Version: 2.1.2
Release:        1%{?dist}
Summary:        Highly DNS-, DoS- and abuse-aware loadbalancer
License: GPL-2.0-only
URL: https://dnsdist.org
Source0:        https://downloads.powerdns.com/releases/%{name}-%{version}.tar.xz
ExcludeArch: %{ix86} #1994125
ExcludeArch: armv7hl #1994125
%ifarch %{ix86} x86_64 %{mips} aarch64
%else
%endif
%if 0%{?uglify}
%endif
Requires(post): systemd
Requires(preun): shadow-utils
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cargo-rpm-macros
BuildRequires:  fstrm-devel
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  libcap-devel
BuildRequires:  libedit-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libsodium-devel
BuildRequires:  lmdb-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  protobuf-devel
BuildRequires:  python3-pyyaml
BuildRequires:  re2-devel
BuildRequires:  readline-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
BuildRequires:  tinycdb-devel
# /oreon:deps
%description
dnsdist is a highly DNS-, DoS- and abuse-aware loadbalancer. Its goal in life
is to route traffic to the best server, delivering top performance to
legitimate users while shunting or blocking abusive traffic.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p2

# run as dnsdist user
sed -i '/^ExecStart/ s/dnsdist/dnsdist -u dnsdist -g dnsdist/' dnsdist.service.in

# Create a sysusers.d config file
cat >dnsdist.sysusers.conf <<EOF
u dnsdist - 'dnsdist user' - -
EOF
cd dnsdist-rust-lib/rust

%build

%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --disable-static \
    --disable-dependency-tracking \
    --disable-silent-rules \
    --enable-dnscrypt \
    --enable-dns-over-https \
    --enable-dns-over-tls \
    --enable-unit-tests \
    --enable-yaml \
    --with-cdb \
    --with-lmdb \
    --with-nghttp2 \
    --with-re2
rm html/js/*
%if 0%{?uglify}
make min_js
%else
cp src_js/*.js html/js
rename .js .min.js html/js/*.js
%endif
pushd dnsdist-rust-lib/rust
cargo generate-lockfile --offline
popd
make %{?_smp_mflags}
%{__cp} dnsdist.conf-dist dnsdist.conf.sample
%install
make install DESTDIR=%{buildroot}
install -D -p -m 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -d %{buildroot}%{_sysconfdir}/%{name}/
%{__mv} %{buildroot}%{_sysconfdir}/%{name}/dnsdist.conf-dist %{buildroot}%{_sysconfdir}/%{name}/dnsdist.conf
chmod 0640 %{buildroot}/%{_sysconfdir}/%{name}/dnsdist.conf
install -m0644 -D dnsdist.sysusers.conf %{buildroot}%{_sysusersdir}/dnsdist.conf
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
