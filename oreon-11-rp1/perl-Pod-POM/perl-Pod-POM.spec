%global source0_hash 1b50fba9bbdde3ead192beeba0eaddd0c614e3afb1743fa6fff805f57c56f7f4
%{!?perl_vendorlib: %global perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}
Name:           perl-Pod-POM
Version:        2.01
Release:        1%{?dist}
Summary:        Object-oriented interface to Perl POD documents
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-POM
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Pod-POM-%{version}.tar.gz
BuildArch:      noarch
Requires:  perl(Encode)
Provides:       perl(Pod::POM)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

PERL_HASH_SEED=0 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
