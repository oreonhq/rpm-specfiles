%global source0_hash a31a0d4430fe14f59622f31db7f25b2275dad2ec52f1040beb030d3e83ad3af4

Name:           perl-Tie-ToObject
Version:        0.03
Release:        51%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Tie to an existing object
Source:         https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/Tie-ToObject-%{version}.tar.gz
Url:            https://metacpan.org/release/Tie-ToObject
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(ok)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::RefHash)


Provides:       perl(Tie::ToObject)
%description
While the perldoc/tie manpage allows tying to an arbitrary object, the
class in question must support this in it's implementation of 'TIEHASH',
'TIEARRAY' or whatever.

This class provides a very tie constructor that simply returns the object
it was given as it's first argument.

This way side effects of calling '$object->TIEHASH' are avoided.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Tie-ToObject-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
