%global source0_hash c180291ae60a89106d1ae2e6493e8b4013f6fee6236279923546722a36d5b1ce

Name:           perl-Hash-DefHash
Version:        0.072
Release:        12%{?dist}
Summary:        Manipulate defhash
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Hash-DefHash
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Hash-DefHash-%{version}.tar.gz
BuildArch:      noarch

# Require module version when importing Exporter (#1788170)
Patch0:         Hash-DefHash_exporter.patch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Regexp::Pattern::DefHash)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Trim::More)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(warnings)

%description
DefHash - Define things according to a specification, using hashes.
See the DefHash specification at https://metacpan.org/pod/DefHash.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Hash-DefHash-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/Hash::DefHash*.*

%changelog
%autochangelog
