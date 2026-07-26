%global source0_hash 589fd21a62d2e6afd5d9c280d5549eac32d200311dd4275daeb972597fd7e4d5

Name:           perl-AI-DecisionTree
Version:        0.11
Release:        45%{?dist}
Summary:        Automatically Learns Decision Trees

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AI-DecisionTree

Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/AI-DecisionTree-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(GraphViz)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Requires:       perl(GraphViz)

%{?perl_default_filter}

%description
The AI::DecisionTree module automatically creates so-called "decision
trees" to explain a set of training data. A decision tree is a kind of
categorizer that use a flowchart-like process for categorizing new
instances. For instance, a learned decision tree might look like the
following, which classifies for the concept "play tennis":

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AI-DecisionTree-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes dist.ini eg LICENSE README
%{perl_vendorarch}/auto/AI
%{perl_vendorarch}/AI
%{_mandir}/man3/AI::DecisionTree*

%changelog
%autochangelog
