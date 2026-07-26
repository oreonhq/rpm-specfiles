%global source0_hash ba93368818d915863cd168cda0baf977f393650e9cc80f2ca9eeb9acb0692b55

%global srcname priority

%global common_description %{expand:
A HTTP/2 Priority Implementation Priority is a pure-Python
implementation of the priority logic for HTTP/2, set out in RFC 7540 Section
5.3 (Stream Priority)_. This logic allows for clients to express a preference
for how the server allocates its (limited) resources to the many outstanding
HTTP requests that may be running over a single HTTP/2 connection.}

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        A pure-Python implementation of the HTTP/2 priority tree

License:        MIT
URL:            http://python-hyper.org/priority/
VCS:            https://github.com/python-hyper/priority
Source0:        %vcs/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Update intersphinx_mapping for Sphinx 8 compatibility
Patch:          %vcs/pull/149.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=%{pyproject_build_lib} sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.rst

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog
