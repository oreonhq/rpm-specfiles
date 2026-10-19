%global source0_hash 70e22f4fd29b204f75f989e3c1e847aa1de267a028aab4233c0db783aaff78c1
%global srcname sortedcontainers
%bcond_with tests
%bcond_with docs
Name:           python-%{srcname}
Version:        2.4.0
Release:        28%{?dist}
Summary:        Pure Python sorted container types
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/grantjenks/python-sortedcontainers/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sortedcontainers = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Pure Python sorted container types
BuildRequires:  make
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)
%endif
%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  dvipng
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(bm.sty)
%endif
%description -n python3-%{srcname}

%package -n python-%{srcname}-doc
Summary:        Pure Python sorted container types
%description -n python-%{srcname}-doc
Documentation for %{srcname} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%if %{with docs}
pushd docs
make html
rm _build/html/.buildinfo
popd
%endif
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/sortedcontainers* usr/lib64/python3*/site-packages/sortedcontainers* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

pushd tests
%{pytest}
popd
%endif
%files
%files -n python3-sortedcontainers -f %{oreon_filedir}/python3-sortedcontainers.list
%files -n python-sortedcontainers-doc -f %{oreon_filedir}/python-sortedcontainers-doc.list

%changelog

%autochangelog
