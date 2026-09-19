%global source0_hash b24bd709865c513cd92ae27fff86d790d804ad1661c3eb3d489a67c39401c161

Name:           perl-Class-DBI-Loader-Relationship
Version:        1.3
Release:        56%{?dist}
Summary:        Easier relationship specification in CDBI::L
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-Loader-Relationship
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHUNZI/Class-DBI-Loader-Relationship-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:	perl-generators
BuildRequires:	perl(Class::DBI::Loader), perl(Lingua::EN::Inflect::Number)
BuildRequires:	perl(Test::More), perl(ExtUtils::MakeMaker)
Requires:  perl(Class::DBI::Loader), perl(Lingua::EN::Inflect::Number)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-Loader-Relationship-%{version}

# Filter false positive provides.
cat <<EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} \
| grep -v 'perl(Class::DBI::Loader::Generic)'
EOF
%global __perl_provides %{_builddir}/Class-DBI-Loader-Relationship-%{version}/%{name}-prov
chmod +x %{__perl_provides}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/Class/DBI/Loader
%{_mandir}/man3/*.3*

%changelog
%autochangelog
