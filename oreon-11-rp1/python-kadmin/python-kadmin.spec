%global source0_hash a60ee735647b28dc7ca7382f820b486d755a38fcbc889739a70dc9743a42a583

%global modname kadmin
%global commit          94e50ed0a788d9ff9e4b47a35a65ca22c69b703a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20181207

Name:               python-kadmin
Version:            0.1.2
Release:            29.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:            Python module for kerberos admin (kadm5)

License:            MIT
URL:                https://github.com/rjancewicz/python-%{modname}
Source0:            %{url}/archive/%{commit}/python-%{modname}-%{shortcommit}.tar.gz
Patch0:             https://patch-diff.githubusercontent.com/raw/rjancewicz/python-kadmin/pull/59.patch#/0001-build-one-package-with-two-extensions.patch
Patch1:             12de82aa48a7faeb5bfc618a226f2cc388e2eb4d.patch
Patch2:             python-kadmin-c99.patch
Patch3:             pointer_types.patch
%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-pip
BuildRequires:      krb5-devel
BuildRequires:      bison
BuildRequires:      gcc

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n python-%{modname}-%{commit}

%build
export CFLAGS="$CFLAGS -fcommon -std=gnu17"
%pyproject_wheel

%install
%pyproject_install

%files -n python%{python3_pkgversion}-%{modname}
%doc README.md
%license LICENSE.txt
%{python3_sitearch}/%{modname}*.so
%{python3_sitearch}/python_%{modname}*.dist-info

%changelog
%autochangelog
