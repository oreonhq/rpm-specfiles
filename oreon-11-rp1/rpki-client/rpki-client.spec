%global source2_hash 075ad8bb1743e16bee3ac99b840e844ac169b3757ba96c98dab1762e666d398f
%global source1_hash 890c580155f2c49340915cf864374965887150167430f4534910cf0175799b0b
%global source0_hash 24985845b7283b071942c9fa44598517461211ee32a690a219ba81a14835e8c8
%if 0%{?with_snapshot}
%global gitdate              20220207
%global portable_commit      20d0b2306452fedf56b8487e517a59848d246eea
%global portable_shortcommit %(c=%{portable_commit}; echo ${c:0:7})
%global openbsd_commit       0c3ff93cf8e4880e3099a7bbee8956929fd6ceb2
%global openbsd_shortcommit  %(c=%{openbsd_commit}; echo ${c:0:7})
%endif
Summary:        OpenBSD RPKI validator to support BGP Origin Validation
Name:           rpki-client
Version:        9.9
Release:        1%{?dist}
License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND OpenSSL AND LicenseRef-Fedora-Public-Domain
URL:            https://www.rpki-client.org/
%if !0%{?with_snapshot}
Source0:        https://ftp.openbsd.org/pub/OpenBSD/rpki-client/%{name}-%{version}.tar.gz
Source1:        https://ftp.openbsd.org/pub/OpenBSD/rpki-client/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/B5B6416FEA6DDA05EA562A9FCB987F2783972FF9
%else
Source1:        https://github.com/rpki-client/rpki-client-openbsd/archive/%{openbsd_commit}/%{name}-openbsd-%{version}-%{openbsd_shortcommit}.tar.gz
%endif
Source3:        %{name}.sysusersd
Source4:        %{name}.service
Source5:        %{name}.timer
Source6:        %{name}.service.el8
%if !0%{?with_snapshot}
%else
%endif
Requires:       rsync
%{?systemd_requires}
%{?sysusers_requires_compat}
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libretls-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  rsync
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%pre

%sysusers_create_compat %{SOURCE3}
%post

%systemd_post %{name}.timer
%preun

%systemd_preun %{name}.timer
%postun

%systemd_postun %{name}.timer
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
