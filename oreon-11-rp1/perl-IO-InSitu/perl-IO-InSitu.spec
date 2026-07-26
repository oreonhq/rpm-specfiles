%global source0_hash c2b78d2167e49061f2e8662d2e7398235edbbb19ce7f707cf5c8ca29e18830f4

Name:		perl-IO-InSitu
Version:	0.0.2
Release:	46%{?dist}
Summary:	Avoid clobbering files opened for both input and output
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/IO-InSitu
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/IO-InSitu-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	perl-generators
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(version)
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::File)

# Filter from provides
%filter_from_provides /perl(IO::File::SE)/d
%filter_setup

%description
This module provides a function called open_rw(), that is passed two
file names and returns two handles, one open for reading and the other
for writing. It's like doing two separate open() calls, except that it
detects cases where the input and output file are the same, and avoids
clobbering the input file when reopening it for output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-InSitu-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}

./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::InSitu.3pm*

%changelog
%autochangelog
