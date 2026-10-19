%global source0_hash 9a08b6327a0923ffa2534c6a2e4e4b8900b7b55d0503accea7d5016963c6d480
Name:           perl-Dist-Zilla-Plugin-CopyFilesFromBuild
Version:        0.170880
Release:        1%{?dist}
Summary:        Copy specific files after building for SCM inclusion
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-CopyFilesFromBuild
Source0:        https://cpan.metacpan.org/authors/id/R/RT/RTHOMPSON/Dist-Zilla-Plugin-CopyFilesFromBuild-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Dist::Zilla::Role::AfterBuild)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Dist::Zilla::Plugin::ReadmeAnyFromPod)
BuildRequires:  perl(Dist::Zilla::Role::AfterBuild)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Has::Sugar)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(autodie)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Dist::Zilla plugin will automatically copy the files that you specify in
dist.ini from the build directory into the distribution directory. This is so
you can commit them to version control.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-CopyFilesFromBuild-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
