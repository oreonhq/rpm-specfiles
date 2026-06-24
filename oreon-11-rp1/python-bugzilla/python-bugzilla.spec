%global source0_hash none

Name:           python-bugzilla
Version:        3.3.0
Release:        8%{?dist}
Summary:        Python library for interacting with Bugzilla

License:        GPL-2.0-or-later
URL:            https://github.com/python-bugzilla/python-bugzilla
Source0:        https://github.com/python-bugzilla/python-bugzilla/archive/v%{version}/%{name}-%{version}.tar.gz

Patch: 0001-Loosen-test-requirements-for-Fedora.patch
BuildArch:      noarch

BuildRequires: python3-devel
# tests need to be able to set en_US.UTF-8 locale
BuildRequires: glibc-langpack-en

%global _description\
python-bugzilla is a python library for interacting with bugzilla instances\
over XMLRPC or REST.\

%description %_description


%package -n python3-bugzilla
Summary: %summary
Requires: python3-requests
%{?python_provide:%python_provide python3-bugzilla}

Obsoletes:      python-bugzilla < %{version}-%{release}
Obsoletes:      python2-bugzilla < %{version}-%{release}

%description -n python3-bugzilla %_description


%package cli
Summary: Command line tool for interacting with Bugzilla
Requires: python3-bugzilla = %{version}-%{release}

%description cli
This package includes the 'bugzilla' command-line tool for interacting with bugzilla. Uses the python-bugzilla API



%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1



%generate_buildrequires
%pyproject_buildrequires -t



%build
%pyproject_wheel



%install
%pyproject_install
%pyproject_save_files bugzilla


%check
%tox



%files -n python3-bugzilla -f %{pyproject_files}
%doc README.md NEWS.md


%files cli
%{_bindir}/bugzilla
%{_mandir}/man1/bugzilla.1.gz


%changelog
%autochangelog

