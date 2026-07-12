%global source0_hash 42c83f4b92ef2785fa8dbcfae69d5d28d5be10141d171472ccf37288682c79ad

Name:           perl-MooseX-SimpleConfig
Version:        0.11
Release:        32%{?dist}
Summary:        Moose role for setting attributes from a simple configfile
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-SimpleConfig
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-SimpleConfig-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Config::Any) >= 0.13
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::ConfigFromFile)
# Tests:
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.120900
BuildRequires:  perl(YAML::Syck)
# Dependencies
Requires:       perl(MooseX::ConfigFromFile)

Provides:       perl(MooseX::SimpleConfig)
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

%check
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/MooseX/
%{_mandir}/man3/MooseX::SimpleConfig.3*

%changelog
%autochangelog
