%global source0_hash 0d8f760e455990f51d5b2f4b57e1b1461cf29c46a9e030898b59a5a5cd54d3d7
%bcond_without perl_CGI_FormBuilder_enables_optional_test
Name:           perl-CGI-FormBuilder
%global         cpanversion 3.20
Version:        %{cpanversion}00
Release:        1%{?dist}
Summary:        Easily generate and process stateful forms
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-FormBuilder
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/CGI-FormBuilder-%{cpanversion}.tar.gz
BuildArch:      noarch
%if %{with perl_CGI_FormBuilder_enables_optional_test}
%endif
Requires:       perl(CGI::FastTemplate) >= 1.09
Requires:       perl(Data::Dumper)
Requires:       perl(HTML::Template) >= 2.06
Requires:       perl(Template) >= 2.08
Requires:       perl(Text::Template) >= 1.43
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((CGI::SSI|HTML::Template|Template|Text::Template)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Cookie)
BuildRequires:  perl(CGI::Session)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The goal of CGI::FormBuilder (FormBuilder) is to provide an easy way for you
to generate and process entire CGI form-based applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-FormBuilder-%{cpanversion}
# Fix permissions
chmod 0644 lib/CGI/FormBuilder/Messages/*
perl -i -ne 'print $_ unless m{\At/2d-template-fast\.t\b}' MANIFEST

%build

unset STRICT_FB_TESTS
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
