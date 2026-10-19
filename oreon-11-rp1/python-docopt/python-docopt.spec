%global source0_hash 2113eed1e7fbbcd43fb7ee6a977fb02d0b482753586c9dc1a8e3b7d541426e99
Name:           python-docopt
Epoch:          1
Version:        0.6.2
Release:        1%{?dist}
Summary:        Pythonic argument parser, that will make you smile
License:        MIT
URL:            https://github.com/docopt/docopt
Source0:        https://github.com/docopt/docopt/archive/%{version}/docopt-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/pull/493.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-docopt = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-docopt
Summary:        Pythonic argument parser, that will make you smile
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-docopt

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir docopt-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-docopt usr/lib/python3*/site-packages/docopt* usr/lib64/python3*/site-packages/docopt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/docopt* usr/lib64/python3*/site-packages/docopt* usr/bin/*

%check

%pytest
%files
%files -n python3-docopt -f %{oreon_filedir}/python3-docopt.list

%changelog

%autochangelog
