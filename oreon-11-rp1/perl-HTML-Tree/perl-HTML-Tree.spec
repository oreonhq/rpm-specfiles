%global source0_hash f0374db84731c204b86c1d5b90975fef0d30a86bd9def919343e554e31a9dbbf

# Perform optional tests
%if 0%{?rhel} >= 7
%bcond_with perl_HTML_Tree_enable_optional_test
%else
%bcond_without perl_HTML_Tree_enable_optional_test
%endif

Name:           perl-HTML-Tree
Epoch:          1
Version:        5.07
Release:        30%{?dist}
Summary:        HTML tree handling modules for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Tree
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/HTML-Tree-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser) >= 3.46
BuildRequires:  perl(HTML::Tagset) >= 3.02
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
%if !%{defined perl_bootstrap}
# HTML::FormatText (perl-HTML-Format) has BR: perl(HTML::TreeBuilder) from this package
BuildRequires:  perl(HTML::FormatText)
%if %{with perl_HTML_Tree_enable_optional_test}
# perl-Test-LeakTrace -> perl-Test-Valgrind -> perl-XML-Twig -> perl-HTML-Tree
BuildRequires:  perl(Test::LeakTrace)
%endif
%endif
Requires:       perl(HTML::Parser) >= 3.46
Requires:       perl(HTML::Tagset) >= 3.02

%description
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevant documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n HTML-Tree-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir="%{buildroot}" create_packlist=0
%{_fixperms} %{buildroot}

%check
./Build test

%files
%doc Changes README TODO
%{_bindir}/htmltree
%{perl_vendorlib}/HTML
%{_mandir}/man1/*1*
%{_mandir}/man3/HTML::*3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.07-30
- Prepare for Oreon 11 (RP1)
