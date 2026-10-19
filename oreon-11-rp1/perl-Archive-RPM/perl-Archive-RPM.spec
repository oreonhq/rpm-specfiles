%global source0_hash b500253cae838bb41e699d168961737d0f62aa1306291b85fad9d88132496b64
Name:       perl-Archive-RPM
Version:    0.07
Release:        1%{?dist}
Summary:        Work with a RPM
License:    LGPL-2.1-or-later
Url:        https://metacpan.org/release/Archive-RPM
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/Archive-RPM-%{version}.tar.gz
Patch0:     Archive-RPM-0.07-Inject-RPM2-Headers-into-INC-for-Moose-2.1005.patch
Patch1:     Archive-RPM-0.07-Adjust-to-Moose-2.1900.patch
BuildArch:  noarch
Requires:       cpio
Requires:       perl(MooseX::Traits)
Requires:       rpm
Obsoletes:      perl-Archive-RPM-tests < 0.07-9
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  cpio
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(DateTime)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::External)
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::ReadmeMarkdownFromPod)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::AttributeHelpers)
BuildRequires:  perl(MooseX::MarkAsMethods)
BuildRequires:  perl(MooseX::Traits)
BuildRequires:  perl(MooseX::Types::DateTimeX)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(RPM2)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  rpm
BuildRequires:  sed
# /oreon:deps
%description
Archive::RPM provides a more complete method of accessing an RPM's meta-
and actual data. We access this information by leveraging RPM2 where we
can, and by "exploding" the rpm with rpm2cpio and cpio when we need
information we can't get through RPM2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Archive-RPM-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Remove bundled modules
rm -r ./inc
sed -i -e '/^inc\//d' MANIFEST
# Remove useless dependency, CPAN RT#100703
sed -i -e "/^requires 'MooseX::Types::DateTime';\$/d" Makefile.PL
# Disable authors tests
sed -i -e '/^extra_tests;$/d' Makefile.PL

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
