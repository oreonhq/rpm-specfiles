%global source0_hash 1b50fba9bbdde3ead192beeba0eaddd0c614e3afb1743fa6fff805f57c56f7f4

%{!?perl_vendorlib: %global perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-Pod-POM
Version:        2.01
Release:        32%{?dist}
Summary:        Object-oriented interface to Perl POD documents
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-POM
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Pod-POM-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
# File::Basename not used at tests
# FindBin not used at tests
# Getopt::Long not used at tests
# Getopt::Std not used at tests
# lib not used at tests
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Slurper) >= 0.004
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(YAML::Tiny)
# Optional tests:
BuildRequires:  perl(Scalar::Util)
# Text::Diff not helpful
# Test::Differences not helpful
Requires:  perl(Encode)

Provides:       perl(Pod::POM)
%description
This module implements a parser to convert Pod documents into a simple
object model form known hereafter as the Pod Object Model.  The object
model is generated as a hierarchical tree of nodes, each of which
represents a different element of the original document.  The tree can
be walked manually and the nodes examined, printed or otherwise
manipulated.  In addition, Pod::POM supports and provides view objects
which can automatically traverse the tree, or section thereof, and
generate an output representation in one form or another.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-POM-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
# http://rt.cpan.org/NoAuth/Bug.html?id=3910
# Need File::Slurper to run tests, not packaged as of 2015-09-08
PERL_HASH_SEED=0 make test


%files
%doc Changes README.md TODO
%{_bindir}/pomdump
%{_bindir}/podlint
%{_bindir}/pom2
%{perl_vendorlib}/Pod
%{_mandir}/man[13]/*.[13]*


%changelog
%autochangelog
