%global source0_hash 81bcd3367c368e03b9813de61e0ba29670e48d7ffb5543accc4b215ae929b788
Name: jc
Summary:        Serialize the output of CLI tools and file-types to structured JSON
License: MIT
Version: 1.25.7
Release:        1%{?dist}
URL: https://github.com/kellyjonbrazil/%{name}
Source0:        https://github.com/kellyjonbrazil/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: python3-%{name} = %{version}-%{release}
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(ruamel-yaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(xmltodict)
# /oreon:deps
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
%oreon_prep
%build

%py3_build
%install
%py3_install
install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -p man/jc.1 %{buildroot}%{_mandir}/man1/
COMPDIR="%{buildroot}%{_datadir}/bash-completion/completions"
install -m 755 -d "${COMPDIR}"
install -m 644 -p completions/jc_bash_completion.sh "${COMPDIR}/%{name}"
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

TZ="America/Los_Angeles" ./runtests.sh
%files -f %{oreon_filedir}/main.list
%files -n python3-jc -f %{oreon_filedir}/python3-jc.list

%changelog

%autochangelog
