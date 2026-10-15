%global source0_hash 087b58a9afe076bb08e2d726478e1f16cb928d67ffa9092817e033c335de522a

Name:           python-libcst
Version:        1.9.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A concrete syntax tree with AST-like properties for Python 3.0 through 3.15 programs.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Instagram/LibCST
Source:         %{pypi_source libcst}
Source1:        python-libcst-%{version}-vendor.tar.xz
%global source1_hash be934874216d1ffa39987553130eac30eb1f0e316dd6bf2b5c13e89d5f0a2633

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'libcst' generated automatically by pyp2spec.}

Patch:          libcst-fix-metadata.diff
Patch:          One-pyyaml-to-rule-them-all.patch

%description %_description

%package -n     python3-libcst
Summary:        %{summary}

%description -n python3-libcst %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libcst-%{version}
tar xf %{SOURCE1}
%cargo_prep -v vendor


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-libcst -f %{pyproject_files}

%changelog
%autochangelog
