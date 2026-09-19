%global source0_hash 958d54e5d711565ffbf48133fe5d0a378480950b3d76320afd5378ed37cf7611

%global srcname journal-brief
%global sum Find new systemd journal entries since last run

Name:		python-%{srcname}
Version:	1.1.8
Release:	19%{?dist}
Summary:	%{sum}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://pypi.python.org/pypi/%{srcname}
Source0:	https://pypi.python.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch
# en_US.UTF-8 locale required for tests
BuildRequires:	glibc-langpack-en
BuildRequires:	python3-devel
%if 0%{?with_check}
BuildRequires:	python3-pytest python3-flexmock
%endif # with_check

%description
Python module for examining, bookmarking, and filtering systemd
journal entries.

%package -n %{srcname}
Summary:	Show interesting new systemd journal entries since last run
Requires:	python3-%{srcname} = %{version}-%{release}
Requires:	python3-setuptools

%description -n %{srcname}
Run this from cron to get a daily or hourly briefing of interesting
new systemd journal entries.

%package -n python3-%{srcname}
Summary:	%{sum}
Requires:	systemd-python3
Requires:	python3-PyYAML
Recommends:	%{srcname} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python module for examining, bookmarking, and filtering systemd
journal entries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%if 0%{?with_check}
%check
%{__python3} %{py_setup} test
%endif # with_check

%files -n %{srcname}
%{_bindir}/%{srcname}

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
%autochangelog
