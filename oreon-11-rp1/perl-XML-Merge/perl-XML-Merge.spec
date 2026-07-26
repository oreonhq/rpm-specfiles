%global source0_hash 9de7cbbbd09e8374e76c2c2f1cafc1e53536c1fe94a2e4f3aa982cac82b8d3a3

Name:           perl-XML-Merge 
Version:        1.4
Release:        28%{?dist}
Summary:        Flexibly merge XML documents

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://metacpan.org/release/XML-Merge
Source0:        https://cpan.metacpan.org/authors/id/P/PI/PIP/XML-Merge-%{version}.tgz
Patch1:         perl-XML-Merge-1.4-makefile.patch

BuildArch:      noarch 
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Tidy)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XML::XPath)

%description
This module inherits from XML::Tidy which in turn inherits from XML::XPath.
This ensures that Merge objects' indenting can be tidied up after any merge
operation since such modification usually spells the ruination of indentation.
Polymorphism allows Merge objects to be utilized as normal XML::XPath objects
as well.
The merging behavior is setup to combine separate XML documents according to
certain rules and configurable options. If both documents have root nodes which
are elements of the same name, the documents are merged directly. Otherwise,
one is merged as a child of the other. An optional XPath location can be
specified as the place to perform the merge. If no location is specified, the
merge is attempted at the first matching element or is appended as the new last
child of the other root if no match is found.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Merge-%{version}
%patch -P1 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%license LICENSE 
%{perl_vendorlib}/*
%{_mandir}/man3/XML::Merge.3pm.gz

%changelog
%autochangelog
