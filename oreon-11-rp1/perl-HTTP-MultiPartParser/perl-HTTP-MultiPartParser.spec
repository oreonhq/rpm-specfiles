%global source0_hash 5eddda159f54d16f868e032440ac2b024e55aac48931871b62627f1a16d00b12

Name:           perl-HTTP-MultiPartParser
Version:        0.02
Release:        27%{?dist}
Summary:        HTTP MultiPart Parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-MultiPartParser
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/HTTP-MultiPartParser-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 1:5.8.1

BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Deep)

BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)

%description
This class provides a low-level API for processing MultiPart MIME data
streams conforming to MultiPart types as defined in RFC 2616.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-MultiPartParser-%{version}
%{__rm} -rf inc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README eg/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
