%global source0_hash f6599ebed73c2d87d7c2bafc8c3a63fb76bda52478e9a1912410d481f7536100

%global gittag 20190131

Name:          fpdns
Epoch:         1
Version:       0.10.0
Release:       21.%{gittag}%{?dist}
Summary:       Fingerprint DNS servers
License:       BSD-3-Clause
URL:           https://github.com/kirei/fpdns
Source0:       https://github.com/kirei/fpdns/archive/%{gittag}/%{name}-%{version}.tar.gz
BuildArch:     noarch
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::DNS)
BuildRequires: make

%description 
fpdns is a program that remotely determines DNS server versions. It does this 
by sending a series of borderline DNS queries which are compared against a 
table of responses and server versions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fpdns-%{gittag}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc LICENSE
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_bindir}/fpdns

%changelog
%autochangelog
