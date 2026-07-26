%global source0_hash 3a9adeffff8d64b157c3ddb9c54468e7296356a07081739e9ab903b4953248b3

Name:           perl-IO-Null
Version:        1.01
Release:        50%{?dist}
Summary:        Class for null filehandles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Null
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBURKE/IO-Null-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Test)

%description
IO::Null is a class for null filehandles.  Calling a constructor of
this class always succeeds, returning a new null filehandle.  Writing
to any object of this class is always a no-operation, and returns
true.  Reading from any object of this class is always no-operation,
and returns empty-string or empty-list, as appropriate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Null-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
