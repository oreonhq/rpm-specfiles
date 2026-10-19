%global source0_hash a31a0d4430fe14f59622f31db7f25b2275dad2ec52f1040beb030d3e83ad3af4
Name:           perl-Tie-ToObject
Version:        0.03
Release:        51%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Tie to an existing object
Source0:        https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/Tie-ToObject-%{version}.tar.gz
Url:            https://metacpan.org/release/Tie-ToObject
BuildArch:      noarch
Provides:       perl(Tie::ToObject)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(ok)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
