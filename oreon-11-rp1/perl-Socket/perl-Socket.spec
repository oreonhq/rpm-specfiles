Name:           perl-Socket
Epoch:          4
Version:        2.040
Release:        3%{?dist}
Summary:        Networking constants and support functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Socket
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Socket-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 be0102fdcea8d43f1b02ef2ef94345ac4bbc7b6c66ece2ddd1a3593d8371ba1b
%global source0_file Socket-2.040.tar.gz
# oreon url source checksums end
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Constant) >= 0.23
# ExtUtils::Constant::ProxySubs not used
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Scalar::Util is needed only if getaddrinfo(3) does not exist. Not our case.
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# Tests only:
BuildRequires:  perl(Errno)
BuildRequires:  perl(Test::More)
Requires:       perl(:VERSION) >= 5.6.1

%{?perl_default_filter}

%description
This Perl module provides a variety of constants, structure manipulators and
other functions related to socket-based networking. The values and functions
provided are useful when used in conjunction with Perl core functions such as
socket(), setsockopt() and bind(). It also provides several other support
functions, mostly for dealing with conversions of network addresses between
human-readable and native binary forms, and for hostname resolver operations.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Socket-2.040.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "be0102fdcea8d43f1b02ef2ef94345ac4bbc7b6c66ece2ddd1a3593d8371ba1b" || { echo "oreon: Source0 SHA256 mismatch for Socket-2.040.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Socket-%{version}

# Help file to recognise the Perl scripts
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
%license Artistic Copying LICENSE
%doc Changes
%{perl_vendorarch}/auto/Socket*
%{perl_vendorarch}/Socket*
%{_mandir}/man3/Socket*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.040-3
- Prepare for Oreon 11 (RP1)
