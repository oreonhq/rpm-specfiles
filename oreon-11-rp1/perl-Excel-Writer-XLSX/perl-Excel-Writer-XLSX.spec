%global source0_hash 7931b4d8e2fa8b4f806db4bf523be396483f55f53e4f4738fdff5e9a0d875331

Name:           perl-Excel-Writer-XLSX
Version:        1.15
Release:        2%{?dist}
Summary:        Create a new file in the Excel 2007+ XLSX format
# LICENSE_Artistic_Perl:    Artistic-1.0-Perl text
# LICENSE_GPL_1.0:          GPL-1.0 text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Excel-Writer-XLSX
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMCNAMARA/Excel-Writer-XLSX-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.2
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Archive::Zip) >= 1.3
BuildRequires:  perl(autouse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp) >= 0.19
# Getopt::Long not used at tests
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(List::Util)
# Pod::Usage not used at tests
BuildRequires:  perl(utf8)
# Optinal run-time:
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Date::Manip)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
# Test::Differences not helpful, a fallback exists
Requires:       perl(Archive::Zip) >= 1.3
Recommends:     perl(Date::Calc)
Recommends:     perl(Date::Manip)
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(IO::File) >= 1.14

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Archive::Zip\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Temp\\)$
%global __requires_exclude %__requires_exclude|^perl\\(IO::File\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(TestFunctions\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(TestFunctions\\)

%description
The Excel::Writer::XLSX Perl module can be used to create an Excel file in the
2007+ XLSX format. Multiple worksheets can be added to a workbook and
formatting can be applied to cells. Text, numbers, and formulas can be written
to the cells.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Date::Calc)
Requires:       perl(Date::Manip)
Requires:       perl(utf8)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Excel-Writer-XLSX-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
# Regenerate lib/Excel/Writer/XLSX/Examples.pm
%{make_build} mydocs
%{make_build} all

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Many tests, e.g. t/regression/chart_axis25.t, create files under CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE_Artistic_Perl LICENSE_GPL_1.0
# ./examples is compiled and packaged as Excel::Writer::XLSX::Examples
%doc Changelog.md CONTRIBUTING.md README
%dir %{perl_vendorlib}/Excel
%dir %{perl_vendorlib}/Excel/Writer
%{perl_vendorlib}/Excel/Writer/XLSX
%{perl_vendorlib}/Excel/Writer/XLSX.pm
%{_mandir}/man3/Excel::Writer::XLSX.*
%{_mandir}/man3/Excel::Writer::XLSX::*
%{_mandir}/man1/extract_vba.*
%{_bindir}/extract_vba

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
