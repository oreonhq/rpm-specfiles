%global source0_hash 7c17a675c6ee76bc7ea12a47377b2df48676fdd9054bbd638f4489f570f99ba8

Name:           perl-Image-Math-Constrain
Version:        1.02
Release:        49%{?dist}
Summary:        Scaling math used in image size constraining (such as thumbnails)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Image-Math-Constrain
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Image-Math-Constrain-%{version}.tar.gz
Patch0:         Image-Math-Constrain-1.02-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(overload)
# Tests only
BuildRequires:  perl(Pod::Simple) >= 3.07
BuildRequires:  perl(Test::CPAN::Meta) >= 0.12
BuildRequires:  perl(Test::MinimumVersion) >= 0.008
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Pod) >= 1.26

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

%check
make test AUTOMATED_TESTING=1

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
