%global source0_hash bc36f404438ac36ad2b9295539227d36f99cd1623f1e347af77c594c40ccbcf8

Name:           perl-Data-HexDump
Version:        0.04
Release:        14%{?dist}
Summary:        Hexadecimal Dumper
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-HexDump
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-HexDump-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
# (no additional dependencies)
# Dependencies
# (no additional dependencies)

%description
Dump in hexadecimal the content of a scalar. The result is returned in a
string. Each line of the result consists of the offset in the source in the
leftmost column of each line, followed by one or more columns of data from
the source in hexadecimal. The rightmost column of each line shows the
printable characters (all others are shown as single dots).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-HexDump-%{version}

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
%license LICENSE
%doc Changes eg/ README
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::HexDump.3*

%changelog
%autochangelog
