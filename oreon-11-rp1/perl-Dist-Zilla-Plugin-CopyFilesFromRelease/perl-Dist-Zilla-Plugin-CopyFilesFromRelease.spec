%global source0_hash 8c6d305f4901df955f79e22891f0d4870d25a96a060e19526b774312e813e52e
%bcond_without perl_Dist_Zilla_Plugin_CopyFilesFromRelease_enables_optional_test
Name:           perl-Dist-Zilla-Plugin-CopyFilesFromRelease
Version:        0.007
Release:        25%{?dist}
Summary:        Copy files from a release for SCM inclusion
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-CopyFilesFromRelease
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-CopyFilesFromRelease-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Dist_Zilla_Plugin_CopyFilesFromRelease_enables_optional_test}
%endif
Requires:       perl(Dist::Zilla::Role::AfterRelease)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Dist::Zilla::Role::AfterRelease)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Conflicts)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(if)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
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

%setup -q -n Dist-Zilla-Plugin-CopyFilesFromRelease-%{version}

%build

export PERL_MM_FALLBACK_SILENCE_WARNING=1
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
