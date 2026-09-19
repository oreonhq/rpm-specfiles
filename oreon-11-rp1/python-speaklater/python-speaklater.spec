%global source0_hash 59fea336d0eed38c1f0bf3181ee1222d0ef45f3a9dd34ebe65e6bfffdd6a65a9

%global tarName speaklater

Name:           python-%{tarName}
Version:        1.3
Release:        43%{?dist}
Summary:        Implements a lazy string for python useful for use with gettext
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://github.com/mitsuhiko/speaklater
Source0:        http://pypi.python.org/packages/source/s/%{tarName}/%{tarName}-%{version}.tar.gz
# Submitted upstream at: https://github.com/mitsuhiko/speaklater/pull/8
# Alternative approach at https://github.com/mitsuhiko/speaklater/pull/3
Patch0:         0001-Enable-building-on-python3-along-with-changes-to-doc.patch
Patch1:         0002-python3-2to3-including-doc.patch
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
A module that provides lazy strings for translations. Basically you get an\
object that appears to be a string but changes the value every time the value\
is evaluated based on a callable you provide.

%description %_description

%package -n python3-speaklater
Summary: Implements a lazy string for python3 useful for gettext

%description -n python3-speaklater
A module that provides lazy strings for translations. Basically you get an
object that appears to be a string but changes the value every time the value
is evaluated based on a callable you provide.

This package provides the python3 version of the module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{tarName}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l 'speaklater*'

%check
%pyproject_check_import

pushd build/lib
%{__python3} -m doctest speaklater.py
popd

%files -n python3-speaklater -f %{pyproject_files}
%doc PKG-INFO README

%changelog
%autochangelog
