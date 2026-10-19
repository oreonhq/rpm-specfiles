%global source0_hash dffdec88deb6da8437a86d82340e213c3a616933807fe3fd5978f0c8c325e5e2
Name:           podman-compose
Version:        1.6.0
Release:        1%{?dist}
Summary:        Run docker-compose.yml using podman
License:        GPL-2.0-only
URL:            https://github.com/containers/podman-compose
Source0:        https://github.com/containers/podman-compose/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-pyyaml
Requires:       podman
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-podman-compose = %{version}-%{release}
# /oreon:deps
%package -n       python3-podman-compose+devel
Summary:        Metapackage for python3-podman-compose devel extras
Requires:       python3-podman-compose = %{version}-%{release}
Provides:       python3dist(podman-compose[devel]) = %{version}-%{release}

%description -n python3-podman-compose+devel
Metapackage for python3-podman-compose devel extras.

%description
An implementation of docker-compose with podman backend.
The main objective of this project is to be able to run docker-compose.yml
unmodified and rootless.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
sed -i /python3/d %{buildroot}%{python3_sitelib}/podman_compose.py
install -Dpm 0644 completion/bash/podman-compose -t %{buildroot}%{bash_completions_dir}
%oreon_autofiles main

%files

%changelog

%autochangelog
