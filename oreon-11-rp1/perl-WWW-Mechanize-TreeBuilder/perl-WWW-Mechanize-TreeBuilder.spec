%global source0_hash 2c88da07515afa87840ee3f9cbeab85d160f624bc23fd9c7d5eeff9acb57cf89
Name:           perl-WWW-Mechanize-TreeBuilder
Version:        1.20000
Release:        34%{?dist}
Summary:        WWW::Mechanize::TreeBuilder Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Mechanize-TreeBuilder
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASH/WWW-Mechanize-TreeBuilder-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(HTML::TreeBuilder)
Requires:       perl(HTML::TreeBuilder::XPath)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Element)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTML::TreeBuilder::XPath)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::WWW::Mechanize)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
