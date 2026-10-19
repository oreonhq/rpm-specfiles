%global source0_hash 2f8589190a16996f3b695c27de84d09c6702f440469680b292450bdc3eb6321f
Name:           mysqltuner
Version:        2.9.2
Release:        1%{?dist}
Summary:        MySQL configuration assistant
License:        GPL-3.0-or-later
URL:            https://github.com/major/MySQLTuner-perl
Source0:        https://github.com/major/MySQLTuner-perl/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
Requires:       which
Requires:       mysql
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
