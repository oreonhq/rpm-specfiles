%global source0_hash 842153c94da93e2b9cb3b54dee572b5064bbf499a36a73c38a23799a0203698a

Name:           perl-Object-Signature
Version:        1.08
Release:        21%{?dist}
Summary:        Cryptographically strong objects 
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-Signature
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Object-Signature-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Digest::MD5) >= 2.00
BuildRequires:  perl(Storable) >= 2.11
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.47

%description
Object::Signature is an abstract base class that you can inherit from in
order to allow your objects to generate unique cryptographic signatures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Object-Signature-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
