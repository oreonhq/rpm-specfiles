%global source0_hash 09ccc176a75e4aa7ff33b04f7f6941c4dd9e9d7053170f499d32ad5ff36d0e12

Name:           perl-Verilog-Readmem
Version:        0.05
Release:        29%{?dist}
Summary:        Parse Verilog $readmemh or $readmemb text file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Verilog-Readmem
Source0:        https://cpan.metacpan.org/authors/id/G/GS/GSULLIVAN/Verilog-Readmem-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
The Verilog Hardware Description Language (HDL) provides a convenient way
to load a memory during logic simulation. The $readmemh() and $readmemb()
system tasks are used in the HDL source code to import the contents of a
text file into a memory variable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Verilog-Readmem-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README examples/
%dir %{perl_vendorlib}/Verilog/
%{perl_vendorlib}/Verilog/Readmem.pm
%{_mandir}/man3/*

%changelog
%autochangelog
