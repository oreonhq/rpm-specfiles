%global source0_hash fee699ca763adca2f4e18f4a8a836fd2102bc2820af708f8eb43356d5ae0d50e

Name:           perl-Text-WordDiff
Version:        0.09
Release:        22%{?dist}
Summary:        Track changes between documents
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Text-WordDiff
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMK/Text-WordDiff-%{version}.tar.gz
Patch0:         Text-WordDiff-0.08-uselib.patch
BuildArch:      noarch
# Module Build
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(Algorithm::Diff) >= 1.19
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(Encode) >= 1.20
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
# Runtime
BuildRequires:  perl(Test::Pod)
Requires:       perl(Algorithm::Diff) >= 1.19

# Filter under-specified dependency
%global __requires_exclude ^perl\\(Algorithm::Diff\\)$

%description
This module is a variation on the lovely Text::Diff module. Rather than
generating traditional line-oriented diffs, however, it generates word-
oriented diffs. This can be useful for tracking changes in narrative
documents or documents with very long lines. To diff source code, one is
still best off using Text::Diff. But if you want to see how a short
story changed from one version to the next, this module will do the job
very nicely.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-WordDiff-%{version}

# Don't try to use upstream's personal modules
%patch -P0

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Text/
%{_mandir}/man3/Text::WordDiff.3pm*
%{_mandir}/man3/Text::WordDiff::ANSIColor.3pm*
%{_mandir}/man3/Text::WordDiff::HTML.3pm*
%{_mandir}/man3/Text::WordDiff::HTMLTwoLines.3pm*

%changelog
%autochangelog
