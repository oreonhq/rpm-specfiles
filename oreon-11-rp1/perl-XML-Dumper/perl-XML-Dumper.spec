%global source0_hash f4170eb5236e1261baeb5c47dd4fe73bdb84baf562dd84f01ddded46b403f8e0

Name:           perl-XML-Dumper
Version:        0.81
Release:        53%{dist}
Summary:        Perl module for dumping Perl objects from/to XML

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Dumper
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKEWONG/XML-Dumper-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Parser)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
Recommends:     perl(Compress::Zlib)


Provides:       perl(XML::Dumper)
%description
XML::Dumper dumps Perl data to XML format. XML::Dumper can also read
XML data that were previously dumped by the module and convert it back
to Perl. Perl objects are blessed back to their original packaging;
if the modules are installed on the system where the perl objects are
reconstituted from xml, they will behave as expected. Intuitively, if
the perl objects are converted and reconstituted in the same
environment, all should be well.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n XML-Dumper-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

for file in README; do
  iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
  mv -f "${file}_" "$file"
done


%check
make test


%files
%doc Changes README
%{perl_vendorlib}/XML/
%{_mandir}/man3/*.3*


%changelog
%autochangelog
