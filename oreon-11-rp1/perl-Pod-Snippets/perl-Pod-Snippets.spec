%global source0_hash c9a8bd3734e20306bcc751af43ec698b3890f35add53c2abf56a0d92ec7550ac

Name:           perl-Pod-Snippets
Version:        0.14
Release:        34%{?dist}
Summary:        Extract and reformat snippets of POD
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Snippets
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOMQ/Pod-Snippets-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Parser)

%description
This class is a very simple extension of Pod::Parser that extracts POD
snippets from Perl code, and pretty-prints it so as to make it usable from
other Perl code. As demonstrated above, Pod::Snippets is immediately useful
to test-driven-development nutcases who want to put every single line of
Perl code under test, including code that is in the POD (typically a
SYNOPSIS section). There are other uses, such as storing a piece of
information that is both human- and machine-readable (e.g. an XML schema)
simultaneously as documentation and code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Snippets-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README eg/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
