%global source0_hash f119058d685bb9f93ed8928be80804d4357d699d6b40f4d2209a0d61981647be
Name:           perl-WWW-Babelfish
Version:        0.16
Release:        1%{?dist}
Summary:        Perl extension for translation via Babelfish or Google
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Babelfish
Source0:        https://cpan.metacpan.org/authors/id/D/DU/DURIST/WWW-Babelfish-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Perl interface to the WWW babelfish translation server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Babelfish-%{version}

%build

echo n | %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
