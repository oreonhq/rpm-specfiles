%global source0_hash 7b5b82eace9924d5b1c1ef3ef0fee4c15e3af9cfe2cd1ac1c22d7f8ef3d6b905
Name:           perl-STD
Version:        20101111
Release:        1%{?dist}
Summary:        The Standard Perl 6 Grammar
License:        Artistic-2.0
URL:            https://metacpan.org/release/STD
Source0:        https://cpan.metacpan.org/authors/id/S/SO/SOREAR/STD-%{version}.tar.gz
Patch0:         STD-20101111-Remove-usr-bin-env-from-shebang.patch
Patch1:         STD-20101111-Enable-loading-objects-from-YAML-documents.patch
BuildArch:      noarch
Requires:       perl(File::ShareDir) >= 1.02
Provides:       perl(STD) = %{version}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::ShareDir\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(mangle.pl|STD_P5|STD_P6|RE_ast|STD::Cursor\\)$
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n STD-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build

perl Build.PL installdirs=core
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
