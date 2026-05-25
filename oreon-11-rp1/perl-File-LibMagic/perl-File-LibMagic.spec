# Filter the Perl extension module
%{?perl_default_filter}

Name:		perl-File-LibMagic
Version:	1.23
Release:	18%{?dist}
Summary:	Perl wrapper/interface for libmagic
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/File-LibMagic
Source0:	https://cpan.metacpan.org/modules/by-module/File/File-LibMagic-%{version}.tar.gz
# Build
BuildRequires:	coreutils
BuildRequires:	file-devel
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config::AutoConf)
# ExtUtils::CBuilder needed for Config::AutoConf to handle C language
# gcc needed on EL-8 because ExtUtils::CBuilder is missing dependency on it (#1547165)
BuildRequires:	perl(ExtUtils::CBuilder) %{?el8: gcc}
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Getopt::Long)
# Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.96
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Dependencies
# (none)

%description
The File::LibMagic module is a simple perl interface to libmagic from the
file (4.x or 5.x) package.

%prep
%setup -q -n File-LibMagic-%{version}

%build
perl Makefile.PL \
  INSTALLDIRS=vendor \
  NO_PACKLIST=1 \
  NO_PERLLOCAL=1 \
  OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{perl_vendorarch}/File/
%{perl_vendorarch}/auto/File/
%{_mandir}/man3/File::LibMagic.3*
%{_mandir}/man3/File::LibMagic::Constants.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.23-18
- Import
