%global source0_hash f0374db84731c204b86c1d5b90975fef0d30a86bd9def919343e554e31a9dbbf
%bcond_without perl_HTML_Tree_enable_optional_test
Name:           perl-HTML-Tree
Epoch:          1
Version:        5.07
Release:        30%{?dist}
Summary:        HTML tree handling modules for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Tree
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/HTML-Tree-%{version}.tar.gz
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%if %{with perl_HTML_Tree_enable_optional_test}
%endif
%endif
Requires:       perl(HTML::Parser) >= 3.46
Requires:       perl(HTML::Tagset) >= 3.02
Provides:       perl(HTML::Element)
Provides:       perl(HTML::TreeBuilder)
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevant documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n HTML-Tree-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir="%{buildroot}" create_packlist=0
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.07-30
- Prepare for Oreon 11 (RP1)
