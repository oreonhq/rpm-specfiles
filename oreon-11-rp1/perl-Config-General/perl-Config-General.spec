%global source0_hash 473d65127b23dac0e8039c01e28bc4072cb9a6e93e81a1ea4893cea08c698db0
Name:           perl-Config-General
Version:        2.67
Release:        4%{?dist}
Summary:        Generic configuration module for Perl
License:        Artistic-2.0
URL:            https://metacpan.org/release/Config-General
Source0:        https://cpan.metacpan.org/modules/by-module/Config/Config-General-%{version}.tar.gz
Patch0:         perl-Config-General-2.50-system-ixhash.patch
Patch1:         perl-Config-General-2.63-utf8.patch
BuildArch:      noarch
Provides:       perl(Config::General)
Provides:       perl(Config::General)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module opens a config file and parses its contents for you. After parsing
the module returns a hash structure that contains the representation of the
config file.

The format of config files supported by Config::General is inspired by the well
known Apache config format: in fact, this module is 100%% read-compatible with
Apache config files, but you can also just use simple name/value pairs in your
config files.

In addition to the capabilities of an Apache config file, it supports some
enhancements such as here-documents, C-style comments or multi-line options. It
is also possible to save the config back to disk, which makes the module a
perfect back-end for configuration interfaces. It is possible to use variables
in config files and there also exists support for object oriented access to the
configuration.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Config-General-%{version}

# Use system-packaged version of Tie::IxHash rather than the bundled one
rm -r t/Tie
%patch -P0 -p1

# Re-code Changelog to UTF8
%patch -P1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
