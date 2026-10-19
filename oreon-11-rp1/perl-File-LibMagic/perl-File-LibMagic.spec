%global source0_hash 52e6b1dc7cb2d87a4cdf439ba145e0b9e8cf28cc26a48a3cf9977c83463967ee
%{?perl_default_filter}
Name:		perl-File-LibMagic
Version:	1.23
Release:        1%{?dist}
Summary:        Perl wrapper/interface for libmagic
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/File-LibMagic
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-LibMagic-%{version}.tar.gz
Provides:       perl(File::LibMagic)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  file-devel
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::AutoConf)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The File::LibMagic module is a simple perl interface to libmagic from the
file (4.x or 5.x) package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.23-18
- Import
