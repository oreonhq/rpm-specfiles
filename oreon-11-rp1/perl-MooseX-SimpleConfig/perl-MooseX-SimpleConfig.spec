%global source0_hash 42c83f4b92ef2785fa8dbcfae69d5d28d5be10141d171472ccf37288682c79ad
Name:           perl-MooseX-SimpleConfig
Version:        0.11
Release:        32%{?dist}
Summary:        Moose role for setting attributes from a simple configfile
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-SimpleConfig
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-SimpleConfig-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(MooseX::ConfigFromFile)
Provides:       perl(MooseX::SimpleConfig)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::ConfigFromFile)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This role loads simple configfiles to set object attributes. It is based on
the abstract role MooseX::ConfigFromFile, and uses Config::Any to load your
configfile. Config::Any will in turn support any of a variety of different
configuration formats, detected by the file extension. See Config::Any for
more details about supported formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-SimpleConfig-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
