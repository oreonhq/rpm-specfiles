%global source0_hash c2c15a254ca74fb8c57d25d7b6cbcaff77a3b4fb5695423f1f80bb423abffea9

Name:           perl-IO-Capture
Version:        0.05
Release:        49%{?dist}
Summary:        Abstract Base Class to build modules to capture output

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Capture
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REYNOLDS/IO-Capture-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
The IO::Capture Module defines an abstract base class that can be used
to create any number of useful sub-classes that capture output being
sent on a filehandle such as STDOUT or STDERR.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Capture-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc BUGS Changes README
%{perl_vendorlib}/IO/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
