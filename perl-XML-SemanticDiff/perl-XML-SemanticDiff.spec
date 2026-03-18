Name:		perl-XML-SemanticDiff
Summary:	Perl extension for comparing XML documents
Version:	1.0007
Release:	22%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/XML-SemanticDiff
Source0:	https://cpan.metacpan.org/modules/by-module/XML/XML-SemanticDiff-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build) >= 0.28
# Module Runtime
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Encode)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XML::Parser)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)
# Optional Tests
%if "%{?rhel}" != "6" && "%{?rhel}" != "8"
BuildRequires:	perl(Test::TrailingSpace)
%endif
# Dependencies
# (none)

%description
XML::SemanticDiff provides a way to compare the contents and structure of two
XML documents. By default, it returns a list of hashrefs where each hashref
describes a single difference between the two docs.

%prep
%setup -q -n XML-SemanticDiff-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes eg/ README
%{perl_vendorlib}/XML/
%{_mandir}/man3/XML::SemanticDiff.3*
%{_mandir}/man3/XML::SemanticDiff::BasicHandler.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0007-22
- Prepare for Oreon 11 (RP1)
