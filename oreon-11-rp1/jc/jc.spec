%global source0_hash a82bb44e21fd565df8dfa8ea9d498280b38eb1ebc36c149962a6e320bbf5f845

Name: jc
Summary: Serialize the output of CLI tools and file-types to structured JSON
License: MIT

Version: 1.25.6
Release: 2%{?dist}

URL: https://github.com/kellyjonbrazil/%{name}
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(pygments) >= 2.4.2
BuildRequires: python3dist(ruamel-yaml) >= 0.15
BuildRequires: python3dist(xmltodict) >= 0.12

# Require the python module in the main package
Requires: python3-%{name} = %{version}-%{release}

%description
JSON CLI output utility. JC is used to JSONify the output of many
command-line tools and file types for easier parsing in scripts.

%package -n python3-%{name}
Summary: Module for serializing output of CLI tools into JSON
BuildArch: noarch

%description -n python3-%{name}
Python module providing functions for parsing the output of command-line
tools and file types into structured JSON, for easier further processing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%py3_build

%install
%py3_install

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -p man/jc.1 %{buildroot}%{_mandir}/man1/

COMPDIR="%{buildroot}%{_datadir}/bash-completion/completions"
install -m 755 -d "${COMPDIR}"
install -m 644 -p completions/jc_bash_completion.sh "${COMPDIR}/%{name}"

%check
TZ="America/Los_Angeles" ./runtests.sh

%files
%doc README.md EXAMPLES.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/*

%files -n python3-%{name}
%doc docs/
%license LICENSE.md
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
