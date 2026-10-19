%global source0_hash 1fef216e70bc425ace3e2c4370dfcdddb5e798b099efba2679244a4d5bc1ab0a
Name:           perl-Test-Script-Run
Version:        0.08
Release:        1%{?dist}
Summary:        Test the script with run
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Script-Run
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SUNNAVY/Test-Script-Run-%{version}.tar.gz
Patch0:         Test-Script-Run-0.08-Strip-author-dependencies.patch
BuildArch:      noarch
Suggests:       perl(String::ShellQuote)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module exports some subs to help test and run scripts in your
distribution's bin/ directory, if the script path is not absolute.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Script-Run-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
