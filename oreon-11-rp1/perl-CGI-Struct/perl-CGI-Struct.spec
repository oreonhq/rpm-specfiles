%global source0_hash d13d8da7fdcd6d906054e4760fc28a718aec91bd3cf067a58927fb7cb1c09d6c

Name:           perl-CGI-Struct
Version:        1.21
Release:        33%{?dist}
Summary:        Build structures from CGI data
# BSD License (two clause), according to lib/CGI/Struct.pm
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

URL:            https://metacpan.org/release/CGI-Struct
Source0:        https://cpan.metacpan.org/authors/id/F/FU/FULLERMD/CGI-Struct-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Deep::NoTest)
BuildRequires:  perl(Test::More) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
CGI::Struct lets you transform CGI data keys that look like perl data
structures into actual perl data structures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Struct-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/CGI*
%{_mandir}/man3/CGI*

%changelog
%autochangelog
