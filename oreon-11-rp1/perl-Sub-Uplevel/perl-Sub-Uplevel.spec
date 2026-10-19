%global source0_hash b4f3f63b80f680a421332d8851ddbe5a8e72fcaa74d5d1d98f3c8cc4a3ece293
Name:           perl-Sub-Uplevel
Summary:        Apparently run a function in a higher stack frame
Epoch:          1
Version:        0.2800
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sub-Uplevel
Source0:        https://cpan.metacpan.org/modules/by-module/Sub/Sub-Uplevel-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
%global __provides_exclude ^perl\\(DB\\)$
Provides:       perl(Sub::Uplevel)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Like Tcl's uplevel() function, but not quite so dangerous. The idea is
just to fool caller(). All the really naughty bits of Tcl's uplevel()
are avoided.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sub-Uplevel-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2800-26
- Prepare for Oreon 11 (RP1)
