%global source0_hash 3c45d22f2eace34ba031464cb667cb583135c797aa3b6b17e9d47c43e542fddf

Name:           perl-Text-Diff-HTML
Version:        0.08
Release:        22%{?dist}
Summary:        XHTML format for Text::Diff::Unified
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Diff-HTML
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMK/Text-Diff-HTML-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Diff) >= 0.11
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.41
# Runtime

%description
This class subclasses Text::Diff::Unified, a formatting class provided by
the Text::Diff module, to add XHTML markup to the unified diff format. For
details on the interface of the diff() function, see the Text::Diff
documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Diff-HTML-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Text/
%{_mandir}/man3/Text::Diff::HTML.3pm*

%changelog
%autochangelog
