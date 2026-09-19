%global source0_hash 8d607d0bf09ca94600b8e42f0721dbe43ee53a0470182344ac7ace7e58dc6177

# what it's called on pypi
%global srcname txZMQ
# what it's imported as
%global libname txzmq
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{libname}

%global common_description %{expand:
txZMQ allows to integrate easily ZeroMQ sockets into Twisted event loop
(reactor).}

%bcond_without  tests

Name:           python-%{pkgname}
Version:        1.0.0
Release:        18%{?dist}
Summary:        Twisted bindings for ZeroMQ
License:        MPL-2.0
URL:            https://github.com/smira/txZMQ
Source0:        %pypi_source
BuildArch:      noarch

%description %{common_description}

%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
%if %{with tests}
BuildRequires:  %{py3_dist twisted pyzmq}
%endif

%description -n python3-%{pkgname} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p 1
rm -rf %{eggname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH=%{buildroot}%{python3_sitelib} trial-3 txzmq
%endif

%files -n python3-%{pkgname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
