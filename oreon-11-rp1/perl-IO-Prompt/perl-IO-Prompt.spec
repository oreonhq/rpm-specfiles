%global source0_hash f17bb305ee6ac8b5b203e6d826eb940c4f3f6d6f4bfe719c3b3a225f46f58615
Name:           perl-IO-Prompt
Summary:        Interactively prompt for user input
%global cpanver 0.997004
Version:        0.997.004
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/IO-Prompt-%{cpanver}.tar.gz
URL:            https://metacpan.org/release/IO-Prompt
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Want)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
An object-oriented way to prompt for user input -- and control how the user is
prompted.

This module is no longer being maintained. Use the IO::Prompter module instead.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Prompt-%{cpanver}
find examples -type f -exec chmod -x {} +

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
