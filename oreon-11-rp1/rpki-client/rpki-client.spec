%global source0_hash fdb3b36e8348a97bb9a37986755cdfc3331a47d2fd684f6814d23cdc63efc9ec

%if 0%{?with_snapshot}
%global gitdate              20220207
%global portable_commit      20d0b2306452fedf56b8487e517a59848d246eea
%global portable_shortcommit %(c=%{portable_commit}; echo ${c:0:7})
%global openbsd_commit       0c3ff93cf8e4880e3099a7bbee8956929fd6ceb2
%global openbsd_shortcommit  %(c=%{openbsd_commit}; echo ${c:0:7})
%endif

Summary:        OpenBSD RPKI validator to support BGP Origin Validation
Name:           rpki-client
Version:        9.7
Release:        2%{?with_snapshot:.git%{gitdate}}%{?dist}
# rpki-client itself is ISC but uses other source codes, breakdown:
# BSD-2-Clause: include/sys/tree.h and src/{http,output}.c
# BSD-3-Clause: compat/{setproctitle,vis}.c and include/{sha2_openbsd,vis,sys/queue}.h and src/mkdir.c
# OpenSSL: compat/x509_purp.c
# LicenseRef-Fedora-Public-Domain: include/{{poll,sha2,stdlib,string,unistd},openssl/{asn1,safestack,x509v3}}.h
#                                  and include/sys/{_null,socket,types,wait}.h and compat/explicit_bzero.c
License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND OpenSSL AND LicenseRef-Fedora-Public-Domain
URL:            https://www.rpki-client.org/
%if !0%{?with_snapshot}
Source0:        https://ftp.openbsd.org/pub/OpenBSD/rpki-client/%{name}-%{version}.tar.gz
Source1:        https://ftp.openbsd.org/pub/OpenBSD/rpki-client/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/B5B6416FEA6DDA05EA562A9FCB987F2783972FF9
%else
Source0:        https://github.com/rpki-client/rpki-client-portable/archive/%{portable_commit}/%{name}-portable-%{version}-%{portable_shortcommit}.tar.gz
Source1:        https://github.com/rpki-client/rpki-client-openbsd/archive/%{openbsd_commit}/%{name}-openbsd-%{version}-%{openbsd_shortcommit}.tar.gz
%endif
Source3:        %{name}.sysusersd
Source4:        %{name}.service
Source5:        %{name}.timer
Source6:        %{name}.service.el8
%if !0%{?with_snapshot}
BuildRequires:  gnupg2
%else
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel >= 1.1.0
BuildRequires:  libretls-devel
BuildRequires:  expat-devel
BuildRequires:  rsync
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
Requires:       rsync
%{?systemd_requires}
%{?sysusers_requires_compat}
# https://github.com/rpki-client/rpki-client-portable/commit/764aadf4d8d42ac198def7ef3e8077f0a324276f
ExcludeArch:    %{ix86}

%description
The OpenBSD rpki-client is a free, easy-to-use implementation of the
Resource Public Key Infrastructure (RPKI) for Relying Parties (RP) to
facilitate validation of the Route Origin of a BGP announcement. The
program queries the RPKI repository system, downloads and validates
Route Origin Authorisations (ROAs) and finally outputs Validated ROA
Payloads (VRPs) in the configuration format of OpenBGPD, BIRD, and
also as CSV or JSON objects for consumption by other routing stacks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if !0%{?with_snapshot}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%else
%setup -q -n %{name}-portable-%{portable_commit}
tar xfz %{SOURCE1}
mv -f %{name}-openbsd-%{openbsd_commit} openbsd
./autogen.sh
%endif

%build
%configure \
  --with-user=%{name} \
  --with-tal-dir=%{_sysconfdir}/pki/tals \
  --with-base-dir=%{_localstatedir}/cache/%{name} \
  --with-output-dir=%{_localstatedir}/lib/%{name}
%make_build

%install
%make_install
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/%{name}.timer
%{?el8:install -D -p -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service}

%pre
%sysusers_create_compat %{SOURCE3}

%post
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.timer

%postun
%systemd_postun %{name}.timer

%files
%license LICENSE
%doc AUTHORS README.md
%{_sbindir}/%{name}
%{_sysconfdir}/pki/tals/
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%{_sysusersdir}/%{name}.conf
%{_mandir}/man8/%{name}.8*
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/cache/%{name}/
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/lib/%{name}/

%changelog
%autochangelog
