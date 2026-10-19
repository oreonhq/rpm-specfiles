%global source0_hash df51d8005655bce42efdc5f8996e3323b015bed2da7241c54cf61aefdb009510
%global use_x11_tests 1
Name:           perl-Wx-Perl-DataWalker
Version:        0.02
Release:        1%{?dist}
Summary:        Implement subclass that shows relatively simple structure
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Wx-Perl-DataWalker
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Wx-Perl-DataWalker-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  font(:lang=en)
BuildRequires:  make
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Devel::Size)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Wx)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl-generators
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
# /oreon:deps
%description
Wx::Perl::DataWalker implements a Wx::Frame subclass that shows a
relatively simple Perl data structure browser. After opening such a frame
and supplying it with a reference to an essentially arbitrary data
structure, you can visually browse it by double-clicking references.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Wx-Perl-DataWalker-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

    xvfb-run -a make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
