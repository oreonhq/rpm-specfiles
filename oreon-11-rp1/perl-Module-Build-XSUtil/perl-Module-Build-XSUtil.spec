%global source0_hash 9063b3c346edeb422807ffe49ffb23038c4f900d4a77b845ce4b53d97bf29400
Summary:        A Module::Build class for building XS modules
Name:		perl-Module-Build-XSUtil
Version:	0.19
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://github.com/hideo55/Module-Build-XSUtil
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Build-XSUtil-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl-devel
Requires:	perl(Devel::CheckCompiler)
Requires:	perl(Devel::PPPort)
Requires:	perl(ExtUtils::CBuilder)
Provides:       perl(Module::Build::XSUtil)
Provides:       perl(Module::Build::XSUtil)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd::Guard)
BuildRequires:  perl(Devel::CheckCompiler)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy::Recursive::Reduced)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Module::Build::XSUtil is a subclass of Module::Build to support building XS
modules. It adds a number of compiler-related optional parameters to
Module::Build's "new" method.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Build-XSUtil-%{version}

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
