%global source0_hash dc249ad0cad16a1261cb8b91441d449151eb0ccea604134172874558bfc9ac11

Name:           perl-Mail-Box-POP3
Version:        3.008
Release:        3%{?dist}
Summary:        Handle POP3 folders as client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Box-POP3
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Box-POP3-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mail::Box::FastScalar) >= 3
BuildRequires:  perl(Mail::Box::Net) >= 3
BuildRequires:  perl(Mail::Box::Net::Message)
BuildRequires:  perl(Mail::Box::Parser::Perl) >= 3
BuildRequires:  perl(Mail::Transport::Receive) >= 3
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Socket)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Mail::Box::Test) >= 3
BuildRequires:  perl(Test::More)
Requires:       perl(Mail::Box::FastScalar) >= 3
Requires:       perl(Mail::Box::Net) >= 3
Requires:       perl(Mail::Box::Parser::Perl) >= 3
Requires:       perl(Mail::Transport::Receive) >= 3

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mail::Box::FastScalar\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::Box::(Net|Parser::Perl)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::Transport::Receive\\)$

%description
Maintain a folder which has its messages stored on a remote server. The
communication between the client application and the server is implemented
using the POP3 protocol. This class uses Mail::Transport::POP3 to hide the
transport of information, and focuses solely on the correct handling of
messages within a POP3 folder.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Mail-Box-POP3-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

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
#!/bin/bash
set -e
# Some tests write into temporary files/directories
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
MARKOV_DEVEL=1 prove -I .
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
MARKOV_DEVEL=1 make test

%files
%doc ChangeLog README.md
%dir %{perl_vendorlib}/Mail
%{perl_vendorlib}/Mail/Box
%{perl_vendorlib}/Mail/Transport
%{_mandir}/man3/Mail::Box*
%{_mandir}/man3/Mail::Transport*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
