%global source0_hash dbe598a455e6d2a71a4b6ee7f02ddbd79c49e3de47315544d258b142ffe52f1d
Name:           python-libdiscid
Version:        2.0.2
Release:        1%{?dist}
Summary:        Python bindings for libdiscid
License:        MIT
URL:            https://github.com/sebastinas/python-libdiscid
Source0:        https://github.com/sebastinas/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) (>= 0.15)
BuildRequires:  python3dist(setuptools) >= 43
Requires:       python3-libdiscid = %{version}-%{release}
# /oreon:deps
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
%oreon_autofiles main usr/lib/python3*/site-packages/libdiscid* usr/lib64/python3*/site-packages/libdiscid* usr/bin/*

%check

pushd libdiscid
PYTHONPATH=%{buildroot}%{python3_sitearch}/ %{python3} -m unittest discover -v
popd
%files
%files -n python3-libdiscid -f %{oreon_filedir}/python3-libdiscid.list

%changelog

%autochangelog
