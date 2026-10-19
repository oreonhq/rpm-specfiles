%global source0_hash 7c17a675c6ee76bc7ea12a47377b2df48676fdd9054bbd638f4489f570f99ba8
Name:           perl-Image-Math-Constrain
Version:        1.02
Release:        1%{?dist}
Summary:        Scaling math used in image size constraining (such as thumbnails)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Image-Math-Constrain
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Image-Math-Constrain-%{version}.tar.gz
Patch0:         Image-Math-Constrain-1.02-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
There are a number of different modules and systems that constrain image
sizes, such as thumbnailing. Every one of these independantly implement the
same logic. That is, given a width and/or height constraint, they check to
see if the image is bigger than the constraint, and if so scale the image
down proportionally so that it fits within the constraints.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Image-Math-Constrain-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test AUTOMATED_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
