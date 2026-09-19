%global source0_hash 7fbe2d6430860059894aeeebf75d4cacf1bf8d7b75294eb87d8e1502f81bd760

Name:           perl-XML-TreePP
Version:        0.43
Release:        32%{?dist}
Summary:        Pure Perl implementation for parsing/writing XML documents
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-TreePP
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-TreePP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
# Optional Functionality
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTTP::Lite)
BuildRequires:  perl(Jcode)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Tie::IxHash)
# Test Suite
BuildRequires:  perl(Test::More)
# Optional Tests (note: t/*_http-*.t tests require network access so we don't try to run them)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(utf8)
# Dependencies
Recommends:     perl(Encode)
Recommends:     perl(HTTP::Lite)
Recommends:     perl(Jcode)
Recommends:     perl(LWP::UserAgent)
Recommends:     perl(Tie::IxHash)

%description
Pure Perl implementation for parsing/writing XML documents

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-TreePP-%{version}

# Remove bogus exec permissions
chmod -c a-x Changes lib/XML/TreePP.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc README README.md Changes
%dir %{perl_vendorlib}/XML
%{perl_vendorlib}/XML/TreePP.pm
%{_mandir}/man3/XML::TreePP.3pm{,.*}

%changelog
%autochangelog
