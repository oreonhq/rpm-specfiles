%global source0_hash b64bce1ff212d7e3ef9d4368e7b62749cf27751fa8360cdf53e969123346a729
Name:           perl-Parse-DebControl
Version:        2.005
Release:        35%{?dist}
Summary:        Easy OO parsing of debian control-like files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parse-DebControl
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JAYBONCI/Parse-DebControl-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Easy OO parsing of debian control-like files .

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Parse-DebControl-%{version}
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
