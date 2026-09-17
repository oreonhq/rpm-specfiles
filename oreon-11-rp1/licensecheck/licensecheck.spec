%global source0_hash 9ef830a9dd0e25a2f603691f30da90976fa1af7456b06ef04f63f4f299e04e9f

Name:           licensecheck
Version:        3.3.9
Release:        8%{?dist}
Summary:        Simple license checker for source files

License:        AGPL-3.0-or-later
BuildArch:      noarch
URL:            https://metacpan.org/release/App-Licensecheck
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/App-Licensecheck-v%{version}.tar.gz

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators

BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Feature::Compat::Class)
BuildRequires:  perl(Feature::Compat::Try)
BuildRequires:  perl(if)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Copyright)
BuildRequires:  perl(String::License)
BuildRequires:  perl(String::License::Naming)
BuildRequires:  perl(String::License::Naming::Custom)
BuildRequires:  perl(String::License::Naming::SPDX)
# BuildRequires:  perl(SVG::Box)
BuildRequires:  perl(Test2::Suite)
BuildRequires:  perl(Test2::Tools::Command)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  make

Requires:       perl(Log::Any::Adapter::Screen)

%description
Licensecheck attempts to determine the license that applies to each file passed
to it, by searching the start of the file for text belonging to various
licenses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n App-Licensecheck-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# Remove .packlist
rm -f %{buildroot}%{perl_vendorarch}/auto/App/Licensecheck/.packlist
# Install bash-completions file
install -Dpm 0644 scripts/licensecheck.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/licensecheck

%check
make test || :

%files
%doc Changes README
%license LICENSE
%{_bindir}/licensecheck
%{_datadir}/bash-completion/
%{perl_vendorlib}/*
%{_mandir}/man1/licensecheck.1*
%{_mandir}/man3/App::Licensecheck.*

%changelog
%autochangelog
