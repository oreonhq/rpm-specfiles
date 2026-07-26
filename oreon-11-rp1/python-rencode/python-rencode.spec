%global source0_hash 480aab74948a7f339b749b5c39bdb4caf15429f4b49a998c770d5f371098d351

%global srcname rencode

Name:           python-rencode
Version:        1.0.8
Release:        4%{?dist}
Summary:        Web safe object pickling/unpickling
# Automatically converted from old format: GPLv3+ and BSD - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://github.com/aresch/rencode

Source0:        https://github.com/aresch/rencode/archive/v%{version}.tar.gz#/rencode-%{version}.tar.gz

# Fix the build on aarc64
# Resolved upstream:
# https://github.com/aresch/rencode/commit/591b9f4d85d7e2d4f4e99441475ef15366389be2
# https://github.com/aresch/rencode/commit/e7ec8ea718e73a8fee7dbc007c262e1584f7f94b
Patch:          fix-arm-build.patch

BuildRequires:  gcc
BuildRequires:  python3-devel

%description
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.

%package -n python3-rencode
Summary:    Web safe object pickling/unpickling

%description -n python3-rencode
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n rencode-%{version}

# Make sure we rebuild the module
rm -f ./rencode/_rencode.c

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L rencode

%check
%pyproject_check_import

pushd tests
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch} %{__python3} test_rencode.py
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch} %{__python3} timetest.py
popd

%files -n python%{python3_pkgversion}-rencode -f %{pyproject_files}
%doc README.md
%license COPYING

%changelog
%autochangelog
