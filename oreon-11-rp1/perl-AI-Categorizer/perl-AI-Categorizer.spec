%global source0_hash 24d8adec512e7be76e99c224b60205a164a14d8889557b6876c9b6e8ef8f8590

Name:           perl-AI-Categorizer
Version:        0.09
Release:        39%{?dist}
Summary:        Automatic Text Categorization

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AI-Categorizer

Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/AI-Categorizer-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  perl-interpreter >= 1:5.6.0
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)

# For the unit tests
BuildRequires:  perl(AI::DecisionTree) >= 0.06
BuildRequires:  perl(Algorithm::NaiveBayes)
BuildRequires:  perl(Algorithm::SVM) >= 0.06
BuildRequires:  perl(Algorithm::SVM::DataSet)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Container) >= 0.09
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Lingua::Stem) >= 0.5
BuildRequires:  perl(Params::Validate) >= 0.18
BuildRequires:  perl(Statistics::Contingency) >= 0.06
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Time::Progress) >= 1.1

Requires:       perl(AI::DecisionTree) >= 0.06
Requires:       perl(Algorithm::NaiveBayes)
Requires:       perl(Algorithm::SVM) >= 0.06
Requires:       perl(Class::Container) >= 0.09
Requires:       perl(Lingua::Stem) >= 0.5
Requires:       perl(Params::Validate) >= 0.18
Requires:       perl(Statistics::Contingency) >= 0.06
Requires:       perl(Time::Progress) >= 1.1

%{?perl_default_filter}

%description
AI::Categorizer is a framework for automatic text categorization. It
consists of a collection of Perl modules that implement common
categorization tasks, and a set of defined relationships among those
modules. The various details are flexible - for example, you can choose
what categorization algorithm to use, what features (words or otherwise) of
the documents should be used (or how to automatically choose these
features), what format the documents are in, and so on.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AI-Categorizer-%{version}

# Fix permissions
find . -name '*.pm' -exec chmod -x '{}' \;

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
%doc Changes README
%{perl_vendorlib}/AI/Categorizer*
%{_mandir}/man3/AI::Categorizer*

%changelog
%autochangelog
