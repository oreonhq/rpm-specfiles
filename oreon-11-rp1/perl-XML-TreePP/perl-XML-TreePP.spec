%global source0_hash 7fbe2d6430860059894aeeebf75d4cacf1bf8d7b75294eb87d8e1502f81bd760
Name:           perl-XML-TreePP
Version:        0.43
Release:        32%{?dist}
Summary:        Pure Perl implementation for parsing/writing XML documents
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-TreePP
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-TreePP-%{version}.tar.gz
BuildArch:      noarch
Recommends:     perl(Encode)
Recommends:     perl(HTTP::Lite)
Recommends:     perl(Jcode)
Recommends:     perl(LWP::UserAgent)
Recommends:     perl(Tie::IxHash)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Lite)
BuildRequires:  perl(Jcode)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
