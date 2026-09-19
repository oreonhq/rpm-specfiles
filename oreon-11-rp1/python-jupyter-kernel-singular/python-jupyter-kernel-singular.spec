%global source0_hash bb5b122bc9c5a2e0b207da3d078fbba6e756cad42a071bf9942b1d1705387b69

Name:           python-jupyter-kernel-singular
Version:        0.9.9
Release:        25%{?dist}
Summary:        Jupyter kernel for Singular

License:        GPL-2.0-or-later
URL:            https://github.com/sebasguts/jupyter_kernel_singular
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/jupyter_kernel_singular-%{version}.tar.gz
# https://github.com/sebasguts/jupyter_kernel_singular/pull/13
Patch:          %{name}-imports.patch

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -l jupyter_kernel_singular

BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist jupyter-client}
BuildRequires:  %{py3_dist pysingular}

%global _description %{expand:This package contains a Jupyter kernel for Singular, to enable using Jupyter
as the front end for Singular.}

%description
%_description

%package     -n python3-jupyter-kernel-singular
Summary:        Jupyter kernel for Singular
Requires:       python-jupyter-filesystem
Requires:       %{py3_dist ipykernel}
Requires:       %{py3_dist pysingular}

%description -n python3-jupyter-kernel-singular
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jupyter_kernel_singular-%{version} -p1

%install -a
# We want /etc, not /usr/etc
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

%files -n python3-jupyter-kernel-singular -f %{pyproject_files}
%doc README.md
%{_datadir}/jupyter/kernels/singular/
%{_datadir}/jupyter/nbextensions/singular-mode/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/singular-mode.json

%changelog
%autochangelog
