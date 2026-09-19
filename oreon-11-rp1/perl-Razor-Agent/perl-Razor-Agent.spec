%global source0_hash 5e062e02ebb65e24b708e7eefa5300c43d6f657bf20d08fec4ca8a0a3b94845f

# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname Razor2-Client-Agent

Summary:        Collaborative, content-based spam filtering network agent
Name:           perl-Razor-Agent
Version:        2.86
Release:        16%{?dist}
License:        Artistic-2.0
URL:            https://metacpan.org/release/%{pkgname}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{pkgname}-%{version}.tar.gz
Patch0:         https://github.com/toddr/Razor2-Client-Agent/commit/033b00e94741550ef3ef087d9903742ac881a7ba.patch#/perl-Razor-Agent-2.86-parallel-make.patch
Patch1:         https://github.com/toddr/Razor2-Client-Agent/commit/1a8dc0ea64c6bbe187babdb1079bc0cf05926e59.patch#/perl-Razor-Agent-2.86-digest-sha.patch
Requires:       perl(Digest::SHA)
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Config)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(vars)
Provides:       perl-%{pkgname} = %{version}-%{release}
Provides:       perl-%{pkgname}%{?_isa} = %{version}-%{release}

%description
Vipul's Razor is a distributed, collaborative, spam detection and
filtering network. Razor establishes a distributed and constantly
updating catalogue of spam in propagation. This catalogue is used
by clients to filter out known spam. On receiving a spam, a Razor
Reporting Agent (run by an end-user or a troll box) calculates
and submits a 20-character unique identification of the spam (a
SHA Digest) to its closest Razor Catalogue Server. The Catalogue
Server echos this signature to other trusted servers after storing
it in its database. Prior to manual processing or transport-level
reception, Razor Filtering Agents (end-users and MTAs) check their
incoming mail against a Catalogue Server and filter out or deny
transport in case of a signature match. Catalogued spam, once
identified and reported by a Reporting Agent, can be blocked out
by the rest of the Filtering Agents on the network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc BUGS Changes CREDITS FAQ README.md SERVICE_POLICY
%{_bindir}/razor-admin
%{_bindir}/razor-check
%{_bindir}/razor-client
%{_bindir}/razor-report
%{_bindir}/razor-revoke
%{perl_vendorarch}/Razor2/
%{perl_vendorarch}/auto/Razor2/
%{_mandir}/man1/razor-admin.1*
%{_mandir}/man1/razor-check.1*
%{_mandir}/man1/razor-report.1*
%{_mandir}/man1/razor-revoke.1*
%{_mandir}/man3/Razor2::Errorhandler.3pm*
%{_mandir}/man3/Razor2::Preproc::deHTMLxs.3pm*
%{_mandir}/man3/Razor2::Syslog.3pm*
%{_mandir}/man5/razor-agent.conf.5*
%{_mandir}/man5/razor-agents.5*
%{_mandir}/man5/razor-whitelist.5*

%changelog
%autochangelog
