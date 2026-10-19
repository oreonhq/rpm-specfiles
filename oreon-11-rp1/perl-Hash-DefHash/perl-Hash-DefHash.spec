%global source0_hash c180291ae60a89106d1ae2e6493e8b4013f6fee6236279923546722a36d5b1ce
Name:           perl-Hash-DefHash
Version:        0.072
Release:        1%{?dist}
Summary:        Manipulate defhash
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-DefHash
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Hash-DefHash-%{version}.tar.gz
BuildArch:      noarch
Patch0:         Hash-DefHash_exporter.patch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Regexp::Pattern::DefHash)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::Trim::More)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DefHash - Define things according to a specification, using hashes.
See the DefHash specification at https://metacpan.org/pod/DefHash.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Hash-DefHash-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
