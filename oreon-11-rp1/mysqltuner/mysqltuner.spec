%global source0_hash dcd789c25f450ab128c050525705396f183a57b117eabdba470653f2ab9dd53e

# https://fedoraproject.org/wiki/Packaging:SourceURL#Github
#%global commit 1333ea9395a381b38535bc1fa05733a32b21f138
#%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mysqltuner
Version:        2.7.0
Release:        2%{?dist}
Summary:        MySQL configuration assistant

License:        GPL-3.0-or-later
URL:            https://github.com/major/MySQLTuner-perl
Source0:        https://github.com/major/MySQLTuner-perl/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       which

# RHBZ 1838780 - mariadb lacks mysql provides on el8
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       (mysql or mariadb)
%else
Requires:       mysql
%endif

%description
MySQLTuner is a script written in Perl that will assist you with your
MySQL configuration and make recommendations for increased performance
and stability.  Within seconds, it will display statistics about your
MySQL installation and the areas where it can be improved.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MySQLTuner-perl-%{version}

%build

%install
install -Dpm 755 mysqltuner.pl $RPM_BUILD_ROOT%{_bindir}/mysqltuner
install -Dpm 644 basic_passwords.txt $RPM_BUILD_ROOT%{_datadir}/mysqltuner/basic_passwords.txt
install -Dpm 644 vulnerabilities.csv $RPM_BUILD_ROOT%{_datadir}/mysqltuner/vulnerabilities.csv

%files
%doc LICENSE README.md mysql_support.md mariadb_support.md
%{_bindir}/mysqltuner
%{_datadir}/mysqltuner/basic_passwords.txt
%{_datadir}/mysqltuner/vulnerabilities.csv

%changelog
%autochangelog
