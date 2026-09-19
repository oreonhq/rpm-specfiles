%global source0_hash f917963d1a9aacdf63aebd4de1e16f38f4352cd8e956aab7465ea77be8d6b67b

Name:           perl-XML-RSS-LibXML
Version:        0.3105
Release:        32%{?dist}
Summary:        XML::RSS with XML::LibXML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/XML-RSS-LibXML
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMAKI/XML-RSS-LibXML-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(utf8)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.66
BuildRequires:  perl(XML::LibXML::XPathContext)
# Test Suite
%if 0%{?fedora} > 34 || 0%{?rhel} > 8
BuildRequires:  glibc-gconv-extra
%endif
BuildRequires:  perl(File::Find)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Warn)
# Dependencies
Requires:       perl(constant)

%{?perl_default_filter}

%description
XML::RSS::LibXML uses XML::LibXML (libxml2) for parsing RSS instead of
XML::RSS' XML::Parser (expat), while trying to keep interface compatibility
with XML::RSS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-RSS-LibXML-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/XML*
%{_mandir}/man3/XML*

%changelog
%autochangelog
