%global source0_hash 3ede829ed8d842f6cd48fc7081d7a41001a56f1f38603f9d49bf3020d59a31ad

Name:           python-frozenlist
Version:        1.8.0
Release:        %autorelease
Summary:        List-like structure which can be made immutable

License:        Apache-2.0
URL:            https://github.com/aio-libs/frozenlist
Source:         %{pypi_source frozenlist}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# Downstream-only: Build normal wheels in-place
#
# Upstream wants to build only editable wheels in-place, building normal
# wheels in a temporary directory. This is reasonable in principle, but
# the implementation conflicts with the pyproject-rpm-macros, resulting in
# an unbounded recursion of nested temporary directories.
Patch:          0001-Downstream-only-Build-normal-wheels-in-place.patch

# Adjust interface test SKIP_METHODS for Python 3.15.0a2
# https://github.com/aio-libs/frozenlist/pull/723
#
# Fixes:
#
# python-frozenlist fails to build with Python 3.15: test_iface:
# AssertionError: assert hasattr(self.FrozenList, name)
# https://bugzilla.redhat.com/show_bug.cgi?id=2416992
Patch:          %{url}/pull/723.patch


BuildRequires:  gcc-c++

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
FrozenList is a list-like structure which implements
collections.abc.MutableSequence, and which can be made immutable.}

%description %{common_description}

%package -n python3-frozenlist
Summary:        %{summary}

%description -n python3-frozenlist %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n frozenlist-%{version} -p1
find . -type f -name '*.c' -print -delete
sed -r -i 's/^([[:blank:]]*)(.*[-_]cov)/\1# \2/' pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l frozenlist

%check
%pytest -v

%files -n python3-frozenlist -f %{pyproject_files}
%doc CHANGES.rst
%doc CONTRIBUTORS.txt
%doc README.rst

%changelog
%autochangelog
