%global source0_hash a8a63e37fa802e8258be99983916cde4512581dc8062de50e73d66af6e2d8535

Name:           perl-Any-Moose
Summary:        Use Moose or Mouse automagically (DEPRECATED)
Version:        0.27
Release:        34%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Any-Moose
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Any-Moose-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Moose)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Mouse) >= 0.40
BuildRequires:  perl(Test::More) >= 0.88
%if !0%{?perl_bootstrap}
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MouseX::Types)
%endif
# Dependencies
# Virtual provides in perl-Moose and perl-Mouse
Requires:       perl(Any-Moose) >= 0.40
Requires:       perl(Carp)

Provides:       perl(Any::Moose)
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

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Any/
%{_mandir}/man3/Any::Moose.3*

%changelog
%autochangelog
