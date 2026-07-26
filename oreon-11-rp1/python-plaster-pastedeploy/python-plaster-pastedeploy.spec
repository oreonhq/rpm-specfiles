%global source0_hash 1551fa006cbad48f8d57259acd3b5eab714664533760be3bf1fae856dc7357e9

%global srcname plaster-pastedeploy
%global sum A PasteDeploy binding to the plaster configuration loader
%global desc \
plaster_pastedeploy is a plaster plugin that provides a \
plaster.Loader that can parse ini files according to the standard set \
by PasteDeploy. It supports the wsgi plaster protocol, implementing \
the plaster.protocols.IWSGIProtocol interface.

Name: python-%{srcname}
Version: 1.0.1
Release: %autorelease
BuildArch: noarch

License: MIT
Summary: %{sum}
URL:     https://github.com/Pylons/plaster_pastedeploy
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: python3-devel

%description %{desc}

%package -n python3-%{srcname}
Summary: %{sum}

%description -n python3-%{srcname} %{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n plaster_pastedeploy-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l plaster_pastedeploy

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGES.rst
%doc README.rst

%changelog
%autochangelog
