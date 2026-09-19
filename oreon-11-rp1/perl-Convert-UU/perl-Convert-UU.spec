%global source0_hash 92329ce1c32b5952c48e1223db018c8c58ceafef03bfa0fd4817cd89c355a3bd

# Perform optional tests
%bcond_without perl_Convert_UU_enables_optional_test

Name:           perl-Convert-UU
Version:        0.5201
Release:        42%{?dist}
Summary:        Perl module for uuencode and uudecode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-UU
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDK/Convert-UU-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
%if %{with perl_Convert_UU_enables_optional_test}
# Optional tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# ext-uu.t needs sharutils for uudecode
BuildRequires:  sharutils
%endif
Requires:       perl(:VERSION) >= 5.4

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Convert-UU-%{version}
perl -i -pe 's|local\/perl5\.002_01\/||' puudecode
%if !%{with perl_Convert_UU_enables_optional_test}
for F in t/ext-uu.t t/pod.t t/podcover.t; do
    rm -- "$F"
    perl -i -ne 'print $_ unless m{^\E'"$F"'\Q}' MANIFEST
done;
%endif

%build
perl Makefile.PL INSTALLDIRS=perl NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc ChangeLog README
%{_bindir}/puudecode
%{_bindir}/puuencode
%dir %{perl_privlib}/Convert
%{perl_privlib}/Convert/UU.pm
%{_mandir}/man1/puudecode.*
%{_mandir}/man1/puuencode.*
%{_mandir}/man3/Convert::UU.*

%changelog
%autochangelog
