%global source0_hash 074f592c10a4541570f7a4b9b1125d30a9575c96b2edb925509d1cc97f196a77

%global srcname xd
%global pypi_name xdfile
%global date 20250519
%global commit 31b2fec79773d62c67db9618ccb6ab1dad82a939
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        1.9.0~%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Python parser for .xd crossword format

License:        MIT
URL:            https://github.com/century-arcade/xd
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  sed

%global _description %{expand:
This package provides a simple parser for .xd -- a corpus-oriented format,
modeled after the simplicity and intuitiveness of the markdown format. It
supports 99.99% of published crosswords, and is intended to be convenient for
bulk analysis of crosswords by both humans and machines, from the present and
into the future.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{commit}

# remove bundled library
rm -r crossword

# remove unnecessary shebangs
sed -i 's:^#!/usr/bin/env python.*$::' xdfile/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# remove sample script
rm %{buildroot}%{_bindir}/sample

%check
# remove broken test
# https://github.com/century-arcade/xd/issues/72
rm xdfile/tests/test_xdfile.py
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md doc/xd-format.md

%changelog
%autochangelog
