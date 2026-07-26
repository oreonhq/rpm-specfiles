%global source0_hash 9a08b6327a0923ffa2534c6a2e4e4b8900b7b55d0503accea7d5016963c6d480

Name:           perl-Dist-Zilla-Plugin-CopyFilesFromBuild
Version:        0.170880
Release:        27%{?dist}
Summary:        Copy specific files after building for SCM inclusion
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-CopyFilesFromBuild
Source0:        https://cpan.metacpan.org/authors/id/R/RT/RTHOMPSON/Dist-Zilla-Plugin-CopyFilesFromBuild-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Dist::Zilla::Role::AfterBuild)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Has::Sugar)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(utf8)
# Tests:
BuildRequires:  perl(autodie)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Dist::Zilla::Plugin::ReadmeAnyFromPod)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Exception)
# Test::Kwalitee 1.21 not used
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Most)
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
# Test::Vars not used
Requires:       perl(Dist::Zilla::Role::AfterBuild)

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
