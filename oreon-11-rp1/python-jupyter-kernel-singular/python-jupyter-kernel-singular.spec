%global source0_hash bb5b122bc9c5a2e0b207da3d078fbba6e756cad42a071bf9942b1d1705387b69
Name:           python-jupyter-kernel-singular
Version:        0.9.9
Release:        1%{?dist}
Summary:        Jupyter kernel for Singular
License:        GPL-2.0-or-later
URL:            https://github.com/sebasguts/jupyter_kernel_singular
VCS:            git:%{url}.git
Source0:        https://github.com/sebasguts/jupyter_kernel_singular/archive/v%{version}/jupyter_kernel_singular-%{version}.tar.gz
Patch:          %{name}-imports.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jupyter-kernel-singular = %{version}-%{release}
# /oreon:deps
%description
This package contains a Jupyter kernel for Singular, to enable using Jupyter
as the front end for Singular.

%package     -n python3-jupyter-kernel-singular
Summary:        Jupyter kernel for Singular
Requires:       python-jupyter-filesystem
Requires:       %{py3_dist ipykernel}
Requires:       %{py3_dist pysingular}
%description -n python3-jupyter-kernel-singular
This package contains a Jupyter kernel for Singular, to enable using Jupyter
as the front end for Singular.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir jupyter_kernel_singular-%{version}
%oreon_prep
%install
%pyproject_install
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}
%oreon_autofiles python3-jupyter-kernel-singular usr/lib/python3*/site-packages/jupyter_kernel_singular* usr/lib64/python3*/site-packages/jupyter_kernel_singular* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jupyter_kernel_singular* usr/lib64/python3*/site-packages/jupyter_kernel_singular* usr/bin/*

%build

%pyproject_wheel
%files
%files -n python3-jupyter-kernel-singular -f %{oreon_filedir}/python3-jupyter-kernel-singular.list

%changelog

%autochangelog
