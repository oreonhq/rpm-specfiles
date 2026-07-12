%global source0_hash 19ce431073b49846af22def5e7a12d43ceaa286f6bad33907dc4970621fc3aa9

Name:           perl-String-Tagged-Terminal
Version:        0.08
Release:        1%{?dist}
Summary:        format terminal output using C<String::Tagged>
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/String-Tagged-Terminal
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/String-Tagged-Terminal-0.08.tar.gz

BuildRequires:  perl(Module::Build)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Convert::Color)
BuildRequires:  perl(Convert::Color::XTerm)
BuildRequires:  perl(String::Tagged)
BuildRequires:  perl(Test2::V0)

%{?perl_default_filter}

Provides:       perl(String::Tagged::Terminal)
Provides:       perl(String::Tagged::Terminal::Win32Console)

%description
format terminal output using C<String::Tagged>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n String-Tagged-Terminal-%{version}

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
