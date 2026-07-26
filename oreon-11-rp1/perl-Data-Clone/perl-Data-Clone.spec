%global source0_hash b8745954f0eff61efb25589cc13b4f2b1b26ce5ac3617d7e8aa3981626579629

Name:           perl-Data-Clone
Version:        0.006
Release:        9%{?dist}
Summary:        Polymorphic data cloning
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Clone
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFUJI/Data-Clone-%{version}.tar.gz
# build requirements
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::XSUtil) >= 0.03
# runtime requirements
BuildRequires:  perl-devel
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
# test requirements
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires) >= 0.03
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(threads)
Requires:       perl(Exporter)

%{?perl_default_filter}

%description
Data::Clone does data cloning, i.e. copies things recursively. This is
smart so that it works with not only non-blessed references, but also
with blessed references (i.e. objects). When clone() finds an object, it
calls a clone method of the object if the object has a clone, otherwise
it makes a surface copy of the object. That is, this module does
polymorphic data cloning.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Clone-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{_mandir}/man3/*

%changelog
%autochangelog
