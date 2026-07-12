%global source0_hash 57686f10843be81affad185ae4131790ba0c4af36d2104d6fb69126528055267

Name:		perl-File-TreeCreate
Version:	0.0.1
Release:	13%{?dist}
Summary:	Recursively create a directory tree
License:	MIT
URL:		https://metacpan.org/release/File-TreeCreate
Source0:	https://cpan.metacpan.org/modules/by-module/File/File-TreeCreate-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build) >= 0.28
# Module Runtime
BuildRequires:	perl(autodie)
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
# (none)

Provides:       perl(File::TreeCreate)
%description
Recursively create a directory tree.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n File-TreeCreate-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/File/
%{_mandir}/man3/File::TreeCreate.3*

%changelog
%autochangelog
