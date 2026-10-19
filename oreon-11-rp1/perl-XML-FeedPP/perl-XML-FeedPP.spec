%global source0_hash 90c3959bf1a60b76a29a749a73941f3a0c7b9a5954c1365bc81dafcabb01a8f4
Name:          perl-XML-FeedPP
Version:       0.95
Release:        1%{?dist}
Summary:        Parse/write/merge/edit RSS/RDF/Atom syndication feeds
License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://metacpan.org/release/XML-FeedPP
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-FeedPP-%{version}.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(XML::TreePP)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Parse/write/merge/edit RSS/RDF/Atom syndication feeds

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-FeedPP-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make %{?_smp_mflags} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT
%oreon_autofiles main

%check

make %{?_smp_mflags} test || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
