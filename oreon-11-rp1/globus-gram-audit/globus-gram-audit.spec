%global source0_hash f0b9814c749a430347c309714693bd95ab26f5857b19958e452866c8b40ae9c9

Name:		globus-gram-audit
%global _name %(tr - _ <<< %{name})
Version:	5.1
Release:	11%{?dist}
Summary:	Grid Community Toolkit - GRAM Jobmanager Auditing

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
BuildArch:	noarch

BuildRequires:	make
BuildRequires:	perl-generators

Requires:	crontabs
Requires:	perl(DBD::SQLite)

Requires(post):	perl(DBD::SQLite)
Requires(post):	perl(Globus::Core::Paths)

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GRAM Jobmanager Auditing

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

%make_build

%install
%make_install

# Rename cron script
mv %{buildroot}%{_sysconfdir}/cron.hourly/globus-gram-audit.cron \
   %{buildroot}%{_sysconfdir}/cron.hourly/globus-gram-audit

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%post
if [ $1 -eq 1 ]; then
    globus-gram-audit --query 'select 1 from gram_audit_table' 2> /dev/null || \
    globus-gram-audit --create --quiet || :
fi

%files
%{_sbindir}/globus-gram-audit
%dir %{_datadir}/globus
%dir %{_datadir}/globus/gram-audit
%{_datadir}/globus/gram-audit/*.sql
%dir %{_localstatedir}/lib/globus
%dir %{_localstatedir}/lib/globus/gram-audit
%config(noreplace) %{_sysconfdir}/cron.hourly/globus-gram-audit
%dir %{_sysconfdir}/globus
%config(noreplace) %{_sysconfdir}/globus/gram-audit.conf
%doc %{_mandir}/man8/globus-gram-audit.8*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%changelog
%autochangelog
