%global source0_hash 45e3ca21c3ce3c339646100de18db8a26a27d240c29f1c9e07b6c13995a969be

%global pypi_name speedtest-cli

Name:		python-%{pypi_name}
Version:	2.1.3
Release:	20%{?dist}
Summary:	Command-line interface for testing internet bandwidth using speedtest.net

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		https://github.com/sivel/speedtest-cli
Source0:	https://github.com/sivel/speedtest-cli/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	help2man

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary:	%{summary}

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

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/speedtest*
%{_mandir}/man1/speedtest*.1*
%{python3_sitelib}/speedtest*.py
%{python3_sitelib}/speedtest_cli-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/__pycache__/speedtest*.cpython-%{python3_version_nodots}*.pyc

%changelog
%autochangelog
