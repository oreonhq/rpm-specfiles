%global source0_hash 0e0ceb30495ecf64dc6cacd12113d604871104c0cfe153487b8d68bc9393d78f

Name:           perl-Perl6-Slurp
Version:        0.051005
Release:        35%{?dist}
Summary:        Implementation of the Perl 6 'slurp' built-in
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl6-Slurp
Source0:        https://cpan.metacpan.org/modules/by-module/Perl6/Perl6-Slurp-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Dependencies
# (none)

%description
slurp takes:

a filename,
a filehandle,
a typeglob reference,
an IO::File object, or
a scalar reference,

converts it to an input stream (using open() if necessary), 
and reads in the entire stream. If slurp fails to set up or 
read the stream, it throws an exception.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn Perl6-Slurp-%{version}

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
%doc Changes demo/ README
%{perl_vendorlib}/Perl6/
%{_mandir}/man3/Perl6::Slurp.3*

%changelog
%autochangelog
