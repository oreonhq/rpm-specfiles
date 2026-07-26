%global source0_hash 3cd41971688990cafd58420bf61f87d8fd03bc68276b3f311482bbfeed952bb0

Name:           perl-App-Nopaste
Version:        1.013
Release:        19%{?dist}
Summary:        Easy access to any pastebin
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-Nopaste
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/App-Nopaste-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(namespace::clean)
# Tests only
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(version)
# for ssh plugin
Requires:       /usr/bin/scp
Requires:       perl(Clipboard)
Requires:       perl(Browser::Open)
Requires:       perl(WWW::Pastebin::PastebinCom::Create)
Requires:       perl(HTTP::Request::Common)

%description
Pastebins (also known as nopaste sites) let you post text, usually code,
for public viewing. They're used a lot in IRC channels to show code that
would normally be too long to give directly in the channel (hence the
name nopaste).

%package -n nopaste
# needs to beat old nopaste-2835-3
Epoch:          1
Summary:        Access pastebins from the command line
Requires:       %{name} = 0:%{version}-%{release}

%description -n nopaste
This application lets you post text to pastebins from the command line.

Pastebins (also known as nopaste sites) let you post text, usually code, for
public viewing. They're used a lot in IRC channels to show code that would
normally be too long to give directly in the channel (hence the name nopaste).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-Nopaste-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 </dev/null
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes CONTRIBUTING README
%license LICENSE
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/Nopaste*
%{_mandir}/man3/App::Nopaste*

%files -n nopaste
%{_bindir}/nopaste
%{_mandir}/man1/nopaste.*

%changelog
%autochangelog
