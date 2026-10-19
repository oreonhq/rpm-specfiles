%global source0_hash 45e3ca21c3ce3c339646100de18db8a26a27d240c29f1c9e07b6c13995a969be
%global pypi_name speedtest-cli
Name:		python-%{pypi_name}
Version:	2.1.3
Release:        20%{?dist}
Summary:        Command-line interface for testing internet bandwidth using speedtest.net
License:	Apache-2.0
URL:		https://github.com/sivel/speedtest-cli
Source0:        https://github.com/sivel/%{pypi_name}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  help2man
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{summary}.

%package -n python3-%{pypi_name}
Summary:        Command-line interface for testing internet bandwidth using speedtest.net
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build

%py3_build
%install
%{__mkdir} -p %{buildroot}%{_mandir}/man1
%py3_install
export PYTHONPATH="%{buildroot}%{python3_sitelib}"
for f in $(%{_bindir}/find %{buildroot}%{_bindir} -type f -name '*' | /bin/sort )
do
	of="$(/bin/basename ${f}).1"
	%{_bindir}/help2man -s 1 -N -o %{buildroot}%{_mandir}/man1/${of} ${f}
done
unset PYTHONPATH
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-speedtest-cli -f %{oreon_filedir}/python3-speedtest-cli.list

%changelog

%autochangelog
