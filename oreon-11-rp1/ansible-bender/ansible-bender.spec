%global source0_hash 2b2786e870106e22e17123b8cd6fa900ee7a72f6fbefbf8bd57aaee909c95089
%bcond_with     check
%bcond_with     privileged_tests
Name:           ansible-bender
Version:        0.10.1
Release:        1%{?dist}
Summary:        Build container images using Ansible playbooks
License:        MIT
URL:            https://github.com/ansible-community/ansible-bender
Source0:        https://files.pythonhosted.org/packages/source/a/ansible-bender/ansible-bender-%{version}.tar.gz
BuildArch:      noarch
%if %{with check}
%endif
Requires:       (ansible-core or ansible)
Suggests:       ansible-core
Requires:       buildah
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ansible-bender = %{version}-%{release}
# /oreon:deps
%description
This is a tool which bends containers using Ansible playbooks and
turns them into container images. It has a pluggable builder selection
- it is up to you to pick the tool which will be used to construct
your container image. Right now the only supported builder is
buildah. More to come in the future. Ansible-bender (ab) relies on
Ansible connection plugins for performing builds.

tl;dr Ansible is the frontend, buildah is the backend.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main
%if %{with check}
%check

%pytest \
  -v \
  --disable-pytest-warnings \
  --numprocesses=auto \
%if %{with privileged_tests}
  tests
%else
  tests/unit
%endif
%endif
%files

%changelog

%autochangelog
