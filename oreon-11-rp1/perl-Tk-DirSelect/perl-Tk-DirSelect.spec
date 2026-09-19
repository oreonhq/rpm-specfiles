%global source0_hash 9d1f7a07763f43f740d701cf8d0093e934e8b68c1cc91794a2d6472842b20f95

# Perform optional tests
%bcond_with perl_Tk_DirSelect_enables_optional_test

Name:           perl-Tk-DirSelect
Version:        1.12
Release:        46%{?dist}
Summary:        Cross-platform directory selection widget
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-DirSelect
Source0:        https://cpan.metacpan.org/authors/id/M/MJ/MJCARMAN/Tk-DirSelect-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tk) >= 800
BuildRequires:  perl(Tk::BrowseEntry)
BuildRequires:  perl(Tk::Button)
BuildRequires:  perl(Tk::DirTree)
BuildRequires:  perl(Tk::Frame)
BuildRequires:  perl(Tk::Label)
BuildRequires:  perl(Tk::Toplevel)
BuildRequires:  perl(vars)
# Win32API::File not used
# Tests:
BuildRequires:  perl(Test::More) 
BuildRequires:  perl(warnings)
%if %{with perl_Tk_DirSelect_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
# Test::CheckManifest not used
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
Requires:       perl(:VERSION) >= 5.4

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

#sed -i 's/\r//' README Changes

%check
unset RELEASE_TESTING
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
