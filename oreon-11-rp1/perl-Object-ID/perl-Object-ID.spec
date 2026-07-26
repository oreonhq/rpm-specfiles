%global source0_hash 57760d69193a77189739edc34509b7624e09ea28c93b4ca7553df096b7987bd2

Name:		perl-Object-ID
Version:	0.1.2
Release:	35%{?dist}
Summary:	A unique identifier for any object
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Object-ID
Source0:	https://cpan.metacpan.org/modules/by-module/Object/Object-ID-v%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(lib)
BuildRequires:	perl(Module::Build)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Data::UUID) >= 1.148
BuildRequires:	perl(Hash::FieldHash) >= 0.10
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Name) >= 0.03
BuildRequires:	perl(version) >= 0.77
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(DirHandle)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(threads)
# Dependencies
Requires:	perl(Data::UUID) >= 1.148

# Don't provide perl(UNIVERSAL)
%{?perl_default_filter}

%description
This is a unique identifier for any object, regardless of its type, structure
or contents. Its features are:

 * Works on ANY object of any type
 * Does not modify the object in any way
 * Does not change with the object's contents
 * Is O(1) to calculate (i.e. doesn't matter how big the object is)
 * The id is unique for the life of the process
 * The id is always a true value

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Object-ID-v%{version}

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
%{perl_vendorlib}/Object/
%{perl_vendorlib}/UNIVERSAL/
%{_mandir}/man3/Object::ID.3*
%{_mandir}/man3/Object::ID::ConfigData.3*
%{_mandir}/man3/UNIVERSAL::Object::ID.3*

%changelog
%autochangelog
