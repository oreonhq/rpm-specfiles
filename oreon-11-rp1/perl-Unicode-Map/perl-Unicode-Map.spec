%global source0_hash 10f0c2f12ebba57dcd4f46d24cf242c1915d31ec0a4ec36b4df18c9ca0cb4a5a

Name:           perl-Unicode-Map
Version:        0.112
Release:        69%{?dist}
Summary:        Perl module for mapping charsets from and to utf16 unicode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Unicode-Map
Source0:        https://cpan.metacpan.org/modules/by-module/Unicode/Unicode-Map-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Script Runtime
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::Simple)
# Test Suite
# (no additional dependencies)
# Dependencies
# (no additional dependencies)

%{?perl_default_filter}

%description
This module converts strings from and to 2-byte Unicode UCS2 format.
All mappings happen via 2 byte UTF16 encodings, not via 1 byte UTF8
encoding. To convert between UTF8 and UTF16 use Unicode::String.

For historical reasons this module coexists with Unicode::Map8.
Please use Unicode::Map8 unless you need to care for >1 byte character
sets, e.g. Chinese GB2312. Anyway, if you stick to the basic
functionality (see documentation) you can use both modules equivalently.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Unicode-Map-%{version}

# See http://bugzilla.redhat.com/191387
echo '
# Add support for perl-Spreadsheet-ParseExcel
name:    CP932Excel
srcURL:  $SrcUnicode/VENDORS/MICSFT/WINDOWS/CP932.TXT
src:     $DestUnicode/VENDORS/MICSFT/WINDOWS/CP932.TXT
map:     $DestMap/MS/WIN/CP932Excel.map
' >> Map/REGISTRY

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE='%{optflags}'
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc Changes README
%{_bindir}/map
%{_bindir}/mirrorMappings
%{_bindir}/mkCSGB2312
%{_bindir}/mkmapfile
%{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/Unicode/
%{_mandir}/man1/map.1*
%{_mandir}/man1/mkmapfile.1*
%{_mandir}/man3/Unicode::Map.3*

%changelog
%autochangelog
