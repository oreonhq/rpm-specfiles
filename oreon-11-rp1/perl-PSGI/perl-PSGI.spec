%global source0_hash a56c446740917da86925c29fc6633b9df839b21cf98f6a27086598ed90ee1f47

Name:       perl-PSGI 
Version:    1.102
Release:    36%{?dist}
# PSGI.pod
# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:    LicenseRef-Callaway-CC-BY-SA
Summary:    Perl Web Server Gateway Interface Specification 
Source0:    https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/PSGI-%{version}.tar.gz 
URL:        https://metacpan.org/release/PSGI
BuildArch:  noarch

BuildRequires: coreutils
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(inc::Module::Install)
BuildRequires: perl(Module::Install::Metadata)
BuildRequires: perl(Module::Install::Repository)
BuildRequires: perl(Module::Install::WriteAll)
BuildRequires: sed

%{?perl_default_filter}

%description
This document specifies a standard interface between web servers and Perl web
applications or frameworks, to promote web application portability and reduce
the duplicated efforts by web application framework developers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PSGI-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
