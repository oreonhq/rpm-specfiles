%global source0_hash 8bd62205e1645c0915d28340801f245e4551b4f580f5e2735a39fc426c066207
Name:           perl-Syntax-Keyword-Gather
Version:        1.003002
Release:        24%{?dist}
Summary:        Implements the Perl 6 'gather/take' control structure in Perl 5
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Keyword-Gather/
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/Syntax-Keyword-Gather-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Perl 6 provides a new control structure -- gather -- that allows lists to
be constructed procedurally, without the need for a temporary variable.
Within the block/closure controlled by a gather any call to take pushes
that call's argument list to an implicitly created array. take returns the
number of elements it took. This module implements that control structure.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Syntax-Keyword-Gather-%{version}

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
