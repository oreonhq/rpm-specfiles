%global source0_hash 36a918355ccc7a6540e0da7ce5b1e80c281215416987eed3a59e7e671e4f5adb

Name:           perl-Test-Unit-Runner-Xml
Version:        0.1
Release:        47%{?dist}
Summary:        Generate XML reports from unit test results
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Unit-Runner-Xml
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Unit-Runner-Xml-%{version}.tar.gz
# Fix perl 5.16 compatibility, CPAN RT #77898
Patch0:         Test-Unit-Runner-Xml-0.1-Load-File-Spec.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Unit::Runner)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::Generator)
# Tests
BuildRequires:  perl(Error)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Unit) >= 0.24
BuildRequires:  perl(Test::Unit::TestCase)
BuildRequires:  perl(Test::Unit::TestSuite)
BuildRequires:  perl(XML::XPath)

%description
Test::Unit::Runner::XML generates XML reports from unit test results. The
reports are in the same format as those produced by Ant's JUnit task, allowing
them to be used with Java continuous integration and reporting tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Unit-Runner-Xml-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
