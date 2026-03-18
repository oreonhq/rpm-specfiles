# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Path_Tiny_enables_optional_test
%else
%bcond_with perl_Path_Tiny_enables_optional_test
%endif

Name:		perl-Path-Tiny
Version:	0.150
Release:	3%{?dist}
Summary:	File path utility
License:	Apache-2.0
URL:		https://metacpan.org/release/Path-Tiny
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Path-Tiny-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Digest) >= 1.03
BuildRequires:	perl(Digest::SHA) >= 5.45
BuildRequires:	perl(Encode)
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Compare)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Glob)
BuildRequires:	perl(File::Path) >= 2.07
BuildRequires:	perl(File::Spec) >= 0.86
BuildRequires:	perl(File::stat)
BuildRequires:	perl(File::Temp) >= 0.19
BuildRequires:	perl(overload)
BuildRequires:	perl(strict)
BuildRequires:	perl(threads)
BuildRequires:	perl(warnings)
BuildRequires:	perl(warnings::register)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Spec::Unix)
BuildRequires:	perl(File::Temp) >= 0.19
BuildRequires:	perl(lib)
BuildRequires:	perl(open)
BuildRequires:	perl(Test::More) >= 0.96
%if %{with perl_Path_Tiny_enables_optional_test}
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(Test::FailWarnings)
BuildRequires:	perl(Test::MockRandom)
%endif
# Dependencies
Requires:	perl(Cwd)
Requires:	perl(Digest) >= 1.03
Requires:	perl(Digest::SHA) >= 5.45
Requires:	perl(Encode)
Requires:	perl(Fcntl)
Requires:	perl(File::Compare)
Requires:	perl(File::Copy)
Requires:	perl(File::Glob)
Requires:	perl(File::Path) >= 2.07
Requires:	perl(File::stat)
Requires:	perl(File::Temp) >= 0.18
Requires:	perl(threads)
Requires:	perl(warnings::register)

# For performance and consistency
%if !(0%{?rhel})
BuildRequires:	perl(PerlIO::utf8_strict) >= 0.003
Requires:	perl(PerlIO::utf8_strict) >= 0.003
%endif
BuildRequires:	perl(Unicode::UTF8) >= 0.58
Requires:	perl(Unicode::UTF8) >= 0.58

%description
This module attempts to provide a small, fast utility for working with file
paths. It is friendlier to use than File::Spec and provides easy access to
functions from several other core file handling modules.

It doesn't attempt to be as full-featured as IO::All or Path::Class, nor does
it try to work for anything except Unix-like and Win32 platforms. Even then, it
might break if you try something particularly obscure or tortuous.

All paths are forced to have Unix-style forward slashes. Stringifying the
object gives you back the path (after some clean up).

File input/output methods flock handles before reading or writing, as
appropriate.

The *_utf8 methods (slurp_utf8, lines_utf8, etc.) operate in raw mode without
CRLF translation.

%prep
%setup -q -n Path-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/Path/
%{_mandir}/man3/Path::Tiny.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.150-3
- Prepare for Oreon 11 (RP1)
