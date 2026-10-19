%global source0_hash aa7e6a5340f149ecaa9f2b1059b422937f94387baae96ad4455d527d1071c3d7
%global _docdir_fmt %{name}
Name:           python-iniparse
Version:        0.5.1
Release:        7%{?dist}
Summary:        Accessing and Modifying INI files
License:        MIT AND Python-2.0.1
URL:            https://github.com/candlepin/python-iniparse
Source0:        https://github.com/candlepin/python-iniparse/archive/refs/tags/0.5.1.tar.gz#/python-iniparse-0.5.1.tar.gz
Patch:          https://github.com/candlepin/python-iniparse/pull/38.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-iniparse = %{version}-%{release}
# /oreon:deps
%description
\
iniparse is an INI parser for Python which is API compatible with the standard
library’s ConfigParser, preserves structure of INI files (order of sections &
options, indentation, comments, and blank lines are preserved when data is
updated), and is more convenient to use.

%package -n python3-iniparse
Summary:        Accessing and Modifying INI files
%description -n python3-iniparse
\
iniparse is an INI parser for Python which is API compatible with the standard
library’s ConfigParser, preserves structure of INI files (order of sections &
options, indentation, comments, and blank lines are preserved when data is
updated), and is more convenient to use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
chmod -c -x html/index.html

%build

%pyproject_wheel
%install
%pyproject_install
rm -vfr %{buildroot}%{_docdir}/*
%oreon_autofiles python3-iniparse usr/lib/python3*/site-packages/iniparse* usr/lib64/python3*/site-packages/iniparse* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/iniparse* usr/lib64/python3*/site-packages/iniparse* usr/bin/*

%check

%{py3_test_envvars} %{python3} ./runtests.py
%files
%files -n python3-iniparse -f %{oreon_filedir}/python3-iniparse.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.1-7
- Prepare for Oreon 11 (RP1)
