%global source0_hash 249a30268bae5c0982ee4f31abb7126577c03602092a0f2c64b06a4f68176b30

Name:           python-markupsafe
Version:        2.0.1
Release:        0%{?dist}
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
License:        BSD-3-Clause
URL:            https://github.com/pallets/markupsafe
Source0:        https://github.com/pallets/markupsafe/archive/2.0.1/MarkupSafe-2.0.1.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
This package installs test- and docs-requirements from files
and uses them to run tests and build documentation.
It also has a less common order of the %%files section.


%package -n python3-markupsafe
Summary:        %{summary}

%description -n python3-markupsafe
...


# In this spec, we put %%files early to test it still works
%files -n python3-markupsafe -f %{pyproject_files}
%doc CHANGES.rst README.rst


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n markupsafe-%{version}

# we don't have pip-tools packaged in Fedora yet
sed -i /pip-tools/d requirements/dev.in

# help the macros understand the URL in requirements/docs.in
sed -Ei 's/sphinx\.git@([0-9a-f]+)/sphinx.git@\1#egg=sphinx/' requirements/docs.in


%generate_buildrequires
# requirements/dev.in recursively includes tests.in and docs.in
# we also list tests.in manually to verify we can pass multiple arguments,
# but it should be redundant if this was a real package
%pyproject_buildrequires requirements/dev.in requirements/tests.in


%build
%pyproject_wheel
%make_build -C docs html SPHINXOPTS='-n %{?_smp_mflags}'


%install
%pyproject_install
%pyproject_save_files -l markupsafe


%check
%pytest

