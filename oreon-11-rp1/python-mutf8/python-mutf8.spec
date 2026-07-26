%global source0_hash c7a86f00bc8d313b9ce184375c944bf5be771127283d82a8d2becf33cc84e1c7

Name:           python-mutf8
Version:        1.0.6
Release:        %autorelease
Summary:        Fast MUTF-8 encoder & decoder

License:        MIT
URL:            http://github.com/TkTech/mutf8
# Get sources from GitHub for tests
Source:         %{url}/archive/v%{version}/mutf8-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc

%global _description %{expand:
This package contains simple pure-python as well as C encoders and decoders for
the MUTF-8 character encoding. In most cases, you can also parse the even-rarer
CESU-8.

These days, you'll most likely encounter MUTF-8 when working on files or
protocols related to the JVM. Strings in a Java .class file are encoded using
MUTF-8, strings passed by the JNI, as well as strings exported by the object
serializer.

This library was extracted from Lawu, a Python library for working with JVM
class files.}

%description %_description

%package -n     python3-mutf8
Summary:        %{summary}

%description -n python3-mutf8 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
#pyproject_extras_subpkg -n python3-mutf8 test

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mutf8-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mutf8

%check
%pyproject_check_import
%pytest

%files -n python3-mutf8 -f %{pyproject_files}

%changelog
%autochangelog
