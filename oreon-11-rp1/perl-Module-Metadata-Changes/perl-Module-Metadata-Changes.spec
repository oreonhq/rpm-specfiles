%global source0_hash 28b407b11acd3d9cbee8afb2074a2ad60bff8a5382dc09778282d2de88164529

Name:           perl-Module-Metadata-Changes
Version:        2.12
Release:        27%{?dist}
Summary:        Manage a module's machine-readable Changes/CHANGES file
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Metadata-Changes
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Module-Metadata-Changes-%{version}.tgz
# Search templates and CSS in the system directories
Patch0:         Module-Metadata-Changes-2.06-Search-assets-in-system-directories.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
BuildRequires:  web-assets-devel
# Run-time:
BuildRequires:  perl(Config::IniFiles) >= 2.88
# DateTime nowhere used
BuildRequires:  perl(DateTime::Format::HTTP) >= 0.42
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.73
BuildRequires:  perl(DateTime::Format::W3CDTF) >= 0.06
BuildRequires:  perl(File::Slurper) >= 0.008
# Getopt::Long not used at tests
# Upstream requires bogus HTML::Entities::Interpolate 1.06 version,
# CPAN RT#109480
BuildRequires:  perl(HTML::Entities::Interpolate) >= 1.05
BuildRequires:  perl(HTML::Template) >= 2.95
BuildRequires:  perl(Moo) >= 2.000002
# Pod::Usage not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny) >= 0.24
BuildRequires:  perl(Types::Standard) >= 1.000005
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1.001002
Requires:       perl(Config::IniFiles) >= 2.88
Requires:       perl(DateTime::Format::HTTP) >= 0.42
Requires:       perl(DateTime::Format::Strptime) >= 1.73
Requires:       perl(DateTime::Format::W3CDTF) >= 0.06
# Upstream requires bogus HTML::Entities::Interpolate 1.06 version,
# CPAN RT#109480
Requires:       perl(HTML::Entities::Interpolate) >= 1.05
Requires:       perl(HTML::Template) >= 2.95
Requires:       perl(File::Slurper) >= 0.008
Requires:       perl(Moo) >= 2.000002
Requires:       perl(Try::Tiny) >= 0.24
Requires:       perl(Types::Standard) >= 1.000005
Requires:       web-assets-filesystem

%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Config::IniFiles|DateTime::Format::W3CDTF|File::Slurper|HTML::Entities::Interpolate|HTML::Template|Moo|Try::Tiny|Types::Standard)\\)$

%description
Module::Metadata::Changes is a pure Perl module. It allows you to convert
old-style Changes/CHANGES files, and to read and write Changelog.ini files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Metadata-Changes-%{version}
%patch -P0 -p1
chmod -x scripts/report.names.pl
sed -i -e '1 s|^#!.*|%(perl -MConfig -e 'print $Config{startperl}')|' \
    bin/ini.report.pl scripts/report.names.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

# Install templates
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/templates/module/metadata/changes
install -m 0644 \
    -t $RPM_BUILD_ROOT%{_datadir}/%{name}/templates/module/metadata/changes \
    htdocs/assets/templates/module/metadata/changes/*

# Install web assets
install -d $RPM_BUILD_ROOT%{_webassetdir}/%{name}/css/module/metadata/changes
install -m 0644 \
    -t $RPM_BUILD_ROOT%{_webassetdir}/%{name}/css/module/metadata/changes \
    htdocs/assets/css/module/metadata/changes/*

%check
make test

%files
%license LICENSE
# The Changelog.ini is an example for ini.report.pl tool
%doc Changelog.ini Changes README scripts
%{_bindir}/*
%{perl_vendorlib}/*
%{_datadir}/%{name}
%{_webassetdir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
