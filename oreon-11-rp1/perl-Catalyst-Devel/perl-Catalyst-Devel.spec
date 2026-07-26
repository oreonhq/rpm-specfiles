%global source0_hash 7ec6f0b6cab5b8c097e47769fc73a4d4c015a58c41fdb40fc24df3ee77c48abd

Name:           perl-Catalyst-Devel
Summary:        Catalyst Development Tools
Version:        1.42
Release:        16%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Devel-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Devel
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst) >= 5.90001
BuildRequires:  perl(Catalyst::Action::RenderView) >= 0.10
BuildRequires:  perl(Catalyst::Plugin::ConfigLoader) >= 0.30
BuildRequires:  perl(Catalyst::Plugin::Static::Simple) >= 0.28
BuildRequires:  perl(Config::General) >= 2.42
BuildRequires:  perl(CPAN)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(File::ChangeNotify) >= 0.07
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(Module::Install) >= 1.02
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Daemonize)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Path::Class) >= 0.09
BuildRequires:  perl(Starman)
BuildRequires:  perl(Template) >= 2.14
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Fatal)

BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(IPC::Run3)

Requires:       perl(Catalyst) >= 5.90001
Requires:       perl(Catalyst::Action::RenderView) >= 0.10
Requires:       perl(Catalyst::Plugin::ConfigLoader) >= 0.30
Requires:       perl(Catalyst::Plugin::Static::Simple) >= 0.28
Requires:       perl(Config::General) >= 2.42
Requires:       perl(File::ChangeNotify) >= 0.07
Requires:       perl(Module::Install) >= 1.02
Requires:       perl(MooseX::Daemonize)
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast)
Requires:       perl(Path::Class) >= 0.09
Requires:       perl(Starman)
Requires:       perl(Template) >= 2.14
Requires:       perl-Catalyst-Runtime-scripts

%{?perl_default_filter}

%description
The Catalyst::Devel package includes a variety of modules useful for the
development of Catalyst applications, but not required to run them. This is
intended to make it easier to deploy Catalyst apps. The runtime parts of
Catalyst are now known as Catalyst::Runtime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Devel-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes t/
%{perl_vendorlib}/*
%{_mandir}/man[13]/*
# we don't need this, and it's causing dep problems.
%exclude %{perl_vendorlib}/Catalyst/Restarter/Win32.pm

%changelog
%autochangelog
