%global source0_hash 51220fcaf9f66a639b69d251d7b0757bf4202f4f9debd45bdd341a6aca62fe4e

Summary:	I/O on in-core objects like strings and arrays for Perl
Name:		perl-IO-stringy
Version:	2.113
Release:	18%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/IO-stringy
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-Stringy-%{version}.tar.gz



BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(overload)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Dependencies
# (none)

# New upstream maintainer for 2.112 finally got the dist name right
Provides:	perl-IO-Stringy = %{version}-%{release}

# Avoid doc-file dependency on /usr/bin/perl
%{?perl_default_filter}

Provides:       perl(IO::Scalar)
Provides:       perl(IO::Stringy)
Provides:       perl(IO::WrapTie)
%description
This toolkit primarily provides modules for performing both traditional
and object-oriented I/O) on things *other* than normal filehandles; in
particular, IO::Scalar, IO::ScalarArray, and IO::Lines.

In the more-traditional IO::Handle front, we have IO::AtomicFile, which
may be used to painlessly create files that are updated atomically.

And in the "this-may-prove-useful" corner, we have IO::Wrap, whose
exported wraphandle() function will clothe anything that's not a blessed
object in an IO::Handle-like wrapper... so you can just use OO syntax
and stop worrying about whether your function's caller handed you a
string, a globref, or a FileHandle.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-Stringy-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING LICENSE
%doc Changes examples/ README
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::AtomicFile.3*
%{_mandir}/man3/IO::InnerFile.3*
%{_mandir}/man3/IO::Lines.3*
%{_mandir}/man3/IO::Scalar.3*
%{_mandir}/man3/IO::ScalarArray.3*
%{_mandir}/man3/IO::Stringy.3*
%{_mandir}/man3/IO::Wrap.3*
%{_mandir}/man3/IO::WrapTie.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.113-18
- Prepare for Oreon 11 (RP1)
