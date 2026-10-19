%global source0_hash db7344de2c03257698c9fc12f140d46cee505241b0df378e6f76925d22c32eaa
Name:           python-urwidtrees
Version:        1.0.4
Release:        1%{?dist}
Summary:        Tree Widget Container API for the urwid toolkit
License:        GPL-3.0-or-later
URL:            https://github.com/pazz/urwidtrees
Source0:        https://github.com/pazz/urwidtrees/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-urwidtrees = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-urwidtrees
Summary:        Tree Widget Container API for the urwid toolkit
%description -n python3-urwidtrees

%package -n python3-urwidtrees-doc
BuildRequires:  python3-sphinx
Summary:        Documentation for urwidtrees
%description -n python3-urwidtrees-doc
Development documentation for urwidtrees

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir urwidtrees-%{version}
%oreon_prep
%build

%pyproject_wheel
pushd docs/
make -e SPHINXBUILD=/usr/bin/sphinx-build-3 html
popd
%install
%pyproject_install
%oreon_autofiles python3-urwidtrees usr/lib/python3*/site-packages/urwidtrees* usr/lib64/python3*/site-packages/urwidtrees* usr/bin/*
%oreon_autofiles python3-urwidtrees-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/urwidtrees* usr/lib64/python3*/site-packages/urwidtrees* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%files
%files -n python3-urwidtrees -f %{oreon_filedir}/python3-urwidtrees.list
%files -n python3-urwidtrees-doc -f %{oreon_filedir}/python3-urwidtrees-doc.list

%changelog

%autochangelog
