%global source0_hash ba62d34dbcf487e8368f6c19762a19e1c5f06af7e705f6c583c0632b35bccf7d

Name:           python-qcengine
Version:        0.30.0
Release:        %autorelease
Summary:        A compute wrapper for Quantum Chemistry

License:        BSD-3-Clause
URL:            https://github.com/MolSSI/QCEngine
Source:         %{pypi_source qcengine}
Patch0:         https://github.com/MolSSI/QCEngine/pull/451.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# for testing
BuildRequires:  python3-pytest
# https://kojipkgs.fedoraproject.org//work/tasks/9840/108019840/build.log
BuildRequires:  python3-msgpack

# For running the tests
#BuildRequires:  xtb # requires xtb-python which is not available in Fedora and whose development appears to be ceased
BuildRequires:  psi4
BuildRequires:  mrchem
#BuildRequires: python3-dftd4 # Package still in review https://bugzilla.redhat.com/show_bug.cgi?id=2310392

%global _description %{expand:
Quantum chemistry program executor and IO standardizer (QCSchema) for quantum
chemistry.}

%description
%{_description}

%package -n     python3-qcengine
Summary:        %{summary}

%description -n python3-qcengine
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n qcengine-%{version}
%patch 0 -p1 -b .psi4

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files qcengine

%check
%pytest

%files -n python3-qcengine -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/qcengine

%changelog
%autochangelog
