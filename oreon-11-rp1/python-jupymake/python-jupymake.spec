%global source0_hash f0f2e275da32cd30e869a5ea5ddf4ffa557a3f9e87050617d401b9d89b1d9dd9

# Upstream does not release tarballs.  Instead the code is copied directly
# into the polymake distribution.  Therefore, we check out the code from git.
%global commit  a6987c8bb455c172e80eed7b5b62a7c13bf85815
%global shortcommit %{sub %{commit} 1 7}
%global gitdate 20231204

Name:           python-jupymake
Version:        0.9
Release:        40.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Python wrapper for the polymake shell

License:        GPL-2.0-or-later
URL:            https://github.com/polymake/JuPyMake
VCS:            git:%{url}.git
Source:         %{url}/archive/%{commit}/JuPyMake-%{shortcommit}.tar.gz
# Upstream patch to fix polymake shell usage
Patch:          %{name}-shell.patch
# Add a missing const keyword
Patch:          %{name}-const.patch
# Fix too-small type sizes
Patch:          %{name}-size.patch
# Adapt to license handling in newer setuptools
Patch:          %{name}-license-files.patch

# Polymake is not available on 32-bit platforms.
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    pyproject
BuildOption(install): -l JuPyMake

BuildRequires:  gcc-c++
BuildRequires:  polymake

%global _description %{expand:This package provides a basic interface to call polymake from python.  It is
meant to be used in the Jupyter interface for polymake.}

%description
%_description

%package     -n python3-jupymake
Summary:        Python wrapper for the polymake shell
Requires:       polymake%{?_isa}

%description -n python3-jupymake
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n JuPyMake-%{commit} -p1

%files -n python3-jupymake -f %{pyproject_files}
%doc README README.md example.py

%changelog
%autochangelog
