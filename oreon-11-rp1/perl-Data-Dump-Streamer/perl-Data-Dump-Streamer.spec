%global source0_hash 47f6e51fb45ce7be561e01481add0c2e1c0cd85df4b9e212f3923cd3064d1cad

Name:           perl-Data-Dump-Streamer
Version:        2.42
Release:        11%{?dist}
Summary:        Accurately serialize a data structure as Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Dump-Streamer
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Dump-Streamer-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(B::Utils) >= 0.05
BuildRequires:  perl(bytes)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(overload)
BuildRequires:  perl(PadWalker) >= 0.99
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::Abbrev)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
# Test Suite
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(bytes)
Requires:       perl(Compress::Zlib)
Requires:       perl(Hash::Util)
Requires:       perl(MIME::Base64)
Requires:       perl(PadWalker) >= 0.99
Requires:       perl(re)

%global __provides_exclude ::_::|Streamer\\.so
%global __requires_exclude ::_::

Provides:       perl(Data::Dump::Streamer)
Provides:       perl(Data::Dump::Streamer)
%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The contents of each
variable is output using the least number of Perl statements as convenient,
usually only one. Self-referential structures, closures, and objects are
output correctly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Dump-Streamer-%{version}

%build
perl Build.PL DDS --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README.md
%{perl_vendorarch}/auto/Data/
%{perl_vendorarch}/Data/
%{perl_vendorarch}/DDS.pm
%{_mandir}/man3/Data::Dump::Streamer.3*
%{_mandir}/man3/DDS.3*

%changelog
%autochangelog
