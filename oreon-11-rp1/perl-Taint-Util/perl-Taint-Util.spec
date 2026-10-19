%global source0_hash 78047c65237ee4ca2451bd8b44936db09a34a3925003eccf4255bcd7fdd9768c
Name:		perl-Taint-Util
Version:	0.08
Release:        1%{?dist}
Summary:        Test for and flip the taint flag without regex matches or eval
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Taint-Util
Source0:        https://cpan.metacpan.org/modules/by-module/Taint/Taint-Util-%{version}.tar.gz
Patch0:		Taint-Util-0.08-utf8.patch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Wraps perl's internal routines for checking and setting the taint flag and
thus does not rely on regular expressions for untainting or odd tricks
involving eval and kill for checking whether data is tainted; instead, it
checks and flips a flag on the scalar in-place.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Taint-Util-%{version}

# Re-code README as UTF-8
%patch -P 0

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
