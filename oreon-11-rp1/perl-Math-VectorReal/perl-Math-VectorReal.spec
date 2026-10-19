%global source0_hash 8c959600865b09ea0d4d5567ad6bc9e0c81040f76bfb451cb27aeb0eb9cc548b
%bcond check 1
Name:           perl-Math-VectorReal
Version:        1.02
Release:        1%{?dist}
Summary:        Module to handle 3D Vector Mathematics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Math-VectorReal
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANTHONY/Math-VectorReal-%{version}.tar.gz
Patch0:         %{name}-tests.patch
%if %{with check}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Math::MatrixReal)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Math::VectorReal package defines a 3D mathematical "vector", in a
way that is compatible with the previous CPAN module Math::MatrixReal.
However it provides a more vector oriented set of mathematical functions
and overload operators, to the MatrixReal package. For example the
normal perl string functions "x" and "." have been overloaded to allow
vector cross and dot product operations. Vector math formula thus looks
like vector math formula in perl programs using this package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Math-VectorReal-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} '%{buildroot}'/*
rm -v %{buildroot}%{perl_vendorlib}/Math/{{matrix,vector}_test,synopsis}.pl
%oreon_autofiles main
%if %{with check}
%check

make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
