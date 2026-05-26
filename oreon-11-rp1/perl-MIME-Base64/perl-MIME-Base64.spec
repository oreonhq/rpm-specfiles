Name:           perl-MIME-Base64
Version:        3.16
Release:        521%{?dist}
Summary:        Encoding and decoding of Base64 and quoted-printable strings
# Base.xs:      (GPL-1.0-or-later OR Artistic-1.0-Perl) AND metamail
# Other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND metamail
URL:            https://metacpan.org/release/MIME-Base64
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/MIME-Base64-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 77f73d6f7aeb8d33be08b0d8c2617f9b6c77fb7fc45422d507ca8bafe4246017
%global source0_file MIME-Base64-3.16.tar.gz
# oreon url source checksums end
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
# Perl::API not yet packaged and does not work since perl 5.8.8
Conflicts:      perl < 4:5.22.0-347

%description
This package contains a Base64 encoder/decoder and a quoted-printable
encoder/decoder. These encoding methods are specified in RFC 2045 - MIME
(Multipurpose Internet Mail Extensions).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/MIME-Base64-3.16.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "77f73d6f7aeb8d33be08b0d8c2617f9b6c77fb7fc45422d507ca8bafe4246017" || { echo "oreon: Source0 SHA256 mismatch for MIME-Base64-3.16.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n MIME-Base64-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/MIME*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.16-521
- Prepare for Oreon 11 (RP1)
