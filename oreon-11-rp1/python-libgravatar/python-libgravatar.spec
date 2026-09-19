%global source0_hash 05cf4f8dfefe995d09078cd3d747c8f04dcf17d6004fc7bb542049a55f2238d9

Name:           python-libgravatar
Version:        1.0.4
Release:        9%{?dist}
Summary:        Python interface for the Gravatar APIs

License:        GPL-3.0-or-later
URL:            https://github.com/pabluk/libgravatar
BuildArch:      noarch
# PyPI source is incomplete
Source0:        %{pypi_source libgravatar}

BuildRequires:  python3-devel

%description
Python interface for the Gravatar API.

%package -n python3-libgravatar
Summary:        Python 3 interface for the Gravatar API

%description -n python3-libgravatar
Python 3 interface for the Gravatar API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libgravatar-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l libgravatar

%check
%py3_check_import libgravatar

%files -n python3-libgravatar -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
