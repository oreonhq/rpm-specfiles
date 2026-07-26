%global source0_hash 66f55a98a08502ec5f4dd1627a2f7806e87b6a5df516466ccd9c5195a0c41fe2

Name:		perl-Time-y2038
Version:	20100403
Release:	41%{?dist}
Summary:	Versions of Perl's time functions which work beyond 2038
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Time-y2038
Source0:	https://cpan.metacpan.org/modules/by-module/Time/Time-y2038-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::CBuilder) >= 0.24
BuildRequires:	perl(JSON) >= 2.17
BuildRequires:	perl(lib)
BuildRequires:	perl(Module::Build) >= 0.36
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(Test::Exception) >= 0.27
BuildRequires:	perl(Test::More) >= 0.82
BuildRequires:	perl(Test::Warn) >= 0.11
# Dependencies
# (none)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
On many computers, Perl's time functions will not work past the year 2038.
This is a design fault in the underlying C libraries Perl uses. Time::y2038
provides replacements for those functions, which will work accurately
+/1 142 million years.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Time-y2038-%{version}

%build
perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes
%{perl_vendorarch}/auto/Time/
%{perl_vendorarch}/Time/
%{_mandir}/man3/Time::y2038.3*
%{_mandir}/man3/Time::y2038::Everywhere.3*

%changelog
%autochangelog
