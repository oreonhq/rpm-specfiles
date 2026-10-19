%global source0_hash 1cf8a724bfc69ade0391eef933883a814782ea674557263c85adb7c16182d082
Name:           perl-Config-Model-Backend-Yaml
Version:        2.134
Release:        1%{?dist}
Summary:        Read and write configuration as a YAML data structure
License:        LGPL-2.1-only
URL:            https://metacpan.org/release/Config-Model-Backend-Yaml/
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-Backend-Yaml-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Model)
BuildRequires:  perl(Config::Model::Backend::Any)
BuildRequires:  perl(Config::Model::Exception)
BuildRequires:  perl(Config::Model::Tester)
BuildRequires:  perl(Config::Model::Tester::Setup)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(base)
BuildRequires:  perl(boolean)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is used directly by Config::Model to read or write the content
of a configuration tree written with YAML syntax in Config::Model
configuration tree.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Model-Backend-Yaml-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
