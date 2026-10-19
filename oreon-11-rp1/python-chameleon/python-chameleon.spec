%global source0_hash f228d32d13562f7d976c0bcd7db56c138662676865a7d78b7d274064076f6cb4
%global srcname Chameleon
Name:           python-chameleon
Version:        4.6.0
Release:        8%{?dist}
Summary:        XML-based template compiler
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/malthe/chameleon
Source0:        https://github.com/malthe/chameleon/archive/%{version}/chameleon-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-chameleon = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-chameleon
Summary: %summary
Requires:   python3-setuptools
Requires:   python3-lxml
%description -n python3-chameleon

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir chameleon-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-chameleon usr/lib/python3*/site-packages/chameleon* usr/lib64/python3*/site-packages/chameleon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/chameleon* usr/lib64/python3*/site-packages/chameleon* usr/bin/*

%check

%pyproject_check_import -e 'chameleon.tests*'
%tox
%files
%files -n python3-chameleon -f %{oreon_filedir}/python3-chameleon.list

%changelog

%autochangelog
