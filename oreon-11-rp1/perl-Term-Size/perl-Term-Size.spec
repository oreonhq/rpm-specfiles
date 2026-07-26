%global source0_hash 5962b4bde52329774718296c92315e936da7f9c4451e92186cf072f27790b3fb

Name:           perl-Term-Size 
Version:        0.211
Release:        18%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Simple way to get terminal size 
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Term-Size-%{version}.tar.gz
Url:            https://metacpan.org/release/Term-Size
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Test::More)

%description
Term::Size is a Perl module which provides a straightforward way to
retrieve the terminal size.

Both functions take an optional filehandle argument, which defaults
to *STDIN{IO}. They both return a list of two values, which are the
current width and height, respectively, of the terminal associated with
the specified filehandle.

Term::Size::chars returns the size in units of characters, whereas
Term::Size::pixels uses units of pixels.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-Size-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING
make test

%files
%doc Changes README
%{perl_vendorarch}/Term*
%{perl_vendorarch}/auto
%{_mandir}/man3/*

%changelog
%autochangelog
