%global source0_hash 8be1bf15af010488a332a6590bd48bcea639388b19c2d25764ef0fdc627ba11b
%bcond tests 0
Name:           python-poetry-dynamic-versioning
Version:        1.10.0
Release:        1%{?dist}
Summary:        Plugin for Poetry to enable dynamic versioning based on VCS tags
License:        MIT
URL:            https://github.com/mtkennerly/poetry-dynamic-versioning
Source0:        https://github.com/mtkennerly/poetry-dynamic-versioning/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-poetry-dynamic-versioning = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-poetry-dynamic-versioning
Summary:        Plugin for Poetry to enable dynamic versioning based on VCS tags
BuildRequires:  python3-devel
BuildRequires:  help2man
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/hg
BuildRequires:  /usr/bin/darcs
BuildRequires:  /usr/bin/svn
BuildRequires:  /usr/bin/bzr
BuildRequires:  /usr/bin/fossil
BuildRequires:  /usr/bin/poetry
%endif
%description -n python3-poetry-dynamic-versioning

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir poetry-dynamic-versioning-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -t %{buildroot}%{_mandir}/man1 -D -p -m 0644 \
    docs/poetry-dynamic-versioning.1
%oreon_autofiles python3-poetry-dynamic-versioning usr/lib/python3*/site-packages/poetry_dynamic_versioning* usr/lib64/python3*/site-packages/poetry_dynamic_versioning* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/poetry_dynamic_versioning* usr/lib64/python3*/site-packages/poetry_dynamic_versioning* usr/bin/*

%check

%if %{with tests}
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
brz whoami "Your Name <name@example.com>"
export DARCS_EMAIL="Yep something <name@example.com>"
%{pytest}
%endif
%files
%files -n python3-poetry-dynamic-versioning -f %{oreon_filedir}/python3-poetry-dynamic-versioning.list

%changelog

%autochangelog
