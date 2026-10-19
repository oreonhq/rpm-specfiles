%global source0_hash 1570ac33312dae96109567eb07e6846a99d7628752d3f527f502b1d41045c371
Name:           joft
Version:        0.1.1
Release:        1%{?dist}
Summary:        CLI tool for automation of user actions on a JIRA instance
License:        MIT
URL:            https://github.com/mcurlej/joft
Source0:        https://github.com/mcurlej/%{name}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-joft = %{version}-%{release}
# /oreon:deps
%package -n       python3-joft+dev
Summary:        Metapackage for python3-joft dev extras
Requires:       python3-joft = %{version}-%{release}
Requires:       python3dist(tox) >= 4.16.0
Provides:       python3dist(joft[dev]) = %{version}-%{release}

%description -n python3-joft+dev
Metapackage for python3-joft dev extras.

%package -n       python3-joft+lint
Summary:        Metapackage for python3-joft lint extras
Requires:       python3-joft = %{version}-%{release}
Requires:       python3dist(ruff) >= 0.6.2
Provides:       python3dist(joft[lint]) = %{version}-%{release}

%description -n python3-joft+lint
Metapackage for python3-joft lint extras.

%package -n       python3-joft+test
Summary:        Metapackage for python3-joft test extras
Requires:       python3-joft = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.1.1
Provides:       python3dist(joft[test]) = %{version}-%{release}

%description -n python3-joft+test
Metapackage for python3-joft test extras.

%package -n       python3-joft+type
Summary:        Metapackage for python3-joft type extras
Requires:       python3-joft = %{version}-%{release}
Requires:       python3dist(mypy) >= 1.11.1
Requires:       python3dist(types-pyyaml) >= 6.0.12.20240724
Requires:       python3dist(types-tabulate) >= 0.9.0.20240106
Provides:       python3dist(joft[type]) = %{version}-%{release}

%description -n python3-joft+type
Metapackage for python3-joft type extras.

%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir joft-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/joft.config.toml
%oreon_autofiles main

%check

%pytest
%files

%changelog

%autochangelog
