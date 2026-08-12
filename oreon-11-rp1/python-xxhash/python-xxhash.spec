%global source0_hash f0162a78b13a0d7617b2845b90c763339d1f1d82bb04a4b07f4ab535cc5e05d6

Name:           python-xxhash
Version:        3.6.0
Release:        %autorelease
Summary:        Python Binding for xxHash

# The entire source is BSD-2-Clause. When the PyPI sdist is used (vs. the
# GitHub archive), a bundled copy of portions of the xxhash C library is also
# present in the source archive; it is under the same license and is removed in
# %%prep.
License:        BSD-2-Clause
URL:            https://github.com/ifduyue/python-xxhash
Source:         %{pypi_source xxhash}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros


BuildRequires:  gcc
BuildRequires:  pkgconfig(libxxhash) >= 0.8.2

%global common_description %{expand:
xxhash is a Python binding for the xxHash library by Yann Collet.}

%description %{common_description}

%package -n python3-xxhash
Summary:        %{summary}

%description -n python3-xxhash %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n xxhash-%{version} -p1
rm -rvf deps

%generate_buildrequires
%pyproject_buildrequires

%build
export CFLAGS="${CFLAGS} $(pkgconf --cflags libxxhash)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs-only-L libxxhash)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs-only-other libxxhash)"
export XXHASH_LINK_SO='1'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l xxhash

%check
cd tests
%{py3_test_envvars} %{python3} -m unittest discover

%files -n python3-xxhash -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst

%changelog
%autochangelog
