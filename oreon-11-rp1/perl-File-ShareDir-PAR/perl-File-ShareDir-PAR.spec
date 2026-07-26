%global source0_hash 8e35ea0744be4548467e13867eb085d01cc9641fed21f1b118bf86c731447ab4

Name:           perl-File-ShareDir-PAR
Version:        0.06
Release:        45%{?dist}
Summary:        File::ShareDir with PAR support
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-ShareDir-PAR
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/File-ShareDir-PAR-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Inspector) >= 1.12
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir) >= 1.02
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(PAR) >= 0.989
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test
BuildRequires:  perl(Cwd)
BuildRequires:  perl(PAR::Dist)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(File::ShareDir) >= 1.02
Requires:       perl(PAR) >= 0.989

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}perl\\(File::ShareDir\\)$

%description
File::ShareDir::PAR provides the same functionality as File::ShareDir but
tries hard to be compatible with PAR packaged applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-ShareDir-PAR-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
rm -rf $RPM_BUILD_ROOT/%{perl_vendorlib}/auto/share/dist/File-ShareDir-PAR
rm -rf $RPM_BUILD_ROOT/%{perl_vendorlib}/auto/share/module/File-ShareDir-PAR/test_file.txt
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/File/ShareDir
%{perl_vendorlib}/auto/share/*/File-ShareDir-PAR
%{_mandir}/man3/*

%changelog
%autochangelog
