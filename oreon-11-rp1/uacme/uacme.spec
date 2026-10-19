%global source0_hash de7588577f8298dcb0d42dfaa9452a918fa692c4e165060207ac22f72fb0425d
Name:           uacme
Version:        1.8.1 
Release:        1%{?dist}
Summary:        Lightweight SSL certificate verification and issue client
License:        GPL-3.0-only
URL:            https://github.com/ndilieto/uacme
Source0:        https://github.com/ndilieto/%{name}/archive/upstream/%{version}/%{name}-%{version}.tar.gz
Requires:       curl
Requires:       gnutls
Requires:       libev
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  libcurl-devel
BuildRequires:  libev-devel
BuildRequires:  make
BuildRequires:  which
# /oreon:deps
%description
A lightweight client for the RFC8555 ACMEv2 protocol, 
written in plain C with minimal dependencies. The 
ACMEv2 protocol allows a Certificate Authority and an 
applicant to automate the process of verification and 
certificate issuance. The protocol also provides 
facilities for other certificate management functions, 
such as certificate revocation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-upstream-%{version}
# remove bundled library
rm -rvf libev

%build

%{set_build_flags}; \
%{_configure} --host=%{_host} --build=%{_build} \
      --program-prefix=%{?_program_prefix} \
      --disable-dependency-tracking \
      --prefix=%{_prefix} \
      --exec-prefix=%{_exec_prefix} \
      --bindir=%{_bindir} \
      --sbindir=%{_sbindir} \
      --sysconfdir=%{_sysconfdir} \
      --datadir=%{_datadir} \
      --includedir=%{_includedir} \
      --libdir=%{_libdir} \
      --libexecdir=%{_libexecdir} \
      --localstatedir=%{_localstatedir} \
      --sharedstatedir=%{_sharedstatedir} \
      --mandir=%{_mandir} \
      --infodir=%{_infodir} \
      --disable-maintainer-mode \
      --without-mbedtls \
      --without-openssl \
      --with-gnutls
%make_build
%install
%make_install
%oreon_autofiles main

%check

${RPM_BUILD_ROOT}%{_bindir}/%{name} --version 2>&1 | grep 'uacme: version %version'
${RPM_BUILD_ROOT}%{_bindir}/ualpn --version 2>&1 | grep 'ualpn: version %version'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
