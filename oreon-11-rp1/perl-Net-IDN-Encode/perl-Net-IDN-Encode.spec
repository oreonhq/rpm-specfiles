%global source0_hash 1e997781afd4e1bf240f4e347159d3e4c77597f2141ab1541c6268a3356961ad

Name:           perl-Net-IDN-Encode
Summary:        Internationalizing Domain Names in Applications (IDNA)
Version:        2.502
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-IDN-Encode
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/Net-IDN-Encode-%{version}.tar.gz
# Make Unicode property generator compatible with perl 5.30-RC1,
# CPAN RT#129588, <https://github.com/cfaerber/Net-IDN-Encode/pull/8>
Patch0:         Net-IDN-Encode-2.500-Make-generated-arrays-available-at-compile-time.patch
# Adapt to perl-5.38.0 and stricter GCC, bug #2241714, CPAN RT#149108,
# proposed to an upstream.

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(integer)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(open)
# An optional dependency, via Unicode::UCD
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(Unicode::UCD)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

# This isn't picked up automatically by rpmbuild
Requires:       perl(XSLoader)

%{?perl_default_filter}

Provides:       perl(Net::IDN::Encode)
%description
This module provides an easy-to-use interface for encoding and decoding
Internationalized Domain Names (IDNs).


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Net-IDN-Encode-%{version}

# Remove incorrect executable bits
chmod -x lib/Net/IDN/Encode.pm \
         lib/Net/IDN/Standards.pod

# Convert files to UTF-8
for FILE in LICENSE README; do
  iconv -f ISO_8859-1 -t UTF8 $FILE > $FILE.utf8
  mv $FILE.utf8 $FILE
done


%build
# Makefile.PL is broken, use Build.PL
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*


%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test


%files
%doc Changes eg README
%license LICENSE
%dir %{perl_vendorarch}/auto/Net
%{perl_vendorarch}/auto/Net/IDN
%dir %{perl_vendorarch}/Net
%{perl_vendorarch}/Net/IDN
%{_mandir}/man3/Net::IDN::*.3pm*

%changelog
%autochangelog
