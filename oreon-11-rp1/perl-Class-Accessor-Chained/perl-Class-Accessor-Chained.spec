Name:           perl-Class-Accessor-Chained
Version:        0.01
Release:        56%{?dist}
Summary:        Make chained accessors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Accessor-Chained
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Class-Accessor-Chained-%{version}.tar.gz
Patch0:         Class-Accessor-Chained-0.01-pod.patch
# oreon url source checksums begin
%global source0_sha256 a5bf49d3804f83ad25a1b16f327d14d4cbee2270132104b28705031dbccc34d2
%global source0_file Class-Accessor-Chained-0.01.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  /usr/bin/pod2text
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)
Requires:       perl(Class::Accessor)
Requires:       perl(Class::Accessor::Fast)

%description
A chained accessor is one that always returns the object when called with
parameters (to set), and the value of the field when called with no arguments.
This module subclasses Class::Accessor in order to provide the same
mk_accessors interface.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Class-Accessor-Chained-0.01.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a5bf49d3804f83ad25a1b16f327d14d4cbee2270132104b28705031dbccc34d2" || { echo "oreon: Source0 SHA256 mismatch for Class-Accessor-Chained-0.01.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Class-Accessor-Chained-%{version}

# Fix broken POD in README (#914250)
%patch -P0

# Convert POD-formatted README to plain text for %%doc
pod2text README > README.txt

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%doc Changes README.txt
%{perl_vendorlib}/Class/Accessor/
%{_mandir}/man3/Class::Accessor::Chained.3pm*
%{_mandir}/man3/Class::Accessor::Chained::Fast.3pm*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.01-56
- Prepare for Oreon 11 (RP1)
