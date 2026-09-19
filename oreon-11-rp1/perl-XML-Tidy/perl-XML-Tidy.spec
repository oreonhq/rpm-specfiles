%global source0_hash 175547e7cf4dbf3e8bf231b2ef1dc55c404150725894a4da928dd7dc5a6a29de

Name:           perl-XML-Tidy
Version:        1.20
Release:        26%{?dist}
Summary:        Tidy indenting of XML documents

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/XML-Tidy
Source0:        https://cpan.metacpan.org/authors/id/P/PI/PIP/XML-Tidy-%{version}.tgz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BaseCnv)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(XML::XPath::XMLParser)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%description
This module creates XML document objects (with inheritance from XML::XPath) to
tidy mixed-content (ie. non-data) text node indenting. There are also some
other handy member functions to compress && expand your XML document object
(into either a compact XML representation or a binary one).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Tidy-%{version}
for i in README; do {
  iconv -f iso-8859-1 -t utf-8 $i > $i.conv \
  && mv $i.conv $i;
};
done;

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
%{_bindir}/xmltidy
%{perl_vendorlib}/*
%{_mandir}/man3/XML::Tidy.3pm.gz

%changelog
%autochangelog
