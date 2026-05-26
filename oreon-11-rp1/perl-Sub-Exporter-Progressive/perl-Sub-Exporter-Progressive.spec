Name:		perl-Sub-Exporter-Progressive
Version:	0.001013
Release:	28%{?dist}
Summary:	Only use Sub::Exporter if you need it
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Sub-Exporter-Progressive
Source0:	https://cpan.metacpan.org/authors/id/F/FR/FREW/Sub-Exporter-Progressive-0.001013.tar.gz
# oreon url source checksums begin
%global source0_sha256 d535b7954d64da1ac1305b1fadf98202769e3599376854b2ced90c382beac056
%global source0_file Sub-Exporter-Progressive-0.001013.tar.gz
# oreon url source checksums end

BuildArch:	noarch
# =============== Module Build ======================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# =============== Module Runtime ====================
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter) >= 5.58
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(warnings)
# =============== Test Suite ========================
BuildRequires:	perl(constant)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.88
# =============== Module Dependencies ===============
Requires:	perl(Carp)
Requires:	perl(Exporter) >= 5.58
Requires:	perl(Sub::Exporter)

%description
Sub::Exporter is an incredibly powerful module, but with that power comes
great responsibility, er- as well as some runtime penalties. This module is a
Sub::Exporter wrapper that will let your users just use Exporter if all they
are doing is picking exports, but use Sub::Exporter if your users try to use
Sub::Exporter's more advanced features, like renaming exports, if they try to
use them.

Note that this module will export @EXPORT and @EXPORT_OK package variables for
Exporter to work. Additionally, if your package uses advanced Sub::Exporter
features like currying, this module will only ever use Sub::Exporter, so you
might as well use it directly.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Sub-Exporter-Progressive-0.001013.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d535b7954d64da1ac1305b1fadf98202769e3599376854b2ced90c382beac056" || { echo "oreon: Source0 SHA256 mismatch for Sub-Exporter-Progressive-0.001013.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Sub-Exporter-Progressive-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Sub/
%{_mandir}/man3/Sub::Exporter::Progressive.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.001013-28
- Prepare for Oreon 11 (RP1)
