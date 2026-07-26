%global source0_hash bdd18e6427559e489041c6e3d71cf91ff5b53d294264c232b1c58773c0f3c678

Name:           perl-Archive-Any-Create
Version:        0.03
Release:        29%{?dist}
Summary:        Abstract API to create archives (tar, tar.gz and zip)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Archive-Any-Create
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Archive-Any-Create-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(warnings)

%description
Archive::Any::Create is a wrapper module to create tar/tar.gz/zip files
with a single easy-to-use API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Archive-Any-Create-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
