%global source0_hash 69170ef84891a0e3ccce50833ac90db75de26b2c8432050256c1bf4ec26c8ad7

Name:           uacme
Version:        1.8.0 
Release:        1%{?dist}
Summary:        Lightweight SSL certificate verification and issue client

License:        GPL-3.0-only
URL:            https://github.com/ndilieto/uacme
Source0:        %{url}/archive/upstream/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  asciidoc
BuildRequires:  gnutls-devel
BuildRequires:  libcurl-devel
BuildRequires:  libev-devel
BuildRequires:  which
Requires:       curl
Requires:       gnutls
Requires:       libev

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

# No tests defined, do a sanity check
# uacme --version and ualpn --version 
%check
${RPM_BUILD_ROOT}%{_bindir}/%{name} --version 2>&1 | grep 'uacme: version %version'
${RPM_BUILD_ROOT}%{_bindir}/ualpn --version 2>&1 | grep 'ualpn: version %version'

%files
%{_bindir}/%{name}
%{_bindir}/ualpn
%{_datadir}/%{name}/%{name}.sh
%{_datadir}/%{name}/ualpn.sh
%{_datadir}/%{name}/nsupdate.sh
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/ualpn.1*
%{_docdir}/%{name}/%{name}.html
%{_docdir}/%{name}/ualpn.html
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS

%changelog
%autochangelog
