%global source0_hash 670ac80b2e42111f1bc38b2a6e405a1759cc2c6a5c12f15a689a2a542415d8f1

Name:           perl-PDF-Reuse
Version:        0.43
Release:        1%{?dist}
Summary:        Reuse and mass produce PDF documents
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Url:            https://metacpan.org/release/PDF-Reuse
Source:         https://cpan.metacpan.org/authors/id/C/CN/CNIGHS/PDF-Reuse-%{version}.tar.gz
Patch0:         PDF-Reuse-0.39-Test-PDF-to-temp.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(autouse)
# Carp not used at tests
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(constant)
# Data::Dumper not used at tests
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::PDF::TTFont0)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Font::TTF)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)
Requires:       perl(Text::PDF::TTFont0)

%description
This module allows you to reuse PDF-files. You can use pages, images,
fonts and Acrobat JavaScript from old PDF-files (if they were not
encrypted), and rearrange the components, and add new graphics, texts etc.

There is also support for graphics. In the tutorial there is a description of
how to transform simple PDF-pages to graphic Perl objects with the help of
programs based on this module.

The module is fairly fast, so it should be possible to use it for mass
production. 

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PDF-Reuse-%{version}
%patch -P0
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
