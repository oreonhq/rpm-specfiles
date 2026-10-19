%global source0_hash 12155a5200033d80a5f07573775f493f170072cf7b28ae3ca2d152b591971f11
Name:           perl-Data-Serializer
Version:        0.65
Release:        1%{?dist}
Summary:        Modules that serialize data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Serializer
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEELY/Data-Serializer-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Compress::Zlib)
Requires:       perl(Crypt::Blowfish)
Requires:       perl(Crypt::CBC)
Requires:       perl(Digest)
Requires:       perl(Digest::SHA)
%{?perl_default_filter}
Provides:       perl(Data::Serializer)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Bencode)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config::General)
BuildRequires:  perl(Convert::Bencode)
BuildRequires:  perl(Convert::Bencode_XS)
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Data::Denter)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Taxi)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::Syck)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PHP::Serialization)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::Dumper)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Provides a unified interface to the various serializing modules currently
available. Adds the functionality of both compression and encryption.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Serializer-%{version}
find lib -name \*.pm -print0 | xargs -0 chmod 0644

%build

/usr/bin/perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
