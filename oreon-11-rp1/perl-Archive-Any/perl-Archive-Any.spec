%global source0_hash 0d57bcdace20eb907ff6f00fefa120a0f6fd05aa638c5d33ef0a8bea15739d84

Name:		perl-Archive-Any
Version:	0.0946
Release:	20%{?dist}
Summary:	Single interface to deal with file archives
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Archive-Any
Source0:	https://cpan.metacpan.org/modules/by-module/Archive/Archive-Any-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Archive::Tar) >= 0.22
BuildRequires:	perl(Archive::Zip) >= 1.07
BuildRequires:	perl(base)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::MMagic) >= 1.27
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(MIME::Types) >= 1.16
BuildRequires:	perl(Module::Find) >= 0.05
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.4
BuildRequires:	perl(Test::Warn)
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
# Runtime

%description
This module is a single interface for manipulating different archive
formats. Tarballs, zip files, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Archive-Any-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS README.md
%{perl_vendorlib}/Archive/
%{_mandir}/man3/Archive::Any.3*
%{_mandir}/man3/Archive::Any::Plugin.3*
%{_mandir}/man3/Archive::Any::Plugin::Tar.3*
%{_mandir}/man3/Archive::Any::Plugin::Zip.3*
%{_mandir}/man3/Archive::Any::Tar.3*
%{_mandir}/man3/Archive::Any::Zip.3*

%changelog
%autochangelog
