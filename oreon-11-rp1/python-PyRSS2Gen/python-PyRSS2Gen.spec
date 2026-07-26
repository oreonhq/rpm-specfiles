%global source0_hash 2a9a3ee7c8e30cb40434ef3a295f9a60166f7d8c3eaefac9f46f7ed4b27c2269

Name:		python-PyRSS2Gen
Version:	1.1
Release:	47%{?dist}
Summary:	A Python library for generating RSS 2.0 feeds

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.dalkescientific.com/Python/PyRSS2Gen.html
Source0:	http://www.dalkescientific.com/Python/PyRSS2Gen-%{version}.tar.gz
BuildArch:	noarch
%global _description\
A Python library for generating RSS 2.0 feeds.

%description %_description

%package -n python3-PyRSS2Gen
BuildRequires:	python3-devel
Requires:	python3-feedparser
Summary:	A Python library for generating RSS 2.0 feeds
BuildArch:	noarch
%description -n python3-PyRSS2Gen
A Python3 library for generating RSS 2.0 feeds.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn PyRSS2Gen-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files PyRSS2Gen

%check
%pyproject_check_import PyRSS2Gen

%files -n python3-PyRSS2Gen -f %{pyproject_files}
%doc README LICENSE

%changelog
%autochangelog
