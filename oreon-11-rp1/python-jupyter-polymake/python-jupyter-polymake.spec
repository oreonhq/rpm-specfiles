%global source0_hash ebb35ebc3cc5bc4a30681b72cbd9f98794dd9cb9cfcfe09ce9e256d6901ec0e0

# Upstream does not release tarballs.  Instead the code is copied directly
# into the polymake distribution.  Therefore, we check out the code from git.
%global commit  704994092647daca93ad18d6853a5540fceb3794
%global shortcommit %{sub %{commit} 1 7}
%global gitdate 20180129

Name:           python-jupyter-polymake
Version:        0.16
Release:        36.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Jupyter kernel for polymake

# The code is WTFPL.  The JavaScript and image files are MIT.
License:        WTFPL AND MIT
URL:            https://github.com/polymake/jupyter-polymake
VCS:            git:%{url}.git
Source:         %{url}/archive/%{commit}/jupyter-polymake-%{shortcommit}.tar.gz
# Changes made in the polymake version that have not been pushed to git
Patch:          %{name}-update.patch

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -l jupyter_kernel_polymake

BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist jupymake}
BuildRequires:  %{py3_dist jupyter-client}
BuildRequires:  %{py3_dist pexpect}

%global _description This package contains a Jupyter kernel for polymake.

%description
%_description

%package     -n python3-jupyter-polymake
Summary:        Jupyter kernel for polymake
Requires:       python-jupyter-filesystem
Requires:       %{py3_dist ipykernel}
Requires:       %{py3_dist jupymake}
Requires:       %{py3_dist pexpect}

Recommends:     %{py3_dist ipython}

Provides:       bundled(npm(three)) = 137

%description -n python3-jupyter-polymake
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jupyter-polymake-%{commit} -p1

%install -a
# Move the jupyter kernel files to where we want them in Fedora
mkdir -p %{buildroot}%{_datadir}/jupyter/kernels/polymake
mv %{buildroot}%{python3_sitelib}/jupyter_kernel_polymake/resources/* \
   %{buildroot}%{_datadir}/jupyter/kernels/polymake
rmdir %{buildroot}%{python3_sitelib}/jupyter_kernel_polymake/resources
sed -i '/resources/d' %{pyproject_files}

%files -n python3-jupyter-polymake -f %{pyproject_files}
%doc README.md
%{_datadir}/jupyter/kernels/polymake/

%changelog
%autochangelog
