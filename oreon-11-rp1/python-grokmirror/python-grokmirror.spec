%global source0_hash 9de56419f00b77eb408caa57805cd697f07bc05b726a09e7b05237740d47a0a1
Name:           python-grokmirror
Version:        2.0.12
Release:        1%{?dist}
Summary:        Framework to smartly mirror git repositories
License:        GPL-3.0-or-later
URL:            https://git.kernel.org/pub/scm/utils/grokmirror/grokmirror.git
Source0:        https://www.kernel.org/pub/software/network/grokmirror/grokmirror-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-grokmirror = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-grokmirror
Summary:        %summary
%description -n python3-grokmirror

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir grokmirror-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p -m 0755 %{buildroot}%{_mandir}/man1
install -pm 0644 man/*.1 %{buildroot}/%{_mandir}/man1/
%oreon_autofiles python3-grokmirror usr/lib/python3*/site-packages/grokmirror* usr/lib64/python3*/site-packages/grokmirror* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/grokmirror* usr/lib64/python3*/site-packages/grokmirror* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-grokmirror -f %{oreon_filedir}/python3-grokmirror.list

%changelog

%autochangelog
