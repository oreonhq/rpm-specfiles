%global source0_hash 43b9a1bca02989dd6310332568cfe95a47c321dae782d9905db4e585b2f27ad8

Name:           perl-TAP-Harness-JUnit
Version:        0.42
Release:        32%{?dist}
Summary:        Generate JUnit compatible output from TAP results
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/TAP-Harness-JUnit
Source0:        https://cpan.metacpan.org/authors/id/J/JL/JLAVALLEE/TAP-Harness-JUnit-%{version}.tar.gz
Patch0:         perl-TAP-Harness-JUnit-0.32-ascii.patch

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
Requires:       perl(TAP::Harness) >= 3.05
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(TAP::Harness) >= 3.05
BuildRequires:  perl(TAP::Parser)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(TAP::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Encode)

%{?perl_default_filter}

%description
The only difference between this module and TAP::Harness is that this adds
mandatory 'xmlfile' argument, that causes the output to be formatted into
XML in format similar to one that is produced by JUnit testing framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TAP-Harness-JUnit-%{version}
%patch -P0 -p1 -b .ascii

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test || :

%files
%doc README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
