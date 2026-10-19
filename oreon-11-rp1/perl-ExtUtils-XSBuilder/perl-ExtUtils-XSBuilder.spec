%global source0_hash 8cced386e3d544c5ec2deb3aed055b72ebcfc2ea9a6c807da87c4245272fe80a
Name:           perl-ExtUtils-XSBuilder
Version:        0.28
Release:        1%{?dist}
Summary:        Modules that parse C header files and create XS glue code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-XSBuilder
Source0:        https://cpan.metacpan.org/modules/by-module/ExtUtils/ExtUtils-XSBuilder-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Find)
Requires:       perl(Tie::IxHash)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
ExtUtils::XSBuilder is a set of modules to parse C header files and create 
XS glue code and documentation out of it. Ideally this allows one to "write" 
an interface to a C library without coding a line. Since no C-API is ideal,
some adjustments are necessary most of the time. So to use this module you
must still be familiar with C and XS programming, but it removes a lot of
stupid work and copy&paste from you. Also when the C API changes, most
of the time you only have to rerun XSBuilder to get your new Perl API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-XSBuilder-%{version}
find . -type f | xargs chmod -c -x

%build

perl Makefile.PL INSTALLDIRS=vendor
make
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
