%global source0_hash 47f6e51fb45ce7be561e01481add0c2e1c0cd85df4b9e212f3923cd3064d1cad
Name:           perl-Data-Dump-Streamer
Version:        2.42
Release:        1%{?dist}
Summary:        Accurately serialize a data structure as Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Dump-Streamer
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Dump-Streamer-%{version}.tar.gz
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
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(B::Utils)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Abbrev)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
