%global source0_hash 4d2472f9684731e58cc9c56c463be63baa1447d674e0d66aeb5627b22f512c29

Summary:        A powerful declarative parser/builder for binary data
Name:           python-construct
Version:        2.10.70
Release:        12%{?dist}
License:        MIT
URL:            http://construct.readthedocs.org
Source0:        https://pypi.python.org/packages/source/c/construct/construct-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Construct is a powerful declarative parser (and builder) for binary
data.

Instead of writing imperative code to parse a piece of data, you
declaratively define a data structure that describes your data. As
this data structure is not code, you can use it in one direction to
parse data into Pythonic objects, and in the other direction, convert
(build) objects into binary data.}

%description %_description
%package     -n python3-construct
Summary:        %summary
Requires:       python3-six
%description -n python3-construct %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n construct-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files -l construct

%check
%pyproject_check_import

%files -n python3-construct -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
