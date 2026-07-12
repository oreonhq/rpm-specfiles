%global source0_hash 49143ba90d0bfda26687e5ad0edda088775cedfa940367c24983171025e06b4d

Name:           perl-utf8-all
Version:        0.026
Release:        1%{?dist}
Summary:        Turn on Unicode everywhere
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/utf8-all
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAYOBAAN/utf8-all-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(feature)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(open)
BuildRequires:  perl(parent)
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(utf8)
# Tests:
BuildRequires:  perl(autodie)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(locale)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(version) >= 0.77
# Dependencies:

Provides:       perl(utf8::all)
%description
Pragma utf8 allows you to write your Perl encoded in UTF-8. That means UTF-8
strings, variable names, and regular expressions. utf8::all goes further, and
makes @ARGV encoded in UTF-8, and file handles are opened with UTF-8 encoding
turned on by default (including STDIN, STDOUT, STDERR), and character names
are imported so \N{...} sequences can be used to compile Unicode characters
based on names. If you don't want UTF-8 for a particular file handle, you'll
have to set binmode $filehandle.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n utf8-all-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} -c $RPM_BUILD_ROOT

%check
make test

%files
%license LICENSE
%doc Changes README.mkdn
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
