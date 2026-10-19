%global source0_hash 3cd41971688990cafd58420bf61f87d8fd03bc68276b3f311482bbfeed952bb0
Name:           perl-App-Nopaste
Version:        1.013
Release:        1%{?dist}
Summary:        Easy access to any pastebin
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-Nopaste
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/App-Nopaste-%{version}.tar.gz
BuildArch:      noarch
Requires:       /usr/bin/scp
Requires:       perl(Clipboard)
Requires:       perl(Browser::Open)
Requires:       perl(WWW::Pastebin::PastebinCom::Create)
Requires:       perl(HTTP::Request::Common)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(base)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Pastebins (also known as nopaste sites) let you post text, usually code,
for public viewing. They're used a lot in IRC channels to show code that
would normally be too long to give directly in the channel (hence the
name nopaste).

%package -n nopaste
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
%oreon_autofiles nopaste usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n nopaste -f %{oreon_filedir}/nopaste.list

%changelog

%autochangelog
