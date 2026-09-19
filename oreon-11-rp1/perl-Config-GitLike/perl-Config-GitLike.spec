%global source0_hash f7ae7440f3adab5b9ff9aa57216d84fd4a681009b9584e32da42f8bb71e332c5

Name:           perl-Config-GitLike
Version:        1.18
Release:        18%{?dist}
Summary:        Git-compatible config file parsing
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Config-GitLike
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/Config-GitLike-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::ExtraTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sed

%{?perl_default_filter}

%description
This module handles interaction with configuration files of the style used
by the version control system Git. It can both parse and modify these
files, as well as create entirely new ones.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-GitLike-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
