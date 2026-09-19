%global source0_hash 9df692e7e90536c28edea2c09ec4c45ac49af789fb2863248cc723210c785403

Summary:        Perl module to read TNEF files
Name:           perl-Convert-TNEF
Version:        0.18
Release:        34%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-TNEF
Source0:        https://cpan.metacpan.org/modules/by-module/Convert/Convert-TNEF-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Wrap)
BuildRequires:  perl(MIME::Body) >= 4.109
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
# (no additional dependencies)
# Dependencies

%description
TNEF stands for Transport Neutral Encapsulation Format, and if you've
ever been unfortunate enough to receive one of these files as an email
attachment, you may want to use this module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Convert-TNEF-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Convert/
%{_mandir}/man3/Convert::TNEF.3*

%changelog
%autochangelog
