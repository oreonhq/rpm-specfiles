%global source0_hash 82c63f0e2defa344f8bb8bd0c0f031520d2d58aba53d7fcf365aefd90d050d6f
Name:           licensecheck
Version:        3.3.10
Release:        1%{?dist}
Summary:        Simple license checker for source files
License:        AGPL-3.0-or-later
BuildArch:      noarch
URL:            https://metacpan.org/release/App-Licensecheck
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/App-Licensecheck-v%{version}.tar.gz
Requires:       perl(Log::Any::Adapter::Screen)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Feature::Compat::Class)
BuildRequires:  perl(Feature::Compat::Try)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::Copyright)
BuildRequires:  perl(String::License)
BuildRequires:  perl(String::License::Naming)
BuildRequires:  perl(String::License::Naming::Custom)
BuildRequires:  perl(String::License::Naming::SPDX)
BuildRequires:  perl(Test2::Suite)
BuildRequires:  perl(Test2::Tools::Command)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(autodie)
BuildRequires:  perl(if)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Licensecheck attempts to determine the license that applies to each file passed
to it, by searching the start of the file for text belonging to various
licenses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir App-Licensecheck-v%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor
%make_build
%install
make pure_install DESTDIR=%{buildroot}
rm -f %{buildroot}%{perl_vendorarch}/auto/App/Licensecheck/.packlist
install -Dpm 0644 scripts/licensecheck.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/licensecheck
%oreon_autofiles main

%check

make test || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
