%global source0_hash dbe598a455e6d2a71a4b6ee7f02ddbd79c49e3de47315544d258b142ffe52f1d

Name:           python-libdiscid
Version:        2.0.2
Release:        13%{?dist}
Summary:        Python bindings for libdiscid

License:        MIT
URL:            https://github.com/sebastinas/python-libdiscid
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libdiscid-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-sphinx

%description
python-libdiscid provides Python bindings for libdiscid. libdiscid's
main purpose is the calculation of identifiers for audio discs to use
for the MusicBrainz database.

%package -n python%{python3_pkgversion}-libdiscid
Summary:        Python 3 bindings for libdiscid
%{?python_provide:%python_provide python%{python3_pkgversion}-libdiscid}

%description -n python%{python3_pkgversion}-libdiscid
python%{python3_pkgversion}-libdiscid provides Python 3 bindings for libdiscid. libdiscid's
main purpose is the calculation of identifiers for audio discs to use
for the MusicBrainz database.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# for sphinx 6.1.3
sed -i 's/("http:\/\/musicbrainz.org\/doc\/%s", "")/("http:\/\/musicbrainz.org\/doc\/%s", "%s")/g' docs/conf.py

%build
%pyproject_wheel
PYTHONPATH="%{pyproject_build_lib}" sphinx-build-3 docs/ html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files libdiscid

%check
pushd libdiscid
PYTHONPATH=%{buildroot}%{python3_sitearch}/ %{python3} -m unittest discover -v
popd

%files -n python%{python3_pkgversion}-libdiscid -f %{pyproject_files}
%doc CHANGELOG.md README.md
%exclude %{python3_sitearch}/*libdiscid*/tests/

%changelog
%autochangelog
