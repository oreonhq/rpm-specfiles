%global source0_hash 2f6e37fb770362b3934e2858fa00e3b45dcaaeec352f00e7f20defefd6c6c1c3

Name:           perl-Mon
Version:        0.11
Release:        48%{?dist}
Summary:        Mon Perl module
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Mon
Source0:        https://cpan.metacpan.org/authors/id/T/TR/TROCKIJ/Mon-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Convert::BER)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Text::ParseWords)
# Tests:
BuildRequires:  perl(Data::Dumper)

%description
This is the Perl5 module for interfacing with the Mon system monitoring
package. Currently only the client interface is implemented, but more
things like special logging routines and persistent monitors are being
considered.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mon-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES COPYING COPYRIGHT monperl.prj README VERSION
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
