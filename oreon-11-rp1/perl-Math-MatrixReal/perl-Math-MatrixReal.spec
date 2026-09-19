%global source0_hash 4f9fa1a46dd34d2225de461d9a4ed86932cdd821c121fa501a15a6d4302fb4b2

Name:           perl-Math-MatrixReal
Version:        2.13
Release:        27%{?dist}
Summary:        Manipulate matrix of reals
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-MatrixReal
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LETO/Math-MatrixReal-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::Complex)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Simple)

%description
Implements the data type "matrix of reals" (and consequently also
"vector of reals") which can be used almost like any other basic
Perl type thanks to OPERATOR OVERLOADING, i.e.,

    $A = $matrix1 * $matrix2;
    $B = $A ** 2;
    $C = $A + 2*B;
    $D = $C - $B/2;
    $inverse = $C ** -1;
    $inverse = 1/$C;
    
does what you would like it to do.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-MatrixReal-%{version}
chmod -x example/*

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc CHANGES CONTRIBUTING.md CREDITS example GOALS README.mkd OLD_README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
