%global source0_hash bfd76acfba988601dc051bda73b4bb25f6839a006dd960b6a7401c249245f65b

# Perform optional tests
%bcond_without perl_Spreadsheet_ParseExcel_enables_optional_test

# Perform automated tests
%bcond_without perl_Spreadsheet_ParseExcel_enables_extra_test

# The debuginfo package is empty. Full-arch package because of
# %%{perl_vendorarch}/Unicode/Map/MS/WIN/CP932Excel.map.
%global debug_package %{nil}

Name:           perl-Spreadsheet-ParseExcel
Epoch:          1
Version:        0.66
Release:        6%{?dist}
Summary:        Extract information from an Excel file
# sample/xls2csv.pl:    Artistic-1.0-Perl
#                       TODO: Clarify with an upstream
#                       <https://github.com/jmcnamara/spreadsheet-parseexcel/issues/10>
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Spreadsheet-ParseExcel
Source0:        https://cpan.metacpan.org/modules/by-module/Spreadsheet/Spreadsheet-ParseExcel-%{version}.tar.gz
# Test Test95.xls from t/excel_files. Required to have the tests relocatable
# without a duplicating Test95.xls. In upstream after 0.66,
# <https://github.com/jmcnamara/spreadsheet-parseexcel/pull/11>.
Patch0:         Spreadsheet-ParseExcel-0.66-Test-Test95.xls-from-t-excel_files.patch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::RC4)
BuildRequires:  perl(Digest::Perl::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::File)
# IO::Scalar not used, we have perl built with PerlIO
BuildRequires:  perl(Jcode)
BuildRequires:  perl(OLE::Storage_Lite) >= 0.19
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Spreadsheet::WriteExcel)
# Text::CSV_XS not used at tests
BuildRequires:  perl(Unicode::Map)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
%if %{with perl_Spreadsheet_ParseExcel_enables_optional_test}
# Optional tests
BuildRequires:  perl(IO::Scalar)
%endif
%if %{with perl_Spreadsheet_ParseExcel_enables_extra_test}
# Extra tests
BuildRequires:  perl(Perl::MinimumVersion) >= 1.20
BuildRequires:  perl(Pod::Simple) >= 3.07
BuildRequires:  perl(Test::CPAN::Meta) >= 0.12
BuildRequires:  perl(Test::MinimumVersion) >= 0.008
BuildRequires:  perl(Test::Pod) >= 1.26
%endif
Requires:       perl(Carp)
Requires:       perl(OLE::Storage_Lite) >= 0.19
Requires:       perl(Text::CSV_XS)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(OLE::Storage_Lite\\)$

%description
The Spreadsheet::ParseExcel module can be used to read information from
Excel 95-2003 binary files.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_Spreadsheet_ParseExcel_enables_optional_test}
# Optional tests
Requires:       perl(IO::Scalar)
%endif
%if %{with perl_Spreadsheet_ParseExcel_enables_extra_test}
# Extra tests
Requires:       perl(Perl::MinimumVersion) >= 1.20
Requires:       perl(Test::CPAN::Meta) >= 0.12
Requires:       perl(Test::MinimumVersion) >= 0.008
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Spreadsheet-ParseExcel-%{version}
%if %{without perl_Spreadsheet_ParseExcel_enables_extra_test}
for T in t/90_pod.t t/91_minimumversion.t t/92_meta.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done
%endif
# Fix line-endings
for file in sample/* t/0[0-5]_*.t; do
    [ -f "$file" ] && perl -pi -e 's/\r\n/\n/' "$file"
done
# Normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}
# For Spreadsheet::ParseExcel::FmtJapan2; see README for details
install -D -m 644 -p CP932Excel.map \
    %{buildroot}%{perl_vendorarch}/Unicode/Map/MS/WIN/CP932Excel.map
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Spreadsheet_ParseExcel_enables_extra_test}
cp -a META.yml t %{buildroot}%{_libexecdir}/%{name}
%endif
# Remove tests that expect modules in a current working directory
rm %{buildroot}%{_libexecdir}/%{name}/t/90_pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/46_save_parser.t writed into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset RELEASE_TESTING
export AUTOMATED_TESTING=1
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset RELEASE_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test AUTOMATED_TESTING=1

%files
%doc Changes README README_Japan.htm examples/ sample/
%dir %{perl_vendorarch}/Unicode
%dir %{perl_vendorarch}/Unicode/Map
%dir %{perl_vendorarch}/Unicode/Map/MS
%dir %{perl_vendorarch}/Unicode/Map/MS/WIN
%{perl_vendorarch}/Unicode/Map/MS/WIN/CP932Excel.map
%dir %{perl_vendorlib}/Spreadsheet
%{perl_vendorlib}/Spreadsheet/ParseExcel
%{perl_vendorlib}/Spreadsheet/ParseExcel.pm
%{_mandir}/man3/Spreadsheet::ParseExcel.3*
%{_mandir}/man3/Spreadsheet::ParseExcel::*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
