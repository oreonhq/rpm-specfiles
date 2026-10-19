%global source0_hash 5d04395be7e14e970a03ea952fb7629ae304d97c031f90cc1c29bd0a6a62fc40
Name:           perl-Config-Properties
Version:        1.80
Release:        1%{?dist}
Summary:        Read and write property files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-Properties
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/Config-Properties-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Text::Wrap) >= 2001.0929
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Config::Properties is a near implementation of the java.util.Properties
API. It is designed to allow easy reading, writing and manipulation of Java-
style property files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Properties-%{version}

# Fix files encoding
for i in Changes README; do {
iconv -f iso8859-1 -t utf-8 $i > $i.utf8 \
&& touch -r $i $i.utf8 \
&& mv -f $i.utf8 $i; };
done;

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
