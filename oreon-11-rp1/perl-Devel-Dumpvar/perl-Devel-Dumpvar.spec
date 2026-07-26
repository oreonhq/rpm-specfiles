%global source0_hash 1e509f090a82abf998901c5a6d6f8d63ebdaf4457592b0d0b78703f994ab920c

Name:           perl-Devel-Dumpvar
Version:        1.06
Release:        44%{?dist}
Summary:        Pure-OO reimplementation of dumpvar.pl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Dumpvar
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Devel-Dumpvar-%{version}.tar.gz
# Update Makefile.PL to not use Module::Install::DSL CPAN RT#148289
Patch0:         Devel-Dumpvar-1.06-Remove-using-of-MI-DSL.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time
BuildRequires:  perl(Scalar::Util) >= 1.18
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 0.42

%description
Most perl dumping modules are focused on serializing data structures into
a format that can be rebuilt into the original data structure. They do
this with a variety of different focuses, such as human readability, the
ability to execute the dumped code directly, or to minimize the size of
the dumped data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Dumpvar-%{version}
%patch -P0 -p1

# Remove bundled libraries
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
