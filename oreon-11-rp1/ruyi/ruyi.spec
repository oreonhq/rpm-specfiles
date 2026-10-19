%global source0_hash e5d6498910d7de6399ac36575616adba16d14900d4f190f3eb784b16422401af
Name:           ruyi
Version:        0.44.0
Release:        1%{?dist}
Summary:        RuyiSDK Package Manager
License:        Apache-2.0
URL:            https://github.com/ruyisdk/%{name}
Source0:        https://github.com/%{name}sdk/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        config.toml
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) < 2
Requires:       python3-ruyi = %{version}-%{release}
# /oreon:deps
%description
The package manager for RuyiSDK.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
export RUYI_TELEMETRY_OPTOUT=1
export RUYI_FORCE_ALLOW_ROOT=1
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}/%{python3_sitelib} help2man --version-string=%{version} \
  -o %{buildroot}%{_mandir}/man1/ruyi.1 %{buildroot}%{_bindir}/ruyi
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/config.toml
%oreon_autofiles main

%check

%pytest
%files

%changelog

%autochangelog
