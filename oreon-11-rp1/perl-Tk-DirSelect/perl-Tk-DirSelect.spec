%global source0_hash 9d1f7a07763f43f740d701cf8d0093e934e8b68c1cc91794a2d6472842b20f95
%bcond_with perl_Tk_DirSelect_enables_optional_test
Name:           perl-Tk-DirSelect
Version:        1.12
Release:        1%{?dist}
Summary:        Cross-platform directory selection widget
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-DirSelect
Source0:        https://cpan.metacpan.org/authors/id/M/MJ/MJCARMAN/Tk-DirSelect-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Tk_DirSelect_enables_optional_test}
%endif
Requires:       perl(:VERSION) >= 5.4
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::BrowseEntry)
BuildRequires:  perl(Tk::Button)
BuildRequires:  perl(Tk::DirTree)
BuildRequires:  perl(Tk::Frame)
BuildRequires:  perl(Tk::Label)
BuildRequires:  perl(Tk::Toplevel)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This module provides a cross-platform directory selection widget. For
systems running Microsoft Windows, this includes selection of local and
mapped network drives. A context menu (right-click or <Button3>) allows the
creation, renaming, and deletion of directories while browsing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-DirSelect-%{version}
sed -i 's/\r//' README Changes
%if !%{with perl_Tk_DirSelect_enables_optional_test}
rm t/pod*
perl -i -ne 'print $_ unless m{^t/pod}' MANIFEST
%endif

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset RELEASE_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
