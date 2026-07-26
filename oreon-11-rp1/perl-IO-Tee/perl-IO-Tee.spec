%global source0_hash 2d9ce7206516f9c30863a367aa1c2b9b35702e369b0abaa15f99fb2cc08552e0

Name:           perl-IO-Tee
Version:        0.66
Release:        16%{?dist}
Summary:        Multiplex output to multiple output handles
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Tee
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/IO-Tee-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(parent)
BuildRequires:  perl(Symbol)

%description
IO::Tee objects can be used to multiplex input and output in two different
ways. The first way is to multiplex output to zero or more output handles.
The IO::Tee constructor, given a list of output handles, returns a tied
handle that can be written to. When written to (using print or printf), the
IO::Tee object multiplexes the output to the list of handles originally
passed to the constructor. As a shortcut, you can also directly pass a
string or an array reference to the constructor, in which case
IO::File::new is called for you with the specified argument or arguments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Tee-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
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
