%global source0_hash 83624b850fd0727f0cc3a574e17471cd003e1d85c46af91854bdab67299058fa

Name:           podman-compose
Version:        1.5.0
Release:        5%{?dist}
Summary:        Run docker-compose.yml using podman
License:        GPL-2.0-only
URL:            https://github.com/containers/podman-compose
Source0:	https://github.com/containers/podman-compose/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pyyaml
Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-pyyaml
Requires:       podman

%description
An implementation of docker-compose with podman backend.
The main objective of this project is to be able to run docker-compose.yml
unmodified and rootless.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
 
%install
%pyproject_install
%pyproject_save_files -l 'podman_compose*'

#Drop spurious shebang
sed -i /python3/d %{buildroot}%{python3_sitelib}/podman_compose.py

#Install bash completion
install -Dpm 0644 completion/bash/podman-compose -t %{buildroot}%{bash_completions_dir}

%files -f %{pyproject_files}
%doc README.md CONTRIBUTING.md docs/ examples
%{_bindir}/podman-compose
%{bash_completions_dir}/podman-compose

%changelog
%autochangelog
