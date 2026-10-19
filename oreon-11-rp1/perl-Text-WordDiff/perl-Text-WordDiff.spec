%global source0_hash fee699ca763adca2f4e18f4a8a836fd2102bc2820af708f8eb43356d5ae0d50e
Name:           perl-Text-WordDiff
Version:        0.09
Release:        1%{?dist}
Summary:        Track changes between documents
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-WordDiff
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMK/Text-WordDiff-%{version}.tar.gz
Patch0:         Text-WordDiff-0.08-uselib.patch
BuildArch:      noarch
Requires:       perl(Algorithm::Diff) >= 1.19
%global __requires_exclude ^perl\\(Algorithm::Diff\\)$
# oreon:deps
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
