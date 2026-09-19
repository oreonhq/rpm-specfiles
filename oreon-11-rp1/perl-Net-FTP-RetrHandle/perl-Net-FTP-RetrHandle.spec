%global source0_hash f4a26a06237c9f87119f5d10d7a25174b2af7f71bd9b3015888401ce0e1a6754

# Perform tests that access the Internet.
%bcond_with perl_Net_FTP_RetrHandle_enables_network_test

%global         cpan_name Net-FTP-RetrHandle
Name:           perl-%{cpan_name}
Version:        0.2
Release:        45%{?dist}
Summary:        File reading interface for reading files on a remote FTP server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GI/GIFF/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
%if %{with perl_Net_FTP_RetrHandle_enables_network_test}
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(Symbol)
%endif
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This Perl module provides a file reading interface for reading all or parts of
files located on a remote FTP server, including emulation of seek and support
for downloading only the parts of the file requested.

Support for skipping the beginning of the file is implemented with the FTP REST
command, which starts a retrieval at any point in the file. Support for
skipping the end of the file is implemented with the FTP ABOR command, which
stops the transfer. With these two commands and some careful tracking of the
current file position, we're able to reliably emulate a seek/read pair, and get
only the parts of the file that are actually read.

This was originally designed for use with Archive::Zip; it's reliable enough
that the table of contents and individual files can be extracted from a remote
ZIP archive without downloading the whole thing.

An interface compatible with IO::Handle is provided, along with a tie-based
interface.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Net::FTP::RetrHandle)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{cpan_name}-%{version}
# Remove any CVS files
find -type d -name CVS -exec rm -rf {} +
perl -i -ne 'print $_ unless m{/CVS/}' MANIFEST
# Remove network tests
%if !%{with perl_Net_FTP_RetrHandle_enables_network_test}
for T in t/10remote.t t/11tie.t; do
  rm "$T"
  perl -i -ne 'print $_ unless m{^'"$T"'}' MANIFEST
done
%endif
# Correct permissions
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
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
%doc TODO NEWS
%dir %{perl_vendorlib}/Net
%dir %{perl_vendorlib}/Net/FTP
%{perl_vendorlib}/Net/FTP/RetrHandle.pm
%{_mandir}/man3/Net::FTP::RetrHandle.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
