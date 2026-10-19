%global source0_hash 1e997781afd4e1bf240f4e347159d3e4c77597f2141ab1541c6268a3356961ad
Name:           perl-Net-IDN-Encode
Summary:        Internationalizing Domain Names in Applications (IDNA)
Version:        2.502
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-IDN-Encode
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/Net-IDN-Encode-%{version}.tar.gz
Patch0:         Net-IDN-Encode-2.500-Make-generated-arrays-available-at-compile-time.patch
Requires:       perl(XSLoader)
%{?perl_default_filter}
Provides:       perl(Net::IDN::Encode)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(Unicode::UCD)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
