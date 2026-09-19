%global source0_hash 49744f42a6f3800bd9755c202f6309bcd75dcc2c325f36568df519764b2ce61f

Name:           perl-Config-Model-Itself
Version:        2.025
Release:        3%{?dist}
Summary:        Model editor for Config::Model
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Config-Model-Itself
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-Itself-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  bash-completion
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(App::Cmd::Tester)
BuildRequires:  perl(App::Cme) >= 1.002
BuildRequires:  perl(App::Cme::Common)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Model) >= 2.142
BuildRequires:  perl(Config::Model::Tester::Setup)
BuildRequires:  perl(Config::Model::TkUI) >= 1.378
BuildRequires:  perl(Config::Model::Value)
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Log4perl) >= 1.11
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(Path::Tiny) >= 0.125
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File::Contents)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Tk)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML::PP)
BuildRequires:  sed
Requires:       bash-completion
Requires:       perl(App::Cme) >= 1.002
#Requires:       perl(Config::Model::TkUI) >= 1.378

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Config::Model\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Config::Model\\) >= 2.064\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Config::Model::TkUI\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Log::Log4perl\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(App::Cme\\)\s*$

%description
Config::Itself module and its model files provide a model of Config:Model
(hence the Itself name).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Model-Itself-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

# Install bash_completion script
install -D -m 0644 contrib/bash_completion.cme_meta %{buildroot}%{_sysconfdir}/bash_completion.d/cme_meta

%check
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md data README.md
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/Cme*
%dir %{perl_vendorlib}/Config
%{perl_vendorlib}/Config/Model*
%{_mandir}/man3/App::Cme::Command::meta*
%{_mandir}/man3/Config::Model::Itself*
%{_mandir}/man3/Config::Model::models::Itself*
%config(noreplace) %{_sysconfdir}/bash_completion.d/cme_meta

%changelog
%autochangelog
