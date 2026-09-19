%global source0_hash cc8de0c140831519e45598b082fdef0e939fd30930be442e38bdec13dc16aab5

%global git_tag 0.4.1-2

Name:           python-axolotl-curve25519
Version:        0.4.1
Release:        %autorelease
Summary:        Python wrapper for curve25519

# The entire source code is GPL-3.0-only except:
# curve/curve25519-donna.[c|h] which is BSD-3-Clause.
License:        GPL-3.0-only and BSD-3-Clause
URL:            https://github.com/tgalal/python-axolotl-curve25519
Source0:        %{url}/archive/%{git_tag}/%{git_tag}.tar.gz
# License file for curve/curve25519-donna.[c|h]
Source1:	LICENSE.curve25519-donna
Patch0: python-axolotl-curve25519-c99.patch

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
This is a python wrapper for the curve25519 library with ed25519 signatures.}

%description %_description

%package -n python3-axolotl-curve25519
Summary:        %{summary}

%description -n python3-axolotl-curve25519 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_tag}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files axolotl_curve25519
cp -p %{SOURCE1} LICENSE.curve25519-donna

%files -n python3-axolotl-curve25519 -f %{pyproject_files}
%doc README.md
%license LICENSE
%license LICENSE.curve25519-donna

%changelog
%autochangelog
