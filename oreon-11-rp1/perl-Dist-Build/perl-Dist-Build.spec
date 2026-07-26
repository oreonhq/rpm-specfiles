%global source0_hash e7fe114af13e22c9b536c144380d9ee6385940a190f9552b8e25acb92aab1b8c

Name:           perl-Dist-Build
Version:        0.025
Release:        1%{?dist}
Summary:        Modern module builder with author tools not included

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Dist-Build
Source0:        https://www.cpan.org/authors/id/L/LE/LEONT/Dist-Build-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Merge)
BuildRequires:  perl(CPAN::Requirements::Dynamic) >= 0.002
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::Builder::Action::Function)
BuildRequires:  perl(ExtUtils::Builder::Compiler) >= 0.034
BuildRequires:  perl(ExtUtils::Builder::Node)
BuildRequires:  perl(ExtUtils::Builder::ParseXS)
BuildRequires:  perl(ExtUtils::Builder::Planner) >= 0.016
BuildRequires:  perl(ExtUtils::Builder::Planner::Extension)
BuildRequires:  perl(ExtUtils::Builder::Serializer)
BuildRequires:  perl(ExtUtils::Builder::Util) >= 0.019
BuildRequires:  perl(ExtUtils::Config)
BuildRequires:  perl(ExtUtils::HasCompiler) >= 0.024
BuildRequires:  perl(ExtUtils::Helpers) >= 0.028
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::InstallPaths)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir::Tiny)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(strict)
BuildRequires:  perl(TAP::Harness::Env)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
Requires:       perl(CPAN::Meta::Merge)
Requires:       perl(CPAN::Requirements::Dynamic) >= 0.002
Requires:       perl(ExtUtils::Builder::Compiler) >= 0.034
Requires:       perl(Perl::OSType)
Requires:       perl(Pod::Man)
Requires:       perl(TAP::Harness::Env)

%{?perl_default_filter}

%description
Dist::Build is a Build.PL implementation. Unlike Module::Build::Tiny it is
extensible, unlike Module::Build it uses a build graph internally which
makes it easy to combine different customizations. It's typically extended
by adding a .pl script in planner/.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Build-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes examples README
%license LICENSE
%dir %{perl_vendorlib}/Dist
%{perl_vendorlib}/Dist/Build.pm
%{perl_vendorlib}/Dist/Build
%{_mandir}/man3/Dist::Build*

%changelog
%autochangelog
