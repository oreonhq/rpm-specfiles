%global source0_hash bfd76acfba988601dc051bda73b4bb25f6839a006dd960b6a7401c249245f65b
%bcond_without perl_Spreadsheet_ParseExcel_enables_optional_test
%bcond_without perl_Spreadsheet_ParseExcel_enables_extra_test
%global debug_package %{nil}
Name:           perl-Spreadsheet-ParseExcel
Epoch:          1
Version:        0.66
Release:        6%{?dist}
Summary:        Extract information from an Excel file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Spreadsheet-ParseExcel
Source0:        https://cpan.metacpan.org/modules/by-module/Spreadsheet/Spreadsheet-ParseExcel-%{version}.tar.gz
Patch0:         Spreadsheet-ParseExcel-0.66-Test-Test95.xls-from-t-excel_files.patch
%if %{with perl_Spreadsheet_ParseExcel_enables_optional_test}
%endif
%if %{with perl_Spreadsheet_ParseExcel_enables_extra_test}
%endif
Requires:       perl(Carp)
Requires:       perl(OLE::Storage_Lite) >= 0.19
Requires:       perl(Text::CSV_XS)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(OLE::Storage_Lite\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::RC4)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::Perl::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Jcode)
BuildRequires:  perl(OLE::Storage_Lite)
BuildRequires:  perl(Perl::MinimumVersion)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Spreadsheet::WriteExcel)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Unicode::Map)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
Requires:       perl(IO::Scalar)
%endif
%if %{with perl_Spreadsheet_ParseExcel_enables_extra_test}
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
install -D -m 644 -p CP932Excel.map \
    %{buildroot}%{perl_vendorarch}/Unicode/Map/MS/WIN/CP932Excel.map
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Spreadsheet_ParseExcel_enables_extra_test}
cp -a META.yml t %{buildroot}%{_libexecdir}/%{name}
%endif
rm %{buildroot}%{_libexecdir}/%{name}/t/90_pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset RELEASE_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test AUTOMATED_TESTING=1
%files -f %{oreon_filedir}/main.list
%files -n perl-Spreadsheet-ParseExcel-tests -f %{oreon_filedir}/perl-Spreadsheet-ParseExcel-tests.list

%changelog

%autochangelog
