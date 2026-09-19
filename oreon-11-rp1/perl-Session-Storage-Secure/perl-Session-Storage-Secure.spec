%global source0_hash 58b2f04eba56a9924494bb3eddd426affa75c3dded1c563f8296fcc13f8e666b

Name:           perl-Session-Storage-Secure
Version:        1.000
Release:        15%{?dist}
Summary:        Encrypted, expiring, compressed, serialized session data with integrity
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Session-Storage-Secure
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Session-Storage-Secure-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::CBC) >= 3.01
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Math::Random::ISAAC::XS)
BuildRequires:  perl(MIME::Base64) >= 3.12
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike::Base) >= 0.16
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Sereal::Decoder) >= 4.005
BuildRequires:  perl(Sereal::Encoder) >= 4.005
BuildRequires:  perl(String::Compare::ConstantTime)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Tolerant)
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(Sereal::Decoder) >= 4.005
Requires:       perl(Sereal::Encoder) >= 4.005

# Remove under-specified dependencies
%global __requieres_exclude %{?__requieres_exclude:%{__requieres_exclude}|}^perl\\(Sereal::Decoder|Sereal::Encoder\\)$

%description
This module implements a secure way to encode session data. It is primarily
intended for storing session data in browser cookies, but could be used
with other back-end storage where security of stored session data is
important.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Session-Storage-Secure-%{version}
# Help generators to recognize a Perl code
for F in t/*.t; do
    perl -i -MConfig -pe 'print qq{$Config{startperl}\n} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset Session_Storage_Secure_Version
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset Session_Storage_Secure_Version
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
