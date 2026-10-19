%global source0_hash 51220fcaf9f66a639b69d251d7b0757bf4202f4f9debd45bdd341a6aca62fe4e
Summary:        I/O on in-core objects like strings and arrays for Perl
Name:		perl-IO-stringy
Version:	2.113
Release:        18%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/IO-stringy
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-Stringy-%{version}.tar.gz
BuildArch:	noarch
Provides:	perl-IO-Stringy = %{version}-%{release}
%{?perl_default_filter}
Provides:       perl(IO::Scalar)
Provides:       perl(IO::Stringy)
Provides:       perl(IO::WrapTie)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.113-18
- Prepare for Oreon 11 (RP1)
