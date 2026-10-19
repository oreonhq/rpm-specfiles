%global source0_hash 12c4989a03e24386e50ec28aecafb9830980d678e274b583cb5869850cd418c9
Name:           perl-OpenFrame
Version:        3.05
Release:        1%{?dist}
Summary:        Framework for network enabled applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/OpenFrame
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/OpenFrame-%{version}.tar.gz
Source1:        README.LICENSE
Patch0:         %{name}-3.05-Adapt-CGI-Cookie-construction-to-CGI-3.51.patch
BuildArch:      noarch
Requires:       perl(CGI::Cookie) >= 0.01
Requires:       perl(File::Temp) >= 0.01
Requires:       perl(File::Type) >= 0.01
Requires:       perl(IO::Null) >= 0.01
Requires:       perl(Pipeline) >= 2.00
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CGI::Cookie\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Temp\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Type\\)$
%global __requires_exclude %__requires_exclude|^perl\\(IO::Null\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Pipeline\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Cookie)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Type)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Null)
BuildRequires:  perl(Pipeline)
BuildRequires:  perl(Pipeline::Production)
BuildRequires:  perl(Pipeline::Segment)
BuildRequires:  perl(Pipeline::Segment::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
OpenFrame is a framework for network services serving to multiple media
channels - for instance, the web, WAP, and digital television. It is built
around the Pipeline API, and provides extra abstraction to make delivery of
a single application to multiple channels easier.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n OpenFrame-%{version}
%patch -P0 -p1 -b .cgi3.51
cp -p %{SOURCE1} .

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
rm -f %{buildroot}%{perl_vendorlib}/saofs.pl
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
