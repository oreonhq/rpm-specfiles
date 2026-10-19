%global source0_hash a8a63e37fa802e8258be99983916cde4512581dc8062de50e73d66af6e2d8535
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-Any-Moose
Summary:        Use Moose or Mouse automagically (DEPRECATED)
Version:        0.27
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Any-Moose
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Any-Moose-%{version}.tar.gz
BuildArch:      noarch
%if !0%{?perl_bootstrap}
%endif
Requires:       perl(Any-Moose) >= 0.40
Requires:       perl(Carp)
Provides:       perl(Any::Moose)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(MouseX::Types)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Any::Moose is deprecated - please use Moo for new code.

This module allows one to take advantage of the features Moose/Mouse
provides, while allowing one to let the program author determine if Moose
or Mouse should be used; when use'd, we load Mouse if Moose isn't already
loaded, otherwise we go with Moose.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Any-Moose-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
