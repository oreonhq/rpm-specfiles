%global source0_hash 6923232111329954a8349f7d99f212b6e96b5206e77fbd39aaf1b3cb4a5e9260
Name:           python-posix-ipc
Version:        1.3.2
Release:        1%{?dist}
Summary:        POSIX IPC primitives for Python
License:        BSD-3-Clause
URL:            https://github.com/osvenskan/posix_ipc
Source0:        https://files.pythonhosted.org/packages/source/p/posix_ipc/posix_ipc-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-posix-ipc = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-posix-ipc
Summary:        POSIX IPC primitives for Python
Obsoletes:      python3-posix_ipc < 1
%py_provides    python3-posix_ipc
%description -n python3-posix-ipc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir posix_ipc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-posix-ipc usr/lib/python3*/site-packages/posix_ipc* usr/lib64/python3*/site-packages/posix_ipc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/posix_ipc* usr/lib64/python3*/site-packages/posix_ipc* usr/bin/*

%check

PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m unittest discover
%files
%files -n python3-posix-ipc -f %{oreon_filedir}/python3-posix-ipc.list

%changelog

%autochangelog
