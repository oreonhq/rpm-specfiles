%global source0_hash ace165b546cb78ac00868a36331df8a91f96a0701951beb2175693baf9a35c5e

Name:           python-cyseq
Version:        0.1.2
Release:        %autorelease
Summary:        A Cython version of ScanCode-toolkit's licensedcode.seq

License:        Apache-2.0
URL:            https://github.com/aboutcode-org/cyseq
Source:         %{pypi_source cyseq}

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
This library is a Cython version of scancode-toolkit's `licensedcode.seq`.}

%description %_description

%package -n     python3-cyseq
Summary:        %{summary}

%description -n python3-cyseq %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n cyseq-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cyseq

%check
%pytest tests

%files -n python3-cyseq -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
