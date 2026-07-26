%global source0_hash 969861622e5fa2021d932d2ccb916a48ccc7c62852b619c899de33b0361ef281

%global srcname h2

%global common_description %{expand:
HTTP/2 Protocol Stack This repository contains a pure-Python
implementation of a HTTP/2 protocol stack. It's written from the ground up to
be embeddable in whatever program you choose to use, ensuring that you can
speak HTTP/2 regardless of your programming paradigm.}

Name:           python-h2
Version:        4.3.0
Release:        %autorelease
Summary:        HTTP/2 State-Machine based protocol implementation

License:        MIT
URL:            https://hyper-h2.readthedocs.io
VCS:            https://github.com/python-hyper/h2
Source0:        %vcs/archive/v%{version}/%{srcname}-%{version}.tar.gz
# downstream only patch
Patch0:         0001-Fedora-tox-adjustments.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots} sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog
