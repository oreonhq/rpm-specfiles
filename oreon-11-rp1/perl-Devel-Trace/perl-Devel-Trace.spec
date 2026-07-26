%global source0_hash f501caf776ff7e986f76e02544d6ce234c89770173283f31df7dcc57800a3868

Name:           perl-Devel-Trace
Version:        0.12
Release:        36%{?dist}
Summary:        Print out each line before it is executed (like sh -x)

License:        LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Devel-Trace

Source0:        https://cpan.metacpan.org/authors/id/M/MJ/MJD/Devel-Trace-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
If you run your program with perl -d:Trace program, this module will print
a message to standard error just before each line is executed.

This is something like the shell's -x option.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Trace-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

# This shouldn't be installed there, it's documentation
rm %{buildroot}%{perl_vendorlib}/Devel/demo.pl

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README sample demo.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
