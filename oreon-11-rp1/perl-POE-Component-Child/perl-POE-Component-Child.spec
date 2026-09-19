%global source0_hash cc721cacec1e2779f0fdeb727237fdadec5eb5a28975ccb98dddffae2e766d5d

Name:           perl-POE-Component-Child
Version:        1.39
Release:        52%{?dist}
Summary:        Child management component for POE
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/POE-Component-Child
Source0: https://cpan.metacpan.org/authors/id/E/EC/ECALDER/POE-Component-Child-%{version}.tar.gz
Patch0:         POE-Component-Child-rt70701.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Driver::SysRW)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Wheel::Run)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
This POE component serves as a wrapper for POE::Wheel::Run, obviating
the need to create a session to receive the events it dishes out.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Child-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
chmod -R u+w %{buildroot}/*

%check
make test

%files
%doc LICENSE Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
