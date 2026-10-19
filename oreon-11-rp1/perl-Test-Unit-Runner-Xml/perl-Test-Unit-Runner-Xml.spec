%global source0_hash 36a918355ccc7a6540e0da7ce5b1e80c281215416987eed3a59e7e671e4f5adb
Name:           perl-Test-Unit-Runner-Xml
Version:        0.1
Release:        1%{?dist}
Summary:        Generate XML reports from unit test results
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Unit-Runner-Xml
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Unit-Runner-Xml-%{version}.tar.gz
Patch0:         Test-Unit-Runner-Xml-0.1-Load-File-Spec.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Error)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Unit)
BuildRequires:  perl(Test::Unit::Runner)
BuildRequires:  perl(Test::Unit::TestCase)
BuildRequires:  perl(Test::Unit::TestSuite)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::Generator)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(base)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
