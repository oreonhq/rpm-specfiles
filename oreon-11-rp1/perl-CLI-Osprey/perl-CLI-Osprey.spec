%global source0_hash 8549a09fdc97981298bd8f3aa2755294acaa7939ca279d3840bebc259a46844e

Name:           perl-CLI-Osprey
Version:        0.09
Release:        2%{?dist}
Summary:        MooX::Options + MooX::Cmd + Sanity
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            http://search.cpan.org/dist/CLI-Osprey/
Source0:        http://www.cpan.org/authors/id/A/AR/ARODLAND/CLI-Osprey-%{version}.tar.gz

BuildArch:      noarch
# build dependencies
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
# runtime dependencies
BuildRequires:  perl(Carp)
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.100
BuildRequires:  perl(Getopt::Long::Descriptive::Usage)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test dependencies
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Test::Lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
Requires:       perl(Pod::Usage)

%{?perl_default_filter}

%description
CLI::Osprey is a module to assist in writing command-line applications with
M* OO modules (Moose, Moo, Mo). With it, you structure your app as one
or more modules, which get instantiated with the command-line arguments
as attributes. Arguments are parsed using Getopt::Long::Descriptive,
and both long and short help messages as well as complete manual pages
are automatically generated. An app can be a single command with
options, or have sub-commands (like git). Sub-commands can be defined
as modules (with options of their own) or as simple code-refs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CLI-Osprey-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes eg README
%license LICENSE
%{perl_vendorlib}/CLI*
%{_mandir}/man3/CLI*

%changelog
%autochangelog
