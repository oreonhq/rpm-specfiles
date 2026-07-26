%global source0_hash fd769448ec977a3626a135b02e0d5fcd41de2d9d14ade0632194d1ad801eeccd

Name:           perl-Algorithm-NaiveBayes
Version:        0.04
Release:        39%{?dist}
Summary:        Bayesian prediction of categories

# There is no license file included with the sources, I asked upstream for one:
#    https://rt.cpan.org/Public/Bug/Display.html?id=79560
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Algorithm-NaiveBayes

Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Algorithm-NaiveBayes-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)

%description
This module implements the classic "Naive Bayes" machine learning
algorithm. It is a well-studied probabilistic algorithm often used in
automatic text categorization. Compared to other algorithms (kNN, SVM,
Decision Trees), it's pretty fast and reasonably competitive in the quality
of its results.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-NaiveBayes-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes
%{_mandir}/man3/Algorithm::NaiveBayes.3pm*
%{perl_vendorlib}/Algorithm

%changelog
%autochangelog
