%global source0_hash 72ac1abbae5bddb4918688713f991f5a7fb6c9b593646a82f4bf3ac53de7eeb5

Name:      python-construct-classes
Version:   0.1.2
Release:   14%{?dist}
Summary:   Parse your binary structs into dataclasses

License:   MIT
URL:       https://github.com/matejcik/construct-classes
Source0:   %{pypi_source construct-classes}

# Only include license and documentation for sdist #2
# https://github.com/matejcik/construct-classes/pull/2
Patch0:    https://patch-diff.githubusercontent.com/raw/matejcik/construct-classes/pull/2.patch#/only-include-license-documentation-for-sdist.patch

BuildArch: noarch

BuildRequires: python3-devel

%global _description %{expand:
Parse your binary data into dataclasses. Pack your dataclasses into binary data.

construct-classes rely on construct for parsing and packing. The programmer
needs to manually write the Construct expressions. There is also no type
verification, so it is the programmer's responsibility that the dataclass and
the Construct expression match.}

%description %_description

%package -n python3-construct-classes
Summary:       %{summary}

%description -n python3-construct-classes %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n construct-classes-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files construct_classes

%check
# Tests are left out from the sdist

%files -n python3-construct-classes -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst
%doc README.rst

%changelog
%autochangelog
