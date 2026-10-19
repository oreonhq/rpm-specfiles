%global source0_hash 92329ce1c32b5952c48e1223db018c8c58ceafef03bfa0fd4817cd89c355a3bd
%bcond_without perl_Convert_UU_enables_optional_test
Name:           perl-Convert-UU
Version:        0.5201
Release:        1%{?dist}
Summary:        Perl module for uuencode and uudecode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-UU
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDK/Convert-UU-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Convert_UU_enables_optional_test}
%endif
Requires:       perl(:VERSION) >= 5.4
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sharutils
# /oreon:deps
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
%oreon_autofiles main

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
