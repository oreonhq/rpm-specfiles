%global source0_hash 2c88da07515afa87840ee3f9cbeab85d160f624bc23fd9c7d5eeff9acb57cf89

Name:           perl-WWW-Mechanize-TreeBuilder
Version:        1.20000
Release:        34%{?dist}
Summary:        WWW::Mechanize::TreeBuilder Perl module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/WWW-Mechanize-TreeBuilder
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASH/WWW-Mechanize-TreeBuilder-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::Parameterized)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Element)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose) >= 0.65
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::WWW::Mechanize)
BuildRequires:  perl(warnings)
BuildRequires:  perl(WWW::Mechanize)
# Optional tests:
BuildRequires:  perl(HTML::TreeBuilder::XPath)
# not automatically detected
Requires:       perl(HTML::TreeBuilder)
# not strictly required, but recommended
Requires:       perl(HTML::TreeBuilder::XPath)

%{?perl_default_filter}

%description
This module combines WWW::Mechanize and HTML::TreeBuilder.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Mechanize-TreeBuilder-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/WWW*
%{_mandir}/man3/WWW*

%changelog
%autochangelog
