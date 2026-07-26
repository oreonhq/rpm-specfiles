%global source0_hash 2bed36978ee4b8c1357d11af648081309f42909f201b5a3314ad62757cdb0718

Name:           perl-V
Version:        0.22
Release:        3%{?dist}
Summary:        Print version of the specified Perl modules

Group:          Development/Libraries
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://search.cpan.org/dist/V
Source0:        http://search.cpan.org/CPAN/authors/id/H/HM/HMBRAND/V-%{version}.tgz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
# Tests
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(warnings)
Requires:       perl(version)

%description
A light-weight module for getting versions of Perl modules without
loading them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n V-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test VERBOSE=1

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README.md SECURITY.md CONTRIBUTING.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
