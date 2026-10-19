%global source0_hash 481b5b86a1dfa03048f134a87921fbba18e47f8eba4b1c624772d53f81c58c7d
Name:           perl-HTML-Toc
Version:        1.12
Release:        1%{?dist}
Summary:        Generate, insert and update HTML Table of Contents
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Toc
Source0:        https://cpan.metacpan.org/authors/id/F/FV/FVULTO/HTML-Toc-%{version}.tar.gz
Patch0:         man3pods.patch
Patch1:         HTML-Toc-1.12-Fix-unescaped-left-brace-in-regex.patch
BuildArch:      noarch
Requires:       perl(Roman)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(HTML::_.*\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(Roman)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Generate, insert and update HTML Table of Contents (ToC).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Toc-%{version}
%patch -P0 -p 1
%patch -P1 -p 1
find . -type f | xargs chmod 0644

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
