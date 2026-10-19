%global source0_hash 3d9bf7c05673df06e32bea23b494b8d36ca6d10f7d5c3c8a6989608c09c986a9
Name:           python-livereload
Version:        2.7.1
Release:        1%{?dist}
Summary:        Reload webpages on changes
License:        BSD-3-Clause
URL:            https://github.com/lepture/python-livereload
Source0:        https://files.pythonhosted.org/packages/source/l/livereload/livereload-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-livereload = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-livereload
Summary:        Reload webpages on changes
%description -n python3-livereload

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir livereload-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-livereload usr/lib/python3*/site-packages/livereload* usr/lib64/python3*/site-packages/livereload* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/livereload* usr/lib64/python3*/site-packages/livereload* usr/bin/*

%check

%pytest
%files
%files -n python3-livereload -f %{oreon_filedir}/python3-livereload.list

%changelog

%autochangelog
