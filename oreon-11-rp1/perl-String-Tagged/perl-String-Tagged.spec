%global source0_hash a3d9ba61af5a419fa4ca40cd084a62642b4ef6533cc42a209f8f7f63e21d74a9

Name:           perl-String-Tagged
Version:        0.24
Release:        1%{?dist}
Summary:        string buffers with value tags on extents
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/String-Tagged
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/String-Tagged-0.24.tar.gz

BuildRequires:  perl(Module::Build)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Test2::V0)

%{?perl_default_filter}

Provides:       perl(String::Tagged)
Provides:       perl(String::Tagged::Extent)

%description
string buffers with value tags on extents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n String-Tagged-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README*
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
