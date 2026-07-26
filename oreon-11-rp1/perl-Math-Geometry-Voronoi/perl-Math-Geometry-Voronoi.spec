%global source0_hash 72075e4e9883cee51446ba9511264c8c32a015a80f4a5648a3f6b382c534402c

Name:           perl-Math-Geometry-Voronoi
Version:        1.3
Release:        48%{?dist}
Summary:        Compute Voronoi diagrams from sets of points
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND MIT
# Perl module is licensed as Perl, underlaying C code is MIT
URL:            https://metacpan.org/release/Math-Geometry-Voronoi
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/Math-Geometry-Voronoi-%{version}.tar.gz
Source1:        Math-Geometry-Voronoi-license-mail1.txt
Source2:        Math-Geometry-Voronoi-license-mail2.txt
BuildRequires:  coreutils
BuildRequires:  dos2unix
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)

%{?perl_default_filter} # Filters (not)shared c libs

%description
This module computes Voronoi diagrams from a set of input points.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Geometry-Voronoi-%{version}
cp -p %{SOURCE1} license-mail1.txt
cp -p %{SOURCE2} license-mail2.txt
dos2unix *.c
chmod -x *.c *.h

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
# Get the license from the e-mail
tail -22 license-mail1.txt | head -20 | base64 -d | dos2unix > C-LICENSE

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
rm -rf %{buildroot}%{perl_vendorarch}/Math/Geometry/leak-test.pl

%check
make test

%files
%license
%doc Changes C-LICENSE README license-mail*
%{perl_vendorarch}/auto/Math*
%{perl_vendorarch}/Math*
%{_mandir}/man3/Math*

%changelog
%autochangelog
