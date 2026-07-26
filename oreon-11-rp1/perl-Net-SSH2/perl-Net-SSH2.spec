%global source0_hash 1c124699745eeb40ed636097fdcc3e722c94cfd7704ebc0acfb0f05541d2809c

Name:           perl-Net-SSH2
Version:        0.74
Release:        5%{?dist}
Summary:        Support for the SSH 2 protocol via libSSH2
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-SSH2
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/Net-SSH2-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libgcrypt-devel
BuildRequires:  libssh2-devel >= 0.18
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(inc::Module::Install) >= 1.17
BuildRequires:  perl(Module::Install::CheckLib)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  zlib-devel
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
# IO::Socket::IP is preferred
# XXX: BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(IO::Scalar)
Requires:       perl(IO::Socket::IP)
Recommends:     perl(Term::ReadKey)
Provides:       perl(Net::SSH2::Constants) = %{version}

%{?perl_default_filter}

%description
Net::SSH2 is a perl interface to the libssh2 (http://www.libssh2.org)
library. It supports the SSH2 protocol (there is no support for SSH1) with
all of the key exchanges, ciphers, and compression of libssh2.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-SSH2-%{version}

# Remove bundled libraries
# Don't remove inc/ to prevent setting $Module::Install::AUTHOR
rm -r inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
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
# note most of these tests will skip -- that's fine, they'd fail in the
# buildsys anyways as they require network access
make test

%files
%doc Changes README.pod example
%{perl_vendorarch}/auto/Net*
%dir %{perl_vendorarch}/Net
%{perl_vendorarch}/Net/SSH2*
%{_mandir}/man3/Net::SSH2*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
