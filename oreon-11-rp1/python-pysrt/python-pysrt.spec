%global source0_hash d23963953579d48004e99c3a1e05e812c2b352116d0efe2329bc416a25780de6
Name: python-pysrt
Version: 1.1.2
Release:        27%{?dist}
Summary:        Library used to edit or create SubRip files
License: GPL-3.0-only
URL: https://github.com/byroot/pysrt
Source0:        https://github.com/byroot/pysrt/archive/v%{version}/pysrt-%{version}.tar.gz
Patch0: %{name}-1.1.2-use_assertEqual.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pysrt = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pysrt
Summary:        Library used to edit or create SubRip files
%description -n python3-pysrt

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pysrt-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
for lib in `find %{buildroot}%{python3_sitelib} -name "*.py"`; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
%oreon_autofiles python3-pysrt usr/lib/python3*/site-packages/pysrt* usr/lib64/python3*/site-packages/pysrt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pysrt* usr/lib64/python3*/site-packages/pysrt* usr/bin/*

%check

%pytest
%files
%files -n python3-pysrt -f %{oreon_filedir}/python3-pysrt.list

%changelog

%autochangelog
