%global source0_hash 73977fc746b36cc41184dd43c3fe81323e7b8b06c2bb0826c4f59a20c56bb9f1
Name:           python-sdnotify
Version:        0.3.2
Release:        1%{?dist}
License:        MIT
Summary:        A pure Python implementation of systemd's service notification protocol
URL:            https://github.com/bb4242/sdnotify
Source0:        https://files.pythonhosted.org/packages/source/s/sdnotify/sdnotify-%{version}.tar.gz
BuildArch:      noarch
Requires: systemd
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sdnotify = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sdnotify
Summary:        A pure Python implementation of systemd's service notification protocol
%description -n python3-sdnotify

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sdnotify-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sdnotify usr/lib/python3*/site-packages/sdnotify* usr/lib64/python3*/site-packages/sdnotify* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sdnotify* usr/lib64/python3*/site-packages/sdnotify* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-sdnotify -f %{oreon_filedir}/python3-sdnotify.list

%changelog

%autochangelog
