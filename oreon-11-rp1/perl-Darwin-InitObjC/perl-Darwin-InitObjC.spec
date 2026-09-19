%global source0_hash 9a5f2887cb2fd427d64937743ffe3e748eab38b5b64906185fc243861e189f91

Name:           perl-Darwin-InitObjC
Version:        0.001
Release:        3%{?dist}
Summary:        Initializes Objective-C runtime
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Darwin-InitObjC
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/Darwin-InitObjC-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny)
# Run-time
BuildRequires:  perl(Config)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(DynaLoader)

%description
Darwin::InitObjC initializes Objective-C runtime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Darwin-InitObjC-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Darwin*
%{_mandir}/man3/Darwin::InitObjC*

%changelog
%autochangelog
