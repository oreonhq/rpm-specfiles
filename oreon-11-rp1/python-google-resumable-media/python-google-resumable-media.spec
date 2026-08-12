%global source0_hash 63e6fff61ef26b136b67c73a370f6604dbbc0cf23d6fc9f5b42890c506e29863

%bcond tests 1

Version:        2.8.0
Name:           python-google-resumable-media
Release:        %autorelease
Summary:        Utilities for Google media downloads and resumable uploads

License:        Apache-2.0
URL:            https://github.com/googleapis/google-resumable-media-python
Source:         %{url}/archive/v%{version}/google-resumable-media-python-%{version}.tar.gz


BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist brotli}
%endif

%global _description %{expand:
%{summary}.}

%description %{_description}

%package -n python3-google-resumable-media
Summary:        %{summary}

%description -n python3-google-resumable-media %{_description}

# We don’t build a metapackage for the aiohttp extra because it currently
# requires google-auth 1.x, and Fedora has version 2.x.
#
# Please consider supporting google-auth 2.x
# https://github.com/googleapis/google-resumable-media-python/issues/417
%pyproject_extras_subpkg -n python3-google-resumable-media requests

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n google-resumable-media-python-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x requests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l google

%check
%if %{with tests}
%pytest tests/unit
%endif

%files -n python3-google-resumable-media -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.rst

%changelog
%autochangelog
