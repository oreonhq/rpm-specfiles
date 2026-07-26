%global source0_hash d02375e85197e8f91b4cb2d3334ae9a89f60022f78f5cd6076dcd4ec6fb27164

Name:           perl-Perl6-Junction
Version:        1.60000
Release:        35%{?dist}
Summary:        Perl6 style Junction operators in Perl5
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl6-Junction
Source0:        https://cpan.metacpan.org/modules/by-module/Perl6/Perl6-Junction-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
# Test Suite
BuildRequires:  perl(Test::More)
# Dependencies
# (none)

%description
Perl6 style Junction operators in Perl5.

This is a lightweight module that provides 'Junction' operators, the most 
commonly used being 'any' and 'all'.

Inspired by the Perl6 design docs, 
<http://dev.perl.org/perl6/doc/design/exe/E06.html>.

Provides a limited subset of the functionality of L<Quantum::Superpositions>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl6-Junction-%{version}

# Fix line endings
sed -i -e 's/\r$//' Changes

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
%{perl_vendorlib}/Perl6/
%{_mandir}/man3/Perl6::Junction.3*

%changelog
%autochangelog
