%global source0_hash bf50b61c24656cc3fc958602d80a9c7d017247af38d8dbfa0e9dec5b75425d5f
Name:           perl-HTML-Gumbo
Version:        0.18
Release:        1%{?dist}
Summary:        HTML5 parser based on gumbo C library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Gumbo
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/HTML-Gumbo-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gumbo-parser-devel
BuildRequires:  perl(Alien::LibGumbo)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented as a
pure C99 library with no outside dependencies.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Gumbo-%{version}

%build

%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir="$RPM_BUILD_ROOT" --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} "$RPM_BUILD_ROOT"/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
